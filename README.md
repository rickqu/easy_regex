# easy_regex
Wrapper over regex that looks like code. 

Write this:
```
NUMBER = D(1,NO_LIMIT) + '.' + D(1,NO_LIMIT)
x = '(' + NUMBER('x') + ',' + NUMBER('y') + ')'
```

Get this:
```
\((?<x>\d{1,}\.\d{1,}),(?<y>\d{1,}\.\d{1,})\)
```
