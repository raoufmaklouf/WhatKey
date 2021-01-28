# WhatKey
A simple script that identifies any text that suspects may be an access key for a service via regular expression
#  Uses
You can simply if you are a linux user add it to the .bashrc file this is my method open a .bashrc file with superuser privileges
and add this  codes 
```
whatkey(){
python3 /home/yourfolder/whatkey.py  $1 
}
```
After that save the file and  enter this command
```
source .bashrc 
```

You can use it now from the terminal directly

```
whatkey 0123456789:AAAAAAAAAAAAAAAAAAAA_BBBBBBBBBBBBgg
```
