import { Component, OnInit } from '@angular/core';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';
import { Router, ActivatedRoute } from '@angular/router';
import { faTrashAlt } from '@fortawesome/free-solid-svg-icons';

import { UserService } from '../../services/user.service';
import { IUser } from '../../interfaces/user';

@Component({
  selector: 'app-user-list',
  templateUrl: './user-list.component.html',
  styleUrls: ['./user-list.component.css']
})
export class UserListComponent implements OnInit {

  trashIcon = faTrashAlt;

  userForm!: FormGroup;
  public formIsCollapsed = true;
  public users: IUser[] = [];
  
  addResponseMsg = '';
  delResponseMsg = '';

  constructor(
    private _userService: UserService, private fb: FormBuilder, 
    private _router: Router, private route: ActivatedRoute) { }

  ngOnInit(): void {
    this.userForm = this.fb.group({
      name: ['', Validators.required]
    })
    this._userService.getUserList().subscribe(
      res => {
        this.users = res;
      },
      err => {
        console.log(err);
      }
    );
  }

  get name(){
    return this.userForm.get('name');
  }

  addUser(){
    console.log(this.userForm.value);
    this._userService.addUser(this.userForm.value).subscribe(
      res => {
        this.captureFaces(res.id)
      }
    );
  }

  captureFaces(user_id:any){
    this._router.navigate(['cap/' + user_id], {relativeTo: this.route});
  }

  deleteUser(user_id:any, index:any){
    this._userService.deleteUser(user_id).subscribe(
      res => {
        this.addResponseMsg = '';
        this.delResponseMsg = res.message;
        this.users.splice(index, 1);
      },
      err => {
      }
    );
  }

}
