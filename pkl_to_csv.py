# -*- coding: utf-8 -*-
"""pkl_to_csv.ipynb

Automatically generated by Colaboratory.


"""

from google.colab import drive
drive.mount('/content/drive')

import numpy as np 
import pandas as pd

import os
for dirname, _, filenames in os.walk('/content/drive/MyDrive/df_run_2_0.pkl'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

trainf = pd.read_pickle('/content/drive/MyDrive/df_run_2_0.pkl')

trainf.head()

trainf.to_csv('X.csv', index=False)
