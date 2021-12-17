from pytest_mock import MockerFixture

pytest_plugins = ["errbot.backends.test"]

extra_plugin_dir = './plugins/github_plugin'


class TestGithubPlugin:
    def test_github_plugin(self, testbot, mocker: MockerFixture) -> None:
        repo, page, sort = 'owner/repo', 1, 'created'
        resp = {
            'repo': repo,
            'page': page,
            'pulls': [
                {
                    'number': 1,
                    'title': 'pr_title_1',
                    'url': 'pr_url_1',
                },
                {
                    'number': 2,
                    'title': 'pr_title_2',
                    'url': 'pr_url_2',
                }
            ]
        }
        testbot.inject_mocks(
            'GithubPlugin',
            {'_list_pulls': mocker.MagicMock(return_value=resp)}
        )
        testbot.push_message(f'!list_pulls {repo}')
        output = testbot.pop_message()

        assert 'Repository: owner/repo' in output
        assert 'Pull Request Page 1' in output

        output_str = output.encode('ascii', 'ignore').decode().replace(' ', '')
        assert '\n1pr_title_1pr_url_1\n' in output_str
        assert '\n2pr_title_2pr_url_2\n' in output_str
