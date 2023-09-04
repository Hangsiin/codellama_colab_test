# Simple Version of testing Meta Code Llama inference in colab environment.

The only difference between original repo (https://github.com/facebookresearch/codellama) is
modifying example_completion.py -> example_completion_colab.py

Because torchrun doens't work well in basic colab environment (in my case),
I used torch.distributed.launch instead of torchrun.

https://colab.research.google.com/drive/1X0AcfX0m2o2kaN9x8_DtiEUoa9f23w_D?usp=sharing

This is my implementation on colab notebook. 
(instructions are written in Korean. But almost same as original repo.)
