# Kraken

Kraken operates by dissecting a given DNA sequence into smaller fragments known as k-mers. These k-mers are then cross-referenced with a comprehensive database. This database associates each k-mer with the Lowest Common Ancestor (LCA) of all genomes containing that specific k-mer. By doing this, Kraken can accurately predict the taxonomic classification of the original DNA sequence. We typically run Kraken on FASTQ reads to get an estimate of identification for each short read sequence, but it can also be used on FASTA files.

## Pros
- Visually intuitive
- HTML files can be shared
- Fast Analysis
- Pre-built databases now available
- Customizable

## Cons
- Large Database
- High memory requirements
- Not imune to database error and bias

## Install
```
conda create -n kraken -c conda-forge -c bioconda kraken2 krona krakentools wget pandas pigz
```

After the conda install additional setup instructions are provided.

[Download](https://benlangmead.github.io/aws-indexes/k2) Kraken database.

There are many Databases to choose from.  If unsure and download speeds allow try the standard database.  If a smaller database is necessary Standard-8 may be a good option.  Look at site for exact database naming.

Example download
```
cd ~; wget https://genome-idx.s3.amazonaws.com/kraken/k2_standard_08gb_20240605.tar.gz
```
```
mkdir k2_standard_08gb; tar -xzf k2_standard_08gb_*.tar.gz -C k2_standard_08gb
```

If needed link database to conda environment and download taxonomy.

```
rm -rf ${HOME}/miniconda3/envs/kraken/opt/krona/taxonomy
ln -s ${HOME}/k2_standard_08gb ${HOME}/miniconda3/envs/kraken/opt/krona/taxonomy
cd ~/k2_standard_08gb; ktUpdateTaxonomy.sh
```
## Run sample
### Kraken
```
db="${HOME}/k2_standard_08gb"
sample_name=$(echo *_R1*fastq.gz | sed 's/[_.].*//')
kraken2 --db ${db} --threads 4 --paired ERR766214_R1.fastq.gz ERR766214_R2.fastq.gz --output ${sample_name}-outputkraken.txt --report ${sample_name}-reportkraken.txt
```
### Krona graph

```
kreport2krona.py --intermediate-ranks -r *reportkraken.txt -o ${sample_name}.krona
ktImportText ${sample_name}.krona -o ${sample_name}_krona.html
rm ${sample_name}.krona
```

### [HOME](../README.md)