# 1st Step
  
Thanks to the video we know that we have to "FIND this first file who can run only as flag00..."  
[find](http://www.linux-france.org/article/memo/node126.html) command will be helpful  
  
```
level00@SnowCrash:~$ find / -user flag00 2>/dev/null
/usr/sbin/john
level00@SnowCrash:~$ cat /usr/sbin/john
cdiiddwpgswtgt
level00@SnowCrash:~$ su flag00
Password: cdiiddwpgswtgt
su: Authentification failure
```  
  
The password must be encode, let [dcode](https://www.dcode.fr/) help us  
  
# 2nd Step
  
Probably by chance, [dcode](https://www.dcode.fr/) proposed me to use the cesar encode tool first so I used it :)  
Then its returned me : **nottoohardhere** *(ROT15)*  
Let's try it  
```
level00@SnowCrash:~$ su flag00
Password:
Don't forget to launch getflag !
flag00@SnowCrash:~$ getflag
Check flag.Here is your token : x24ti5gi3x0ol2eh4esiuxias
flag00@SnowCrash:~$ su level01
Password:
level01@SnowCrash:~$
```  
Level00 passed !
