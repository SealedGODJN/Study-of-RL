# Date:2019.8.10
# author:morvanzhou
# editor:hjn

# Topic:To introduce the placeholder in Tensorflow

import tensorflow as tf

# 在tensoflow中需要定义placeholder的type,一般为float32形式
input1 = tf.placeholder(tf.float32)
input2 = tf.placeholder(tf.float32)

# mul = multiply 是将input1和input2做乘法运算，并输出为output
output = tf.multiply(input1,input2)

with tf.Session() as sess:
    print(sess.run(output,feed_dict = {input1:[7.],input2:[2.]}))
# [14.]