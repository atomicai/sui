# sui
![](./docs/sui.png)
> A microservice bridge between your backend and client, allowing you to configure any CORS, choose the desired port, and serve SPA files lovingly crafted by your frontend developers.

## How to Run
```bash
sudo docker buildx build --platform linux/amd64 -t sui:latest . && docker-compose up -d
```

## Configure
> We use [Quart](https://github.com/pallets/quart) together with [quart-cors](https://pypi.org/project/quart-cors/), and run everything through [hypercorn](https://hypercorn.readthedocs.io/en/latest/). The complete configuration file is specified in [hypercorn.toml](./hypercorn.toml).

:exclamation::exclamation::exclamation: Make sure to set the SUI_PORT_ALLOW_ORIGIN environment variable; otherwise, CORS issues won’t be resolved properly.