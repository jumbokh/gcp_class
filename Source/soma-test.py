import tensorflow as tf
valor1 = tf.constant(2)
valor2 = tf.constant(3)
type(valor1)
print(valor1)
soma=valor1+valor2
type(soma)
print(soma)
sess = tf.compat.v1.Session()
with sess:
    print(sess.run(soma))