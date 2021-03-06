# encoding: utf-8
"""
@author: monitor1379 
@contact: yy4f5da2@hotmail.com
@site: www.monitor1379.com

@version: 1.0
@license: GNU General Public License(Version 3)
@file: example3_mnist_nn.py
@time: 2016/10/13 0:07

构建一个多层神经网络来对MNIST数据集进行分类。
使用进度条功能来显示过程。
"""

from hamaa.datasets.datasets import load_mnist_data
from hamaa.layers import Dense, Activation
from hamaa.models import Sequential
from hamaa.optimizers import SGD
from hamaa.utils.np_utils import split_training_data


def run():
    # 加载MNIST数据集，preprocess表示是否进行归一化预处理，flatten表示是否将二维图像平铺成一维
    print 'loading MNIST dataset...'
    training_data, test_data = load_mnist_data(nb_training=60000, nb_test=10000, preprocess=True, flatten=True)
    training_data, validation_data = split_training_data(training_data, split_ratio=0.95)

    print 'training_data:', training_data[0].shape
    print 'validation_data:', validation_data[0].shape
    print 'test_data:', test_data[0].shape

    # 构建一个每层神经元数为 [784->100->10] 的神经网络
    model = Sequential()
    model.add(Dense(input_dim=784, output_dim=100, init='glorot_normal'))
    model.add(Activation('sigmoid'))
    model.add(Dense(output_dim=10, init='glorot_normal'))
    model.add(Activation('sigmoid'))
    model.set_objective('categorical_crossentropy')
    model.set_optimizer(SGD(lr=0.2, momentum=0.2, decay=1e-3))

    print model.summary()

    model.train(training_data=training_data,
                nb_epochs=10,
                mini_batch_size=100,
                verbose=2,  # 使用进图条功能
                validation_data=validation_data,
                log_epoch=1
                )

    print 'test accuracy:', model.evaluate_accuracy(test_data[0], test_data[1])
    model.plot_training_iteration()


if __name__ == '__main__':
    run()
