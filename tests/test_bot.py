#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from class_project_1.bot import recognize_greeting

__author__ = "Yerim Lee"
__copyright__ = "Yerim Lee"
__license__ = "mit"


def test_recognize_greeting():
    assert recognize_greeting('Hi') == True
    assert recognize_greeting('Yo') == False
    assert recognize_greeting('') == False
    # with pytest.raises(AssertionError):
    #     fib(-10)
