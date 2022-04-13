The initial django app was created a few months ago as a bit of practice.
It has an email file-based backed, so if you forget passwords, look for the email in the sent_emails folder.

I decided to add an api route to it very recently. Whilst the api authentication works and the api can be consumed on the frontend, the angular app itself, apart from some initial routing and the register/login form, has not been developed (django's view and template system has been built out more).

To continue:
- Auth Backend for API √
- Login/logout frontend √
- Auth Guard Frontend
- Add tailwind and start to build out frontend √
- Investigate: Several models aren't in use
- Move to MySql

