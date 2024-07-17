# prefect-3-demo

this project demonstrates

1. prefect-3
2. deployment of a flow in a custom Dockerfile
3. uploading an image to a private docker registry
4. deploying a flow in a AWS ECS cluster

## Setup

1.Create a virtual environment and install the dependencies

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2.you will need the following tools installed in the cli

- [docker](https://docs.docker.com/get-docker/)
- [aws-cli](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html)
- [prefect](https://docs.prefect.io/core/getting_started/installation.html)

3.run the following command to deploy

```bash
prefect deploy --prefect-file prefect.yaml
```

### Links

- [Docker Repo](https://hub.docker.com/repository/docker/entreecapital/prefect-3-demo/general)
