from typing import NamedTuple


class PullRequest(NamedTuple):
    number: int
    title: str
    url: str
