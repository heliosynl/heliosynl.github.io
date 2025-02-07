---
title: 'HKU hpc2021 connection in Windows'
date: 2025-01-15
excerpt: 'Tutorial for HKU hpc2021 connection in Windows system, basic in Linux and sshfs file manager'
permalink: /HKUhpc2021windows/
type: record # blog
tags:
  - Tutorial
  - record # blog
---

Content
=====
{:.no_toc}

* toc
{:toc}

HPC: high performance computer, HPC service provided by HKU is basically [hpc2021](https://hpc.hku.hk/hpc/hpc2021/)

# 1. HPC account
Apply for account [Account application](https://hpc.hku.hk/documentation/access/)

# 2. HPC login basic command
**Recommanded** install **Windows Terminal** with **Windows PowerShell**

After installation, use `Win+x` to start up a menu, open Windows Terminal directly with a hotkey `i`

## login to hpc2021
ssh is installed, by typing `ssh` can see. The output will be

```sh
usage: ssh [-46AaCfGgKkMNnqsTtVvXxYy] [-B bind_interface] [-b bind_address]
           [-c cipher_spec] [-D [bind_address:]port] [-E log_file]
           [-e escape_char] [-F configfile] [-I pkcs11] [-i identity_file]
           [-J destination] [-L address] [-l login_name] [-m mac_spec]
           [-O ctl_cmd] [-o option] [-P tag] [-p port] [-Q query_option]
           [-R address] [-S ctl_path] [-W host:port] [-w local_tun[:remote_tun]]
           destination [command [argument ...]]
```

to login hpc2021, use

```sh
ssh username@hpc2021.hku.hk
```

Mostly `username` is the uid of HKU account, like mine is `ynl08`

Than type in your password, also the password of HKU account

```sh
(base) PS D:\Onedrive> ssh ynl08@hpc2021.hku.hk
ynl08@hpc2021.hku.hk's password:
******************************************************************************
Welcome to HPC2021 cluster (hpc2021.hku.hk)
------------------------------------------------------------------------------
This frontend node is reserved for program modification, compilation and job
queue submission/manipulation.

User Guide: https://hpc.hku.hk/hpc/hpc2021/userguide

Please acknowledge the support of HKU Research Computing facilities(HPC/HTC)
in any research report, journal, or publications. This information would be
important for us to acquire funding for new resources.

Our suggested acknowledgement for academic publications is:

The computations were performed using research computing facilities offered
by Information Technology Services, the University of Hong Kong.

For technical issues, you are welcomed to contact us at GROUP-ITS-HPC@hku.hk.

Lilian Chan
Information Technology Services, HKU                            1 July 2021
******************************************************************************
Activate the web console with: systemctl enable --now cockpit.socket

Last login: Wed Jan 15 12:57:42 2025 from 10.68.87.159
[ynl08@hpc2021 ~]$
```

The system is in **Linux**, a **command line** based system, meaning all of your operation need to be type by keyboard.

For the resource assignment system used in hpc2021, called **slurm**, meaning all the **calculation** cannot be run in this terminal but by *job submission and queuing*
## basic command in linux
- `pwd`
  - present working directory, to print the current directory you are in now
- `cd <your destination>`
  - change directory, to your destination
- `ls`
  - list all files and directories in the current directory
- `ls -lh`
  - same as `ls` but with more information
- as directory/destination
  - `./` is the current directory
  - `../` is the parent directory
  - `~` is the home directory `/home/username`

```sh
total 345M
-rwxr-xr-x 1 ynl08 student 176M Jan 10 12:14 Dipole100_0109.mph
-rwxr-xr-x 1 ynl08 student 170M Jan  8 21:07 Dipole100.mph
-rw-r--r-- 1 ynl08 student  101 Jan 15 10:00 dipole.err
-rw-r--r-- 1 ynl08 student 250K Jan 15 10:00 dipole.out
drwxr-xr-x 2 ynl08 student    0 Jan 11 18:34 Jan11_100hrs
-rw-r--r-- 1 ynl08 student   80 Jan 13 10:05 out.mph.recovery
-rw-r--r-- 1 ynl08 student   21 Jan 13 10:00 out.mph.status
-rwxr-xr-x 1 ynl08 student  949 Jan 12 08:30 recover.sh
-rwxr-xr-x 1 ynl08 student  930 Jan 11 15:22 run.sh
```

|no need|no need|user|no need|file size|last modified date (in month|day|time)|file name|
|-------|-------|----|-------|---------|----------------------------|---|-----|---------|
|-rwxr-xr-x|1|ynl08|student|930|Jan|11|15:22|run.sh|

- `mkdir <new directory name>`
  - make new directory (folder)
- `rm <some files>`
  - remove files
- `rm -r <directories>`
  - remove directories
- `mv <files here> <new directories>`
  - move file to new directory
- `cp <files here> <new directories>`
  - cp file to new directory
- `sq`
  - slurm queuing of your account, to see the running and pending list of jobs your submitted.

```sh
[ynl08@hpc2021 comsol]$ sq
JOBID     PARTITION  NAME         ST   USER       QOS      NODES CPUS  TRES_PER_NODE TIME_LIMIT  TIME_LEFT   NODELIST(REASON)
1884668   amd        dipolelg     PD   ynl08      normal   1     128   N/A           2-10:00:00  2-10:00:00  (Priority)
1884807   amd        dipole       R    ynl08      normal   1     64    N/A           2-00:00:00  16:35:02    GPA-1-1
```
only need to know the column `ST`, `NODES`, `CPUS`, `TIME_LIMIT`, `TIME_LEFT`

|ST|NODES|CPUS|TIME_LIMIT|TIME_LEFT|
|--|-----|----|----------|---------|
|PD: pending|number of nodes assigned (like computer)|number of CPUs assigned|Time limit you set|left time of your job|
|R: Running|usually 1 is ok|usually more CPUs, faster, but longer queuing time|days-hrs:mins:secs|days-hrs:mins:secs|

- `sbatch <run.sh>`
  - job submission, see below the format of `run.sh` file

```sh
#!/bin/bash
#SBATCH --job-name=example                # 1. Job name, only display the first 8 characters
#SBATCH --mail-type=BEGIN,END,FAIL        # 2. Send email upon events (Options: NONE, BEGIN, END, FAIL, ALL)
#SBATCH --partition=amd                   # 3. Request a partition
#SBATCH --mail-user=youremail@connect.hku.hk  #    Email address to receive notification
#SBATCH --qos=normal                      # 4. Request a QoS
#SBATCH --ntasks=64                       # 5. Request total number of jobs (MPI workers)
#SBATCH --nodes=1                         # 6. Request number of node(s), 1 is ok
#SBATCH --mem=200G                        # 7. RAM assignment, more RAM makes longer queuing time, comsol need larger, but 200G is ok
#SBATCH --time=0-12:00:00                 # 8. Job execution duration limit day-hour:min:sec
#SBATCH --output=%x.out                   # 9. Standard output log as $job_name_$job_id.out
#SBATCH --error=%x.err                    #    Standard error log as $job_name_$job_id.err

# print the start time
date
export OMP_NUM_THREADS=1
module load comsol/6.1
export COMSOLTMP=~/group/tmpcomsol

comsol batch -recoverydir $COMSOLTMP -np 64 -inputfile input.mph -outputfile out.mph
# print the end time
date
```

If submitted successfully, terminal shows
```sh
Submitted batch job 1887295
```

the last is the job id of the job

## `run.sh` how to modify
```sh
#!/bin/bash
#SBATCH --job-name=example                # 1. Job name, only display the first 8 characters
#SBATCH --mail-type=BEGIN,END,FAIL        # 2. Send email upon events (Options: NONE, BEGIN, END, FAIL, ALL)
#SBATCH --partition=amd                   # 3. Request a partition
#SBATCH --mail-user=youremail@connect.hku.hk  #    Email address to receive notification
#SBATCH --qos=normal                      # 4. Request a QoS
#SBATCH --ntasks=64                       # 5. Request total number of tasks (MPI workers)
#SBATCH --nodes=1                         # 6. Request number of node(s), 1 is ok
#SBATCH --mem=200G                        # 7. RAM assignment, more RAM makes longer queuing time, comsol need larger, but 200G is ok
#SBATCH --time=0-12:00:00                 # 8. Job execution duration limit day-hour:min:sec
#SBATCH --output=%x.out                   # 9. Standard output log as $job_name_$job_id.out
#SBATCH --error=%x.err                    #    Standard error log as $job_name_$job_id.err

# print the start time
date
export OMP_NUM_THREADS=1
module load comsol/6.1
export COMSOLTMP=~/group/tmpcomsol

comsol batch -recoverydir $COMSOLTMP -np 64 -inputfile input.mph -outputfile out.mph
# print the end time
date
```

[Download file here](/files/codes/run.sh)

Don't try to change other thing except the below:
- Job name, can modify as `--job-name=DFT1`, here is 4 characters, so can display. Otherwise, only the first 8 characters will display if too long, for exakmple 'ultrasound' only display 'ultrasou'
- email address, the system will send you email when the job begin, end, fail
- ntasks, same as number of CPUs, usually 64 can have a shorter queuing time
- nodes, 1 is ok, larger makes longer queuing time
- memory, same as RAM, for comsol 200G is ok
- time, the job will end sharply at this time after begining, whatever the job is finished or not. No need to too long, can try from 0-12:00:00
- make sure the number after `-np` is the same as `--ntasks`
- `input.mph` need to change the input file you created in local computer, at the same directory
- `out.mph` will be the output file of the calculation

## running directory in hpc2021
only run job in two directories:
- `/scr/u/username` that is the only directory ITS assigned to you, have 500G storage
- `/group/mech_greennano` directory opened for our group, you can create a new directory for your jobs. Now only my directory is in.
```sh
[ynl08@hpc2021 mech_greennano]$ ls -l
total 1
-rw-r--r-- 1 ynl08 student        155 Sep  6 00:03 DISK_USAGE
drwxrwxr-x 5 ynl08 mech_greennano   0 Jan  8 20:56 ynl08
```

ask Helios to help you link the these two directories to your home directory (`/home/username/`)

# 3. send file to and modify file on hpc2021 (for Windows)
go to [winfsp](https://winfsp.dev/)

go download **WinFsp Installer** and **SSHFS-Win (x64)** and install them

then go to [sshfs-win-manager](https://github.com/evsar3/sshfs-win-manager?tab=readme-ov-file)

![github](/images/records/2025-01-15-HPC2021/githubsshfswinman.png)

find **Release** and click the latest version

![githubrelease](/images/records/2025-01-15-HPC2021/githubrelease.png)

find `.exe` and download and install

![githubdownload](/images/records/2025-01-15-HPC2021/githubdownload.png)

## SSHFS-Win Manager
main menu

![sshfswinman](/images/records/2025-01-15-HPC2021/sshfswinmanmenu.jpg)

Add connection

![sshfswinmanadd](/images/records/2025-01-15-HPC2021/sshfswinmannewconnection.jpg)

ip/host needs to be `hpc2021-io1.hku.hk`, port is `22`

**DONT USE `hpc2021.hku.hk`!!!!!!!!!!!!!!!!!!!!!!!!** the administrator will cancel your account if they find you

**Updated 2025Jan15** something wrong happened in `hpc2021-io1.hku.hk`, can use `hpc2021-io2.hku.hk`

USER and PASSWORD just enter yours

PATH use the output of `pwd` when you first time get into the system

DRIVE LETTER can change any one you like

after setting, just press the connection button, and you will find a new disk appeared in your File Explorer

![newdisk](/images/records/2025-01-15-HPC2021/newdisk.jpg)

get into here and you can modiry/add/delete files and directory in Windows

use Notepad to modify the `run.sh` file and save