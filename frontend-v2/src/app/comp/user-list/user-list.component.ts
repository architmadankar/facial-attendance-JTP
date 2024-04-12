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

  userForm: FormGroup =  new FormGroup({});
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

    this._userService.getUserList().subscribe({
      next: data => { 
        this.users = data;  
      } 
    });
  }
  get name(){
    return this.userForm.get('name');
  }

  addUser(){
    console.log(this.userForm.value);
    this._userService.addUser(this.userForm.value).subscribe(data => {
      this.captureFaces(data.id);
    });
  }

  captureFaces(user_id: number){
    this._router.navigate(['capture/'+ user_id], {relativeTo: this.route});
  }
  deleteUser(user_id: number, index: number){
    this._userService.deleteUser(user_id).subscribe(data => {
      this.deleteRespMsg = '';
      this.deleteRespMsg = data.msg;
      this.users.splice(index, 1);
    });
  }
}
