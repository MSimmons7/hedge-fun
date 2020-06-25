FROM python:3

ADD samplealgo/algo.py samplealgo/algo.py
ADD samplealgo/__init__.py samplealgo/__init__.py
ADD samplealgo/btest.py samplealgo/btest.py
ADD samplealgo/universe.py samplealgo/universe.py
ADD samplealgo/algo_polygon.py samplealgo/algo_polygon.py
ADD main.py main.py

RUN pip3 install alpaca-trade-api

CMD ["python3", "main.py"]
