# AMRFinderPlus

## Pros:

- AMRFinderPlus uses NCBI’s curated Reference Gene Database, very comprehensive.  This allows for accurate identification of AMR genes, resistance-associated point mutations, and other classes of genes.
- Regular Updates
- Detailed Results

## Cons:

- Confusion when using ABRicate with the default “ncbi” database, as they expected similar results to AMRFinderPlus. It’s important to note that ABRicate uses a subset of the AMRFinderPlus database and different methods, so the results are not the same.

##
## Usage

[Documenation](https://www.ncbi.nlm.nih.gov/pathogens/antimicrobial-resistance/AMRFinder/)

Notice Abricate subset

[Conda install](https://github.com/ncbi/amr/wiki/Install-with-bioconda#2-install-amrfinder-with-bioconda)
```
conda create -n amrfinder -c conda-forge -c bioconda ncbi-amrfinderplus
```

Update Database
```
amrfinder -U
```

[AMRFinderPlus test](https://github.com/ncbi/amr/wiki/Test-your-installation)

[Local test file](../data/GCF_000008865.2_ASM886v2_genomic.fasta) 

```
amrfinder -h
```

Standard call
```
amrfinder --nucleotide *fasta --output test-amrfinder1.tab --threads 4
```

--plus option enables the identification of not only the core set of AMR elements, but also includes genes related to stress response and virulence
```
amrfinder --nucleotide *fasta --plus --output test-amrfinder2.tab --threads 4
```

Specifying the organism for screening known resistance-causing point mutations and helps in blacklisting common, non-informative genes that are extremely prevalent in the specified organism

[Organism option](https://github.com/ncbi/amr/wiki/Running-AMRFinderPlus#--organism-option)

```
amrfinder --nucleotide *fasta -O Escherichia --output test-amrfinder3.tab --threads 4
```

## Coverting a tab delimited file to Excel

In amrfinder environment

```
conda install python pandas openpyxl
```

```
#!/usr/bin/env python

import sys
import pandas as pd

tab_file = sys.argv[1]
excel_file = tab_file.replace("tab", "xlsx")
df = pd.read_csv(tab_file, sep="\t")
df.to_excel(excel_file)
```

```
chmod 755 *py
```
```
./to_excel.py <input>
```

[Link](https://www.ncbi.nlm.nih.gov/datasets/genome/GCF_000008865.2/) to Escherichia coli O157:H7 </br>

### [README](../README.md)