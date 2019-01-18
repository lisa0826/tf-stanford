import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
#用于隐藏这个提示”Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2 FMA“

import tensorflow as tf

a = tf.constant(2)
b = tf.constant(3)
x = tf.add(a, b)
with tf.Session() as sess:
	print(sess.run(x))