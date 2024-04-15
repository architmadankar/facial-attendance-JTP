import { Time } from '@angular/common';
import { IUser } from './user';

export interface IAttendance {
    date: Date,
    user: IUser,
    time: Time
}