# [kSNP](https://academic.oup.com/bioinformatics/article/31/17/2877/183216)

kSNP identifies SNPs in genomes without the requirement for genome alignment or a reference genome.

### Pros
- No reference is needed.
- There’s no reference bias.
- It handles more divergent datasets better.
- It’s useful for finding references for reference-based comparisons (vSNP).

### Cons
- Is there contamination?
  - Majority at 0.8.
- It’s difficult to validate SNPs.
- It’s slow with large datasets.
  
## Download
[sourceforge](https://sourceforge.net/projects/ksnp/files/).

Download the prebuild binary for either Mac or Linux.

Place unzipped file in desired location (${HOME} will work)

```
 mv kSNP4.1\ Linux\ package kSNP4
```

Add to PATH, `PATH="${HOME}/kSNP4/kSNP4.1pkg":$PATH`

## Sample set
TB Complex representative samples
```
CP041800
CP017920
CP046309
NC_000962
CP020381
CP089775
CP041837
CP069067
NZ_CP014617
CP041791
CP048071
NC_002945
CP109681
CP016401
LR882497
CP063804
```
Download RefSeq genomes
```zsh
while read i; do vsnp3_download_fasta_gbk_gff_by_acc.py -a $i -f; done < list
```
Rename
```
CP041800	CP041800-L1
CP017920	CP017920-L2
CP046309	CP046309-L3
NC_000962	NC000962-L4
CP020381	CP020381-L4
CP089775	CP089775-L4
CP041837	CP041837-L4
CP069067	CP069067-L5
NZ_CP014617	NZCP014617-L6
CP041791	CP041791-L7
CP048071	CP048071-L8
NC_002945	NC002945-bovis
CP109681	CP109681-bovisBCG
CP016401	CP016401-caprae
LR882497	LR882497-microti
CP063804	CP063804-orygis
```
```
for i in *fasta; do name=`grep ${i%.fasta} rename | awk '{print $2}'`; mv $i ${name}.fasta; done
```
```
rm list rename
```
## Run sample set
```
MakeKSNP4infile -indir ./ -outfile myInfile S
```
```
Kchooser4 -in myInfile
```
```
optimum_k=23; kSNP4 -in myInfile -outdir run -CPU 8 -k ${optimum_k} -core -ML -min_frac 0.8
```
SNP counts
```
echo "COUNT_SNPs"
cat ./run/COUNT_SNPs
echo ""
echo "COUNT_coreSNPs"
cat ./run/COUNT_coreSNPs
echo ""
```

## Understanding metrics/stats
- **FraCtion of Kmers (FCK)** that are present in all genomes. FCK is a measure of sequence diversity, the lower is FCK the more diverse are the sequences. As diversity increases the efficiency with which kSNP3 detects SNPs decreases. Experience has shown when FCK is ≥ 0.05 SNP detection efficiency is adequate, and the accuracy of parsimony trees estimated by kSNP3 is > 97%; i.e. the trees can be considered to be reliable
- **K-mer Size Used:** This refers to the length of the k-mer used in the analysis.
- **K-mer = Position:** In a 19-mer, the SNP is located 9 nucleotides upstream and downstream from the SNP.
- **Core:** A core k-mer is found in all samples. Only the middle nucleotide of the k-mer is considered as the SNP.
- **Non-Core:** A non-core k-mer is not found in all samples.
- **0.8 Fraction:** A k-mer found in more than 80% of the samples. It’s important to check if the - SNP counts make sense with the sample set and whether the core count is ridiculously high or low.

## Organize files
```
mkdir starting_files; mv *fasta starting_files
cp ./run/tree_tipAlleleCounts.SNPs_in_majority0.8.ML.tre .
cp ./run/tree_tipAlleleCounts.SNPs_all.ML.tre .
```

### [HOME](../README.md)