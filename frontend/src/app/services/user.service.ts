import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

import { Observable } from 'rxjs';

import { IUser } from '../interfaces/user';


@Injectable({
  providedIn: 'root'
})
export class UserService {

  _userListUrl = "http://localhost:5000/users";
  _userAddUrl = "http://localhost:5000/users/add";
  _userCaptureUrl = "http://localhost:5000/users/cap";
  _userDeleteUrl = "http://localhost:5000/users/delete";
  _trainClassifierUrl = "http://localhost:5000/users/train";

  constructor(private http: HttpClient) { }

  getUserList(): Observable<IUser[]> {
    return this.http.get<IUser[]>(this._userListUrl);
  }

  addUser(user: IUser) {
    return this.http.post<any>(this._userAddUrl, user);
  }

  captureUser(user_id: any, image: any) {
    return this.http.post<any>(this._userCaptureUrl + "/" + user_id, image);
  }

  deleteUser(user_id: any) {
    return this.http.delete<any>(this._userDeleteUrl + "/" + user_id);
  }

  trainClassifier() {
    return this.http.get<any>(this._trainClassifierUrl);
  }

}
