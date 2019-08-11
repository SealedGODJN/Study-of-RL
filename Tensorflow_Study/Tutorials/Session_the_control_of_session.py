# Date:2019.8.9
# author:morvanzhou
# editor:hjn

# Topic:Session是tensorflow为了控制和输出文件的执行的语句。
# 运行session.run()可以获得你需要的运算结果，或者是你所要运算的部分。

import tensorflow as tf

# create two matrixes
matrix1 = tf.constant([[3,3]])
matrix2 = tf.constant([[2],[2]])
product = tf.matmul(matrix1,matrix2)

# method 1
sess = tf.Session()
result = sess.run(product)
print(result)
sess.close()
#[[12]]

# method 2
with tf.Session() as sess:
    result2 = sess.run(product)
    print(result2)
#[[12]]