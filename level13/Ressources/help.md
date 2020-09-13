level13@SnowCrash:~$ ls -l
total 8
-rwsr-sr-x 1 flag13 level13 7303 Aug 30  2015 level13
level13@SnowCrash:~$ strings level13
/lib/ld-linux.so.2
__gmon_start__    
libc.so.6
_IO_stdin_used
exit
strdup
printf
getuid
__libc_start_main
GLIBC_2.0
PTRh`
UWVS
[^_]
0123456
UID %d started us but we we expect %d    
boe]!ai0FB@.:|L6l@A?>qJ}I
your token is %s
;*2$"$
GCC: (Ubuntu/Linaro 4.6.3-1ubuntu5) 4.6.3
.symtab
.strtab
.shstrtab
.interp
.note.ABI-tag
.note.gnu.build-id
.gnu.hash
.dynsym
.dynstr
.gnu.version
.gnu.version_r
.rel.dyn
.rel.plt
.init
.text
.fini
.rodata
.eh_frame_hdr
.eh_frame
.ctors
.dtors
.jcr
.dynamic
.got
.got.plt
^?ELF^A^A^A^@^@^@^@^@^@^@^@^@^B^@^C^@^A^@^@^@À<83>^D^H4^@^@^@H^Q^@^@^@^@^@^@4^@ ^@      ^@(^@^^^@^[^@^F^@^@^@4^@^@^@4<80>^D^H4<80>^D^H ^A^@^@ ^A^@^@^E^@^@^@^D^@^@^@^C^@^@^@T^A^@^@T<81>^D^HT<81>^D^H^S^@^@^@^S^@^@^@^D^@^@^@^A^@^@^@^A^@^@^@^@^@^@^@^@<80>^D^H^@<80>^D^HD^H^@^@D^H^@^@^E^@^@^@^@^P^@^@^A^@^@^@^T^O^@^@^T<9f>^D^H^T<9f>^D^H^L^A^@^@^T^A^@^@^F^@^@^@^@^P^@^@^B^@^@^@(^O^@^@(<9f>^D^H(<9f>^D^HÈ^@^@^@È^@^@^@^F^@^@^@^D^@^@^@^D^@^@^@h^A^@^@h<81>^D^Hh<81>^D^HD^@^@^@D^@^@^@^.data
.bss
.comment
crtstuff.c
__CTOR_LIST__
__DTOR_LIST__
__JCR_LIST__
__do_global_dtors_aux
completed.6159
dtor_idx.6161
frame_dummy
__CTOR_END__
__FRAME_END__
__JCR_END__
__do_global_ctors_aux
level13_back.c
__init_array_end
_DYNAMIC
__init_array_start
_GLOBAL_OFFSET_TABLE_
__libc_csu_fini
__i686.get_pc_thunk.bx
data_start
ft_des
printf@@GLIBC_2.0
strdup@@GLIBC_2.0
_edata
_fini
getuid@@GLIBC_2.0
__DTOR_END__
__data_start
__gmon_start__
exit@@GLIBC_2.0
__dso_handle
_IO_stdin_used
__libc_start_main@@GLIBC_2.0
__libc_csu_init
_end
_start
_fp_hw
__bss_start
main
_Jv_RegisterClasses
_init
level13@SnowCrash:~$ level13 5
level13: command not found
level13@SnowCrash:~$ level13 getflag
level13: command not found
level13@SnowCrash:~$ level13 0123456
level13: command not found
level13@SnowCrash:~$ level13 "0123456"
level13: command not found
level13@SnowCrash:~$ ./level13 4242
UID 2013 started us but we we expect 4242
level13@SnowCrash:~$ ./level13 getflag
UID 2013 started us but we we expect 4242
level13@SnowCrash:~$ vim level13
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
(gdb) p $eax=0x1092
No registers.
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
(gdb) p $eax=0x1092
No registers.
(gdb) print $eax
No registers.
(gdb) b getuid
Breakpoint 1 at 0x8048380
(gdb) run
Starting program: /home/user/level13/level13

Breakpoint 1, 0xb7ee4cc0 in getuid () from /lib/i386-linux-gnu/libc.so.6
(gdb) step
Single stepping until exit from function getuid,
which has no line number information.
0x0804859a in main ()
(gdb) print $eax
$1 = 2013
(gdb) p $eax=0x1092
$2 = 4242
(gdb) set $eax=4242
(gdb) step
Single stepping until exit from function main,
which has no line number information.
your token is 2A31L79asukciNyi8uppkEuSx
0xb7e454d3 in __libc_start_main () from /lib/i386-linux-gnu/libc.so.6
(gdb) exit
Undefined command: "exit".  Try "help".
(gdb) quit
A debugging session is active.

        Inferior 1 [process 2653] will be killed.

Quit anyway? (y or n) y
level13@SnowCrash:~$ su level14
Password:
level14@SnowCrash:~$





Premiere étape de recherche

$ ls -la
-rwsr-sr-x 1 flag13  level13 7303 Aug 30  2015 level13
On trouve un binaire setuid/setgid

$ ./level13
UID 2013 started us but we we expect 4242
Il demande a etre executé par un uid specifique

Regardons sa zone text avec strings

$ strings level13
...
UID %d started us but we we expect %d
boe]!ai0FB@.:|L6l@A?>qJ}I
your token is %s
...
On dirait bien le token hashé?

Regardons avec GDB

$ gdb level13
(gdb) disas main
Dump of assembler code for function main:
   0x0804858c <+0>:		push   %ebp
   0x0804858d <+1>:		mov    %esp,%ebp
   0x0804858f <+3>:		and    $0xfffffff0,%esp
   0x08048592 <+6>:		sub    $0x10,%esp
   0x08048595 <+9>:		call   0x8048380 <getuid@plt>
   0x0804859a <+14>:	cmp    $0x1092,%eax
   0x0804859f <+19>:	je     0x80485cb <main+63>
   0x080485a1 <+21>:	call   0x8048380 <getuid@plt>
   0x080485a6 <+26>:	mov    $0x80486c8,%edx
   0x080485ab <+31>:	movl   $0x1092,0x8(%esp)
   0x080485b3 <+39>:	mov    %eax,0x4(%esp)
   0x080485b7 <+43>:	mov    %edx,(%esp)
   0x080485ba <+46>:	call   0x8048360 <printf@plt>
   0x080485bf <+51>:	movl   $0x1,(%esp)
   0x080485c6 <+58>:	call   0x80483a0 <exit@plt>
   0x080485cb <+63>:	movl   $0x80486ef,(%esp)
   0x080485d2 <+70>:	call   0x8048474 <ft_des>
   0x080485d7 <+75>:	mov    $0x8048709,%edx
   0x080485dc <+80>:	mov    %eax,0x4(%esp)
   0x080485e0 <+84>:	mov    %edx,(%esp)
   0x080485e3 <+87>:	call   0x8048360 <printf@plt>
   0x080485e8 <+92>:	leave
   0x080485e9 <+93>:	ret
End of assembler dump.
Le check est fait avec getuid a la ligne +9, il faut le forcer a retourner un faux uid

On met un breakpoint sur la fonction getuid

(gdb) b getuid
On lance le programme

(gdb) run
Starting program: /home/user/level13/level13

Breakpoint 2, 0xb7ee4cc0 in getuid () from /lib/i386-linux-gnu/libc.so.6
On avance step by step jusqu'au return du getuid

(gdb) step
Single stepping until exit from function getuid,
which has no line number information.
0x0804859a in main ()
On regarde le registre eax ou est stocké la valeur de retour de getuid (https://opensourceforu.com/2011/08/modify-function-return-value-hack-part-1/)

(gdb) print $eax
$1 = 2013
C'est bien ça, on la change pour 4242, le uid attendu par le programme

(gdb) set $eax=4242

(gdb) step
Single stepping until exit from function main,
which has no line number information.
your token is machin truc bidule