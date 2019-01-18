import tensorflow as tf

x = 2
y = 3
add_op = tf.add(x, y)
mul_op = tf.multiply(x, y)
useless = tf.multiply(x, add_op)
pow_op = tf.pow(add_op, mul_op)
with tf.Session() as sess:
	z = sess.run(pow_op)
	print(z)


#Interactive Coding       交互式编码
#Mean squared error       均方误差
#Specify loss function    指定损失函数
#Initialize variables     初始化变量
#Fetch argument           获取参数
#Huber loss               湖贝儿损失
#Placeholder              占位符
