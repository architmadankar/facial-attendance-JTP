import { Component, OnInit } from '@angular/core';
import { AuthService } from '../../services/auth.service';
import { Router } from '@angular/router';
import { FormGroup, FormBuilder, Validators, FormControl } from '@angular/forms';


@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  // loginUserModel = new User('', '');
  loginForm!: FormGroup;
  errorMsg = '';

  constructor(private _auth: AuthService, private _router: Router, private fb: FormBuilder) { }

  ngOnInit() {
    this.loginForm = this.fb.group({
      username: ['', Validators.required],
      password: ['', Validators.required]
    });
  }

  get username(){
    return this.loginForm.get('username');
  }

  get password(){
    return this.loginForm.get('password');
  }

  loginUser(){
    this._auth.loginUser(this.loginForm.value).subscribe({
      next: (res) => {
        this.errorMsg = '';

        localStorage.setItem('access_token', res.access_token);
        this._router.navigate(['/dashboard']);
      },
      error: (err) => {
        this.errorMsg = err.error.message;
      }
  });
  }
}
