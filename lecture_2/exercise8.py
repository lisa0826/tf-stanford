import tensorflow as tf

# s = tf.Variable(2, name="scalar") 
# m = tf.Variable([[0, 1], [2, 3]], name="matrix") 
# W = tf.Variable(tf.zeros([784,10]))

# s = tf.get_variable("scalar", initializer=tf.constant(2)) 
# m = tf.get_variable("matrix", initializer=tf.constant([[0, 1], [2, 3]]))
# W = tf.get_variable("big_matrix", shape=(784, 10), initializer=tf.zeros_initializer())

# with tf.Session() as sess:
# 	print(sess.run(W))

# W is a random 700 x 100 variable object
W = tf.Variable(tf.truncated_normal([700, 10]))
with tf.Session() as sess:
	sess.run(W.initializer)
	print(W.eval())	