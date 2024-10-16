# Command-Line Basics

- Why the command-line?
    - Big data files
        - open partial files
        - piping
        - Unix/Linux pratices
            - permissions/file sharing
            - tools, do one thing well
            - terminal - networking, speed, compute
            - open source community
    - Available [tools](https://github.com/danielecook/Awesome-Bioinformatics)
      - [Common tools](../docs/nvsl_common_tools.md) used at NVSL
    - Fast - low overhead, no GUI
    - Fast - scripting
        - File system access
        - Wildcard'ing, regular expressions
        - Shortcuts
        - Automate repetition
    - Creativity

- Resources
    - Man pages
        - [ls](https://man7.org/linux/man-pages/man1/ls.1.html)
        - [grep](https://linuxcommand.org/lc3_man_pages/grep1.html)
        - [sed](https://linux.die.net/man/1/sed)
    - Websites
        - AI: [ChatGPT](https://chat.openai.com/), [Claude](https://claude.ai/), [Perplexity](https://www.perplexity.ai/)
        - Google
        - [StackOverFlow](https://stackoverflow.com/)
        - [Biostar](https://www.biostars.org/)
        
    - Books
        - [Practical Computing for Biologists](https://practicalcomputing.org/)
        - [Bash Pocket Reference](https://www.amazon.com/Bash-Pocket-Reference-Power-Admins/dp/1491941596/ref=sr_1_5?crid=3DMBHHOWJXUEH&keywords=bash+handbook&qid=1676661164&sprefix=bash+handbook%2Caps%2C178&sr=8-5)
        - [Python Programming](https://www.amazon.com/Python-Complete-Course-Becoming-Programming-ebook/dp/B01FGZ8UXW/ref=sr_1_1?crid=76CILJ1J2HOX&keywords=python+programming+goddard&qid=1677242761&sprefix=python+programming+goddard%2Caps%2C109&sr=8-1#customerReviews)
    - Workshops
        - [Software Carpentry](https://software-carpentry.org/)
        - [UC Davis](https://bioinformatics.ucdavis.edu/training)

- Unix Standard tools
    - cd
    - cp
    - mkdir
    - echo
    - ls
    - pwd
    - head
    - grep
    - sed
    - pigz
    - mv (danger)
    - rm (danger)

# Installing tools
## Anaconda package manager

Other source for installing tools:
- Source
    - Dependency libraries needed
    - Compiled manually: config, make, make install
- GitHub
- Container
  - Docker
  - Singularity/Apptainer

# New user most common troubleshooting

## Understanding space character (white space) with Linux
- space
    - cd mydir
    - cdmydir

- tabs
    - set amount of spaces
    - \t

## Newline versus carriage returns
- Unix: \n
- Windows: \r
  
## Use the tab key for auto completion
- tab key for auto completion is faster but most importantly ensures correct spelling

## Know where you are on the filesystem
- cd
- ls
- pwd
- mkdir
- cp
- mv

## File permissions
- Ownership:  chown
   -  User - Group - All
- Permission:  chmod
    - Read - Write - Execute: 4 - 2 - 1

## $PATH variable
- Where a Linux system will look for a program
- You need to know your PATH variable locations
- Anaconda packages are automatically added to your PATH

## File access
- Copying files to your local machine.
  - WinSCP/FileZilla
  - Web Interface - OnDemand
  - Mounted drive
  - scp command-line
  - VS Code

## Testing
- Always have known, good datasets.
- When using a script for the first time if there is a failure don't assume it can only be the script.

# General Discussion

  - Terminal - emulators - end points
  - The shell - program running in the terminal - command line interpreter - running other programs
  - ssh, secure shell standard network protocol
      - ssh keys
      - .ssh/authorized_keys
      - .ssh/known_host
  - User's profile
      - ~/.bash_profile
      - ~/.zshrc
  - User's PATH variable
  - Tab completion
  - Space character
      - command mistakes
          - `ls-lh`
          - `cd~/myfolder`
          - `cd..`
  - Standard [tools](https://opensource.com/article/22/5/essential-linux-commands)/[GNU coreutils](https://www.gnu.org/software/coreutils/manual/html_node/index.html#toc-Introduction-1)
  - Options
      - dash "-"
      - flags
  - Wildcards
      - *: Matches any sequence of characters
      - ?: Matches any single character.
      - [...]: Matches any one of the characters inside the brackets
      - [!...]: Matches any character that is not inside the brackets
  - Absolute versus relative paths
      - absolute: root /
      - ~/ ${HOME}
      - relative: from working directory
  - Command History, ctrl-r, .zsh_history
  - Logic
      - [Loops](../notes/loop.md)
      - [IF Statements](../notes/if_statement.md)


### Exersize:
Make directory

Copy files from repo's "data" folder into new directory
```
cd <cloned repo>
```
```
mkdir test_dir
```
```
cp data/* test_dir; cd test_dir; ls
```
```
which pigz
```
```
conda install pigz
```
```
pigz -d *gz
```

### Simple tools

```
grep -c '^@SRR' *fastq
```
```
head *_R1*fastq
```
```
head -4 *fastq | grep '^@SRR' | sed 's/ .*//'
```
```
for i in *fastq; do head -4 $i | grep '^@SRR' | sed 's/ .*//'; done
```
```
for i in *fastq; do count=$(grep -c '^@SRR' $i); printf "$i has this $count reads\n"; done 
```
```
for file in *; do
    if [[ $file == *.fasta ]]; then
        echo "$file is a FASTA"
    fi
done
```
```
echo "PDF samples in list not found in directory:"; while read filename; do name=$(ls ${filename}*.pdf); [ ! -e "$name" ] && echo "$filename"; done < list 2> /dev/null
```
```
echo "PDF samples in list found in directory:"; while read filename; do name=$(ls ${filename}*.pdf); [ -e "$name" ] && echo "$filename"; done < list 2> /dev/null
```
### Find the error
```
pwd; dir=`pwd`; cd~; cd $dir; pwd # find the error
```
```
for *_R1*; echo $i; done # find the error
```
```
for i in *fastq; do count=$(wc -l | sed 's/ .*//'); printf "$i has $count lines\n"; done # find the error
```
```
for i in *_R1*fastq; count=`grep -c 'GTGTAA' $i`; echo "$count in $i"; done # find the error
```
```
#find error
for file in *; do
    if [[ $file == SRR* ]]; then
        echo "-> \t\t$file starts with SRR"
    elif [[ $file == ERR* ]]; then
        echo "----> \t$file starts with ERR"
    else
        echo "$file - starts with something else"
    if
done
```

#
# Examples

```
conda activate <env>
```
```
conda env list
```

## AMRFinder-Plus

# Salmonella enterica SZL 38
```
amrfinder --nucleotide SRR17276215_amr.fasta --output SRR17276215_output.txt
```

## SRA Tools
```
conda create -n sra-tools -c conda-forge -c bioconda -n sra-tools
```
```
fasterq-dump --split-files -O . SRR26282520
```
```
wget https://sra-pub-run-odp.s3.amazonaws.com/sra/SRR6046640/SRR6046640 
```
```
fastq-dump --split-files SRR6046640
```
### macOS
```
~/sratoolkit.3.0.7-mac64/bin/fasterq-dump -S SRR6046640
```
### Docker
Download Docker.  It must be running.
```
docker pull ncbi/sra-tools
docker run -t --rm -v $PWD:/output:rw -w /output ncbi/sra-tools fasterq-dump -e 2 -p SRR6046640
```
### Singularity
```
singularity pull docker://ncbi/sra-tools
singularity run sra-tools_latest.sif fasterq-dump -e 2 -p SRR6046640
```

## Kraken
```
~/anaconda3/envs/vsnp3/bin/vsnp3_kraken2_wrapper.py -r1 SRR6046640_R1.fastq.gz -r2 SRR6046640_R2.fastq.gz --database ~/k2_standard_08gb
```

## vSNP
Download test data
```
cd ~; git clone https://github.com/USDA-VS/vsnp3_test_dataset.git
```
Step 1
```
vsnp3_step1.py -r1 *_R1*.fastq.gz -r2 *_R2*.fastq.gz -t Mycobacterium_AF2122
```
Step 2
```
vsnp3_step2.py -a -t Mycobacterium_AF2122
```


### [HOME](../README.md)