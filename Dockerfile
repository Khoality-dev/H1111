FROM pytorch/pytorch:2.7.1-cuda12.8-cudnn9-runtime

RUN apt-get update && apt-get install -y git \
    ffmpeg libsm6 libxext6 \
    build-essential

ADD . /workspace/
WORKDIR /workspace

RUN pip install -r requirementsTorch27.txt --no-cache-dir

CMD ["python", "h1111.py"]