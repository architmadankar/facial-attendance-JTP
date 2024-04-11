import { HttpBackend, HttpClient } from '@angular/common/http';
import { Injectable, Injector } from '@angular/core';
import { AuthService } from './auth.service';

@Injectable({
  providedIn: 'root'
})
export class DashboardService {

  private _dashboardUrl = 'http://localhost:5000/dashboard';
  private _httpWH: HttpClient;

  constructor(private _injector: Injector, private http: HttpClient, private handler: HttpBackend) {
    this._httpWH = new HttpClient(handler);
  }
  getDashboard() {
    let _authService = this._injector.get(AuthService);
    if (_authService.getToken()) {
      return this.http.get<any>(this._dashboardUrl);
    }
    return this._httpWH.get<any>(this._dashboardUrl);
  }
}
