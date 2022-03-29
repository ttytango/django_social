import { Component, OnInit } from '@angular/core';
import {ProfileService} from "../profile.service";
import {map} from "rxjs";
import {ActivatedRoute, Router} from '@angular/router';

@Component({
  selector: 'app-user',
  templateUrl: './user.component.html',
  styleUrls: ['./user.component.scss']
})
export class UserComponent implements OnInit {
 user;

  constructor(
    private profileService: ProfileService,
    private route: ActivatedRoute,
    private router: Router
  ) { }

  ngOnInit(): void {
    const id = +this.route.snapshot.params['user']
    this.profileService.getSingleProfile(id).pipe(
      map(profileData => {
        this.user = profileData;
      })
    ).subscribe(
      data => this.profileService.notify(data)
    )
  }

  back() {
    this.router.navigate(['profiles'])
  }
}
