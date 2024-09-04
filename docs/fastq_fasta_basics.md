# FASTQ and FASTA Basics

SRR23410316 - Salmonella

ERR766214 - BCG

## Download
```
conda install bioconda::sra-tools
fasterq-dump -S ERR766214 # 2.2GB not compressed
```
wget
```
sra_number="ERR766214"
wget -O "${sra_number}.fastq.gz" "https://sra-pub-run-odp.s3.amazonaws.com/sra/${sra_number}/${sra_number}"
fasterq-dump -S ${sra_number}.fastq.gz
# faster than fasterq-dump, compressed - single FASTQ, then split
```
ENA browser tools downloads files as compressed but slower than wget
```
conda install bioconda::enabrowsertools # old
```
Download [ENA](https://github.com/enasequence/enaBrowserTools) at GitHub
```
sra_number="ERR766214"; enaDataGet --format fastq "$sra_number" # git pull if tool does not work to get the latest version.
```
## FASTQs
List
```
ls -lh *fastq
```
View 
```
head ERR766214_R1.fastq
```
Zip
```
pigz *fastq
```
List
```
ls -lh *fastq.gz
```
Add "R" for read
```
mv ERR766214_1.fastq.gz ERR766214_R1.fastq.gz
mv ERR766214_2.fastq.gz ERR766214_R2.fastq.gz
```
Get stats using SeqKit
```
seqkit stats *.fastq.gz -T > out.tab
```
Simple search
```
seqkit grep -s -m 1 -p "ATGGCGGGGTCA" *gz -C
```
Parse sequence
```
seqkit grep -s -m 1 -p "ATGGCGGGGTCA" *_R1*gz > found_sequence_R1.fastq
```
## FASTA
Assembly
```
spades.py -1 *_R1*fastq.gz -2 *_R2*fastq.gz -o spades_assembly
```

If SPAdes fails [download](https://github.com/ablab/spades) binaries and add bin to your PATH

```
PATH=$PATH:${HOME}/SPAdes-3.15.5-Darwin/bin
```
```
which spades.py
```
```
PATH=${HOME}/SPAdes-3.15.5-Darwin/bin:$PATH
```
```
vsnp3_assembly.py -f ./spades_assembly/scaffolds.fasta
```
View
head ./spades_assembly/scaffolds.fasta

## Seqkit wrapper

```
vsnp3_fastq_stats_seqkit.py -r1 ERR766214_R1.fastq.gz -r2 ERR766214_R2.fastq.gz
```

[Excel](../data/ERR766214_2024-07-25_06-25-04_stats.xlsx)

[PDF](../data/ERR766214_2024-07-25_06-25-04_report.pdf)

## FASTQC
```
fastqc ERR766214_R1.fastq.gz ERR766214_R2.fastq.gz
```

[FASTQC Report](../data/ERR766214_R1_fastqc.html)


## Stats on a general ID wrapper script report

[ERR766214](../data/ERR766214_2024-07-25_08-18-02_report.pdf)

[Poor sample Example](../data/SRR6856085_2023-09-11_23-52-52_report.pdf)

[SRR23410316](../data/SRR23410316_2024-07-25_07-33-00_report.pdf)

### [HOME](../README.md)