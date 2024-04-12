# VS Code Debugger

Select Python interpreter

launch.json

```
    "configurations": [
        {
            "name": "get_meta_demo",
            "type": "python",
            "request": "launch",
            "console": "integratedTerminal",
            "program": "/Users/tstuber/git/gitlab/nvsl_bioinformatic_training/data/get_meta_demo.py",
            "args": ["-f", "a.txt", "-e", "metadata.xlsx",],
            "cwd": "/Users/tstuber/test/meta",
        },
    ]
```

# Sample Naming

- Unique
- Never use spaces
    - Not in sample names
    - Not in folder names (use underscores in-place of spaces)
- Do not use special characters is <u>sample</u> names.
    - our lab allows "-" dashes, but not "_" underscores or periods
    - 20-037580-001s_S1_L001_R1_cut.fastq.gz --> 20-037580-001s
    - 18-05314-rpob.fas --> 18-05314-rpob
    - 18-05314_rpob.fas --> 18-05314
    - 18_05314-rpob.fas --> 18
- Pad numbers with zeros if starting from 1 and going beyond 10
    - searching "sample-1" vs "sample-0001" will find:
        - "sample-1"
        - "sample-10"
        - "sample-100"
        - "sample-1000"

# Metadata

- No Personal Identification
    - this becomes increasingly important with big datasets
        - Less secure environments
        - Large sample numbers increases chance to miss mistakes
- Sample names
  - Must be unique
    - Recommend laboratory accession
    - No simple sequential numbering

### [README](../../README.md)
