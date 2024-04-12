import { Component, OnInit } from '@angular/core';
import { IAttendance } from '../../interface/iattendance';
import { AttendanceService } from '../../services/attendance.service';
import { Iuser } from '../../interface/iuser';

@Component({
  selector: 'app-attendance',
  templateUrl: './attendance.component.html',
  styleUrl: './attendance.component.css'
})
export class AttendanceComponent implements OnInit {
  public attendances: IAttendance[] = [];
  public users: Iuser[] = [];
  constructor(private _attendanceService: AttendanceService) { }

  ngOnInit(): void {
    this._attendanceService.getAttendance()
      .subscribe(res => this.attendances = res);

  }

}
