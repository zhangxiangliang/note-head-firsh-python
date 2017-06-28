## Write File
### Uses
```
out = open("data.out", "w")
print('aaa', file=out)
out.close()
```
### Mode
* `w` will cleared file contents, and wrire.
* `a` will append to a file.
* `w+` will writing and reading a file.
* `rb` use binary mode open file.
* `wb` use binary mode open file.
* if file does not already exist, it is first created for you, and then opened for writing.

## BIF
* Searching the collection returned by the `locals()` BIF for the string data.
* `print(value, sep=' ', end='\n', 'file=sys.stdout')`

## pickle
* save with dump
* restore with load
