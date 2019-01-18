import tensorflow as tf

# create a placeholder for a vector of 3 elements, type tf.float32
a = tf.placeholder(tf.float32, shape=[3])

b = tf.constant([5, 5, 5], tf.float32)

# use the placeholder as you would a constant or a variable
c = a + b  # short for tf.add(a, b)

with tf.Session() as sess:
	print(sess.run(c, feed_dict={a: [1, 2, 3]}))

with tf.Session() as sess:
	for a_value in list_of_values_for_a:
		print(sess.run(c, {a: a_value}))

