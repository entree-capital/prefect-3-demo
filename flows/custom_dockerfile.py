from prefect import flow
from prefect.docker import DockerImage


@flow(log_prints=True)
def buy():
    print("Selling securities")


if __name__ == "__main__":
    buy.deploy(
        name="my-custom-dockerfile-deployment",
        work_pool_name="my-docker-pool",
        image=DockerImage(
            name="kaminskypavel/prefect-3-demo", tag="latest", dockerfile="Dockerfile"
        ),
        push=True,
    )
