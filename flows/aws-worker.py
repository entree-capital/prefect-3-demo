from prefect import flow
from prefect.docker import DockerImage


@flow(log_prints=True)
def my_flow(name: str = "world"):
    print(f"Hello {name}! I'm a flow AWS ✨✨✨✨✨✨✨✨")


if __name__ == "__main__":
    my_flow.deploy(
        name="my-deployment1",
        work_pool_name="my-ecs-pool",
        image=DockerImage(
            name="kaminskypavel/prefect-3-demo",
            tag="latest",
            dockerfile="Dockerfile",
            platform="linux/amd64",
        ),
    )
