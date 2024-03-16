# Git Hooks

This repository contains a collection of Git hooks that I use in my projects.
Most of the hooks are optimized for use with a development container.

There exists a bunch of great tools to make githooks easier such as [husky](https://typicode.github.io/husky/) and [pre-commit](https://pre-commit.com/).
However, I prefer to implement the hooks directly using bash or python and mounting them using `cp -r hooks/* .git/hooks/` as a devcontainer creation script.

## Hooks

- `pre-commit` - Run all pre-commit hooks
- `black` - Lint stage python files with [black](https://pypi.org/project/black/)
- `gitleaks` - Scan for secrets with [gitleaks](https://github.com/gitleaks/gitleaks)

