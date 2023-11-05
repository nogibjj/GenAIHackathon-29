# app/Dockerfile

FROM python:3.10-slim

WORKDIR /GenAIHackathon-29

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

COPY . .

RUN pip install -r requirements.txt && pip uninstall -y streamlit && pip install streamlit

EXPOSE 80

HEALTHCHECK CMD curl --fail http://localhost:80/_stcore/health

ENTRYPOINT ["streamlit", "run", "About.py", "--server.port=80", "--server.address=0.0.0.0", " --server.enableCORS false"]
