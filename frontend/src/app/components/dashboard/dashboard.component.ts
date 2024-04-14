import { Component, OnInit } from '@angular/core';
import { HttpErrorResponse } from '@angular/common/http';
import { DashboardService } from '../../services/dashboard.service';
@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit {

  responseMsg = "";
  errorMsg = "";

  constructor(private _dashboardService: DashboardService) { }

  ngOnInit(): void {
    this._dashboardService.getDashboard().subscribe(
      res => {
        this.errorMsg = "";
        this.responseMsg = res.message;
      },
      err => {
        if (err instanceof HttpErrorResponse){
          if (err.status === 401){
            this.responseMsg = "";
            this.errorMsg = err.error.message;
          }
        }
      }
    );
  }

}
