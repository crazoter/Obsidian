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