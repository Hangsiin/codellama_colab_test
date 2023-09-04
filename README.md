# Simple Version of testing code llama inference in colab environment.

the only difference between original repo (https://github.com/facebookresearch/codellama) is
modifying example_completion.py -> example_completion_colab.py

Because torchrun doens't work well in basic colab environment,
I used torch.distributed.launch instead of torchrun.

