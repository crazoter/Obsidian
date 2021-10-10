#### Writing file
#### writelines (array)
```
# Writing to file
# w+: create if not exists, overwrite
with open(file, "w+") as outfp:
    fp.writelines([])
```

##### write (line)
```
# Writing to file
with open(outfile, "w") as outfp:
    fp.write(s)
```

#### Reading file

##### for loop
``` 
# Read file w/ for loop
with open(file) as fp:
    for line in fp:
        parts = line.strip().split('-')
		if len(parts) > 0:
			# todo
```

##### readline
``` 
# Read file w/ readline()
with open(file) as fp:
    while True:
        line = fp.readline()
        if not line:
            break
        # print(line.strip())
``` 

##### readlines
```
# Read file w/ readlines()
with open(file) as fp:
    for line in fp.readlines():
        # print(line.strip())
``` 

#### Recursively read files in a directory
```Python
# This is an automatically generated template for Sublime Text snippets. For more information, see https://sublime-text-unofficial-documentation.readthedocs.io/en/stable/extensibility/snippets.html
# Fields: ${1:this} is a ${2:snippet}
# Context: $SELECTION
# File is saved using tabTrigger name.

#region SNIPPET
<snippet><content><![CDATA[
# Req: Python 3.4+
# https://stackoverflow.com/questions/18394147/recursive-sub-folder-search-and-return-files-in-a-list-python
from pathlib import Path
for filename in Path(${1:rootFolder}).rglob("*.[mM][dD]"):
	with open(filename, 'r',errors='replace') as fp:
		${2:body}
]]></content>
<tabTrigger>io-iterdir</tabTrigger>
<scope>source.python</scope>
</snippet>
#endregion
```

NOTES
Codec management for unknown decoding

https://stackoverflow.com/questions/35028683/python3-unicodedecodeerror-with-readlines-method

> I think the best answer (in Python 3) is to use the `errors=` parameter:

```python
with open('evil_unicode.txt', 'r', errors='replace') as f:
    lines = f.readlines()
```

Read and replace file
https://stackoverflow.com/questions/2746758/how-do-i-overwrite-a-file-currently-being-read-by-python
```python
import os
f = open('input.pdf', 'rb')
# do stuff to temp.pdf
f.close()
os.rename('temp.pdf', 'input.pdf')
```