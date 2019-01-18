import tensorflow as tf

t_0 = 19 			         			# scalars are treated like 0-d tensors
tf.zeros_like(t_0)                  			# ==> 0
tf.ones_like(t_0)                    			# ==> 1

t_1 = [b"apple", b"peach", b"grape"] 	# 1-d arrays are treated like 1-d tensors
tf.zeros_like(t_1)                   			# ==> [b'' b'' b'']
tf.ones_like(t_1)                    			# ==> TypeError: Expected string, got 1 of type 'int' instead.

t_2 = [[True, False, False],[False, False, True],[False, True, False]]         		# 2-d arrays are treated like 2-d tensors

tf.zeros_like(t_2)                   			# ==> 3x3 tensor, all elements are False
tf.ones_like(t_2)          
