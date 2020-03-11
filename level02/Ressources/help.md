# 1st Step
First of all you have to copy level02.pcap on your local machine with the [scp](https://linux.die.net/man/1/scp) command.  
*On a new terminal window (out of your VM):*
`scp -P 4242 level02@10.11.200.76:~/level02.pcap ~/.`  
  
# 2nd Step
[.pcap](https://www.reviversoft.com/file-extensions/pcap?ncr=1&lang=en) files are data files created using the program and they contain the packet data of a network. These files are mainly used in analyzing the network characteristics of a certain data.  
[Here](https://osxdaily.com/2015/04/23/sniff-packet-capture-packet-trace-mac-os-x-wireless-diagnostics/) is another website to have a better idea of how .pcap files are used.
In the introduction video, Wandre talk about .pcap file reader : cloudshark  
1. So go on [cloudshark](www.cloudshark.org)  
Products -> personal SaaS and login with my personal id (will work until the 27/03/20)  
*login / password* maxime.simon42@gmail.com / password  
2. Upload the .pcap file on the platform  
*You will maybe have to change permissions on level02.pcap:*  
`chmod 644 level02.pcap`
3. Click on the uploded file then follow the transmission : `Analysis Tools` -> `Follow Stream`  
You will see this window:
[insert the capture here]  

Scroll a little bit and you will see :  
```
Password: 
ft_wandr...NDRel.L0L
```
Let's try it  
```
level02@SnowCrash:~$ su flag02
Password:
su: Authentication failure
level02@SnowCrash:~$
```  
Seems that it is not the good password..  
If you go back on cloudshark and follow the transmission again, click on `Hex Dump`:  
 66 | 74 | 5f | 77 | 61 | 6e | 64 | 72 | 7f | 7f | 7f | 4e | 44 | 52 | 65 | 6c | 7f | 4c | 30 | 4c
--- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | --
  f |  t |  _ |  w |  a |  n |  d |  r |  . |  . |  . |  N |  D |  R |  e |  l |  . |  L |  O |  L

In the ascii-table, the 7f is DEL, so we have to delete one previous character par 7f.  
 66 | 74 | 5f | 77 | 61 | 4e | 44 | 52 | 65 | 4c | 30 | 4c
--- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | --
  f |  t |  _ |  w |  a |  N |  D |  R |  e |  L |  O |  L
  
-> ft_waNDReL0L  
Let's try again !  
```
level02@SnowCrash:~$ su flag02
Password:
Don't forget to launch getflag !
flag02@SnowCrash:~$ getflag
Check flag.Here is your token : kooda2puivaav1idi4f57q8iq
flag02@SnowCrash:~$ su level03
Password:
level03@SnowCrash:~$
```  
Level02 passed !