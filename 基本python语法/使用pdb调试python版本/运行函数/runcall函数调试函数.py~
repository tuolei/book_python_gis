>>> import pdb
>>> def sum(*args):
...     r = 0
...     for arg in args:
...         r = r + arg
...     return r
... 
>>> pdb.runcall(sum,1,2,3,4)
> <stdin>(2)sum()
(Pdb) n
> <stdin>(3)sum()
(Pdb) n
> <stdin>(4)sum()
(Pdb) print(r)
0
(Pdb) continue
10
>>> pdb.runcall(sum,1,2,3,4,5,6)
> <stdin>(2)sum()
(Pdb) continue
21

