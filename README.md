# lectures-fall2018

A repository hosting materials for a lecture series aimed at undergraduates offered at the University of Chicago during the Fall quarter in 2018.
The modules contained herein are meant to aid students through a series of lectures describing technical computing techniques often used in gravitational wave analyses. 

## lecture notes

Some lecture notes can be found within this repostitory.
Others can be found in [Google Drive](https://drive.google.com/drive/folders/1xwmOKxjHyTkvSpeAOS_-NaUv-15uKVEA).

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
