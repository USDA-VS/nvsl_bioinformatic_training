## New user most common troubleshooting

### Understanding space character (white space) with Linux
- space
    - cd mydir
    - cdmydir

- tabs
    - set amount of spaces
    - \t

### Newline versus carriage returns
- Unix: \n
- Windows: \r
  
### Use the tab key for auto completion
- tab key for auto completion is faster but most importantly ensures correct spelling

### Know where you are on the filesystem
- cd
- ls
- pwd
- mkdir
- cp
- mv

### File permissions
- Ownership:
   -  User - Group - All
- Permission:  chmod
    - Read - Write - Execute: 4 - 2 - 1

### $PATH variable
- Where a Linux system will look for a program
- You need to know your PATH variable locations
- Anaconda packages are automatically added to your PATH

### File access
- Copying files to your local machine.
  - WinSCP/FileZilla
  - Web Interface - OnDemand
  - Mounted drive
  - scp command-line
  - VS Code

### Testing
- Always have known, good datasets.
- When using a script for the first time if there is a failure don't assume it can only be the script.
 
###

# Getting tools
# Anaconda package manager

Other places we could be getting tools:
- Source
    - Dependency libraries needed
    - Compiled manually: config, make, make install
- GitHub
- Container
  - Docker
  - Singularity/Apptainer
 
###

#
# Examples

```
git clone https://github.com/USDA-VS/nvsl_bioinformatic_training.git
```

```
conda activate <env>
```
```
conda env list
```

## AMRFinder-Plus

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

### [README](../README.md)
