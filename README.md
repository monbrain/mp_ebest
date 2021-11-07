## mp_ebest

<!-- <h1>mp_ebest<img src='https://cdn.rawgit.com/miyuchina/mistletoe/master/resources/logo.svg' align='right' width='128' height='128'></h1>

[![Build Status][build-badge]][travis]
[![Coverage Status][cover-badge]][coveralls]
[![PyPI][pypi-badge]][pypi]
[![is wheel][wheel-badge]][pypi] -->

Moon Package for Ebest API

Features
--------




Installation
------------

0. Requirements
- os:
- python:
- api:


1. git+https

```sh
pip install git+https://github.com/moonstock/mp_ebest.git
```

2. clone the repo:

```sh
git clone https://github.com/miyuchina/mistletoe.git
cd mistletoe
pip3 install -e .
```


Usage
-----

### Basic usage

Here's how you can use mistletoe in a Python script:

1. alias package
```python
import mp_ebest as ebest


```

2. alias module
```python
from mp_ebest import (
    tranaction as ebest_tr,
    fetch as ebest_fetch,
    search as ebest_search,
)
    
```

### From the command-line

pip installation enables mistletoe's command-line utility. Type the following
directly into your shell:

```sh
ebest order --side <side> --ticker <ticker>  --price <price> --volume <volume> --type <type>
```

Performance
-----------



Copyright & License
-------------------
* mistletoe is released under [MIT][license].

<!-- [build-badge]: https://img.shields.io/travis/miyuchina/mistletoe.svg?style=flat-square
[cover-badge]: https://img.shields.io/coveralls/miyuchina/mistletoe.svg?style=flat-square
[pypi-badge]: https://img.shields.io/pypi/v/mistletoe.svg?style=flat-square
[wheel-badge]: https://img.shields.io/pypi/wheel/mistletoe.svg?style=flat-square
[travis]: https://travis-ci.org/miyuchina/mistletoe
[coveralls]: https://coveralls.io/github/miyuchina/mistletoe?branch=master
[pypi]: https://pypi.python.org/pypi/mistletoe
[mistune]: https://github.com/lepture/mistune
[license]: LICENSE
[pythonpath]: https://stackoverflow.com/questions/16107526/how-to-flexibly-change-pythonpath -->