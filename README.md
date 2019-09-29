## Summary

The project provides a `search` module exposing a single function `min_search`. Given an array of elements, such
that the first few elements are strictly monotonically decreasing and the remaining elements are strictly monotonically
increasing, `min_search` will find the minimum element inside the array. The type of data inside the array is not
necessarily integers, but any objects implementing `__lt__` method. Therefore the minimum element is defined as the
element which is less than all other elements in the same set of data.

A strictly monotonically decreasing data is a set of elements such that `data[0] > data[1] ...  > data[n-1] > data[n]`.
In contracts, a strictly monotonically increasing data is a set of elements such that 
`data[0] < data[1] ... < data[n-1]] < data[n]`. For both cases, no two consecutive elements are equal.

The function applies a binary search on the data set, slightly modified to support those properties given about the data.
The resulting runtime has both an average and a worst case performance of `O(log n)`. The average and worst case space
complexity are both `O(1)`.

Detailed documentation available in the module

## Installation

Project supports python2.5 to python3.7

```
python setup.py
```

or via pip

```
pip install pip install https://github.com/3rHzf65m5DBrB2/micropsi-search/tarball/master
```

## Usage

```
from micropsi import search

search.min_search([3, 2, 1, 2, 5, 10])
> 1

search.min_search("edcbabcdefghijklmnopqrstxz")
> "a"
```

## Tests

You can run the tests manually against your desired python version
```
python -m unittests
```

or using Tox
```
tox .
```