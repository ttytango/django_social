import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { AuthComponent } from './auth.component';
import {FormsModule} from "@angular/forms";
import { RouterModule } from '@angular/router';


const authRoutes = [
  {
    path: '',
    component: AuthComponent
  }
]

@NgModule({
  declarations: [
    AuthComponent
  ],
  imports: [
    CommonModule,
    FormsModule,
    RouterModule.forChild(authRoutes)
  ]
})
export class AuthModule { }
