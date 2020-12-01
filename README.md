<a href="https://www.42.fr/">
    <p><img src="https://www.universfreebox.com/UserFiles/image/site_logo.gif" alt="42 logo" title="42" align="right" /></p>
</a>
<p align="center"><img src="https://user-images.githubusercontent.com/34480775/100727740-f14f9d80-33c6-11eb-8729-bdc8cddb63c7.JPG" /></p>


<p align="center">
    <img src="https://img.shields.io/badge/Skill%201-Security-9cf">
    <img src="https://img.shields.io/badge/Skill%202-Unix-blue">
    <img src="https://img.shields.io/badge/Objectives-Perl/Python/Shell%20scripts-brightgreen">
</p>

<br/>

This project is an introduction to computer security. Snow Crash will make you discover security in various sub-domains, with a developer-oriented approach. You will become familiar with several languages (ASM/perl/php…), develop a certain logic to understand unknown programs, and become aware of problems linked to simple programming errors.  
This project is composed of 14 levels, each one contains a security breach that gives you access to the next level.  
<br/>

## General instructions
To make this project, you will have to use a VMV(64 bits). Once you have started your machine with the ISO provided with this subject, if your configuration is right, you will get a simple prompt with an IP :  
![alt tag](https://user-images.githubusercontent.com/34480775/100728223-923e5880-33c7-11eb-8188-e360404180bf.JPG)  
Then, you will be able to log-in using the following couple of login:password :  
`level00:level00`  
You really shoud use the SSH connection available on port 4242 :  
`$> ssh level00@[VM_IP] -p 4242`  
Once registered, you’re gonna have to find the password that will log you in with the "flagXX" account (XX = current level number).  
Once logged to the "flagXX" account, launch the "getflag" command.  
It will give you the password to connect to the next level (You may not be able to connect to a "flagXX" account - in this case, you will have to find an alternative method, like a command injection on the program depending on its rights, for instance!).  
• Here is a session example :  
![alt tag](https://user-images.githubusercontent.com/34480775/100729210-c403ef00-33c8-11eb-95d5-ff44954aa1d1.JPG)  
• To help you with some levels, you’re gonna have to use external softwares. You should learn how to use the SCP command.  

## Minimal setup requirements of the VM
For this project, I used VirtualBox in order to create the VM. You will also need to download the ISO, avaible in the 42 school intranet (as the subject of this project).  
- Name : SnowCrash
- Type : Linux
- Version : Ubuntu (64-bit)
- RAM : 1024 MB
- CPU : 1
- Network access mode : bridge
- Port : 4242

## Rate : 125/100
