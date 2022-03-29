export interface IProfile {
  user: number;
  first_name: string;
  last_name: string;
  middle_names?: string;
  locality?: string,
  profile_image?: string,
  friends?: Array<any>,
  expertise?: Array<any>;
}
