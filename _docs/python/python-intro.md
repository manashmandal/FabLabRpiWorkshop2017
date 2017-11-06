---
title: Python Intro
permalink: /docs/python-intro/
---

### Instructor: Mamun EEE, 2k14


```python
print("Hi there, Python 3")     # How to print something?
```

    Hi there, Python 3


### semicolon

`Where are those semicolons?`




```python
print('Hi '); print('there, '); print('Pyhton 3')    # Interpreters vs Compilers
                                                     # Youtube streaming vs Downloading analogy
```

    Hi 
    there, 
    Pyhton 3



```python
a = input('a = ')                             # CLI
b = input('b = ')

a += '0'                                      # string concatenation
b += '0'                                      # operator overloading

print(type(a))                                # string

print(a+b)
                            
```

    a = 16
    b = 2
    <class 'str'>
    16020



```python
a = input('a = ')                             # CLI
b = input('b = ')

a += '0'                                      # string concatenation
b += '0'

print(type(a))                                # string

print(a+b)

a = int(a)                                    # type-casting
b = int(b)

print(type(b))                                # integer

a += 5
b += 5

print(a,b,a+b)

```

    a = 10
    b = 5
    <class 'str'>
    10050
    <class 'int'>
    105 55 160



```python
a = input('a = ')                             # CLI
b = input('b = ')

a += '0'                                      # string concatenation
b += '0'

print(type(a))                                # string

print(a+b)

a = int(a)                                    # type-casting
b = int(b)

print(type(b))                                # integer

a += 5
b += 5

print(a,b,a+b)

if a < b:
    print('Just gonna print a 0')
elif a == b:
    print('Just gonna print a 1')
else:
    print("Can't predict :( ")

print(a//b)                                   
```

    a = 7
    b = 17
    <class 'str'>
    70170
    <class 'int'>
    75 175 250
    Just gonna print a 0
    0


### a little bit of modular arithmetic

  * How many multiples of $3$ are there in a list?

  * Find all such $y$ such that, $y = 57*x + 13$     where, $0 <= y <= 1000$ and $x$ belongs to *$N$*


```python
# a_list = [1,2,3,4,5,6,7,8,9,10]          # list

a_list = list(range(1,11))               # why 11?

print(type(a_list))

print(a_list)

for a_i in a_list:
     if a_i % 3 == 0:
        print(a_i,end = ' ')
```

    <class 'list'>
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    3 6 9 


```python
y_rng = range(1,1001)                    # why 1001?

print(type(y_rng))

for y in y_rng:
    if y % 57 == 13:
        print(y,end=' ')
```

    <class 'range'>
    13 70 127 184 241 298 355 412 469 526 583 640 697 754 811 868 925 982 


```python
! pip install future             # Using pip
```

    Requirement already satisfied: future in c:\anaconda3\lib\site-packages


### packages, subpackages and modules

> Requirement already satisfied: future in 'dir' ....

* Let's see, how the directory 'dir' is organized
 * `__init__.py`, packages, subpackages, modules, namespace, `__path__`


```python
from future.backports import datetime as dt
 
# year = input('year : ')

print(dt)

print(dir(dt),'\n')                 #  dir() method tries to return a list of valid attributes of the object

today = dt.date.today()

print(today,'\n')

another_day = dt.date(2017,11,11)

print(another_day)


```

    <module 'future.backports.datetime' from 'C:\\Anaconda3\\lib\\site-packages\\future\\backports\\datetime.py'>
    ['MAXYEAR', 'MINYEAR', 'PY2', '_EPOCH', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'absolute_import', 'bytes', 'date', 'datetime', 'datetime_CAPI', 'division', 'int', 'map', 'native_str', 'object', 'print_function', 'round', 'str', 'time', 'timedelta', 'timezone', 'tzinfo', 'unicode_literals'] 
    
    2017-11-04 
    
    2017-11-11


### python 2/3 compatibility and future

*  run python 2 code from python 3 using past


```python
from past.builtins import xrange                # running python 2 in python 3

a = list(xrange(11))

a[0] += 2
a[0] **= 2

print('length of a = ',len(a),'\n')

a[len(a)-1] *= 2 

print(sorted(a))

print('\n')

for x in xrange(11):
    print(a[x],end = ' ')
    
print('\n')
    
a.sort()

for x in xrange(11):
    print(a[x],end = ' ')
```

    length of a =  11 
    
    [1, 2, 3, 4, 4, 5, 6, 7, 8, 9, 20]
    
    
    4 1 2 3 4 5 6 7 8 9 20 
    
    1 2 3 4 4 5 6 7 8 9 20 


```python
from __future__ import division            # running python 3 in pyhton 2


```

### our own functions and default parameters

* `def`, `return`


```python
def my_fun():
    
    print("Hi there, Python 3")
```


```python
my_fun()
```

    Hi there, Python 3



```python
def your_fun(a,b,c=5):
    
    print(a,b,c)
    return a * b + c

```


```python
k1 = your_fun(5,4,3)
print(k1)
k2 = your_fun(1,2)
print(k2)
```

    5 4 3
    23
    1 2 5
    7



```python
def add_str(a, c, i_am_string=''):          # why i_am_string is the last argument?
    i_am_string += a
    i_am_string += c
    return i_am_string
```


```python
st = add_str('a','b')
print(st)
st = add_str('c','d')
print(st)
```

    ab
    cd


### let's develop our lil_geometry module

* `go to a new fresh directory`
* `create a folder 'pack_lev1'`
* `inside, 'pack_lev1' create a python script named 'lil_geometry.py'`


![nm1]({{site.url}}{{site.baseurl}}/docs/python/nm1.png)


```python
# lil_geometry.py
import math as m

def area_of_circle(rad):
    return 2*m.pi*rad


print(__name__)
```

    __main__



```python
# lil_geometry.py
import math as m

def area_of_circle(rad):
    return 2*m.pi*rad


print(__name__)

if ( __name__ == '__main__' ):
    rad = input('Enter radius : ')
    print("radius of cirlce is {}".format(area_of_circle(int(rad))))
```

    __main__
    Enter radius : 12
    radius of cirlce is 75.39822368615503


### module_test
* `go to root`
* `create a script named 'module_test'`


```python
# testing module lil_geometry.py

from pack_lev1 import lil_geometry as lg
```

![nm2]({{site.url}}{{site.baseurl}}/docs/python/nm2.png)

### running module_test

* `open cmd in that folder and type 'python module_test.py'`

![nm3]({{site.url}}{{site.baseurl}}/docs/python/nm3.png)

![nm4]({{site.url}}{{site.baseurl}}/docs/python/nm4.png)

![nm5]({{site.url}}{{site.baseurl}}/docs/python/nm5.png)

![nm6]({{site.url}}{{site.baseurl}}/docs/python/nm6.png)

![nm7]({{site.url}}{{site.baseurl}}/docs/python/nm7.png)


```python
# testing module lil_geometry.py

from pack_lev1 import lil_geometry as lg

print('module_test __name__ : {}'.format(__name__))

print(lg.area_of_circle(5))  # using functions from imported module
```

### github, git
* a break for me  `    `  :P
* go to `https://github.com` and open an account
* verify email address

### pip, easy_install and setup.py


* `https://github.com/pyjokes/pyjokes`
* clone this repo
* python setup.py install command


```python
! cd
```


```python
% pwd
```




    'A:\\GitUps\\FabLabIntroPythonWorkshop\\fab-lab-python-intro-workshop\\Notebook'



- Go to the folder where you cloned pyjokes
- Shift + Right Mouse button -> Open CMD here



![setup_py1]({{site.url}}{{site.baseurl}}/docs/python/setup_py1.png)


### In cmd, type
- `python`
- `import pyjokes as pj`
- `a_joke = pj.get_joke()`
- `print(a_joke)` 




![setup_py2]({{site.url}}{{site.baseurl}}/docs/python/setup_py2.png)


### forget about pycharm for a moment
- `Go to a new fresh directory`
- `Create a new python script 'finally.py'`
- `Write some creative piece of code using just an editor`
- `Open cmd in that folder`
- `python finally.py`

### command line arguments
* sys
* argv
* argv[0] is name of the script



![cl1]({{site.url}}{{site.baseurl}}/docs/python/cl1.png)


![cl2]({{site.url}}{{site.baseurl}}/docs/python/cl2.png)



```python
import sys as s_

print(s_.argv)

if len(s_.argv) == 1:
    print('The name of the script is {} and there are no extra args'.format(argv[0]))
elif len(s_.argv) == 3:
    print('First name : {} Last name : {}'.format(s_.argv[1],s_.argv[2]))
    
```

![cl4]({{site.url}}{{site.baseurl}}/docs/python/cl4.png)

![cl5]({{site.url}}{{site.baseurl}}/docs/python/cl5.png)
![cl6]({{site.url}}{{site.baseurl}}/docs/python/cl6.png)
![cl3]({{site.url}}{{site.baseurl}}/docs/python/cl3.png)



```python
import sys as s_

print(s_.argv)

if len(s_.argv) == 1:
    print('The name of the script is {} and there are no extra args'.format(argv[0]))
elif len(s_.argv) == 3:
    print('First name : {1} Last name : {0}'.format(s_.argv[1],s_.argv[2]))
    
```

    ['C:\\Anaconda3\\lib\\site-packages\\ipykernel_launcher.py', '-f', 'C:\\Users\\zabir\\AppData\\Roaming\\jupyter\\runtime\\kernel-ffc5e574-b2b9-480f-b1ea-0b1b87f3d267.json']
    First name : C:\Users\zabir\AppData\Roaming\jupyter\runtime\kernel-ffc5e574-b2b9-480f-b1ea-0b1b87f3d267.json Last name : -f


![cl7]({{site.url}}{{site.baseurl}}/docs/python/cl7.png)
![cl8]({{site.url}}{{site.baseurl}}/docs/python/cl8.png)

