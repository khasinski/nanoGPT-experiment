FROM pytorch/pytorch:2.2.2-cuda12.1-cudnn8-devel

RUN /opt/conda/bin/python -mpip install numpy transformers datasets tiktoken wandb tqdm

WORKDIR /app
