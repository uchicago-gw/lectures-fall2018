# lectures-fall2018

A repository hosting materials for a lecture series aimed at undergraduates offered during the Fall quarter in 2018.
The modules contained herein are meant to aid students through a series of lectures describing technical computing techniques often used in gravitational wave analyses. 

## installation

This repository can be installed via standard tools

```
    git clone https://github.com/uchicago-gw/lectures-fall2018.git
    cd lectures-fall2018
    python setup.py install --prefix /path/to/install
```

don't forget to update your `PYTHONPATH` accordingly. For example,

```
    python setup.py install --prefix /home/albert.einstein/opt
    export PYTHONPATH=/home/albert.einstein/opt/lib/python2.7/site-packages:$PYTHONPATH
```
