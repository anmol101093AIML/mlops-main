import tensorflow as tf
import tensorflow_datasets as tfds
mnist=tfds.load('fashion_mnist',split='train',as_supervised=True)
print(type(mnist))

# mnist_train = tfds.load(name="fashion_mnist", split="train")
# if isinstance(mnist_train, tf.data.Dataset)==True:
#     print(type(mnist_train))
#
for item in mnist.take(1):
 print(type(item))
 print(item)