>>> import pdb
>>> l = [1,2,3]
>>> pdb.runeval('l[1]')
> <string>(1)<module>()
(Pdb) n
--Return--
> <string>(1)<module>()->2
(Pdb) n
2
>>> pdb.runeval('3+5*6/2')
> <string>(1)<module>()->2
(Pdb) n
--Return--
> <string>(1)<module>()->18
(Pdb) n
18

