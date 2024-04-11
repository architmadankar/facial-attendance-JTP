import { Component, OnInit } from '@angular/core';
import { DashboardService } from '../../services/dashboard.service';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrl: './dashboard.component.css'
})
export class DashboardComponent {
  respMsg = '';
  err = '';

  constructor (private _dashboardService: DashboardService) {}

  ngOnInit(): void{
    this._dashboardService.getDashboard()
      .subscribe({
        next: res => {
          this.respMsg = res.message;
          this.err = "";
        },
        error: err => {
          if (err.status === 401) {
            this.err = err.error.message;
            this.respMsg = "";
          }
        }
  }) 
  }
}
