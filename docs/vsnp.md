# [vSNP](https://github.com/USDA-VS/vSNP3)

Reference based SNP calling.  Workflow used to continually add samples to a dataset, and organize that data in way that allows for SNP validation.

### Pros
- high resolution SNP analysis
- confidence in SNP calls
- visualize SNP differences in tables
- workflow provides a predictable and familiar data structure
- handles large datasets

### Cons
- reference based
- time intensive 
  - reference setup
  - data validation
- subjective SNP filtering

## Installation

vSNP can be installed via Anaconda.

If Anaconda is not installed follow steps at [package_manager](../docs/package_manager.md) setup.

Follow setup and testing at [vSNP3 GitHub page](https://github.com/USDA-VS/vSNP3/tree/main).

## Dependency files
- reference.fasta
- define_filter.xlsx
- metadata.xlsx

## Output
- Organized by reference type
- Step 1 - alignments
- Step 2 - VCF collection

## Install
```bash
conda create -c conda-forge -c bioconda -n vsnp3 vsnp3=3.24
```
## Download test files
```
cd ~; git clone https://github.com/USDA-VS/vsnp3_test_dataset.git
```
## Add reference:
```
cd ~/vsnp3_test_dataset/vsnp_dependencies
```
```
vsnp3_path_adder.py -d `pwd`
```
## Run
```bash
vsnp3_path_adder.py -s
```
```bash
vsnp3_step1.py -r1 ERR766214_R1.fastq.gz -r2 ERR766214_R2.fastq.gz -t Mycobacterium_AF2122
```
Look over [stats](../data/ERR766214_2024-07-25_08-58-42_stats.xlsx)

Add VCF to database and run step 2
```bash
vsnp3_step2.py -t Mycobacterium_AF2122 -a
```
## Run multiple
BCG samples
```bash
ERR766216
ERR766219
ERR766220
ERR766213
ERR766225
ERR766224
SRR398629
ERR766223
ERR234151
SRR7983756
ERR017778
ERR766218
ERR766215
ERR766217
ERR766214
ERR766222
ERR766221
ERR766226
```

Package FASTQs
```zsh
for fastq in *.fastq.gz; do name=$(echo $fastq | sed 's/[._].*//'); mkdir -p $name; mv -v $fastq $name/; done
```

Loop directories
```zsh
NUM_PER_CYCLE=4; starting_dir=$(pwd); for dir in ./*/; do (echo "starting: $dir"; cd ./$dir; vsnp3_step1.py -r1 *_R1*.fastq.gz -r2 *_R2*.fastq.gz; cd $starting_dir) & let count+=1; [[ $((count%NUM_PER_CYCLE)) -eq 0 ]] && wait; done
```

Collect Stats
```zsh
mkdir stats; cp ./*/*stats.xlsx stats; cd stats; vsnp3_excel_merge_files.py
```

### [HOME](../README.md)