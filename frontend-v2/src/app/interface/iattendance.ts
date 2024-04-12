import { Time } from '@angular/common';
import { Iuser } from './iuser';

export interface IAttendance {
    date: Date,
    user: Iuser[],
    time: Time
}