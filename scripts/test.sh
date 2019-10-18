#!/usr/bin/env bash

set -e
set -x

pytest --cov=responder_base_classes --cov=tests --cov-report=term-missing ${@}
bash ./scripts/lint.sh