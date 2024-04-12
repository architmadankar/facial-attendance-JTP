import { Component, OnInit } from '@angular/core';
import { IAttendance } from '../../interface/iattendance';
import { AttendanceService } from '../../services/attendance.service';

@Component({
  selector: 'app-attendance',
  templateUrl: './attendance.component.html',
  styleUrl: './attendance.component.css'
})
export class AttendanceComponent implements OnInit {
  public attendances: IAttendance[] = [];
  constructor(private _attendanceService: AttendanceService) { }

  ngOnInit(): void {
    this._attendanceService.getAttendance()
      .subscribe({
      next:  res => this.attendances = res,
      error:  err => console.error('There was an error: ', err)
  });
  }

}
