#!/usr/bin/env python
import pandas as pd
import numpy as np

train = pd.read_csv("./train.csv")
test = pd.read_csv("./test.csv")


print(train.head())
print(test.head())

print(train.shape)
print(test.shape)

print(train.describe())
print(test.describe())
