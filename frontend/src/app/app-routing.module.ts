import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { UserAuthGuard } from './guards/user-auth.guard';

import { DashboardComponent } from './components/dashboard/dashboard.component';
import { RegisterComponent } from './components/register/register.component';
import { LoginComponent } from './components/login/login.component';
import { VideoPreviewComponent } from './components/video-preview/video-preview.component';
import { VideoListComponent } from './components/video-list/video-list.component';
import { UserListComponent } from './components/user-list/user-list.component';
import { UserCaptureComponent } from './components/user-capture/user-capture.component';
import { AttendanceComponent } from './components/attendance/attendance.component';
import { ErrorComponent } from './components/error/error.component';


const routes: Routes = [
  { path: '', redirectTo: '/register', pathMatch: 'full' },
  { path: 'dashboard', component: DashboardComponent },
  { path: 'register', component: RegisterComponent },
  { path: 'login', component: LoginComponent },
  { path: 'video', component: VideoListComponent, canActivate:[UserAuthGuard] },
  { path: 'video/preview/:feed_id', component: VideoPreviewComponent, canActivate:[UserAuthGuard] },
  { path: 'users', component: UserListComponent, canActivate:[UserAuthGuard] },
  { path: 'users/cap/:user_id', component: UserCaptureComponent, canActivate:[UserAuthGuard] },
  { path: 'attendance', component: AttendanceComponent, canActivate:[UserAuthGuard] },
  { path: '**', component: ErrorComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
export const routingComponents = [
  DashboardComponent, 
  RegisterComponent, LoginComponent, 
  VideoListComponent, VideoPreviewComponent, 
  UserListComponent, UserCaptureComponent,
  AttendanceComponent, 
  ErrorComponent
]
