#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import time


def factrial(x):
  y = 1
  for i in range(x):
    y *= i+1

  return y


if __name__ == '__main__':
  a = int(input("xを入力してください（x!を求める）:"))
  start = time.time()  # start time
  print ("{0}!={1}".format(a,factrial(a)))
  elapsed_time = time.time() - start  # end time
  print ("elapsed_time: {0}[sec]".format(elapsed_time))