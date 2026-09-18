# Jenkins Docker CI/CD Project

A simple Python calculator app, built into a Docker image by a Jenkins pipeline and pushed to DockerHub whenever code is committed to GitHub.

Push to GitHub → Jenkins auto-builds a Docker image → pushes it to DockerHub.

.
├── Jenkinsfile
├── Dockerfile
├── mohammadmusaab.py
└── README.md


## Setup

**VM:** Azure VM via Terraform (Pluralsight sandbox — check allowed regions/SKUs).

**Jenkins:** install OpenJDK + Jenkins, runs as systemd service on `8080`.
```bash
sudo systemctl status jenkins
```

**Docker permissions:** add `jenkins` user to `docker` group, or pipeline gets permission denied on `/var/run/docker.sock`.
```bash
sudo usermod -aG docker jenkins
sudo systemctl restart jenkins
sudo usermod -aG docker azureuser   # if using azure vm, give permission to run docker commands
newgrp docker
groups   # confirm
```

**Networking:** open inbound port `8080` on the Azure NSG.

## GitHub webhook

- Add webhook
- Payload URL: `http://<vm-public-ip>:8080/github-webhook/`
- Content type: `application/json`
- Trigger: `push` events
- If the VM's public IP changes, update the URL

## Jenkins job

| Setting | Value |
|---|---|
| Type | Pipeline |
| Definition | Pipeline script from SCM |
| SCM / Branch | Git / `main` |
| Build Trigger | ✅ GitHub hook trigger for GITScm polling |

DockerHub credential `dockerhub-creds`: username + access token.

## Pipeline stages

**`<Name> - Build Docker Image`**
```bash
docker build -t image:build-${BUILD_NUMBER} -t image:latest .
```
`${BUILD_NUMBER}` = unique permanent tag per build; `latest` = moving pointer.

**`<Name> - Login to Dockerhub`**
```bash
echo $DOCKERHUB_TOKEN | docker login -u $DOCKERHUB_USER --password-stdin
```
Credentials pulled via `withCredentials`; token piped via stdin, never in plain text.

**`<Name> - Push image to Dockerhub`**
```bash
docker push image:build-${BUILD_NUMBER}
docker push image:latest
```
Numbered tags are never overwritten → enables rollback.

## Trigger a build

Commit + push to `main` → Jenkins auto-runs → check DockerHub for `build-N` + updated `latest`.
