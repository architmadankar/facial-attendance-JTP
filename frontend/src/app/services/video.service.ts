import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { IVideoFeed } from '../interfaces/video-feed';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class VideoService {
  _feedListUrl = "http://localhost:5000/video";
  _feedAddUrl = "http://localhost:5000/video/add"
  _feedPreviewUrl = "http://localhost:5000/video/preview";
  _feedStartUrl = "http://localhost:5000/video/start";
  _feedStopUrl = "http://localhost:5000/video/stop";
  _feedDeleteUrl = "http://localhost:5000/video/delete";

  constructor(private http: HttpClient) { }

  getFeedList(): Observable<IVideoFeed[]> {
    return this.http.get<IVideoFeed[]>(this._feedListUrl);
  }

  addVideoFeed(_feed: IVideoFeed) {
    return this.http.post<any>(this._feedAddUrl, _feed);
  }

  getVideoFeed(feed_id: string) {
    return this.http.get<any>(this._feedListUrl + "/" + feed_id.toString());
  }

  deleteVideoFeed(feed_id: string) {
    return this.http.delete<any>(this._feedDeleteUrl + "/" + feed_id);
  }

  start_feed(feed_id: string) {
    return this.http.get<any>(this._feedStartUrl + "/" + feed_id.toString());
  }

  stop_feed(feed_id: string) {
    return this.http.get<any>(this._feedStopUrl + "/" + feed_id.toString());
  }
}
