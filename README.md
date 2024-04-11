# Dockerized nanoGPT experiment

This takes [nanoGPT](https://github.com/karpathy/nanoGPT) and tries to run both training and running a model in Docker.

# Requirements

- docker
- docker-compose

# Installation

Run
```bash
docker-compose build
```

To train it run:
```bash
docker-compose run nanoGPT python train.py
```
By default it uses shakespear-char dataset taken from
`data/input/input.txt` and processed into:

- `meta.pkl` - metadata for the dataset
- `train.bin` & `val.bin` - dataset itself

Feel free to provide your own `input.txt` and run `python prepare.py` in the input directory to tokenize it.

After the training is done if all goes well you should just run:

```bash
docker-compose run nanoGPT python run.py
```
and see an example output from a working model.





