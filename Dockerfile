FROM python:3.10.13-slim-bookworm

RUN apt-get update && apt-get install -y curl gnupg2 lsb-release
RUN export GCSFUSE_REPO=gcsfuse-`lsb_release -c -s` && \
    echo "deb https://packages.cloud.google.com/apt $GCSFUSE_REPO main" | tee /etc/apt/sources.list.d/gcsfuse.list && \
    curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add -
RUN apt-get update && apt-get install -y gcsfuse

WORKDIR /app
RUN mkdir -p /app/data
RUN pip install poetry
RUN poetry config virtualenvs.in-project true

COPY ./ ./
RUN poetry install

CMD ["poetry", "run", "streamlit", "run", "app.py", "--server.port", "8080"]

#ENTRYPOINT ["bash", "start.sh"]
