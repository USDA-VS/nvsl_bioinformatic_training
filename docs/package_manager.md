# Managing Programs
- Traditional software installation
    - config, make, make install
    - find dependencies
- Operating System specific precompiled binaries
- Anaconda package Manager
    - System calls
    - Python
    - Environments
- Python's Pip
- GitHub (versioning, collaboration, transparency)
- HPC Modules
- Containers

## Install Anaconda
On Mac install xcode developer tools:
```bash
xcode-select --install
```
Download and install Miniconda Python 64-bit Installer<br>
https://docs.anaconda.com/free/miniconda/#quick-command-line-install<br>

Use installation defaults

[Manage conda environment](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)

See available modules
```
conda env list
```

```
conda update -n base -c defaults conda
```
```
conda create -n vsnp3 -c bioconda -c conda-forge vsnp3
```
If conda install is slow, restarting computer may help.
```
conda update --all
```

Test tool

```
vsnp3_download_fasta_gbk_gff_by_acc.py -fbg -a NC_045512
```

### Download sratoolkit

Download from conda
```zsh
conda install bioconda::sra-tools
```


Download compiled binaries

https://github.com/ncbi/sra-tools/wiki/01.-Downloading-SRA-Toolkit

```
tar -xzf sratoolkit*.tar.gz
```

add bin to PATH

```
PATH=$PATH:${HOME}/Downloads/sratoolkit.3.0.7-mac64/bin
```

```
fasterq-dump -S SRR3135071
```

```
mv SRR3135071_1.fastq SRR3135071_R1.fastq
mv SRR3135071_2.fastq SRR3135071_R2.fastq
```

```
pigz *fastq
```
### [HOME](../README.md)