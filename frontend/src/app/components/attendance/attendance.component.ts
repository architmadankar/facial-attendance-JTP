import { Component, OnInit } from '@angular/core';
import { IAttendance } from '../../inter/attendance';
import { AttendanceService } from '../../services/attendance.service';


@Component({
  selector: 'app-attendance',
  templateUrl: './attendance.component.html',
  styleUrls: ['./attendance.component.css']
})
export class AttendanceComponent implements OnInit {

  public attendances: IAttendance[] = [];

  constructor(private _attendanceService: AttendanceService) { }

  ngOnInit(): void {
    this._attendanceService.getAttendanceList()
      .subscribe({
      next:  (res) => this.attendances = res,
      error:  (err: any) => console.error('There was an error: ', err)
  });
  }

}
