from collections.abc import Iterable
from typing import Optional

from github import Github
from github.PullRequest import PullRequest as GitHubPR

from .pull_request import PullRequest


class GithubSVC:
    """GitHub service"""

    def __init__(self, client: Github):
        self.__client: Github = client

    def list_pulls(
            self,
            repo: str,
            page: Optional[int] = None,
            sort: str = 'created',
    ) -> list[PullRequest]:
        """list pull requests in given repository"""
        
        if page is not None and page < 0:
            raise ValueError('page must be greater than or equal to 0')

        sort_opts = ['created', 'updated', 'popularity', 'long-running']
        if sort not in sort_opts:
            raise ValueError(
                'sort must be either {} or {}'.format(
                    ', '.join(sort_opts[:len(sort_opts) - 1]),
                    sort_opts[-1]
                )
            )

        res = self.__client.get_repo(repo).get_pulls(sort=sort)

        prs: Iterable[GitHubPR] = res
        if page is not None:
            prs = res.get_page(page=page)

        return [
            PullRequest(number=p.number, title=p.title, url=p.url)
            for p in prs
        ]
