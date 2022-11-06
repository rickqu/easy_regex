# easy_regex
Wrapper over regex that looks like code. Still WIP.

Write this:
```
NUMBER = D(1,NO_LIMIT) + '.' + D(1,NO_LIMIT)
POINT = '(' + NUMBER('x') + ',' + NUMBER('y') + ')'
print(POINT.render())
```

Get this:
```
\((?<x>\d{1,}\.\d{1,}),(?<y>\d{1,}\.\d{1,})\)
```
Which matches any 2D coordinate points (without accounting for whitespace). 
