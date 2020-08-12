import tensorflow as tf

a = tf.constant([1.0, 2.0], name='a')
b = tf.constant([3.0, 4.0], name='b')

result = a + b

print(a)
print(b)
print(result)

"""
Tensor("a:0", shape=(2,), dtype=float32)
Tensor("b:0", shape=(2,), dtype=float32)
Tensor("add:0", shape=(2,), dtype=float32)
"""
"""
对于任意一个张亮来说，都具备这三个属性：操作、维度和数据类型。
""""""
* 操作：它可以被看作是一个张量的名字，或者作为一个张量的唯一标识符。
操作的命名具有一定的规则，这和计算图中的节点有关。
计算图中的每一个节点都表示一个运算，
而张量则将节点运算结果的属性保存了下来。
操作的命名符合“node:src_output”的形式，
其中node就是节点的名称（如上述的add)，
src_output表示这个张量是节点的第几个输出（编号从0开始)。

"""
