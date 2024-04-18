# [kSNP](https://academic.oup.com/bioinformatics/article/31/17/2877/183216)

kSNP identifies SNPs in genomes without the requirement for genome alignment or a reference genome.

We will be following the [Additional Tools link](https://github.com/USDA-VS/vSNP3/blob/main/docs/instructions/additional_tools.md) within the vSNP documentation


See [folder](../data/trees/) for example data

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

## [Metrics/stats](../data/trees/ksnp/ksnp_bruc_comparison_stats.png)
- **K-mer Size Used:** This refers to the length of the k-mer used in the analysis.
- **K-mer = Position:** In a 19-mer, the SNP is located 9 nucleotides upstream and downstream from the SNP.
- **Core:** A core k-mer is found in all samples. Only the middle nucleotide of the k-mer is considered as the SNP.
- **Non-Core:** A non-core k-mer is not found in all samples.
- **0.8 Fraction:** A k-mer found in more than 80% of the samples. It’s important to check if the - SNP counts make sense with the sample set and whether the core count is ridiculously high or low.
- **Core Homoplastic SNP:** A SNP position (k-mer) that is not obviously determined by a common ancestor and is seen in all samples. This could indicate a messy SNP call.
- **0.8 Homoplastic SNP:** A SNP position (k-mer) that is not obviously determined by a common ancestor and is seen in more than 80% of samples. If the count of homoplastic SNPs is high, it could indicate an issue with the input sample set, quality, or transposable elements.

### [README](../README.md)