import tensorflow as tf

x = tf.Variable(10, name='x')
y = tf.Variable(20, name='y')
z = tf.add(x, y) 		# create the node before executing the graph

writer = tf.summary.FileWriter('./graphs/normal_loading', tf.get_default_graph())
with tf.Session() as sess:
	sess.run(tf.global_variables_initializer())
	for _ in range(10):
		sess.run(z)
writer.close()

#normal_loading

# summary operations以记录信息
# tf.summary.scalar记录标量
# tf.summary.histogram记录数据的直方图
# tf.summary.distribution记录数据的分布图
# tf.summary.image记录图像数据