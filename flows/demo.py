from prefect import flow, task


@task(log_prints=True)
def say_hello(name: str):
    print(f"Hello, {name}!")


@flow
def hello_universe(names: list[str]):
    for name in names:
        say_hello(name)


@flow
def snoop_dogg():
    print("Whadap yo , shout out to my boy Shimi always first in da house 🚬")


if __name__ == "__main__":
    # create your first deployment to automate your flow
    hello_universe.serve(name="your-first-deployment")
