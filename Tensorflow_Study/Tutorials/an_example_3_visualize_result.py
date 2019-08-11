# Date:2019.8.9
# author:morvanzhou
# editor:hjn

# Topic:Create a network

import tensorflow as tf
import numpy as np

import matplotlib.pyplot as plt

# 1、构造添加一个神经层的函数

def add_layer(inputs, in_size, out_size, activation_function=None):
    Weights = tf.Variable(tf.random_normal([in_size,out_size]))
    biases = tf.Variable(tf.zeros([1,out_size]) + 0.1)
    Wx_plus_b = tf.matmul(inputs, Weights) + biases
    if activation_function is None:
            outputs = Wx_plus_b
    else:
            outputs = activation_function(Wx_plus_b)
    return outputs

# 2、导入数据

x_data = np.linspace(-1,1,300,dtype=np.float32)[:,np.newaxis]
noise = np.random.normal(0,0.05, x_data.shape).astype(np.float32)
y_data = np.square(x_data)-0.5+noise

xs = tf.placeholder(tf.float32,[None,1])
ys = tf.placeholder(tf.float32,[None,1])

# 3、搭建网络

l1 = add_layer(xs,1,10,activation_function=tf.nn.relu) # 定义隐藏层
prediction = add_layer(l1,10,1,activation_function = None) # 定义输出层
loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys-prediction), reduction_indices = [1]))
train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)

#init = tf.initialize_all_variables() #废弃
init = tf.global_variables_initializer() # 替换成这样

sess = tf.Session()
sess.run(init)

# plot the real data
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.scatter(x_data, y_data)
# plt.ion()#本次运行请注释，全局运行不要注释
# plt.show()

# 4、训练

for i in range(1000):
    # training
    sess.run(train_step, feed_dict={xs: x_data, ys: y_data})
    if i % 50 == 0:
        # to visualize the result and improvement
        try:
            ax.lines.remove(lines[0])
            plt.show()
        except Exception:
            pass
            #print (str(e))
        
        prediction_value = sess.run(prediction, feed_dict={xs: x_data})
        # plot the prediction
        lines = ax.plot(x_data, prediction_value, 'r-', lw=5)
        plt.pause(0.1)