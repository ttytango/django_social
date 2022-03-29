import { Component, OnInit } from '@angular/core';
import { Emitters } from '../emitter-utils';
import {AuthService} from "../../auth/auth.service";

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.scss']
})
export class HeaderComponent implements OnInit {
  isAuthenticated: boolean = false;

  constructor(private authService: AuthService) { }

  ngOnInit(): void {
    Emitters.authEmitter.subscribe(
      (auth: boolean) => {
        this.isAuthenticated = auth;
      }
    )
  }

  logout() {
    this.authService.logout();
    this.authService.notify(data => console.log(data))
    this.isAuthenticated = false;
  }

}
