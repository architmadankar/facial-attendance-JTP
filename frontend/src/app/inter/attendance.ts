import { Time } from '@angular/common';
import { IUser } from './user';

export interface IAttendance {
    date: Date,
    users: IUser,
    time: Time
}