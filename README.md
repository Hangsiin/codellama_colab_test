# Simple Version of testing Code Llama inference in Google Colab environment.

The only difference between original repo (https://github.com/facebookresearch/codellama) is
modifying example_completion.py -> example_completion_colab.py

Because torchrun doens't work well in basic colab environment (in my case),
I used torch.distributed.launch instead of torchrun.

https://colab.research.google.com/drive/1X0AcfX0m2o2kaN9x8_DtiEUoa9f23w_D?usp=sharing

This is my implementation on colab notebook. 
(instructions are written in Korean. But almost same as original repo.)

Requirements
- Google colab pro plan for High system RAM.
(If you do hyperparameter tuning, you might be able to do it in the free version, but I'm not sure.)
- at least 12.5GB of free space on your Google Drive. (7b models = 12.5 GB)
- 7b models can be run with a T4 GPU (Free).
