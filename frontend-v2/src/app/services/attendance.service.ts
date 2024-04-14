import { IAttendance } from '../interface/iattendance';
import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class AttendanceService {

  constructor(private http: HttpClient) { }

getAttendance(): Observable<IAttendance[]> {
  return this.http.get<IAttendance[]>('http://localhost:5000/attendance');
}
}
