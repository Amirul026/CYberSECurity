#Day 2 - Linux Command and Bandit 0-17


##bandit 0
## command practiced
ssh -p 2220 username@address(ip or url) 
ssh -p 2220 bandit0@bandit.labs.overthewire.org
##bandit level notes
how to connect with bandit server using ssh read file see the pass for next level
##what i learned 
how to use ssh and cat
##Problem i faced
connceting with server need to write the address corectly witout any space


##bandit1
## Commands Practiced
cat ./- cat <-
## Bandit Level Notes
how read file name - 
## What I Learned
can < to read unique file name < used to get output 
## Problems I Faced
how to read - name file used " " didn't work 

##bandit2
## Commands Practiced
cat < "--space with file name--"
## Bandit Level Notes
how to read a file name with space in between and with -- 
like --spaces in this filename--
## What I Learned
in these kind of problem simple cat will not work for space used " " and get output
used <
## Problems I Faced
how to handal spcae in file name 


##bandit3
## Commands Practiced
cat < "file name"
## Bandit Level Notes
read hidden file
## What I Learned
how to read  hidden file
## Problems I Faced

##bandit4
## Commands Practiced
find . -type f -exec file {} +|grep -i text
## Bandit Level Notes
find the correct file with the pass 
## What I Learned
how to use find with batch execute extra ccmd and used pipe to use the cmd output
for another cmd input and grep to find the needed text 
## Problems I Faced
how to 2 command with signel cmd ,batch execute

##bandit5
## Commands Practiced
find ./inhere/ -type f -size 1033c -exec file {} +|grep -i text
## Bandit Level Notes
find file with properties like human-readable,1033b size,not executable
## What I Learned
using find cmd with -size -type -exec flag
## Problems I Faced
for byte use c


##bandit6
## Commands Practiced
find / -type f -size 33c -user bandit7 -group bandit6 2>/dev/null
## Bandit Level Notes
find file in the server with properties owned by user bandit7,owned by group bandit6,
33 bytes in size
## What I Learned
uses of user,group flag and how surpress error msg using 2>/dev/null
## Problems I Faced
output was showing multiple error message like perssion denied 
2>/dev/null	This is a STDERR redirection to the 'null device',
 ensures that no errors are displayed in the terminal

##bandit7
## Commands Practiced
cat data.txt |grep -i millionth
## Bandit Level Notes
 password for the next level is stored in the file data.txt next to the word millionth
## What I Learned
uses of grep
## Problems I Faced


##bandit8
## Commands Practiced
strings data.txt|sort|uniq -u
## Bandit Level Notes
The password for the next level is stored in the file data.txt and is the only 
line of text that occurs only once
## What I Learned
uses of strings,sort,uniq with -u flag
## Problems I Faced
One limitation of the uniq command is that it will only identify duplicates 
that are adjacent so need to use sort before using uniq

##bandit9
## Commands Practiced
strings data.txt |grep -E "={3,}"
## Bandit Level Notes
The password for the next level is stored in the file data.txt in one of the few
 human-readable strings, preceded by several ‘=’ characters.
## What I Learned
-E enables extended regex + to mean "one or more"
## Problems I Faced
={3,} “Several” ≠ one,Avoids noise,Faster to spot the real password

##bandit10
## Commands Practiced
base64 -d data.txt
## Bandit Level Notes
The password for the next level is stored in the file data.txt, which 
contains base64 encoded data
## What I Learned
decode encode file in base64
## Problems I Faced


##bandit11
## Commands Practiced
cat <data.txt |tr "A-Za-z" "N-ZA-Mn-za-m"
## Bandit Level Notes
The password for the next level is stored in the file data.txt, where all 
lowercase (a-z) and uppercase (A-Z) letters have been rotated by 13 positions
## What I Learned
decode rot13 encoded text 
## Problems I Faced
how decoding works for rot13 

##bandit12
## Commands Practiced
xxd -r 
## Bandit Level Notes
form a hex dump file which compress using various method like gzip,bzip2,tar to get pass
## What I Learned
xxd -r to reverse a hex dump file.decompress the file
## Problems I Faced
while true; do
    file=$(ls | grep -v '\.txt$' | head -n 1)
 
    # Check if file exists and is not empty
    if [ -z "$file" ]; then
        echo "No files found"
        break
    fi
 
    type=$(file "$file" | cut -d: -f2)
 
    echo "Processing $file → $type"
 
    case "$type" in
        *gzip*)
            mv "$file" "$file.gz"
            gunzip "$file.gz"
            ;;
        *bzip2*)
            mv "$file" "$file.bz2"
            bunzip2 "$file.bz2"
            ;;
        *tar*)
            tar xf "$file"
            rm "$file"
            ;;
        *ASCII*)
            cat "$file"
            break
            ;;
        *)
            echo "Unknown format: $type"
            break
            ;;
    esac
done

##bandit13
## Commands Practiced
scp -P 2220 bandit13@bandit.labs.overthewire.org:/home/bandit13/sshkey.private .
chmod 700 sshkey.private
ssh -i sshkey.private -p 2220  bandit14@bandit.labs.overthewire.org
## Bandit Level Notes
in these level there is no pass for the next level but was given a privete key for 
the next level .using this needs login in bandit14 get pass for it as only bandit14
user can read the pass file
## What I Learned
using scp to copy ssh key file form bandit13 then using this key login into bandit14
## Problems I Faced
ssh file permission need be 700 which means only user have read,write and ececute access
which is ssh rule for private key

##bandit14
## Commands Practiced
nc localhost 30000
## Bandit Level Notes
The password for the next level can be retrieved by submitting the password
 of the current level to port 30000 on localhost.
## What I Learned
localhost nc cmd to connct with a runnig server for communication
## Problems I Faced

##bandit15
## Commands Practiced
openssl s_client -connect localhost:30001
## Bandit Level Notes
The password for the next level can be retrieved by submitting the password of the
 current level to port 30001 on localhost using SSL/TLS encryption
## What I Learned
nc connect without any security attacker can listen on communication(eavesdropping 
and tampering.)but using ssl/tls the connetion is secure
## Problems I Faced


##bandit16
## Commands Practiced
nmap localhost -p 31000-32000 -sV
echo "pass of 16" |openssl s_client -connect localhost:31790 -quiet
## Bandit Level Notes
passkey is in port range form 31000-32000 find out with port have which 
of those speak SSL/TLS and which don’t
## What I Learned
using nmap to see which  port running which service 
## Problems I Faced
ans was the passskey

##bandit17
## Commands Practiced
diff  passwords.old  passwords.new
## Bandit Level Notes
The password for the next level is in passwords.new and is the only line that 
has been changed between passwords.old and passwords.new
## What I Learned
using diff can find differenc in file
## Problems I Faced
none
