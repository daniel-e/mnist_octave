#!/usr/bin/env python

import struct, gzip
import scipy.io
import numpy as np
import matplotlib.pyplot as plt

def load_mnist(fnimg, fnlabel):
	# read labels
	f = gzip.open(fnlabel, 'rb')
	# read magic number and number of items
	f.read(8)
	# read labels
	labels = np.frombuffer(f.read(), dtype = np.uint8)

	# read data
	f = gzip.open(fnimg, 'rb')
	# read magic number, number of images, number of rows, number of cols
	magic_nr, N, rows, cols = struct.unpack(">IIII", f.read(16))
	# read data
	images = np.frombuffer(f.read(), dtype = np.uint8).reshape((-1, rows * cols))

	return images, labels


if __name__ == "__main__":
	trainX, trainY = load_mnist("train-images-idx3-ubyte.gz", "train-labels-idx1-ubyte.gz")
	testX, testY = load_mnist("t10k-images-idx3-ubyte.gz", "t10k-labels-idx1-ubyte.gz")

	print("{} {} {} {}", trainX.shape, trainY.shape, testX.shape, testY.shape)

	for i in range(5):
		plt.imshow(trainX[i].reshape(28, 28) / 255.0)
		print(trainY[i])
		plt.show()
	for i in range(5):
		plt.imshow(testX[i].reshape(28, 28) / 255.0)
		print(testY[i])
		plt.show()

	scipy.io.savemat("mnist.mat", 
		{
			"trainX": trainX, "trainY": trainY,
		 	"testX": testX, "testY": testY
		}, 
		do_compression = True)
