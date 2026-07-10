
#Day 3 - bandit 18-23 and netcat

##bandit18
## Commands Practiced
ssh -p 2220 bandit18@bandit.labs.overthewire.org /bin/bash
## Bandit Level Notes
The password for the next level is stored in a file readme in the homedirectory.
 Unfortunately, someone has modified .bashrc to log you out when you log in with SSH
## What I Learned
how access bash if the .bashrc terminates bash CLI 
## Problems I Faced
chain cmd with ssh

##bandit19
## Commands Practiced
./ban
./bandit20-do cat /etc/bandit_pass/bandit20
## Bandit Level Notes
introduction to SUID baandit20-do set with suid(rws) use it access /etc/bandit_pass/bandit20
file to open it as a bandit20 user
## What I Learned
The program runs with the permissions of the file owner,
NOT the permissions of the user who runs it. with SUID set file
## Problems I Faced


##bandit20
## Commands Practiced
echo -n "bandit20passwordhere"|nc -l -p 1234 &
./suconnct 1234
## Bandit Level Notes
there is file named suconnect when run it will read pass of bandit20 if correct will
give the pass of bandit21
## What I Learned
run nc as a server and how i run a command in the background
## Problems I Faced
& → Run in background , .suconnect is clinet so i have to  be the server 

##bandit21
## Commands Practiced
ls -la /etc/cron.d/
cat /etc/cron.d/cronjob_banditXX
cat /usr/bin/cronjob_banditXX.sh
## Bandit Level Notes
A program is running automatically at regular intervals from cron, the time-based job 
scheduler. Look in /etc/cron.d/ for the configuration and see what command is being executed
## What I Learned
## Cron
Cron is a Linux scheduler that runs commands or scripts automatically at specific times.
In Bandit, cron jobs are stored in /etc/cron.d/. I used ls and cat to inspect cron files,
 then checked the script paths to understand what command was running automatically.
## Problems I Faced

##bandit22
## Commands Practiced

## Bandit Level Notes
A program is running automatically at regular intervals from cron,the time-based job 
scheduler. Look in /etc/cron.d/ for the configuration and see what command is being 
executed.
## What I Learned
how to read shell script like:
To declare a variable in bash scripting use the following syntax: var_name=var_value
to save the output of a command in a variable with the following 
syntax: var_name=$(command). Access the value of an existing variable like this: $var_name
## Problems I Faced

##bandit23
## Commands Practiced
cat /usr/bin/cronjob_bandit24.sh
mktemp -d
cd /tmp/tmp.UAWVpzVJCM
chmod 777 /tmp/tmp.UAWVpzVJCM
touch password
chmod 666 password
touch pass.sh
chmod 777 pass.sh
nano pass.sh
script:
#!/bin/bash

cat /etc/bandit_pass/bandit24 > /tmp/tmp.UAWVpzVJCM/password
cp pass.sh /var/spool/bandit24/foo/pass.sh
 cat password
## Bandit Level Notes
A program is running automatically at regular intervals from cron, the time-based job 
scheduler. Look in /etc/cron.d/ for the configuration and see what command is 
being executed.
## What I Learned
The password for bandit24 is stored in /etc/bandit_pass/bandit24.
 I cannot read it directly because I am logged in as bandit23.
However, the cron job runs as bandit24 and executes files placed 
inside /var/spool/bandit24/foo if those files are owned by bandit23.
So I created a script owned by bandit23 that copies the 
bandit24 password into a file in /tmp. 
When cron executes my script as bandit24, it has permission 
to read the password and write it into my temporary file.
## Problems I Faced
file directory permission mismatch 
