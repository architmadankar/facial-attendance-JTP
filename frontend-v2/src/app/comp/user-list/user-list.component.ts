import { Component, OnInit } from '@angular/core';
import { Iuser } from '../../interface/iuser';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { UserService } from '../../services/user.service';
import { faTrashAlt } from '@fortawesome/free-solid-svg-icons';

@Component({
  selector: 'app-user-list',
  templateUrl: './user-list.component.html',
  styleUrls: ['./user-list.component.css'], 
})

export class UserListComponent implements OnInit {

  userForm!: FormGroup;
  public formIsCollapsed = true;
  public x: Iuser[] = [];

  addRespMsg: string = '';
  deleteRespMsg: string = '';
  trashIcon = faTrashAlt;

  constructor(
    private _userService: UserService, 
    private fb: FormBuilder,
    private _router: Router, 
    private route: ActivatedRoute
  ) { }

  ngOnInit(): void{
    this.userForm = this.fb.group({
      name: ['', Validators.required]
    });
    this._userService.getUserList().subscribe(
      data => {
        this.x = data;
      },
      error => {
        console.log(error);
      }
    );
  }

  get name() {
    return this.userForm.get('name');
  }

  addUser() {
    console.log(this.userForm.value);
    this._userService.addUser(this.userForm.value).subscribe(
      data => {
        this.captureFaces(data.id)
      }
    );
  }

  captureFaces(user_id: any) {
    this._router.navigate(['cap/' + user_id], { relativeTo: this.route });
  }

  deleteUser(user_id: any, index: any) {
    this._userService.deleteUser(user_id).subscribe(
      data => {
        this.addRespMsg ='';
        this.deleteRespMsg = data.message;
        this.x.splice(index, 1);
      },
      error => {
        console.log(error);
      }
    );
  }
}