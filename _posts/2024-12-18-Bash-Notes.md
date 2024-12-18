---
title: "Bash Notes"
date: 2024-12-18
type: notes
tags:
  - bash
  - notes
---

```
#!/bin/bash
```

```
chmod +x filename
```

```
for var in 'abc' 'erere' 'erererss'; do
cp ${var} file
done
```

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

``[]`` can be a comparison between two strings:
``[ "$str1" = "$str2" ]``
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

```
[ -f "abc.abi" ] && echo "It is a file."
Or
if [ -f "abc.abi" ]; then
  echo "It is a file."
fi
```
determine whether abc.abi is a file, if true, output "It is a file." on command line



Applications:
```
cp `find -name 'it_is_file_name'` folder/
```
Copy file with name it_is_file_name into folder/


### functions
```
function my_func {
Shell script
}
```

### Extract
```
tar -zxvf ./file.tar.gz
tar -xvjf ./file.tar.bz2
tar -xf ./file.tar
```

### Compress
```
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
```
systemctl reboot --firmware-setup
```

### Find ip
```
ifconfig
or 
nmcli device show
```

### xrdp/remote desktop
- Boot
```
who -u
```
- find :0, referring to the local display
- kill the pid
- Use remote desktop to login

``${parameter/pattern/string}``
Replace 'pattern' in 'parameter' with 'string'

``tmp=${a#*_}``remove prefix ending in "_"

``b=${tmp%_*}``remove suffix starting with "_"

```
sed -i -e 's/abc/XYZ/g' /tmp/file.txt
```
which will invoke ``sed`` to do an in-place edit due to the -i option. The /g flag for sed's s command says to replace globally, i.e. do not substitute only the first occurrence on each input line. This can be called from Bash.

### Lock screen by bash
```
gnome-screensaver-command -l
```

### RAM testing inspection
```
sudo dmidecode --type memory | less
```

### check my pc ip at 109 by login to hpc2021.hku.hk
```
last -a | grep ynl08
```