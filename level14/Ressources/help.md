# 1st step
```
level14@SnowCrash:~$ ls -l
total 0
level14@SnowCrash:~$ find / -user flag14 2>/dev/null
/proc/2301
/proc/2301/*
[...]
level14@SnowCrash:~$ cat /etc/passwd
root:x:0:0:root:/root:/bin/bash
[...]
level14@SnowCrash:~$ cd /var/mail
level14@SnowCrash:/var/mail$ ls
level05
level14@SnowCrash:/var/mail$ cd
level14@SnowCrash:~$
```
Seems there is no file, no script, no executable ... nothing  

# 2nd step
We should try to debug getflag with main as we did with the `level13` executable :
```
level14@SnowCrash:~$ gdb /bin/getflag
GNU gdb (Ubuntu/Linaro 7.4-2012.04-0ubuntu2.1) 7.4-2012.04
Copyright (C) 2012 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.  Type "show copying"   
and "show warranty" for details.
This GDB was configured as "i686-linux-gnu".
For bug reporting instructions, please see:
<http://bugs.launchpad.net/gdb-linaro/>...
Reading symbols from /bin/getflag...(no debugging symbols found)...done.     
(gdb) run
Starting program: /bin/getflag 
You should not reverse this
[Inferior 1 (process 2282) exited with code 01]
```
It looks like protected.. disass the main to see if we can find something
```
(gdb) disass main
Dump of assembler code for function main:      
   0x08048946 <+0>:     push   %ebp
   [...]
   0x08048989 <+67>:    call   0x8048540 <ptrace@plt>
   [...]
   0x08048a4c <+262>:   cmpl   $0xffffffff,0x14(%esp)
   0x08048a51 <+267>:   jne    0x8048e88 <main+1346>
   0x08048a57 <+273>:   mov    0x804b040,%eax
---Type <return> to continue, or q <return> to quit---q
Quit
```
The file is protected by ptrace ! we can bypass it with a little [trick](https://gist.github.com/poxyran/71a993d292eee10e95b4ff87066ea8f2)
```
(gdb) catch syscall ptrace
Catchpoint 1 (syscall 'ptrace' [26])
(gdb) commands 1
Type commands for breakpoint(s) 1, one per line.
End with a line saying just "end".
>set $eax=0
>continue
>end
```
Good, now we can disass the main again to see if there is more protection
```
(gdb) disass main
Dump of assembler code for function main:
   0x08048946 <+0>:     push   %ebp
   [...]
   0x08048989 <+67>:    call   0x8048540 <ptrace@plt>
   [...]
   0x08048a4c <+262>:   cmpl   $0xffffffff,0x14(%esp)
   0x08048a51 <+267>:   jne    0x8048e88 <main+1346>
   0x08048a57 <+273>:   mov    0x804b040,%eax
---Type <return> to continue, or q <return> to quit---
   0x08048a5c <+278>:   mov    %eax,%edx
   [...]
   0x08048afd <+439>:   call   0x80484b0 <getuid@plt>
   [...]
   0x08048b5d <+535>:   ja     0x8048ca7 <main+865>
   0x08048b63 <+541>:   jmp    0x8048c5f <main+793>
   0x08048b68 <+546>:   cmp    $0xbc2,%eax
---Type <return> to continue, or q <return> to quit---q
Quit
```
As in the `level13` executable, a call to getuid protect it.  
There is a lot of cmp, we can assume that the program also check the UID to know what token it have to give when we tape `getflag`. We should retrieve the `flag14` UID!  
In an new terminal we can find the `flag14` UID with the command `id`
```
level14@SnowCrash:~$ id flag14
uid=3014(flag14) gid=3014(flag14) groups=3014(flag14),1001(flag)
level14@SnowCrash:~$
```
Go back to our first terminal window who is running gdb and put a breakpoint on getuid before change the value of the register `$eax` where the value of the UID is stock.
```
(gdb) b getuid
Breakpoint 2 at 0xb7ee4cc0
(gdb) run
Starting program: /bin/getflag

Catchpoint 1 (call to syscall ptrace), 0xb7fdd428 in __kernel_vsyscall ()

Catchpoint 1 (returned from syscall ptrace), 0xb7fdd428 in __kernel_vsyscall ()

Breakpoint 2, 0xb7ee4cc0 in getuid () from /lib/i386-linux-gnu/libc.so.6
```
Move step by step until the return, change `$eax` then keep moving step by step until we give you the token
```
(gdb) step
Single stepping until exit from function getuid,
which has no line number information.
0x08048b02 in main ()
(gdb) p $eax
$1 = 2014
(gdb) set $eax=3014
(gdb) step
Single stepping until exit from function main,
which has no line number information.
Check flag.Here is your token : 7QiHafiNa3HVozsaXkawuYrTstxbpABHD8CPnHJ
0xb7e454d3 in __libc_start_main () from /lib/i386-linux-gnu/libc.so.6
(gdb) quit
A debugging session is active.

        Inferior 1 [process 2291] will be killed.

Quit anyway? (y or n) y
level14@SnowCrash:~$ su flag14
Password:
Congratulation. Type getflag to get the key and send it to me the owner of this livecd :)
flag14@SnowCrash:~$ getflag
Check flag.Here is your token : 7QiHafiNa3HVozsaXkawuYrTstxbpABHD8CPnHJ
flag14@SnowCrash:~$
```

Level14 passed !
