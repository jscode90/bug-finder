#!/usr/bin/env bash
ARGS_COMPILE="--no-emit-index-url"

for file in base test dev mypy;
    do
        pip-compile $ARGS_COMPILE requirements/${file}.in
    done
pip-sync requirements/base.txt requirements/test.txt requirements/dev.txt requirements/mypy.txt
