# Simple Version of testing code llama inference in colab environment.

the only difference between original repo (https://github.com/facebookresearch/codellama) is
modifying example_completion.py -> example_completion_colab.py

Because torchrun doens't work well in basic colab environment,
I used torch.distributed.launch instead of torchrun.

https://colab.research.google.com/drive/1X0AcfX0m2o2kaN9x8_DtiEUoa9f23w_D?usp=sharing

this is my implementation on colab notebook. 
(instruction is written in Korean. But almost same as original repo.)
