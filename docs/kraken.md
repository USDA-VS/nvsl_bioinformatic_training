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

Follow [link](https://github.com/USDA-VS/vSNP3/blob/main/docs/instructions/additional_tools.md#krakenkrona) to kraken instructions

### [README](../README.md)