# Date:2019.8.9
# author:morvanzhou
# editor:hjn

# Topic:To illustrate how tensorflow use code 
# to execute the struction constructed by us.

# 1、创建数据

import tensorflow as tf
import numpy as np

# create data
x_data = np.random.rand(100).astype(np.float32)
y_data = x_data*0.1 + 0.3

# 2、搭建模型

Weights = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
biases = tf.Variable(tf.zeros([1]))

y = Weights*x_data + biases

# 3、计算误差

loss = tf.reduce_mean(tf.square(y-y_data))

# 4、传播误差

optimizer = tf.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(loss)

# 5、训练

# init = tf.initialize_all_variables # tf马上要废弃这种写法
init = tf.global_variables_initializer() # 替换成这样

sess = tf.Session() # 创建会话
sess.run(init) # Very important

for step in range(201):
    sess.run(train)
    if step % 20 == 0:
        print(step, sess.run(Weights), sess.run(biases))