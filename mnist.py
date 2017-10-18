#!/usr/bin/env python3

import struct, gzip
import scipy.io
import numpy as np

def loadY(fnlabel):
	f = gzip.open(fnlabel, 'rb')
	f.read(8)
	return np.frombuffer(f.read(), dtype = np.uint8)

def loadX(fnimg):
	f = gzip.open(fnimg, 'rb')
	f.read(16)
	return np.frombuffer(f.read(), dtype = np.uint8).reshape((-1, 28*28))


if __name__ == "__main__":
	trainX = loadX("train-images-idx3-ubyte.gz")
	trainY = loadY("train-labels-idx1-ubyte.gz")
	testX = loadX("t10k-images-idx3-ubyte.gz")
	testY = loadY("t10k-labels-idx1-ubyte.gz")

	data = {"trainX": trainX, "trainY": trainY, "testX": testX, "testY": testY}
	scipy.io.savemat("mnist.mat", data, do_compression = True)
