#!/bin/bash

CODE_DIR="/workspace"

OUTPUT_BASE_DIR="/output"

RESULTS_DIR="${OUTPUT_BASE_DIR}/$CODE_DIR_results"

mkdir -p $RESULTS_DIR

# Запускаем Trivy
echo "Running Trivy..."
trivy plugin install github.com/fatihtokus/scan2html
trivy scan2html fs --vuln-type library --scanners vuln,misconfig $CODE_DIR $RESULTS_DIR/trivy.html

# Запускаем Checkov
echo "Running Checkov..."
checkov -d $CODE_DIR > $RESULTS_DIR/checkov.results

# Запускаем TruffleHog
echo "Running TruffleHog..."
trufflehog filesystem $CODE_DIR --only-verified > $RESULTS_DIR/trufflehog.results

# Запускаем Semgrep
echo "Running Semgrep..."
semgrep scan $CODE_DIR --config auto --text > $RESULTS_DIR/semgrep.results
