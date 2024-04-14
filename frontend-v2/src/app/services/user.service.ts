import { Observable } from 'rxjs';
import { Iuser } from '../interface/iuser';
import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class UserService {
  _trainUrl = 'http://localhost:5000/users/train';
  _userListURl = 'http://localhost:5000/users';
  _addUserURL = 'http://localhost:5000/users/add';
  _deleteUserURL = 'http://localhost:5000/users/delete';
  _captureUserURL = 'http://localhost:5000/users/cap';

  constructor(private http: HttpClient) { }

  getUserList(): Observable<Iuser[]>{
    return this.http.get<Iuser[]>(this._userListURl);
  }
  addUser(user: Iuser){
    return this.http.post<any>(this._addUserURL, user);
  }

  deleteUser(user_id: any){
    return this.http.delete<any>(this._deleteUserURL + "/" + user_id);
  }

  captureUser(user_id: any, image: any){
    return this.http.post<any>(this._captureUserURL + "/" + user_id, image);
  }
  trainClassifier(){
    return this.http.get<any>(this._trainUrl);
  }
}
