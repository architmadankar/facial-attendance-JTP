import { Component, OnInit } from '@angular/core';
import { FormBuilder, Validators, FormGroup } from '@angular/forms';
import { AuthService } from '../../services/auth.service';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent implements OnInit {

  // registerUserModel = new User('', '');
  // registrationForm: FormGroup;
  submitted = false;
  errorMsg = '';
  responseMsg = '';
  passwordPattern = /^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$/;
  registrationForm!: FormGroup;
  constructor(private _auth: AuthService, private fb: FormBuilder) { }

  ngOnInit(): void {
    this.registrationForm = this.fb.group({
      username: ['', [Validators.required, Validators.minLength(4)]],
      password: ['', [Validators.required, Validators.pattern(this.passwordPattern)]]
    });
  
  }


  get username(){
    return this.registrationForm.get('username');
  }

  get password(){
    return this.registrationForm.get('password');
  }

  registerUser(){
    this.submitted = true;
    this._auth.registerUser(this.registrationForm.value).subscribe({
      next: res => {
        this.responseMsg = res.message;
        this.errorMsg = '';
      },
      error: err => {
        this.errorMsg = err.error.message;
        this.responseMsg = '';
      }
  });
  }
}
