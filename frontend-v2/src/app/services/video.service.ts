import { Observable } from 'rxjs';
import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { IVideo } from '../interface/ivideo';

@Injectable({
  providedIn: 'root'
})
export class VideoService {

  _videoListURL = 'http://localhost:5000/video';
  _addVideoURL = 'http://localhost:5000/video/add';
  _deleteVideoURL = 'http://localhost:5000/video/delete';
  _videoURL =   'http://localhost:5000/video/preview';
  _videoStartURL = 'http://localhost:5000/video/start';
  _videoStopeURL = 'http://localhost:5000/video/stop';

  constructor(private http: HttpClient) { }

  getVideoList(): Observable<IVideo[]>{
    return this.http.get<IVideo[]>(this._videoListURL);
  }

  addVideo(_video: IVideo){
    return this.http.post<any>(this._addVideoURL, _video);
  }

  getVideo(_id: string){
    return this.http.get<any>(this._videoURL + '/' + _id.toString());
  }

  deleteVideo(_id: string){
    return this.http.delete<any>(this._deleteVideoURL + '/' + _id);
  }

  startVideo(_id: string){
    return this.http.get<any>(this._videoStartURL + '/' + _id.toString());
  }

  stop_video(_id: string){
    return this.http.get<any>(this._videoStopeURL + '/' + _id.toString());
  }
}
