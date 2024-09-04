# Simple Examples

```
conda activate <env>
```
```
conda env list
```

### AMRFinder-Plus

```
amrfinder --nucleotide SRR17276215_amr.fasta --output SRR17276215_output.txt
```

### Kraken
```
wget https://sra-pub-run-odp.s3.amazonaws.com/sra/SRR6046640/SRR6046640 
```
```
fastq-dump --split-files SRR6046640
```
```
~/anaconda3/envs/bio1/bin/vsnp3_kraken2_wrapper.py -r1 SRR6046640_R1.fastq.gz -r2 SRR6046640_R2.fastq.gz --database ~/k2_standard_08gb
```

### vSNP
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