import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {environment} from "../../environments/environment";
import {IProfile} from "./profile";
import { Observable, Subject } from "rxjs";

@Injectable({
  providedIn: 'root'
})
export class ProfileService {
  private url: string = environment.apiUrl;
  subject: Subject<any> = new Subject();
  obs: Observable<any> = this.subject.asObservable();



  constructor(
    private http: HttpClient
  ) { }


  notify = (data: any) => {
    this.subject.next(data)
  }

  getProfiles() {
    return this.http.get<IProfile[]>(this.url + '/profiles')
  }

  getSingleProfile(id: number) {
    return this.http.get<IProfile[]>(this.url + `/profiles/${id}`)
  }
}
