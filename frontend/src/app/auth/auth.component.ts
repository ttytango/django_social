import { Component, OnInit } from '@angular/core';
import {FormBuilder, FormGroup} from '@angular/forms';
import { AuthService } from './auth.service';

@Component({
  selector: 'app-auth',
  templateUrl: './auth.component.html',
  styleUrls: ['./auth.component.scss']
})
export class AuthComponent implements OnInit {
  public user: any;
  public isLoginMode = false;
  authForm: FormGroup;

  constructor(
    private fb: FormBuilder,
    private authService: AuthService
  ) { }

  ngOnInit() {
    this.authForm = this.fb.group({
      email: '',
      password: '',
    })
  }

  onSubmit(): void {
    this.isLoginMode ?
      this.authService.loginUser(this.authForm) :
      this.authService.registerUser(this.authForm)
  }


  onSwitchMode() {
    this.isLoginMode = !this.isLoginMode;
  }

  // refreshToken() {
  //   this.authService.refreshToken();
  // }
  //
  // logout() {
  //   this.authService.logout();
  // }


}
