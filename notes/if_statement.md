```
n=5
```
```
if [ $n -gt 10 ]; then echo "greater than 10"; else echo "less or equal to 10"; fi
```
```
n=11
```
```
n=m
```
```
for d in ./*; do if [[ ! -n $(echo ./${d}/*pdf) ]]; then echo "$d"; fi; done 2> /dev/null
```

### [README](../README.md)