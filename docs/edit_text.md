# Editing Text
- `open .`
- vim
- VS Code
    `code .`

### File types

- Unicode (UTF-8) - a standard character encoding system

- Unix(LF) - new line type

### Exercise

### Make file in vim

    vim test.txt

    `i`, `esc`, `:`

In normal mode "i" to enter insert

":" command mode

Escape to go betwen modes

"wq" to write and quit

### View profile

```
vim ~/.bash_profile
```

or

```
vim ~/.bashrc
```

or 

```
vim ~/.zshrc
```

### PATH Example
    echo $PATH
Make it easier to read

    echo $PATH | tr ":" "\n"

Make a directory for tools

    cd; mkdir mytools; cd mytools

Make a script

    printf '#!/bin/sh\n\necho "Line1\tLine2!"' > myscript1.sh

Look at permissions

    ls -lh *

Make executable

    chmod 755 myscript1.sh

Look at permissions

    ls -lh *

Change directory and run script

    cd
    ./myscript1.sh

Check shell type

    echo $0

Open profile

    vim ~/.zshrc

Add text: `echo "--> Profile has been read <--"`

Add text: `export PATH="$PATH:${HOME}/mytools"`

Reload terminal

`echo $PATH | tr ":" "\n"`

Make a script that echos a message.

`vim myscript1.sh`

Add the script's path to PATH

Run script

### [HOME](../README.md)