---
title: "AMS simulation suite installation"
date: 2025-05-30
excerpt: 'AMS suite installaion notes'
type: record
tags:
  - record
---

Content
=====
{:.no_toc}

* toc
{:toc}

# [tutorial](https://www.scm.com/doc/Tutorials/index.html)

# 1. download
k
# 2. unzip 
```sh
tar -zxvf ams-----.bin.tgz
```

then can move the fodler to `/Software`

# 3. install with .sh
add
```sh
SCM_TMPDIR=$PWD
```
to the `amsbashrc.sh` file, 
```sh
. /home/yongnanli08/Software/ams2025.102/amsbashrc.sh
```

`/bin` can be found in that folder

# 4. add path to $PATH
remember to add the initialization to `~/.bashrc`
`. /home/yongnanli08/Software/ams2025.102/amsbashrc.sh` add this
- `source ~/.bashrc`

# 5. start GUI
```sh
amsjobs &
```

then go back to terminal to create a desktop icon
```sh
$AMSBIN/create_linux_icon.sh
```

# 6. license
can see a gui with name **Get License**
- fill in
  - email
  - SCM ID and password
- continue

if receive notification that
- folder is not rewritable, install license manually
  - switch to root, copy license file to installation path
  - rename as `license.txt`
    - if needed, `sudo chmod 777 license.txt`

then restart PC

# 7. use
when use, go to your directory then
```sh
amsjob &
```

=====
# ADF
# how to choose basis set
[see](https://www.scm.com/doc/ADF/Rec_problems_questions/What_basis_set_should_I_use.html)
SZ < DZ < DZP < TZP < TZ2P < TZ2P+ < ET/ET-pVQZ < ZORA/QZ4P

single < double < triple < even tempered < quadra

ZORA should be default (in relativity)

# frozen core
in general recommend to use, in particular including heavier atoms

invoking the frozen core approximation, error is smaller than using higher quality basis set

dybrid functional with frozen core may cause error

but for accurate results of properties like nuclear dipole hyperfine interactions (ESR), nuclear quadrupole coupling constants, chemical shift (NMR), all electron basis set are needed