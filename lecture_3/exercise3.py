import tensorflow as tf

dataset = tf.data.Dataset.from_tensor_slices((data[:,0], data[:,1]))
iterator = dataset.make_one_shot_iterator()
X, Y = iterator.get_next()         # X is the birth rate, Y is the life expectancy
with tf.Session() as sess:
	print(sess.run([X, Y]))		# >> [1.822, 74.82825]
	print(sess.run([X, Y]))		# >> [3.869, 70.81949]
	print(sess.run([X, Y]))		# >> [3.911, 72.15066]