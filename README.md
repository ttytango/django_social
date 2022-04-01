The initial django app was created a few months ago as a bit of practice.
It has an email file-based backed, so if you forget passwords, look for the email in the sent_emails folder.

I decided to add an api route to it very recently. Whilst the api authentication works and the api can be consumed on the fronted, the app itself apart from some initial routing and the register/login form has been developed the app hasn't been built on the frontend yet (other than through django's view and template system).

To continue:
- Auth Backend for API
- Auth Guard Frontend
- Add tailwind and build out frontend
- Several models aren't in use
- Move to MySql
