import tensorflow as tf

a = tf.constant([2, 2], name='a')
b = tf.constant([[0, 1], [2, 3]], name='b')
with tf.Session() as sess:
	print(sess.run(tf.div(b, a)))     
	print(sess.run(tf.divide(b, a)))     
	print(sess.run(tf.truediv(b, a)))        
	print(sess.run(tf.floordiv(b, a)))       
	print(sess.run(tf.realdiv(b, a)))         
	print(sess.run(tf.truncatediv(b, a)))     
	print(sess.run(tf.floor_div(b, a)))  