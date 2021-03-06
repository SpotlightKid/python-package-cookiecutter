#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Unit-tests for {{ cookiecutter.package_name }}.api module."""

import pytest  # noqa

from {{ cookiecutter.package_name }} import api


class TestApi(object):

    @classmethod
    def setup_class(cls):
        pass

    def test_api(self):
        """add(1,2) correctly sums 1 and 2."""
        assert api.add(1, 2) == 3

    @classmethod
    def teardown_class(cls):
        pass
