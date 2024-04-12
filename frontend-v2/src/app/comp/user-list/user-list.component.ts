import { Component, OnInit } from '@angular/core';
import { Iuser } from '../../interface/iuser';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { UserService } from '../../services/user.service';

@Component({
  selector: 'app-user-list',
  templateUrl: './user-list.component.html',
  styleUrl: './user-list.component.css'
})
export class UserListComponent implements OnInit{

  userForm: FormGroup;
  public formIsCollapsed = true;
  public users: Iuser[] = [];

  addRespMsg: string = '';
  deleteRespMsg: string = '';

  constructor(
    private _userService: UserService, private fb: FormBuilder,
    private _router: Router, private route: ActivatedRoute){}

  ngOnInit(): void{
    this.userForm = this.fb.group({
      name: ['', Validators.required]
    });

    this._userService.getUsers().subscribe(data => this.users = data);

  });
}
