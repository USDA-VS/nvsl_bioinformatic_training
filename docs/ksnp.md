# [kSNP](https://academic.oup.com/bioinformatics/article/31/17/2877/183216) - reference free

We will be following the [Additional Tools link](https://github.com/USDA-VS/vSNP3/blob/main/docs/instructions/additional_tools.md) within the vSNP documentation

- [kSNP metrics](../data/trees/ksnp/ksnp_bruc_comparison_stats.png)


See [folder](../data/trees/) for example data
    
- Cons
    - Is there contamination?
        - 0.8 majority
    - Difficult to validate SNPs
    - Slow with large datasets
- Pros
    - Reference isn't needed
    - No reference bias
    - Better hands more diverant datasets
    - Useful for finding references for reference based comparison (vSNP)
- [Metrics/stats](../data/trees/ksnp/ksnp_bruc_comparison_stats.png)
    - kmer size used
    - kmer = position, 19mer - 9 up and down stream from SNPs
    - core - kmer found in all samples - only looking at the middle kmer nucleotide as SNP.  
    - non-core - kmer is not found in all samples
    - 0.8 fraction - kmer found in >80% of samples.
        - Do SNP counts make sense with sample set
        - Is core count ridiculous high or low
    - core homoplastic snp - snp position (kmer) not obvious by common ancestor and seen in all samples (messy SNP call)
    - 0.8 homoplastic snp - snp position (kmer) not obvious by common ancestor and seen in >80% of samples
        - If homoplastic SNPs are high could be an input sample set, quality, transposable element issue

### [README](../README.md)