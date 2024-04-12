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

### [README](../README.md)