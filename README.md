# ML App Template

Simple application for testing productization/deployment of ML apps. 

### Building & Running

```
docker build --no-cache -t ml_app_template .
docker run --rm -p 8000:8000 ml_app_template
```

### Sending Requests

When docker container is running, endpoint should be available on http://0.0.0.0:8000/predict and JSON payload with features can be sent via POST. Here is an example payload with 13 features (see [dataset description](https://scikit-learn.org/stable/datasets/toy_dataset.html#boston-dataset)):

```
{
    "crim": 6.71772,
    "zn": 0.0,
    "indus": 18.1,
    "chas": 0.0,
    "nox": 0.713,
    "rm": 6.749,
    "age": 92.6,
    "dis": 2.323,
    "rad": 24.0,
    "tax": 666.0,
    "ptratio": 20.2,
    "b": 0.32,
    "lstat": 17.44
}
```