import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { IAttendance } from '../interface/iattendance';

@Injectable({
  providedIn: 'root'
})
export class AttendanceService {
  _attendanceUrl = "http://localhost:5000//attendance";

  constructor(private http: HttpClient) { }

getAttendance(): Observable<IAttendance[]> {
  return this.http.get<IAttendance[]>('http://localhost:5000/attendance');
}
}
