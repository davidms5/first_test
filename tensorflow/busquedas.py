from ast import Constant
from numpy import dtype
import tensorflow as tf
import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"
"esto es para acortar la de texto que sale"

x = tf.constant(2.5, shape=(2,1), dtype=tf.float32)
print(x)

y = tf.constant(-254, shape=(3,4), dtype="int32")
print(y)

test = tf.compat.v1.Session()
test.run(tf.compat.v1.global_variables_initializer())
print(test.run(y))