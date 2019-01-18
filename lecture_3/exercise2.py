import tensorflow as tf

data = utils.read_birth_life_data(DATA_FILE)
X = tf.placeholder(tf.float32, name='X')
Y = tf.placeholder(tf.float32, name='Y')

with tf.Session() as sess:
	# Step 8: train the model
	for i in range(100): # run 100 epochs
		for x, y in data:
			# Session runs train_op to minimize loss
			sess.run(optimizer, feed_dict={X: x, Y:y}) 