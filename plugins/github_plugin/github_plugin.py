import os

from errbot import BotPlugin, botcmd, arg_botcmd
from errbot.templating import tenv
from github import Github

from plugins.github_plugin.service import GithubSVC


class GithubPlugin(BotPlugin):
    """GitHub Plugin"""
    
    _svc: GithubSVC

    def activate(self):
        self._svc = GithubSVC(Github(login_or_token=os.getenv('GITHUB_TOKEN'), per_page=5))
        super(GithubPlugin, self).activate()

    @botcmd
    @arg_botcmd('repo', type=str)
    @arg_botcmd('--page', dest='page', type=int)
    @arg_botcmd('--sort', dest='sort', type=str, default='created')
    def list_pulls(self, _, repo, page, sort):
        """List pull requests"""

        return tenv().get_template('list_pulls.md').render(
            self._list_pulls(repo, page, sort)
        )

    def _list_pulls(self, repo, page=None, sort='created') -> dict:
        return {
            'repo': repo,
            'page': page,
            'pulls': self._svc.list_pulls(repo, page, sort)
        }
