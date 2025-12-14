#!/usr/bin/env python3

import encoding
import models

import absl
import matplotlib.pyplot as plt
import tensorflow as tf
from logger import Logger

absl.flags.DEFINE_boolean("train_quantum", True,
                          "Whether to train a Quantum CNN.")
absl.flags.DEFINE_boolean("train_classical", True,
                          "Whether to train a Classical CNN.")
FLAGS = absl.flags.FLAGS


def main(_):
    # Use the mnist handwritten digits dataset
    (x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
    EPOCHS = 5
    x_train = x_train[:50]
    y_train = y_train[:50]
    x_test = x_test[:50]
    y_test = y_test[:50]
    Logger.log(f"Training data shape: x_train={x_train.shape}, y_train={y_train.shape}")
    Logger.log(f"Testing data shape: x_test={x_test.shape}, y_test={y_test.shape}")
    
    
    if FLAGS.train_quantum:
        qcnn = models.QuantumCnn(x_train, y_train, x_test, y_test, epochs=EPOCHS)
        qcnn.train()
        # qcnn.save_model()
        qcnn.plot()
    if FLAGS.train_classical:
        nn = models.ClassicalNn(x_train, y_train, x_test, y_test, epochs=EPOCHS)
        nn.train()
        # nn.save_model()
        nn.plot()

    plt.show()


if __name__ == "__main__":
    absl.app.run(main)
