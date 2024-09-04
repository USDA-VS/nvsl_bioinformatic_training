Loop everything in directory
```
for i in *; do
    echo $i
done
```
Make it a one-liner
```
for i in *; do echo $i; done
```
Read file line by line
```
while read line; do echo "$line"; done < infile.txt
```