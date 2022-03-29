import { Component, OnInit } from '@angular/core';
import { ProfileService } from './profile.service';
import { map } from "rxjs";
import { IProfile } from './profile';

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.scss']
})
export class ProfileComponent implements OnInit {
  profiles: IProfile[] = [];

  constructor(
    private profileService: ProfileService
  ) { }

  ngOnInit(): void {
    this.profileService.getProfiles().pipe(
      map(profileData => {
        this.profiles = profileData;
      })
    ).subscribe(
      data => this.profileService.notify(data)
    )
  }

}
