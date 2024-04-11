"""
Poor Man's Configurator. Probably a terrible idea. Example usage:
$ python train.py config/override_file.py --batch_size=32
this will first run config/override_file.py, then override batch_size to 32

The code in this file will be run as follows from e.g. train.py:
>>> exec(open('configurator.py').read())

So it's not a Python module, it's just shuttling this code away from train.py
The code in this script then overrides the globals()

I know people are not going to love this, I just really dislike configuration
complexity and having to prepend config. to every single variable. If someone
comes up with a better simple Python solution I am all ears.
"""

import sys
from ast import literal_eval

# Base configuration
# Good for debugging and playing on macbooks and such

out_dir = 'data/model'
eval_interval = 250 # keep frequent because we'll overfit
eval_iters = 20
log_interval = 5 # don't print too often

# we expect to overfit on this small dataset, so only save when val improves
always_save_checkpoint = False

wandb_log = False # override via command line if you like
wandb_project = 'input'
wandb_run_name = 'mini-gpt'

dataset = 'input'
gradient_accumulation_steps = 1
batch_size = 12
block_size = 64 # context of up to 256 previous characters

# baby GPT model :)
n_layer = 4
n_head = 4
n_embd = 128
dropout = 0.0

learning_rate = 1e-3 # with baby networks can afford to go a bit higher
max_iters = 2000
lr_decay_iters = 2000 # make equal to max_iters usually
min_lr = 1e-4 # learning_rate / 10 usually
beta2 = 0.99 # make a bit bigger because number of tokens per iter is small

warmup_iters = 100 # not super necessary potentially

for arg in sys.argv[1:]:
    assert arg.startswith('--')
    key, val = arg.split('=')
    key = key[2:]
    if key in globals():
        try:
            # attempt to eval it it (e.g. if bool, number, or etc)
            attempt = literal_eval(val)
        except (SyntaxError, ValueError):
            # if that goes wrong, just use the string
            attempt = val
        # ensure the types match ok
        assert type(attempt) == type(globals()[key])
        # cross fingers
        print(f"Overriding: {key} = {attempt}")
        globals()[key] = attempt
    else:
        raise ValueError(f"Unknown config key: {key}")
