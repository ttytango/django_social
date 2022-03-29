import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {environment} from "../../environments/environment";
import { Router } from '@angular/router';
import {map, Observable, Subject} from "rxjs";
import { IProfile } from '../profile/profile';

export class User {
  constructor(public email: string, public id: string) { }
}

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  url: string = environment.apiUrl;
  subject: Subject<any> = new Subject();
  obs: Observable<any> = this.subject.asObservable();
  users: User[] = [];


  constructor(
    private http: HttpClient,
    private router: Router
  ) {}

  notify = (data: any) => {
    this.subject.next(data)
  }

  registerUser(form) {
      return this.http.post(this.url + '/register/', form.getRawValue())
        .subscribe(response => console.log(response))
  }

  loginUser(form) {
      return this.http.post(this.url + '/login/', form.getRawValue(), {
        withCredentials: true
      }).subscribe(() => this.router.navigate(['/']))
  }

  getCurrentUser(): Observable<User[]> {
    return this.http.get<User[]>(this.url + '/user/', {withCredentials: true})
      .pipe(
        map((response: User[]) => {
          return this.users = response
        })
    )
  }

  logout() {
    return this.http.post(this.url + '/logout/', {}, {withCredentials: true})
      .subscribe(() => this.router.navigate(['/auth']))
  }


}
