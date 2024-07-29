#!/usr/bin/env python3
"""
A module for testing the client module.

This module contains unit and integration tests for the
GithubOrgClient class.
"""


import unittest
from typing import Dict
from unittest.mock import MagicMock, Mock, PropertyMock, patch

from parameterized import parameterized, parameterized_class
from requests import HTTPError

from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """Tests the githubOrgClient class."""

    @parameterized.expand(
        [
            ("google", {"login": "google"}),
            ("abc", {"login": "abc"}),
        ]
    )
    @patch("client.get_json")
    def test_org(
        self, org: str, response: Dict[str, str], mocked_org_method: MagicMock
    ) -> None:
        """Tests the 'org' method."""
        mocked_org_method.return_value = response
        get_org_client = GithubOrgClient(org)
        self.assertEqual(get_org_client.org, response)
        mocked_org_method.assert_called_once_with(
            f"https://api.github.com/orgs/{org}")

    def test_public_repos_url(self):
        """Tests the _public_repos_url property."""
        with patch(
            "client.GithubOrgClient.org", new_callable=PropertyMock
        ) as mocked_property:
            mocked_property.return_value = {
                "repos_url": "https://api.github.com/orgs/google/repos"
            }
            self.assertEqual(
                GithubOrgClient("google")._public_repos_url,
                "https://api.github.com/orgs/google/repos",
            )

    @patch("client.get_json")
    def test_public_repos(self, mocked_get_json: MagicMock):
        """Tests the public_repos method."""
        test_payload = {
            "repos_url": "https://api.github.com/orgs/google/repos",
            "repos": [
                {
                    "id": 7697149,
                    "node_id": "MDEwOlJlcG9zaXRvcnk3Njk3MTQ5",
                    "name": "episodes.dart",
                    "full_name": "google/episodes.dart",
                    "private": False,
                    "forks": 22,
                    "open_issues": 0,
                    "watchers": 12,
                    "default_branch": "master",
                    "permissions": {
                        "admin": False,
                        "push": False,
                        "pull": True
                    },
                },
                {
                    "id": 7776515,
                    "node_id": "MDEwOlJlcG9zaXRvcnk3Nzc2NTE1",
                    "name": "cpp-netlib",
                    "full_name": "google/cpp-netlib",
                    "private": False,
                    "forks": 59,
                    "open_issues": 0,
                    "watchers": 292,
                    "default_branch": "master",
                    "permissions": {
                        "admin": False,
                        "push": False,
                        "pull": True
                    },
                },
            ],
        }
        mocked_get_json.return_value = test_payload["repos"]
        with patch(
            "client.GithubOrgClient._public_repos_url",
            new_callable=PropertyMock
        ) as mocked_public_repos_url:
            mocked_public_repos_url.return_value = test_payload["repos_url"]
            self.assertEqual(
                GithubOrgClient("google").public_repos(),
                ["episodes.dart", "cpp-netlib"],
            )
            mocked_public_repos_url.assert_called_once()
        mocked_get_json.assert_called_once()

    @parameterized.expand(
        [
            ({"license": {"key": "my_license"}}, "my_license", True),
            ({"license": {"key": "other_license"}}, "my_license", False),
        ]
    )
    def test_has_license(
        self, repo: Dict[str, Dict],
        key: str, expected: bool
    ) -> None:
        """Tests for 'has_license' method."""
        mocked_org_client = GithubOrgClient("google")
        client_has_license = mocked_org_client.has_license(repo, key)
        self.assertEqual(client_has_license, expected)


@parameterized_class(
    [
        {
            "org_payload": TEST_PAYLOAD[0][0],
            "repos_payload": TEST_PAYLOAD[0][1],
            "expected_repos": TEST_PAYLOAD[0][2],
            "apache2_repos": TEST_PAYLOAD[0][3],
        },
    ]
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration tests for the GithubOrgClient class."""

    @classmethod
    def setUpClass(cls) -> None:
        """Set up the tests class with mocked HTTP get requests."""
        cls.route_payload = {
            "https://api.github.com/orgs/google": cls.org_payload,
            "https://api.github.com/orgs/google/repos": cls.repos_payload,
        }

        # Start patching 'requests.get'
        cls.get_patcher = patch("requests.get", side_effect=cls.get_payload)
        cls.get_patcher.start()

        # Single instance of GithubOrgClient
        cls.client = GithubOrgClient("google")

    @classmethod
    def get_payload(cls, url: str) -> Mock:
        """Return a mock response object for the given URL."""
        if url in cls.route_payload:
            return Mock(json=lambda: cls.route_payload[url])
        raise HTTPError

    @classmethod
    def tearDownClass(cls) -> None:
        """Clean up the test class by stopping the patcher."""
        cls.get_patcher.stop()

    def test_public_repos(self) -> None:
        """Tests the public_repos method."""
        self.assertEqual(self.client.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self) -> None:
        """Tests the public_repos method with a license."""
        self.assertEqual(
            self.client.public_repos(license="apache-2.0"),
            self.apache2_repos,
        )
