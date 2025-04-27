---
title: "Bash Notes"
date: 2024-12-18
excerpt: 'Coding notes for bash/sh command line in ubuntu'
type: notes
tags:
  - bash
  - notes
---

Content
=====
{:.no_toc}

* toc
{:toc}

# Header
```sh
#!/bin/bash
```

```sh
chmod +x filename
```

```sh
for var in 'abc' 'erere' 'erererss'; do
cp ${var} file
done
```

`command 1 && command 2` go to next command only if the previous one is successful

`command > log.txt 2>&1 &` save log and error to log.txt file. The first `>` refers to the standard output redirection (to log.txt here). The second `2>` refers to the error output redirection, it was redirected to the 'log' category by `&1` (same log.txt here). The last `&` refers to no standard output and run in the background.

|representation||
|-|-|
|``${}``|as variable|
``$?``|result value from the previous command of shell
``\`\```|as command
``a > b``|output of a as input (content) of b
``a < b``|output (content) of b as input of a
``a >> b ``|output of a append to b
``a 2> b``|error output of a as input (content) of b
``[]``|condition command, containing the essence of condition
``[ -f "abc.abi" ]``|determine whether abc.abi is a file

``[]`` can be a comparison between two strings:`[ "$str1" = "$str2" ]`

| can use ||
|-|-|
-f|File
-x|Executable
-d|Directory
 -e|exist
-eq|Equal to
-ne|Not equal to
-gt|Greater than
-lt|Less than
-ge|Greater or equal to
-le|Less or equal to

```sh
[ -f "abc.abi" ] && echo "It is a file."
Or
if [ -f "abc.abi" ]; then
  echo "It is a file."
fi
```
determine whether abc.abi is a file, if true, output "It is a file." on command line



Applications:
```sh
cp `find -name 'it_is_file_name'` folder/
```
Copy file with name it_is_file_name into folder/


### functions
```sh
function my_func {
Shell script
}
```

### Extract
```sh
tar -zxvf ./file.tar.gz
tar -xvjf ./file.tar.bz2
tar -xf ./file.tar
```

### Compress
```bash
tar -zcvf name-of-archive.tar.gz ./directory
```

|tags||
|-|-|
-z|Compress the archive with gzip
-x|Extract
-v|Display
-f|Specify file name
-c|Create an archive

### BIOS from linux
```sh
systemctl reboot --firmware-setup
```

### Find ip
```sh
ifconfig
or 
nmcli device show
```

### xrdp/remote desktop
- Boot
```sh
who -u
```
- find :0, referring to the local display
- kill the pid
- Use remote desktop to login

``${parameter/pattern/string}``
Replace 'pattern' in 'parameter' with 'string'

``tmp=${a#*_}``remove prefix ending in "_"

``b=${tmp%_*}``remove suffix starting with "_"

### sed
```sh
sed -i 's/abc/XYZ/g' /tmp/file.txt
```
which will invoke ``sed`` to do an in-place edit due to the -i option. The **g** flag use to replace globally without line number, i.e. do not substitute only the first occurrence on each input line. This can be called from Bash.

#### replace
```sh
sed -i '3s/origin/new/' /tmp/file.txt
```
replace the **origin** string to **new** in **line 3**


### Lock screen by bash
```sh
gnome-screensaver-command -l
```

### RAM testing inspection
```sh
sudo dmidecode --type memory | less
```

### check my pc ip at 109 by login to hpc2021.hku.hk
```sh
last -a | grep ynl08
```

### soft link
```sh
ln -s {source-filename} {symbolic-filename}
```

for example, I have a directory at `/home/heliosynl/test` and I want it a new name is `/data/newname`, I can do

```sh
ln -s /home/heliosynl/test /data/newname
```

it will create a softlink name `newname` at `/data/` directory, pointing to `/home/heliosynl/test`

# Gnuplot
```sh
gnuplot -p -e "set terminal dumb; plot '' u 1:3 w l" 
```
plot in terminal

- -p for new window to show 
- -e for in-line command, using ; to separate lines 
- `plot 'filename' u 1:2 w l` (using 1:2 default) 
- `set terminal dumb` for plotting in terminal but not new window 
- `plot 'filename' u 1:2 w l t 'labelname'`

check [gnuplot cheat sheet](http://www.gnuplot.info/docs_4.0/gpcard.pdf)
# ssh
```sh
sudo apt install openssh openssh-server
```

- start ssh server: `sudo service sshd start` or `sudo systemctl start sshd`
- check server status: `sudo service sshd status` or `sudo systemctl status sshd`

## password-less login: client
- Generate private and public keys
  - `ssh-keygen`
    - press Enter is ok
  - can find:
    - public key at `~/.ssh/id_rsa.pub`
    - private key at `~/.ssh/id_rsa`
  - copy **public key** to the **server**
    - `ssh-copy-id name@serverip`
    - instead, copy the content in `id_rsa.pub` to server side `~/.ssh/authorized_keys`
## sshfs
- Install openssh openssh-server
  - It is okay when the machine can be connected with other machine through ssh
- Install sshfs
  - `sudo apt install sshfs`
- Then add the current user into the fuse group (administrative group of using sshfs)
  - Check if there is a fuse group: `cat /etc/group | grep 'fuse'`
  - If there is not: `sudo groupadd fuse`
- Then: `sudo usermod -a -G fuse your_username`