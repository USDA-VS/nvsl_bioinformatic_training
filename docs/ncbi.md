# NCBI

- Huge datasets
- Organization today is an evolution of the past
- Serving the public
    - Maintain computing capacity and speed
    - How to take all biological data
    - How to provide a confortable user experience
    - Allow many ways to find
    - Share data "easily"
    - Stay modern

Issues:
- Too many choices
- Inconsistent results
- Difficult to interpret
- Difficult to navigate
- Lose out on improvements
- Avoidance

## [NCBI Entry Point](https://www.ncbi.nlm.nih.gov/)
- Log in
- List of databases
- Search "All Databases"
    - `Mycobacterium tuberculosis`
    - Sectioned search results
        - Genomes
            - Assembly
            - BioProject
            - BioSample
            - Genome
            - SRA

## Genomes
- Assembly
    - Status
        - GenBank, can be redundant, collaboration of NCBI, ENA, DDBJ (INSDC)
        - RefSeq, curated, non-redundant, owned by NCBI
    - Assembly level
    - Get files
        - "Download Assemblies"
        - "Send to, File, ID Table, Accession
        - NCBI Datasets
- BioProject
    - Collection of BioSamples
    - Collection of data determined by the submitter
        - publication
        - organization
        - description
        - timespan
- BioSample
    - Unique identifier given to any submitted file
    - Description of physical sample data is from
- Genome
    - Genomes page switching to Datasets Taxonomy page June 2023 (aka "list")
    - Numbers
        - INSDC (AL123456.3)
        - RefSeq number (NC_000962.3)
        - GenBank assembly accession (GCA_000195955.2)
        - RefSeq assembly accession (GCF_000195955.2)
- SRA
    - Data containers
    - FASTQs

- Tools
    - Website
    - E-utilities
    - NCBI Datasets
    - SRA Toolkit

E-utilities
```
from Bio import Entrez

Entrez.email = 'marty_mcfly@gmail.com'
accession = "NC_000962"
entryData = Entrez.efetch(db="nucleotide", id=accession, retmode="text", rettype='fasta')
writeFile = accession + ".fasta"
local_file=open(writeFile,"w")
local_file.write(entryData.read())
entryData.close()
local_file.close()
```
```
accession="AL123456"
```
```
accession="GCA_000195955"
```
NCBI Datasets
```
datasets download genome accession $accession --filename ${accession}.zip 
```
Wrappers
```
vsnp3_download_fasta_gbk_gff_by_acc.py -fbg -a NC_000962
```
```
fasta_GCA_get_metadata.py -a GCA_000195955 -gr
```
SRA Toolkit
```
fasterq-dump -S $i
```
Loop a list
```
total=`wc -l list`
counter=0
for i in `cat list`; do 
    counter=$((counter + 1))
    print "\n ### ${i}
    $counter of $total"
    fasterq-dump -S $i -t /dev/shm -e 10 -p
    pigz *fastq
done
```
Metadata - SRA Example.
- [NCBI](https://www.ncbi.nlm.nih.gov/)
- Search, "Mycobacterium bovis"
- Select SRA
- Run Selector
- Select samples
- Iterate list
- Add metadata

Sample Submissions
- [Portal](https://submit.ncbi.nlm.nih.gov/)
- Start a new submission - Types
- Upload options
- New submission
- Will need to work closely with SME
- Release Dates
- Assemblies and Annotation

BLAST
`CCCAGACTCCTACGGGAGGCAGCAGTGGGGAATATTGCACAATGGGCGCAAGCCTGATGCAGCGACGCCGCGTGAGGGATGACGGCCTTCGGGTTGTAAACCTCTTTCAATAGGGACGAAGCGCAAGTGACGGTACCTATAGAAGAAGGACCGGCCAACTACGTGCCAGCAGCCGCGGTAATACGTAGGGTCCGAGCGTTGTCCGGAATTACTGGGCGTAAAGAGCTCGTAGGTGGTTTGTCGCGTTGTTCGTGAAAACTCACAGCTTAACTGTGGGCGTGCGGGCGATACGGGCAGACTAGAGTACTGC`
- [web interface](https://blast.ncbi.nlm.nih.gov/Blast.cgi?PAGE=Nucleotides&PROGRAM=blastn&MEGABLAST=on&BLAST_PROGRAMS=megaBlast&PAGE_TYPE=BlastSearch&SHOW_DEFAULTS=on)
    - [help doc](https://ftp.ncbi.nlm.nih.gov/pub/factsheets/HowTo_BLASTGuide.pdf)
    - Choose Search Set
    - Program Selection
    - Site does a great job explaining the details
- BLAST types (task)
    - blastn
    - blastn-short
    - dc-megablast
    - megablast
    - rmblastn
- Command-line
    - Faster
    - Local options
    - Output format options
- [Databases](https://ftp.ncbi.nlm.nih.gov/blast/db/)
    - [Types](https://ftp.ncbi.nlm.nih.gov/blast/db/README)
        - nt
        - ref_viruses_rep_genomes
        - 16S_ribosomal_RNA
        - custom
    - update_blastdb.pl
- Local or remote access
    - local is default
    - `-remote` option
- Local builds
    - Faster
    - Keeps data internal
    - Must keep up-to-date

Example:
```
blastn -query <FASTA> -db nt -word_size 11 -out blast_out.txt -outfmt "6 sacc qlen slen gaps length qcovs evalue bitscore pident mismatch stitle" -num_alignments 15 -remote
```
See NCBI BLAST website for remote databases available

### [HOME](../README.md)