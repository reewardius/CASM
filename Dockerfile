FROM python:3.7-slim

RUN apt-get update && apt-get install -y \
    curl \
    git \
    golang \
    && rm -rf /var/lib/apt/lists/*

# Устанавливаем Trivy
RUN curl -sfL https://raw.githubusercontent.com/aquasecurity/trivy/main/contrib/install.sh | sh -s -- -b /usr/local/bin

# Устанавливаем Checkov
RUN pip install --no-cache-dir checkov

# Устанавливаем Semgrep
RUN pip install --no-cache-dir semgrep

# Устанавливаем TruffleHog
RUN curl -sSfL https://raw.githubusercontent.com/trufflesecurity/trufflehog/main/scripts/install.sh | sh -s -- -b /usr/local/bin

WORKDIR /workspace

COPY run_scanners.sh /usr/local/bin/run_scanners.sh

RUN chmod +x /usr/local/bin/run_scanners.sh

CMD ["/usr/local/bin/run_scanners.sh"]
