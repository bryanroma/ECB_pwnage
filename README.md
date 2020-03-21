# ECB_pwnage
Python script to auto-generate a privileged cookie, abusing a ECB encryption. 

## Exploit

The script will create different users adding some rubbish chars (b's), then compare the encrypted cookie HEX to guess the corresponding encrypted portion to the assigned b's, after detecting the b's , an authenticated cookie is generated based on the rest of the username.



## POC
We have a login & register form, we can enumerate users on register form, detecting an admin username. That's going to be our objective, log in with admin account.

<img src="/img/screen1.png" width="500" height="506">

Knowing that the authentication is using ECB encryption we can use the python script to auto generate an authenticated cookie for us.

If you look closely 2 users are created `bbbbbbb` and `bbbbbbbadmin` , in the first line of each we get the base64 of the encrypted value, on the second we have the decoded base64 in hex, after that, compare them to detect the HEX values assigned to the b's, encode the rest of the string (admin) and GG.

<img src="/img/screen2.png" width="1200" height="480">

After that, we just need to copy the cookie and change it in our burp session. And we have succesfully logged in as admin!

<img src="/img/session3.png" width="1100" height="362">


