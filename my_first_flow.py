import prefect
from prefect import task, flow, get_run_logger

# Define a simple task
@task
def say_hello(name):
    logger = get_run_logger()
    logger.info(f"Hello, {name}!")

# Another simple task
@task
def add(x, y):
    return x + y

# Define the flow
@flow(name="my-first-flow")
def my_first_flow():
    # Set up tasks and dependencies
    greeting = say_hello("World")
    result = add(1, 2)

# Run the flow
if __name__ == "__main__":
    my_first_flow()
