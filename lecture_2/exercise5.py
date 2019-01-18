import tensorflow as tf

with tf.Session() as sess:
	#tf.zeros(shape, dtype=tf.float32, name=None)
	print(sess.run(tf.zeros([2, 3], tf.int32))) #==> [[0, 0, 0], [0, 0, 0]]

	#tf.zeros_like(input_tensor, dtype=None, name=None, optimize=True)
	#tf.zeros_like(input_tensor) #==> [[0, 0], [0, 0], [0, 0]]

	#tf.ones(shape, dtype=tf.float32, name=None)
	#tf.ones_like(input_tensor, dtype=None, name=None, optimize=True)

	#tf.fill(dims, value, name=None) 
	print(sess.run(tf.fill([2, 3], 8))) #==> [[8, 8, 8], [8, 8, 8]]

	#tf.lin_space(start, stop, num, name=None) 
	print(sess.run(tf.lin_space(10.0, 13.0, 4))) #==> [10. 11. 12. 13.]

	#tf.range(start, limit=None, delta=1, dtype=None, name='range')
	print(sess.run(tf.range(3, 18, 3))) #==> [3 6 9 12 15]
	print(sess.run(tf.range(5))) #==> [0 1 2 3 4]