from typing import NamedTuple

from github import Github
import pytest
from pytest_mock import MockerFixture

from plugins.github_plugin.pull_request import PullRequest
from plugins.github_plugin.service import GithubSVC


class PullRequestRespMock(NamedTuple):
    number: int
    title: str
    url: str


class TestGithubSVC:
    __repo = 'owner/repo'

    def test_list_pulls_with_invalid_page(self) -> None:
        with pytest.raises(ValueError, match='page must be greater than or equal to 0'):
            GithubSVC(Github()).list_pulls(self.__repo, page=-1)

    def test_list_pulls_with_invalid_sort(self) -> None:
        with pytest.raises(
                ValueError,
                match="sort must be either created, updated, popularity or long-running"
        ):
            GithubSVC(Github()).list_pulls(self.__repo, sort='random')

    def test_list_all_pulls(self, mocker: MockerFixture) -> None:
        client = mocker.MagicMock()
        client.get_repo.return_value.get_pulls.return_value = [
            PullRequestRespMock(1, 'pr_1', 'url_1')
        ]

        assert GithubSVC(client).list_pulls(self.__repo) == [PullRequest(1, 'pr_1', 'url_1')]
        client.get_repo.assert_called_once_with(self.__repo)
        client.get_repo.return_value.get_pulls.assert_called_once_with(sort='created')

    def test_list_pulls_by_given_page(self, mocker: MockerFixture) -> None:
        sort, page = 'updated', 0
        client = mocker.MagicMock()
        client.get_repo.return_value.get_pulls.return_value.get_page.return_value = [
            PullRequestRespMock(1, 'pr_1', 'url_1')
        ]

        assert GithubSVC(client).list_pulls(self.__repo, page=page, sort=sort) == [
            PullRequest(1, 'pr_1', 'url_1')
        ]
        client.get_repo.assert_called_once_with(self.__repo)
        client.get_repo.return_value.get_pulls.assert_called_once_with(sort=sort)
        client.get_repo.return_value.get_pulls.return_value.get_page.assert_called_once_with(page=page)
