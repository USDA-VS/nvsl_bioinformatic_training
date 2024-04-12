# AMRFinderPlus

[Documenation](https://www.ncbi.nlm.nih.gov/pathogens/antimicrobial-resistance/AMRFinder/)

Notice Abricate subset

[Conda install](https://github.com/ncbi/amr/wiki/Install-with-bioconda#2-install-amrfinder-with-bioconda)


Update Database
```
amrfinder -u
```

[Organism option](https://github.com/ncbi/amr/wiki/Running-AMRFinderPlus#--organism-option)

[Test](https://github.com/ncbi/amr/wiki/Test-your-installation)

```
amrfinder -h
```

Standard call
```
amrfinder --nucleotide {assembly} --output {sample_name}-amrfinder.tab --threads {threads}
```

Using the plus genes
```
amrfinder --nucleotide {assembly} --plus --output {sample_name}-amrfinder.tab --threads {threads}
```

Specifying the organism
```
amrfinder --nucleotide {assembly} -O {self.organism} --output {sample_name}-amrfinder.tab --threads {threads}
```

[Link](https://www.ncbi.nlm.nih.gov/datasets/genome/GCF_000008865.2/) to Escherichia coli O157:H7 </br>
[Local file](../data/GCF_000008865.2_ASM886v2_genomic.fasta) 

If in amrfinder environment
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
./file.py <input>
```

Escherichia

### [README](../README.md)