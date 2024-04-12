# FASTQ and FASTA Basics

```
fasterq-dump -S SRR23410316
````
List
```
ls -lh *fastq
```
View 
```
head SRR23410316_R1.fastq
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
mv SRR23410316_1.fastq.gz SRR23410316_R1.fastq.gz
mv SRR23410316_2.fastq.gz SRR23410316_R2.fastq.gz
```
Get stats using SeqKit
```
seqkit stats *.fastq.gz -T > out.tab
```
Simple search
```
seqkit grep -s -m 1 -p "ATGGCGGGGTCA" *gz -C
```
Search list
Make id.txt with sequence and search many

 ```
 seqkit grep -s -m 1 -f id.txt *gz -C
 ```
Parse sequence
```
seqkit grep -s -m 1 -p "ATGGCGGGGTCA" *_R1*gz > found_sequence_R1.fastq
```

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

## Seqkit 

using vsnp3_fastq_stats_seqkit.py

[Excel](../data/ERR4769503_2023-10-13_09-45-09_stats.xlsx)

[PDF](../data/ERR4769503_2023-10-13_09-45-08_report.pdf)

## FASTQC

[FASTQC Report](../data/ERR4769503_R1_fastqc.html)


## Stat on a general ID report

[TB PDF Example](../data/ERR2383627_2023-09-11_11-02-31_report.pdf)

[Sample as above but in Excel Format](../data/ERR2383627_2023-09-11_11-02-31_stats.xlsx)

[Excel is more efficent with a large sample set](../data/stats-2023-09-20_07-35-43.xlsx)

Sort by Total assembly length

Look at some problem samples

[SRR1239339](../data/SRR1239339_2023-09-11_17-25-20_report.pdf) with a bit of contamination

[SRR6856085](../data/SRR6856085_2023-09-11_23-52-52_report.pdf) also a bit of contamination

## Stats on AMR report

[SRR17276215](../data/SRR17276215_amr.pdf)

A better sample

[SRR26217755](../data/SRR21152630.pdf)

## vSNP stats

[stats](../data/stats-2023-10-13_09-39-07.xlsx)

## Kraken

[Clean sample](../data/ERR2383627_2023-09-11_09-40-10_krona.html)

[Contamination present](../data/SRR6856085_2023-09-11_22-05-33_krona.html)

[Escherichia coli SRR26282520](../data/SRR26282520_2023-10-13_13-49-32_krona.html) contaminated sample?

[SRR26282520 AMR stats](../data/SRR26282520.pdf)

### [README](../README.md)