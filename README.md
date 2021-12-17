# GitHub ChatBot Sample

A GitHub ChatBot sample built with ErrBot.

## Features

* List Pull Requests from any given GitHub repository, supports sort and pagination (page starts from 0).

```shell
!list_pulls --sort created --page 0 CameronXie/github-chatbot
```

## Install

* Make sure you have docker engine 19.03+ installed.
* Update `.env` file with your GitHub personal access token.
* Simply run `make up` from the project root directory to spin up docker containers.
* Create or modify the ErrBot configure file (config.py) in the project root directory.
* Run `errbot` in `bot_python` container.

## Test

* Simply run `make up` from the project root directory to spin up docker containers.
* Run `make ci-test` to start the lint and unit tests.

## Contributing
Feedback is welcome.
