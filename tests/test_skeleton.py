#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from class_project_1.skeleton import fib

__author__ = "Yerim Lee"
__copyright__ = "Yerim Lee"
__license__ = "mit"


def test_fib():
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(7) == 13
    with pytest.raises(AssertionError):
        fib(-10)
