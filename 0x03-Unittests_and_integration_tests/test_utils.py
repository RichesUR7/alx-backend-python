#!/usr/bin/env python3
"""
A Module for testing the utils module.

This module contains tests for the following functions:
- access_nested_map
- get_json
- memoize
"""

import unittest
from typing import Dict, Tuple, Type, Union
from unittest.mock import Mock, patch

from parameterized import parameterized

from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """Tests the 'access_nested_map' function."""

    @parameterized.expand(
        [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2),
        ]
    )
    def test_access_nested_map(
        self,
        nested_map: Dict[str, Union[Dict, int]],
        path: Tuple[str, ...],
        expected: Union[Dict[str, int], int],
    ) -> None:
        """Test 'access_nested_map' output."""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand(
        [
            ({}, ("a",), KeyError),
            ({"a": 1}, ("a", "b"), KeyError),
        ]
    )
    def test_access_nested_map_exception(
        self,
        nested_map: Dict[str, Union[Dict, int]],
        path: Tuple[str, ...],
        exception: Type[BaseException],
    ) -> None:
        """Tests 'access_nested_map' exception raising."""
        with self.assertRaises(exception):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Test class for 'get_json' function."""

    @parameterized.expand(
        [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False}),
        ]
    )
    def test_get_json(self, test_url: str,
                      test_payload: Dict[str, bool]) -> None:
        """Tests 'get_json' output."""
        mock_json_method = Mock(return_value=test_payload)
        with patch("requests.get",
                   return_value=Mock(json=mock_json_method)) as get_req:
            self.assertEqual(get_json(test_url), test_payload)
            get_req.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """Test class for the 'memoize' decorator."""

    def test_memoize(self) -> None:
        """Tests the 'memoize' caches the output of a method."""

        class TestClass:
            """A test class with a method and a memoized property."""

            def a_method(self) -> int:
                """A method that returns a constant value."""
                return 42

            @memoize
            def a_property(self) -> int:
                """
                A property that returns the result of 'a_method',
                memoized.
                """
                return self.a_method()

        # Mock 'a_method' to ensure it only called once
        with patch.object(TestClass, "a_method",
                          return_value=42) as mocked_method:
            test_class = TestClass()
            self.assertEqual(test_class.a_property, 42)
            self.assertEqual(test_class.a_property, 42)
            mocked_method.assert_called_once()
