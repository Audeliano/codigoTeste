## Testando constantes, placeholder e tensorboard

# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np
import tensorflow as tf

#tf.placeholder funciona como um input.
#isso quer dizer que essas variaveis virao de fora
a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)

soma = tf.add(a, b)

# Toda vez que quisermos execultar o metono run
# Isso nos permite compilar e execultar o codigo solicitado.
sess = tf.Session()

a2 = tf.constant(2.0)
a3 = 4.0
print(sess.run(soma,feed_dict={a:1,b:2}))
print(a2, a3)

#TensorFlow provides a utility called TensorBoard. 
#One of TensorBoard's many capabilities is 
#visualizing a computation graph. 
#You can easily do this with a few simple commands.

#First you save the computation graph to a TensorBoard 
#summary file as follows:

writer = tf.summary.FileWriter('.')
writer.add_graph(tf.get_default_graph())

#Now, in a new terminal, launch TensorBoard with the 
#following shell command:

#tensorboard --logdir .

#Then open TensorBoard's graphs page in your browser, 
#and you should see a graph

#http://localhost:6006/#graphs




