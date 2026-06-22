#!/usr/bin/env bash
set -ex
REPORT_PATH="${REPORT_PATH:-./}"
pytest --junit-xml="$REPORT_PATH/pytest.xml" \
    --cov=talon --cov-report=xml:"$REPORT_PATH/coverage.xml" \
    tests
