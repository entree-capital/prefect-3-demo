from prefect import flow


my_flow = flow.from_source(
    source="https://github.com/entree-capital/prefect-3-demo.git",
    entrypoint="flows/demo.py:snoop_dogg",
)


if __name__ == "__main__":
    my_flow()
