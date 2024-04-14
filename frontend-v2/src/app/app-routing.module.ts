import { AuthGuard } from './guards/auth.guard';

import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { RegisterComponent } from './comp/register/register.component';
import { LoginComponent } from './comp/login/login.component';
import { DashboardComponent } from './comp/dashboard/dashboard.component';
import { AttendanceComponent } from './comp/attendance/attendance.component';
import { UserListComponent } from './comp/user-list/user-list.component';
import { UserCaptureComponent } from './comp/user-capture/user-capture.component';
import { VideoListComponent } from './comp/video-list/video-list.component';
import { VideoPreviewComponent } from './comp/video-preview/video-preview.component';


const routes: Routes = [
  { path: 'dashboard', component: DashboardComponent },
  { path: 'register', component: RegisterComponent },
  { path: 'login', component: LoginComponent },
  { path: 'attendance', component: AttendanceComponent, canActivate: [AuthGuard] },
  { path: 'users', component: UserListComponent, canActivate: [AuthGuard] },
  { path: 'users/cap/:user_id', component: UserCaptureComponent, canActivate: [AuthGuard] },
  { path: 'video', component: VideoListComponent, canActivate: [AuthGuard] },
  { path: 'video/preview/:feed_id', component: VideoPreviewComponent, canActivate: [AuthGuard] },
  { path: '', redirectTo: '/dashboard', pathMatch: 'full' },

];


@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
export const routingComponents = [
  RegisterComponent, LoginComponent, 
  DashboardComponent,
  UserListComponent,
  UserCaptureComponent,VideoListComponent, VideoPreviewComponent,

  AttendanceComponent];