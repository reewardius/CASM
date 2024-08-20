# CASM

CASM (code assessment) automate the process of checking code security and quality, ensuring early detection and remediation of vulnerabilities and misconfigurations.

To ensure the security and quality of the code in the repository (RASM), the following tools are used:

- **Trivy**: Performs vulnerability scanning of container images, file systems, and source code for known vulnerabilities in dependencies and configurations. Trivy helps identify and fix potential vulnerabilities before they can be exploited by attackers.

- **Checkov**: Analyzes infrastructure as code (IaC) and checks it for misconfigurations that could lead to security vulnerabilities. Checkov scans IaC files such as Terraform, CloudFormation, Dockerfile and Kubernetes, identifying risks and helping to correct configurations before they are applied.

- **TruffleHog**: Searches for secrets (such as passwords, API tokens, access keys) in source code and commit history. TruffleHog helps prevent the leakage of sensitive data that might be accidentally committed to the repository, protecting against potential compromises.

- **Semgrep**: Conducts static code analysis, checking for security issues, vulnerabilities, and adherence to coding best practices. Semgrep scans source code using rules tailored to various programming languages and frameworks, helping developers detect and fix issues early in the development process.

- **Detect-Secrets**: An aptly named module for detecting secrets within a code base.

# Scan repository with code
```
docker run --rm -v $(pwd)/<path-to-code>:/workspace -v $(pwd)/output:/output byrains/casm:1.0.0
```
