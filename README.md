# ECB_pwnage
Python script to auto-generate a privileged cookie, abusing a ECB encryption.

## POC
We have a login & register form, we can enumerate users on register form, detecting an admin username. That's going to be our objective, log in with admin account.

<img src="/img/screen1.png" width="500" height="506">

Knowing that the authentication is using ECB encryption we can use the python script to auto generate an authenticated cookie for us.

<img src="/img/screen2.png" width="1200" height="480">

After that, we just need to copy the cookie and change it in our burp session. And we have succesfully logged in as admin!

<img src="/img/session3.png" width="1100" height="362">


