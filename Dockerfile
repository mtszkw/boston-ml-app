FROM python:3.6.9-slim

WORKDIR /boston-ml-app

COPY Pipfile Pipfile.lock ./

RUN pip install pipenv && \
    apt-get update && \
    apt-get install -y --no-install-recommends gcc python3-dev libssl-dev && \
    pipenv install --deploy --system && \
    apt-get remove -y gcc python3-dev libssl-dev && \
    apt-get autoremove -y && \
    pip uninstall pipenv -y

COPY boston_inference.py xgbregressor_boston.json .

CMD ["uvicorn", "boston_inference:app", "--host", "0.0.0.0", "--port", "8000"]
