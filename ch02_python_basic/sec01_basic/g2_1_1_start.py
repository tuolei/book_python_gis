# -*- coding: utf-8 -*-

print('Hello, python world!')
strval1 = 'Welcome'
strval2 = 'Python World!'
print(strval1)
print(strval2 + strval1)

def Test():
    assert 'WelcomePython World!' == (strval1 + strval2)
