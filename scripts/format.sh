#!/bin/sh -e
set -x

autoflake --remove-all-unused-imports --recursive --remove-unused-variables --in-place responder_base_classes tests --exclude=__init__.py
black responder_base_classes tests
isort --multi-line=3 --trailing-comma --force-grid-wrap=0 --combine-as --line-width 88 --recursive --thirdparty responder_base_classes --apply responder_base_classes tests