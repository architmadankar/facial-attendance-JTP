import { User } from '../class/user';
import { Injectable } from '@angular/core';
import { Router } from '@angular/router';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  private _registerUrl = "http://localhost:5000//admin/register";
  private _loginUrl = "http://localhost:5000//admin/login";

  constructor(private http: HttpClient, private _router: Router) { }

  registerUser(user: User){
    return this.http.post<any>(this._registerUrl, user)
  }

  loginUser(user: User){
    return this.http.post<any>(this._loginUrl, user);
  }


  loggedIn(){
    return !!localStorage.getItem('access_token');
  }

  logoutUser(){
    localStorage.removeItem('access_token');
    this._router.navigate(['/login']);
  }

  getToken(){
    return localStorage.getItem('access_token');
  }
}
