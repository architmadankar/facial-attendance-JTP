import { DashboardService } from '../../services/dashboard.service';
import { HttpErrorResponse } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrl: './dashboard.component.css'
})
export class DashboardComponent implements OnInit {
  respMsg = '';
  err = '';

  constructor (private _dashboardService: DashboardService) {}

  ngOnInit(): void {
    this._dashboardService.getDashboard().subscribe(
      res => {
        this.err = "";
        this.respMsg = res.message;
      },
      err => {
        if (err instanceof HttpErrorResponse){
          if (err.status === 401){
            this.err = "";
            this.respMsg = err.error.message;
          }
        }
      }
    );
  }

}

