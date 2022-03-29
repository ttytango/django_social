import {Component, OnDestroy, OnInit} from '@angular/core';
import { ProfileService } from './profile.service';
import {map, Subject, Subscription, takeUntil} from "rxjs";
import { IProfile } from './profile';
import {AuthService, User} from "../auth/auth.service";
import {Emitters} from "../shared/emitter-utils";

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.scss']
})
export class ProfileComponent implements OnInit, OnDestroy {
  profiles: IProfile[] = [];
  currentUser;
  // currentUserSub = Subscription;
  private destroy$ = new Subject<boolean>();
  isAuthenticated: boolean = false;


  constructor(
    private profileService: ProfileService,
    private authService: AuthService
  ) { }

  ngOnInit(): void {
      this.profileService.getProfiles().pipe(
      (takeUntil(this.destroy$)),
      map(profileData => {
        this.profiles = profileData;
      })
    ).subscribe(
      data => this.profileService.notify(data)
    )

     this.authService.getCurrentUser()
       .pipe(takeUntil(this.destroy$), map(data => this.currentUser = data))
       .subscribe((response: any) => {
         this.isAuthenticated = true;
         Emitters.authEmitter.emit(true)
       }),
         error => {
         Emitters.authEmitter.emit(false)
       }

  }

  ngOnDestroy() {
    this.destroy$.next(true);
    this.destroy$.unsubscribe();
  }

}
