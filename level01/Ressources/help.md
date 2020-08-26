# 1st Step
  
Traditional Unix systems keep user account information, including encrypted passwords, in a text file called `/etc/passwd` ([sources](http://www.linux-france.org/article/sys/lame/html/x829.html)).
Look at the file /etc/passwd  
`flag01@SnowCrash:~$ cat /etc/passwd`  
You should see this line:  
`flag01:42hDRfypTqqnw:3001:3001::/home/flag/flag01:/bin/bash`  
-> 42hDRfypTqqnw *Let's try this password*  
```
level01@SnowCrash:~$ su flag01
Password:
su: Authentication failure
```  
Again an encode password, this time JohnTheRipper will help us

# 2nd Step
The installation of JTR follow immediately in the file  
*On a new terminal window (out of your VM):*  
```
/Users/maxisimo:~$ echo 42hDRfypTqqnw > passwd
/Users/maxisimo:~$ cd JTR/run
/run$ ./john --show ../../passwd
?:abcdefg

1 password hash cracked, 0 left
```  
The decode password is : **abcdefg**  
Let's try it  
```
level01@SnowCrash:~$ su flag01
Password:
Don't forget to launch getflag !
flag01@SnowCrash:~$ getflag
Check flag.Here is your token : f2av5il02puano7naaf6adaaf
flag01@SnowCrash:~$ su level02
Password:
level02@SnowCrash:~$
```  
Level01 passed !
  
# John the Ripper
## Install John The Ripper on MacOsX
*On a new terminal window (out of your VM):* 
``` 
/Users/maxisimo:~$ ftp anonymous@ftp.openwall.com  
Password: anonymous
```
*If you don't have the ftp command you can see [this tutorial](https://osxdaily.com/2018/08/07/get-install-ftp-mac-os/) to install it with [homebrew](https://brew.sh/)*  
`ftp> cd pub/projects/john/contrib/macosx`  
Then download the last version you can see:  
```
ftp> ls
229 Entering Extended Passive Mode (|||51621|).
150 Here comes the directory listing.
-rw-r--r--    1 ftp      ftp          1049 Nov 27 16:25 README.txt
drwxr-xr-x    2 ftp      ftp          4096 Jan 17  2018 historical
-rw-r--r--    1 ftp      ftp      33028971 Nov 27 16:16 john-1.8.0.9-jumbo-macosx_avx2.zip
-rw-r--r--    1 ftp      ftp      32982729 Nov 27 16:15 john-1.8.0.9-jumbo-macosx_sse4.zip
226 Directory send OK.
```  
`ftp> get john-1.8.0.9-jumbo-macosx_sse4.zip`  
`ftp> quit`  
You can unzip the file with the `unzip` command  
Rename the new folder may be easier  
`mv john-1.8.0.9-jumbo-macosx_sse4 JTR`  
  
## Use John The Ripper
Consider that *JTR* is the name of the JohnTheRipper's folder that you have downloaded and renamed during the installation
```
/Users/maxisimo:~$ cd JTR/run
/run$ ./john path/to/the/file
```
Tape `./john` without argument will show you usage  
For more informations `cd ~/JTR/doc` or go to [doc](https://www.openwall.com/john/doc/)
  
*source: [Mac OSX as a Pentest Platform - 04 - John the Ripper (video)](https://youtu.be/Erfm1Erck0U)*  
  
## Install and use John The Ripper on Windows
*Follow this tutorial on youtube : [John the Ripper in Windows 10 [2020] || "Crack all passwords"](https://www.youtube.com/watch?v=iL2sbAKaBOY)*  
Then open a terminal as indicate on the tutorial and tape these commands :  
```
C:\Users\Maxime\Desktop\john-1.9.0-jumbo-1-win64\run>echo 42hDRfypTqqnw > passwd
C:\Users\Maxime\Desktop\john-1.9.0-jumbo-1-win64\run>john.exe passwd
```
Done ;)
