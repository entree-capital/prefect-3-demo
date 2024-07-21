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

- [Entree Docker Repo](https://hub.docker.com/repository/docker/entreecapital/prefect-3-demo/general)
- [Entree AWS ECR](https://us-east-2.console.aws.amazon.com/ecr/repositories/private/573574571452/prefect-flows?region=us-east-2)

### Amazon ECS/ECR

1. Create a new ECR repository
2. build and [push an image](https://docs.aws.amazon.com/AmazonECR/latest/userguide/docker-pull-ecr-image.html) to it
3. Setup [ECS worker in prefect](https://docs.prefect.io/latest/integrations/prefect-aws/ecs_guide/)
4. Deploy the flow in `prefect.yaml`

