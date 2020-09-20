# 1st Step  
List the files in level09 user home directory to find 'level09' executable and 'token' file owned by `flag09` user  
```
level09@SnowCrash:~$ cat token
f4kmm6p|=pnDBDu{
level09@SnowCrash:~$
```
The token looks like crypted and it does'nt work as password for `flag09` user  
Let's try to understand how 'level09' executable work  
```
level09@SnowCrash:~$ ./level09
You need to provied only one arg.
level09@SnowCrash:~$ ./level09 token
tpmhr
level09@SnowCrash:~$ ./level09 a
a
level09@SnowCrash:~$ ./level09 b
b
level09@SnowCrash:~$ ./level09 c
c
level09@SnowCrash:~$ ./level09 abc
ace
```
It seems that 'level09' executable encrypt the string passed as argument by adding to each character its own index  
Let's try with our token :  
```
level09@SnowCrash:~$ ./level09 'f4kmm6p|=pnDBDu{'
f5mpq;vEyxONQ
level09@SnowCrash:~$ su flag09
Password:
su: Authentication failure
level09@SnowCrash:~$
```
The token must be already crypted by 'level09', we should try to decrypt it !  

# 2nd Step
Now we can build a simple script that will reverse the encrypted file by subtract to each character its own index (see decrypt.py)  
You can copy decrypt.py (first line on your local machine, not on your VM)  
```
~/Snow-Crash/level09/Ressources$ scp -P 4242 decrypt.py level09@172.20.10.11:/tmp/.
level09@SnowCrash:~$ python /tmp/decrypt.py `cat token`
f3iji1ju5yuevaus41q1afiuq
level09@SnowCrash:~$ su flag09
Password:
Don't forget to launch getflag !
flag09@SnowCrash:~$ getflag
Check flag.Here is your token : s5cAJpM8ev6XHw998pRWG728z
flag09@SnowCrash:~$ su level10
Password:
level10@SnowCrash:~$
```
level09 passed !
