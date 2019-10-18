#!/usr/bin/env bash

set -e
set -x

mypy responder_base_classes --disallow-untyped-defs
black responder_base_classes tests --check
isort --multi-line=3 --trailing-comma --force-grid-wrap=0 --combine-as --line-width 88 --recursive --check-only --thirdparty responder_base_classes responder_base_classes tests