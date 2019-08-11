# Date:2019.8.10
# author:morvanzhou
# editor:hjn

# Topic:How to use variable in tensorflow

import tensorflow as tf

state = tf.Variable(0,name='counter')

# 定义常量one
one = tf.constant(1)

# 定义加法步骤（注：此步并没有直接计算）
new_value = tf.add(state,one)

# 将State更新成new_value
update = tf.assign(state, new_value)

# 如果定义Variable，就一定要initialize
# init = tf.initialize_all_variables() # tf马上就要废弃这种写法
init = tf.global_variables_initializer() # 替换成这样

# 使用Session
with tf.Session() as sess:
    sess.run(init)
    for _ in range(3):
        sess.run(update)
        print(sess.run(state))