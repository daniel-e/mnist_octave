## Checkout the repository

    git clone XXX

## Load data with Octave

Start Octave.

```matlab
d=load('mnist.mat');

  # d.trainX  is a (60000,784) matrix which
  #           contains the pixel data for training
  # d.trainY  is a (1,60000) matrix which
  #           contains the labels for the training data
  # d.testX   is a (10000,784) matrix which
  #           contains the pixel data for testing
  # d.testY   is a (1,10000) matrix which
  #           contains the labels for the test set

X=d.trainX;
i=reshape(X(3,:), 28,28)';
image(i);
```


## Setup an environment

This is optional if you already have all packages installed. You can either install the required packages directly on your system with pip or you can create a virtual environment into which the packages are installed.

### Install packages directly

    pip3 install scipy numpy matplotlib

### Install the packages into a virtual environment

    virtualenv -p python3 venv
    source venv/bin/activate
    pip3 install --upgrade pip
    pip3 install scipy numpy matplotlib

## Download the data (optional)

If you clone the GitHub repository this step is optional.

Download the data from http://yann.lecun.com/exdb/mnist/

    wget http://yann.lecun.com/exdb/mnist/train-images-idx3-ubyte.gz
    wget http://yann.lecun.com/exdb/mnist/train-labels-idx1-ubyte.gz
    wget http://yann.lecun.com/exdb/mnist/t10k-images-idx3-ubyte.gz
    wget http://yann.lecun.com/exdb/mnist/t10k-labels-idx1-ubyte.gz

## Execute mnist.py to create a matrix for Octave

    ./mnist.py

A new file `mnist.mat` is created which contains the data. This matrix can be loaded with Octave (see above).



