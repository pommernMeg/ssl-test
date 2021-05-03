#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""helper.py: Script with helpfully functions."""

__author__      = "Marcel Eggert"
__copyright__   = "Copyright 2021, Heinlein-Support"
__version__ = "0.0.1"

def git_pull_change(path):
    import git
    
    repo = git.Repo(path)
    current = repo.head.commit

    repo.remotes.origin.pull()

    if current == repo.head.commit:
        print("Repo not changed. Sleep mode activated.")
        return False
    else:
        print("Repo changed! Activated.")
        return True