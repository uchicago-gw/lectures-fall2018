# lectures-fall2018

Lectures will be held in **[KPTC 206](https://www.google.com/maps/place/Kersten+Physics+Teaching+Center/@41.7910228,-87.6037179,17z/data=!3m1!4b1!4m5!3m4!1s0x880e293e862a1b5f:0x3726b2d1e371c9b8!8m2!3d41.7910228!4d-87.6015292)** on **Wednesdays at 7pm** throughout the quarter.

**Please fill out [this short survey](https://goo.gl/forms/deUMrr7leHhrq0eo1)!**

This repository hosts materials for a lecture series aimed at undergraduates offered at the University of Chicago during the Fall quarter in 2018.
The modules contained herein are meant to aid students through a series of lectures describing technical computing techniques often used in gravitational wave analyses. 

## lecture notes

Some lecture notes can be found within [this repostitory](https://github.com/uchicago-gw/lectures-fall2018/tree/master/lecture_notes).
Others can be found in [Google Drive](https://drive.google.com/drive/folders/1xwmOKxjHyTkvSpeAOS_-NaUv-15uKVEA).

A great list of papers about GW measurements is available at [papers.ligo.org](https://www.ligo.caltech.edu/page/detection-companion-papers).

## syllabus and futher reading

  * Oct 17: Introduction
    * Lecturer: [Zoheyr Doctor](zdoctor@uchicago.edu)
    * lecture notes
      * [google sheet for zero-crossing times](https://docs.google.com/spreadsheets/d/1-KZ8zCI0sLLdETamXjnFnUk6ODnxpDhkcZ6ssXGQuc4/edit?usp=sharing)
    * further reading
        * [GW150914 detection PRL](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.116.061102)
        * [The basic physics of the binary black hole merger GW150914](https://arxiv.org/abs/1608.01940)

  * Oct 24: Stellar Structure and Neutron Stars
    * Lecturer: [Phil Landry](landryp@uchicago.edu)
    * lecture notes: ...
    * further reading
        * ...

  * Oct 31: Fourier Analysis
    * Lecturer: [Reed Essick](reedessick@uchicago.edu)
    * [lecture notes](https://github.com/uchicago-gw/lectures-fall2018/blob/master/lecture_notes/fourier_analysis.md)
    * further reading
        * ...

  * Nov 7: Initial Value Problems and GW Sources
    * Lecturer: [Zoheyr Doctor](zdoctor@uchicago.edu)
    * lecture notes: ...
    * further reading
        * ...

  * Nov 14: Cosmology
    * Lecturer: [Maya Fishbach](mfishbach@uchicago.edu)
    * lecture notes: ...
    * further reading
        * ...

  * Nov 21: Tolman-Oppenheimer-Volkoff Equations
    * Lecturer: [Phil Landry](landryp@uchicago.edu)
    * lecture notes: ...
    * further reading
        * ...

  * Nov 28: Time-series Analysis and Basci Parameter Estimation
    * Lecturer: [Reed Essick](reedessick@uchicago.edu)
    * [lecture notes](https://github.com/uchicago-gw/lectures-fall2018/blob/master/lecture_notes/stationary_gaussian_timeseries.md)
    * further reading
        * ...

  * Dec 5: Monte-Carlo Methods and the Hubble Constant
    * Lecturer: [Maya Fishbach](mfishbach@uchicago.edu)
    * lecture notes: ...
    * further reading
        * ...

### possible final projects

As part of this lecture series, you will be expected to complete a small project.
Please check with one of the lecturers if you have a specific idea you'd like to pursue.
Below, we've listed a few possibilities.

  * a few-parameter search for Gravitational Waves in stationary colored Gaussian noise
  * inferring Hubble's constant using real, publicly available [GW170817 data](https://www.gw-openscience.org/events/GW170817/)
  * determining the mass-radius, mass-lambda curves for a few neutron star equations of state
  * ...

## installation

We highly recommend you use Python notebooks with standard anaconda installations.
However, if you are comfortable with other IDEs, all our modules should work with relatively standard dependencies (numpy, scipy, etc).

### anaconda

(Ana)conda installation instructions are available [here](https://conda.io/docs/user-guide/install/index.html).
There are separate instructions for various OSs

  * [Windows](https://conda.io/docs/user-guide/install/windows.html)
  * [MacOS](https://conda.io/docs/user-guide/install/macos.html) (ask Zoheyr or Maya for help if needed)
  * [Linux](https://conda.io/docs/user-guide/install/linux.html) (ask Reed or Phil for help if needed)

### this repository

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
