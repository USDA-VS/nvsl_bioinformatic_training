# AMRFinderPlus

## AMRFinderPlus: Pros and Cons

### Pros:

1. **Comprehensive Database:**
   - Utilizes NCBI's curated Reference Gene Database
   - Accurately identifies:
     - AMR genes
     - Resistance-associated point mutations
     - Other gene classes

2. **Regular Updates:**
   - Frequent database updates ensure up-to-date information
   - Improves accuracy and relevance of results over time

3. **Detailed Results:**
   - Provides comprehensive information about identified genes and mutations
   - Enhances understanding of antimicrobial resistance profiles

4. **Versatility:**
   - Applicable to various bacterial species
   - Useful for both research and clinical applications

5. **Integration:**
   - Can be easily integrated into bioinformatics pipelines
   - Supports high-throughput analysis

### Cons:

1. **Database Discrepancies:**
   - May cause confusion when compared to other tools (e.g., ABRicate with "ncbi" database)
   - Users should be aware that AMRFinderPlus uses a more comprehensive database and different methods

2. **Species-Specific Limitations:**
   - Does not account for inherent species characteristics (e.g., M. bovis resistance to pza)
   - Focuses on acquired antimicrobial resistance genes and mutations

3. **Interpretation Challenges:**
   - Results may require expert knowledge for proper interpretation
   - Some resistance mechanisms may be missed if they are not in the database

4. **Computational Requirements:**
   - May require significant computational resources for large datasets
   - Processing time can be longer compared to simpler tools

5. **False Positives:**
   - Potential for detecting genes that may not confer resistance in all contexts
   - Users should validate results with phenotypic testing when possible

**Note:** AMRFinderPlus is designed to detect acquired antimicrobial resistance genes and mutations. It may not identify inherent species characteristics or resistance mechanisms not included in its database. Always interpret results in the context of the specific organism and consider complementary methods for comprehensive resistance profiling.

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
```
amrfinder -h
```
Examples:

ERR766214 - BCG

SRR23410316 - Salmonella

Standard call
```
amrfinder --nucleotide ERR766214.fasta --output test-amrfinder.tab --threads 4
```

--plus option enables the identification of not only the core set of AMR elements, but also includes genes related to stress response and virulence
```
amrfinder --nucleotide ERR766214.fasta --plus --output test-amrfinder_plus.tab --threads 4
```

M. bovis, including BCG strains, is resistant to pza but does not show in AMRFinderPlus output.  AMRFinder Plus is designed to detect acquired antimicrobial resistance genes and mutations, not an inherent characteristic of the species such as pncA gene mutations conferring resistence for all isolates.  Mutations in the pncA gene are intrestic to pza resistanc in M. bovis.

Using the `--plus` option, searches for other genes of interest beyond AMR genes, gives broader gene coverage including virulence factors, stress response genes, and other relevant genetic elements

Specifying the `--organism` option, screens for known organism specific resistance-causing point mutations and helps in blacklisting common, non-informative genes that are extremely prevalent in the specified organism

[Organism option](https://github.com/ncbi/amr/wiki/Running-AMRFinderPlus#--organism-option)

```
amrfinder --nucleotide *fasta --output test-amrfinder_normal.tab --threads 4
```
```
amrfinder --nucleotide *fasta --plus --output test-amrfinder_plus.tab --threads 4
```
```
amrfinder --nucleotide *fasta -O Salmonella --output test-amrfinder_O.tab --threads 4
```

## Coverting a tab delimited file to Excel

In amrfinder environment

```
conda install python pandas openpyxl
```
### Tab to Excel
tab_to_excel.py
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
./tab_to_excel.py <input>
```

[Link](https://www.ncbi.nlm.nih.gov/datasets/genome/GCF_000008865.2/) to Escherichia coli O157:H7 </br>

### [HOME](../README.md)