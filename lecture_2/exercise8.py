# -*- coding: utf-8 -*
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
# W = tf.Variable(tf.truncated_normal([700, 10]))
# with tf.Session() as sess:
# 	sess.run(W.initializer)
# 	print(W.eval())	


W = tf.Variable(10)
W.assign(100)
with tf.Session() as sess:
	sess.run(W.initializer)
	print(W.eval()) 

W = tf.Variable(10)
assign_op = W.assign(100)
with tf.Session() as sess:
	sess.run(W.initializer)
	sess.run(assign_op)
	print(W.eval())


my_var = tf.Variable(10)
sess1 = tf.Session()
sess2 = tf.Session()

sess1.run(W.initializer)
sess2.run(W.initializer)

with tf.Session() as sess:
	sess.run(my_var.initializer)
		
	# increment by 10 
	print(sess.run(my_var.assign_add(10))) # >> 20
	# decrement by 2 
	print(sess.run(my_var.assign_sub(2))) # >> 18

	print(sess1.run(W.assign_add(100))) 		# >> 120
	print(sess2.run(W.assign_sub(50))) 		# >> -42

	sess1.close()
	sess2.close()



