import { Component, OnInit } from '@angular/core';
import { AuthService } from '../../services/auth.service';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrl: './register.component.css'
})
export class RegisterComponent implements OnInit{

  submit = false;
  err = '';
  respMsg = '';
  paswdRegex =/^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{6,}$/;
  regFrom!: FormGroup;

  constructor(private _auth: AuthService, private fb: FormBuilder) { }

  ngOnInit(): void {
    this.regFrom = this.fb.group({
      username: ['' ],
      password: ['']
    });
  }

  // regFrom = this.fb.group({
  //   username: ['',Validators.required, Validators.minLength(3) ],
  //   password: ['',Validators.pattern(this.paswdRegex), Validators.required, Validators.minLength(6)]
  // });
  get username(){ return this.regFrom.get('username'); }
  get password(){ return this.regFrom.get('password'); }

  registerUser(){
    this.submit = true;
    this._auth.registerUser(this.regFrom.value).subscribe({
      next: (res) => {
        this.respMsg = res.message;
        this.err = '';
      },
      error: (err) => {
        this.err = err.error.message;
        this.respMsg = '';
      }
  });
  }
}
