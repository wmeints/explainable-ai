# Explainable AI Demo

This repository contains the code for the explainable AI talk that I've 
presented in a number of places. Feel free to explore the code and use it in 
your own projects.

## System requirements

You'll need the following tools on your system to use the code:

* [Python 3.8][PYTHON]
* [Poetry][POETRY]

## Getting started

Please use the following commands to prepare the repository for use:

* `git clone https://github.com/wmeints/explainable-ai`
* `cd explainable-ai`
* `poetry install`
* `poetry shell`

By executing these commands you're cloning the code to your harddrive,
installing the dependencies and activating a shell for the project.

After you've completed these steps you can open the code in Visual Studio Code
by executing the following command in the shell you just opened:

```shell
code .
```

## Contents of the demo

The notebooks in this repository explain how to use explainers in various ways to
better understand the behavior of a machine-learning model.

The demo code is based on the [UCI credit card defaulters dataset][DATASET]. For
the purposes of this demo, I've created a random forest classifier that predicts
whether a customer is going to default on their credit card.

The dataset contains some demographic information about customers and their
payment history. The following groups of columns are available in the dataset in
regards to payment history of customers:

* payment history: Did the customer pay on time? (-1: On time, > 0 how many months over due.)
* payment amount: How much did the customer pay for their credit card? (amount in taiwanese dollars)
* billing history: How much was billed to the customer? (amount in taiwanese dollars)

Please check [the official description of the dataset][DATASET] to get a full
description of what is in the dataset.

You're free to navigate the demo code in any way you like. But I recommend you
read the notebooks in this order:

1. [Uncover model structure](./notebooks/uncover-model-structure.ipynb)
2. [Debug model predictions](./notebooks/debug-model-predictions.ipynb)

## Comments or improvements

Feel free to post any comments and/or improvements in the issues section or
create a pull request.

[POETRY]: https://python-poetry.org/
[PYTHON]: https://www.python.org/
[DATASET]: https://archive.ics.uci.edu/ml/datasets/default+of+credit+card+clients