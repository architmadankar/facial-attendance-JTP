import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Iuser } from '../interface/iuser';

@Injectable({
  providedIn: 'root'
})
export class UserService {
  _trainUrl = 'http://localhost:5000/user/train';
  _userListURl = 'http://localhost:5000/user';
  _addUserURL = 'http://localhost:5000/user/add';
  _deleteUserURL = 'http://localhost:5000/user/delete';
  _captureUserURL = 'http://localhost:5000/user/cap';

  constructor(private http: HttpClient) { }

  getUserList(): Observable<Iuser[]>{
    return this.http.get<Iuser[]>(this._userListURl);
  }
  addUser(user: Iuser){
    return this.http.post<any>(this._addUserURL, user);
  }

  deleteUser(user_id: number){
    return this.http.delete<any>(this._deleteUserURL + "/" + user_id);
  }

  captureUser(user_id: number, image: any){
    return this.http.post<any>(this._captureUserURL+ "/" +user_id, image);
  }
  trainClassifier(){
    return this.http.get<any>(this._trainUrl);
  }
}
