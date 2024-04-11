import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { AppComponent } from './app.component';
import { AppRoutingModule } from './app-routing.module';

import { routingComponents } from './app-routing.module';

import { ReactiveFormsModule } from '@angular/forms';
import { NgbAlertModule, NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { CommonModule } from '@angular/common';
import { HTTP_INTERCEPTORS, HttpClientModule } from '@angular/common/http';
import { TokenInterceptorService } from './services/token-interceptor.service';
import { DashboardComponent } from './comp/dashboard/dashboard.component';


@NgModule({
  declarations: [
    AppComponent,
    routingComponents,
    DashboardComponent],
  imports: [
    BrowserModule,
    AppRoutingModule,
    NgbModule,
    CommonModule,
    HttpClientModule,
    ReactiveFormsModule,
    NgbAlertModule
  ],
  providers: [ { provide: HTTP_INTERCEPTORS, useClass: TokenInterceptorService, multi: true}],
  bootstrap: [AppComponent]
})
export class AppModule { }
