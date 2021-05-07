#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""helptools.py: Script with helpfully functions."""

__author__ = "Marcel Eggert"
__copyright__ = "Copyright 2021"
__version__ = "0.0.1"


def git_pull_change(path):
    import git

    repo = git.Repo(path)
    current = repo.head.commit

    repo.remotes.origin.pull()

    if current == repo.head.commit:
        news = "Repo not changed."
        return False, news
    else:
        news = "Repo changed!"
        return True, news


def loadConfig():
    import os
    import yaml

    script_dir = os.path.dirname(__file__)
    path = os.path.join(script_dir, ".config.yaml")
    with open(path, 'r') as f:
        cfg = yaml.safe_load(f.read())

    return cfg


def separatorLine():
    print(f"##########################################################################################################")
