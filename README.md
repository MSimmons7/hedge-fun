# Hedge-Fun
A playground for algorithmic trading.

## Docker
The image can be built and run from the Dockerfile using the following:

`docker build -td <image_name> .docker`

`docker run -e KEY_ID=<alpaca_key_id> -e SECRET_ID=<alpaca_secret_key> -td <algo_image_name>`