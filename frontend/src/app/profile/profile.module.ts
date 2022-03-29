import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ProfileComponent } from './profile.component';
import { RouterModule, Routes} from '@angular/router';
import { UserComponent } from './user/user.component';

const profileRoutes: Routes = [
  {
    path: '',
    component: ProfileComponent
  },
  {
    path: ':user',
    component: UserComponent,
    children: [
        {
          path: 'posts',
          loadChildren: () => import('../posts/posts.module').then(m => m.PostsModule)
        },
    ]
  },
]

@NgModule({
  declarations: [
    ProfileComponent,
    UserComponent
  ],
  imports: [
    CommonModule,
    RouterModule.forChild(profileRoutes)
  ]
})
export class ProfileModule { }
