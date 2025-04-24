
Docker

docker pull ghcr.io/open-webui/open-webui:main

To run normal:
docker run -d -p 3000:8080 -v open-webui:/app/backend/data --name open-webui ghcr.io/open-webui/open-webui:main

to run with Nividia:
docker run -d -p 3000:8080 --gpus all -v open-webui:/app/backend/data --name open-webui ghcr.io/open-webui/open-webui:cuda

pyenv 


```

    $env:DATA_DIR="C:\open-webui\data"; uvx --python 3.11 open-webui@latest serve

```