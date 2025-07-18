#!/usr/bin/env python3
import pytest
from sea_depth import compare_to_prev, add_trios

# Test each case for compare_to_prev
def test_depth_less_than_prev():
    assert compare_to_prev(10, 20) == -1

def test_depth_equal_to_prev():
    assert compare_to_prev(15, 15) == 0

def test_depth_greater_than_prev():
    assert compare_to_prev(30, 10) == 1

# Test each case for add_trios
def test_under_3():
    with pytest.raises(ValueError):
        add_trios([3,5])

def test_negs():
    assert add_trios([2,0,-4,-1,5]) == [-2,-5,0]

def test_floats():
    with pytest.raises(ValueError):
        add_trios([0.2,0.4,0.1,0.5])