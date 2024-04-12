import { authGuard } from './guards/auth.guard';

import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { RegisterComponent } from './comp/register/register.component';
import { LoginComponent } from './comp/login/login.component';
import { DashboardComponent } from './comp/dashboard/dashboard.component';
import { AttendanceComponent } from './comp/attendance/attendance.component';
import { UserListComponent } from './comp/user-list/user-list.component';
const routes: Routes = [
  { path: '', redirectTo: '/dashboard', pathMatch: 'full' },
  { path: 'dashboard', component: DashboardComponent },
  { path: 'register', component: RegisterComponent },
  { path: 'login', component: LoginComponent },
  { path: 'attendance', component: AttendanceComponent, canActivate: [authGuard] },
  { path: 'users', component: UserListComponent, canActivate: [authGuard], title: 'Dashboard' }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
export const routingComponents = [RegisterComponent, LoginComponent, 
  DashboardComponent,
  UserListComponent, 
  AttendanceComponent];