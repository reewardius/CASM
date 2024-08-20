FROM python:3.8-slim

RUN apt-get update && apt-get install -y \
    curl \
	git \
	unzip \
    && rm -rf /var/lib/apt/lists/*

# Устанавливаем Trivy
RUN curl -sfL https://raw.githubusercontent.com/aquasecurity/trivy/main/contrib/install.sh | sh -s -- -b /usr/local/bin

# Устанавливаем Checkov
RUN curl -L https://github.com/bridgecrewio/checkov/releases/download/3.2.213/checkov_linux_X86_64.zip -o checkov.zip
RUN unzip checkov.zip && cd dist/ && cp checkov /usr/local/bin

# Устанавливаем Semgrep
RUN pip install --no-cache-dir semgrep

# Устанавливаем TruffleHog
RUN curl -sSfL https://raw.githubusercontent.com/trufflesecurity/trufflehog/main/scripts/install.sh | sh -s -- -b /usr/local/bin

# Устанавливаем detect-secrets
RUN pip install --no-cache-dir detect-secrets

WORKDIR /workspace

COPY run_scanners.sh /usr/local/bin/run_scanners.sh

RUN chmod +x /usr/local/bin/run_scanners.sh

CMD ["/usr/local/bin/run_scanners.sh"]