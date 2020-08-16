import tensorflow as tf

a = tf.constant([1.0, 2.0], name='a')
b = tf.constant([3.0, 4.0], name='b')

result = a + b

print(a.graph is tf.get_default_graph())
print(b.graph is tf.get_default_graph())


"""
2020年8月10日 16:45:21
### ????理应是True
False
False

2020年8月10日 16:47:21
###原来是get_default_graph忘了加括号
True
True
"""