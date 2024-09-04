# Python
- [Python Library](https://docs.python.org/3/library/intro.html)
    - [Core](https://docs.python.org/3/library/index.html), Built-in, import not needed
    - [Standard Library](https://docs.python.org/3/library/), comes installed but needs import
    - Other
        - [Pandas](https://pandas.pydata.org/)
        - [BioPython](https://biopython.org/)
        - Custom scripts
- Object Oriented Programming
    - Additional layer of code organization
    - Classes create new objects
    - Still have functions under classes
    - `self` allows access outside defined function
- Spaces, Tabs and Indentation

imports
```
import os
import pandas as pd
from Bio import SeqIO
from usda_file_setup import Setup
```
defining a class
```
class Call_Class():
```
defining a function
```
class Call_Class():
    def call_fuction(self,):
        <instructions>
```
special init function
```
class Call_Class():
    def __init__(self, FASTA=None, debug=False):
        <instructions>
```
arguments
```
if __name__ == "__main__": # execute if directly access by the interpreter
    parser = argparse.ArgumentParser(prog='PROG', formatter_class=argparse.RawDescriptionHelpFormatter,)


    parser.add_argument('-f', '--fasta', action='store', dest='FASTA', help='FASTA file')
    parser.add_argument('-b', '--myboolean', action='store_true', dest='myboolean', help='description')
    args = parser.parse_args()
    
    print(f'\n{os.path.basename(__file__)} SET ARGUMENTS:')
    print(args)
    print("\n")

    myclass = Call_Class()
    myclass.call_fuction(FASTA=args.FASTA)
```

- [Interpreter](https://docs.python.org/3/tutorial/interpreter.html)
    - `python`
    - `ipython`
- Jupyter Labs
    - `jupyter lab`
      - `conda install -c conda-forge jupyterlab`
    - \<shift\>\<enter>
- VS Code
    - Text editor
    - Light weight but extensible
    - File management
    - Git integration
    - Debugging
- Debugging
    - Find errors
    - Breakpoints
    - Check variable and file output
    - Step through loops and logic
- Data Types
    - strings
    - integers
    - floats
    - tuples
    - list
    - dictionaries
    - dataframes

### Data type examples:
string
```
a = "axl"
```
integer
```
b = 1
```
float
```
c = 1.0
```
tuple - immutable
```
d = ("sue", 1, 1.0)
```
list
```
e = ["brick", 1.0]
e.append(1)
```
dictionary
```
f={}
f["a"] = "frankie"
f["b"] = 1
f["c"] = 1.0
f["c"] = "mike"
```

Indexing
```
g = [a, b, c, d, e, f]
g[0]
g[1]
g[5]
g[-1]
h, i, j, k, l, m = g
```

Loops
```
n=[]
for i in g:
    n.append(i)
```

Logic
```
if n == g:
    print("g and n are the same")
else:
    print("Difference between n and g")
    # list comprehension
    o = [x for x in n if x not in g]
    p = [x for x in g if x not in n]
    q = p + o
    print (q)
```
```
n.append("colin_firth")
g.append("doris")
```
Packages
```
from Bio import SeqIO

seq_dict=[]
for seq_record in SeqIO.parse('assembly.fasta', "fasta"):
    seq_dict[seq_record.id] = seq_record.seq

```

### [HOME](../README.md)