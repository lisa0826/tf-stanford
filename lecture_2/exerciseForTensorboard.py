from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
import sys
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

max_step = 1000  # 最大迭代次数
learning_rate = 0.001   # 学习率
dropout = 0.9   # dropout时随机保留神经元的比例

data_dir = os.path.join('data', 'mnist')# 样本数据存储的路径
if not os.path.exists('log'):
    os.mkdir('log')
log_dir = 'log'   # 输出日志保存的路径

