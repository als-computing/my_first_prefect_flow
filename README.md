
# My First Prefect Flow

Welcome to the "My First Prefect Flow" tutorial! This guide will help you design your first Prefect flow using Python. Prefect is a modern workflow orchestration framework that makes it easy to build, run, and monitor data pipelines.

## Table of Contents

1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Setting Up Your First Flow](#setting-up-your-first-flow)
4. [Visualizing Your Flow](#visualizing-your-flow)
5. [Running Your Flow](#running-your-flow)
6. [Conclusion](#conclusion)

## Introduction

Prefect allows you to define workflows as code, making it simple to manage and automate complex data workflows. In this tutorial, we will create a simple flow that processes some data and logs the results. For more information on Prefect Flows, check out the documentation: 

> https://docs.prefect.io/latest/concepts/flows/

## Installation

To get started, you'll need to install Prefect. You can do this using `pip`:

First, check if prefect is already installed:

```bash
pip show prefect
```
If it is not installed, use `pip install`:
```bash
pip install prefect
```

## Setting Up Your First Flow

Let's create a basic Prefect flow. We'll start by importing the necessary modules and defining a couple of simple tasks.

```
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
```

As you can see, we have added a few decorators to our Python functions, `@task` and one `@flow`. A Prefect Task can be thought of as a singular unit of work, whereas the Flow can manage the execution order of multiple tasks into a coherent workflow.

You might also notice that we imported `get_run_logger` from Prefect. This allows us to capture information about our workflow for monitoring and troubleshooting, similar to `print()` but with nicer formatting and more details. To add a log, you can this pattern: `logger.info(f'Flow action started with id: {flow_run_id}')`. Notice you can also include variables for more meaningful messages.

## Visualizing Your Flow

Prefect comes with a visualization tool that helps you see the structure and status of your flow. You can use the Prefect UI to monitor your flow in real time.

To start the Prefect server locally, run this in your terminal:

    prefect server start

Then, either click the link that appears in your terminal or open your web browser and go to `http://localhost:8080` (make sure the port number is correct). Once you run the next step, you will be able to see your flow and its execution history.

## Running Your Flow

To run your flow, you'll use the Prefect CLI. Make sure your flow is saved in a file, such as `my_first_flow.py`. In your terminal, run this command:

    python my_first_flow.py

You should see an output indicating that your flow has been successfully run and tasks have been executed.

## Conclusion

Congratulations! You've created and run your first Prefect flow. This tutorial covered the basics of defining and running a Prefect flow. From here, you can explore more advanced features of Prefect, such as scheduling, retries, and parameterization.

For more information, visit the Prefect documentation:

https://docs.prefect.io/latest/
