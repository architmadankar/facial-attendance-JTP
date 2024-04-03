# original https://github.com/kizniche/Mycodo/blob/master/mycodo/mycodo_flask/camera/base_camera.py
# From https://github.com/miguelgrinberg/flask-video-streaming
import time
import logging
import threading


try:
    from greenlet import getcurrent as get_ident
except ImportError:
    try:
        from thread import get_ident
    except ImportError:
        from _thread import get_ident

logger = logging.getLogger(__name__)

class CameraEvent(object):
    """An Event-like class that signals all active clients when a new frame is
    available.
    """
    def __init__(self):
        self.events = {}

    def wait(self):
        """Invoked from each client's thread to wait for the next frame."""
        ident = get_ident()
        if ident not in self.events:
            # this is a new client
            # add an entry for it in the self.events dict
            # each entry has two elements, a threading.Event() and a timestamp
            self.events[ident] = [threading.Event(), time.time()]
        return self.events[ident][0].wait()

    def set(self):
        """Invoked by the camera thread when a new frame is available."""
        now = time.time()
        remove = None
        for ident, event in self.events.items():
            if not event[0].isSet():
                # if this client's event is not set, then set it
                # also update the last set timestamp to now
                event[0].set()
                event[1] = now
            else:
                # if the client's event is already set, it means the client
                # did not process a previous frame
                # if the event stays set for more than 5 seconds, then assume
                # the client is gone and remove it
                if now - event[1] > 5:
                    remove = ident
        if remove:
            del self.events[remove]

    def clear(self):
        """Invoked from each client's thread after a frame was processed."""
        self.events[get_ident()][0].clear()


class BaseCamera:
    _cameras = {}

    def __init__(self, unique_id=None):
        self.unique_id = unique_id
        self.event = CameraEvent()
        self.last_access = time.time()
        self._running = True
        self._thread = threading.Thread(target=self._thread)
        self._thread.start()
        BaseCamera._cameras[unique_id] = self

        # Wait for the initial frame
        while self.get_frame() is None:
            time.sleep(0)

    def get_frame(self):
        self.last_access = time.time()
        self.event.wait()
        self.event.clear()
        return self._frame  # Assuming the _thread populates this

    @staticmethod
    def frames():
        raise RuntimeError('Must be implemented by subclasses')

    def _thread(self):
        print(f'Camera Start [{self.unique_id}]')
        try:
            for frame in self.frames():
                if self._running:
                    self._frame = frame
                    self.event.set()
                    time.sleep(0)
        except GeneratorExit:  # Expected closure of the frames generator
            pass
        except Exception as e:  # Catch unexpected errors
            logger.error(f"Camera thread error: {e}")
        finally:
            self._running = False
            print(f"Camera Stop [{self.unique_id}]")
            del BaseCamera._cameras[self.unique_id]

    @classmethod
    def stop(cls, unique_id):
        if unique_id in cls._cameras:
            cls._cameras[unique_id]._running = False

    @classmethod
    def is_running(cls, unique_id):
        return unique_id in cls._cameras and cls._cameras[unique_id]._running 