#!/bin/bash

CODE_DIR="/workspace"

OUTPUT_BASE_DIR="/output"

RESULTS_DIR="${OUTPUT_BASE_DIR}/$CODE_DIR_results"

mkdir -p $RESULTS_DIR

# Запускаем Trivy
echo "Running Trivy..."
trivy plugin install github.com/fatihtokus/scan2html
trivy scan2html fs --cache-dir /tmp/trivy/ --vuln-type library --scanners vuln,misconfig $CODE_DIR $RESULTS_DIR/trivy.html

# Запускаем Checkov
echo "Running Checkov..."
checkov -d $CODE_DIR --output github_failed_only > $RESULTS_DIR/checkov.md

# Запускаем TruffleHog
echo "Running TruffleHog..."
trufflehog filesystem $CODE_DIR --only-verified > $RESULTS_DIR/trufflehog.txt

# Запускаем detect-secrets
echo "Running detect-secrets..."
detect-secrets scan $CODE_DIR --all-files > $RESULTS_DIR/detect-secrets.txt

# Запускаем Semgrep
echo "Running Semgrep..."
semgrep scan $CODE_DIR --config auto --json > $RESULTS_DIR/semgrep.json

curl https://raw.githubusercontent.com/reewardius/RASM/main/semgrep_friendly.py -o semgrep_friendly.py
python semgrep_friendly.py -f $RESULTS_DIR/semgrep.json -o $RESULTS_DIR/semgrep_report.md
rm $RESULTS_DIR/semgrep.json