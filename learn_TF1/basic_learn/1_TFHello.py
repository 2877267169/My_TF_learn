import tensorflow as tf

# ################运行模型##################
a = tf.constant([1.0, 2.0], name='a')
b = tf.constant([3.0, 4.0], name='b')

result = a + b

# #########################################
sess = tf.Session()
print(sess.run(result))
sess.close()

"""
2020年8月10日 16:39:45 结果：
[4. 6.]
"""