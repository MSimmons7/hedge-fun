# Hedge-Fun
A playground for algorithmic trading.

## What is Alpaca?
Alpaca is a commission free trading platform similar to Robinhood but has an API to allow for the development of algorithmic trading and a variety of app integrations. It provides both live trading accounts and paper trading accounts to test out trading strategies.
More information can be found [here](https://alpaca.markets/). In order to use this files in this repo, you must create an account and generate a set of API keys.

## This Repo
This repository currently has folders for different types of algorithms. Currently there are two. Long-short takes positions in the S&P 100 based on market movements. SP-Dips looks for market dips in all of the companies in the S&P 500 in order to take long positions based on the theory that S&P 500 stocks will always trend towards long term growth. Both of these algorithms are examples provided by Alpaca for testing purposes, with the modification of the stock space on Long-short being the S&P 100. **NOTE: if you plan on running these on a live trading account, be sure to keep the FINRA pattern day trader rules in mind. A pattern day trader is someone who executes four or more day trades in a five business day period. In order to day trade, an account minimum of $25,000 must be maintained.**

## Docker
Both programs can be built and run from the Dockerfiles using the following commands, executed in the root of both folders:

`docker build -td <image_name> .`

`docker run -e KEY_ID=<alpaca_key_id> -e SECRET_ID=<alpaca_secret_key> -td <algo_image_name>`

Additionally, they can be pulled from my Docker Hub [here](https://hub.docker.com/repository/docker/msimmons719/hedge-fun).

## Kubernetes
Due to the importance of up-time, k8s is a good choice for running trading algorithms. Both have been provided as Docker images for this purpose. Attached is a ReplicaSet YAML for each algorithm to spin up a single pod of either of the algorithms.

## Future Work
In the future, I would like to improve these algorithms because currently they are operating at a loss. I also would like to add an HFT (High Frequency Trading) algorithm to take advantage of small market shifts. 
