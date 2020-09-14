# 1st Step
List files in level13 user home directory will show us `level13` executable owned by `flag13` user :
```
level13@SnowCrash:~$ ls -l
total 8
-rwsr-sr-x 1 flag13 level13 7303 Aug 30  2015 level13
```
If we look at the executable with strings :
```
level13@SnowCrash:~$ strings level13
[...]
[^_]
0123456
UID %d started us but we we expect %d    
boe]!ai0FB@.:|L6l@A?>qJ}I
your token is %s
;*2$"$
[...]
level13@SnowCrash:~$
```
If we try to execute it we can see that the executable will check our UID
```
level13@SnowCrash:~$ ./level13
UID 2013 started us but we we expect 4242
```

# 2nd Step
Seems that we have to change our UID by a way or another, let's try it with gdb (here is a good [introduction](https://beta.hackndo.com/introduction-a-gdb/))
```
level13@SnowCrash:~$ gdb level13
GNU gdb (Ubuntu/Linaro 7.4-2012.04-0ubuntu2.1) 7.4-2012.04
Copyright (C) 2012 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.  Type "show copying"
and "show warranty" for details.
This GDB was configured as "i686-linux-gnu".
For bug reporting instructions, please see:
<http://bugs.launchpad.net/gdb-linaro/>...
Reading symbols from /home/user/level13/level13...(no debugging symbols found)...done.
(gdb) disas main
Dump of assembler code for function main:
   0x0804858c <+0>:     push   %ebp
   0x0804858d <+1>:     mov    %esp,%ebp
   0x0804858f <+3>:     and    $0xfffffff0,%esp
   0x08048592 <+6>:     sub    $0x10,%esp
   0x08048595 <+9>:     call   0x8048380 <getuid@plt>
   0x0804859a <+14>:    cmp    $0x1092,%eax
   0x0804859f <+19>:    je     0x80485cb <main+63>
   0x080485a1 <+21>:    call   0x8048380 <getuid@plt>
   0x080485a6 <+26>:    mov    $0x80486c8,%edx
   0x080485ab <+31>:    movl   $0x1092,0x8(%esp)
   0x080485b3 <+39>:    mov    %eax,0x4(%esp)
   0x080485b7 <+43>:    mov    %edx,(%esp)
   0x080485ba <+46>:    call   0x8048360 <printf@plt>
   0x080485bf <+51>:    movl   $0x1,(%esp)
   0x080485c6 <+58>:    call   0x80483a0 <exit@plt>
   0x080485cb <+63>:    movl   $0x80486ef,(%esp)
   0x080485d2 <+70>:    call   0x8048474 <ft_des>
   0x080485d7 <+75>:    mov    $0x8048709,%edx
   0x080485dc <+80>:    mov    %eax,0x4(%esp)
   0x080485e0 <+84>:    mov    %edx,(%esp)
   0x080485e3 <+87>:    call   0x8048360 <printf@plt>
   0x080485e8 <+92>:    leave
   0x080485e9 <+93>:    ret
End of assembler dump.
```
We can see that the program check the UID with the command `getuid`, we have to change the return value by 4242
```
(gdb) b getuid
Breakpoint 1 at 0x8048380
```
Launch the program
```
(gdb) run
Starting program: /home/user/level13/level13

Breakpoint 1, 0xb7ee4cc0 in getuid () from /lib/i386-linux-gnu/libc.so.6
```
Then move step by step until the return of getuid
```
(gdb) step
Single stepping until exit from function getuid,
which has no line number information.
0x0804859a in main ()
```
Let's take a look at the register `eax` where the value of our UID is stock
```
(gdb) print $eax
$1 = 2013
```
This is our UID ! Change it by 4242 (0x1092 in hexa value)
```
(gdb) p $eax=0x1092         # print to confirm that is the good value before set it
$2 = 4242                   # perfect
(gdb) set $eax=4242         # set the value
(gdb) step                  # Then continue to move step by step until the token is print
Single stepping until exit from function main,
which has no line number information.
your token is 2A31L79asukciNyi8uppkEuSx
0xb7e454d3 in __libc_start_main () from /lib/i386-linux-gnu/libc.so.6
(gdb) quit
A debugging session is active.

        Inferior 1 [process 2653] will be killed.

Quit anyway? (y or n) y
level13@SnowCrash:~$ su level14
Password:
level14@SnowCrash:~$
```

Level13 passed !