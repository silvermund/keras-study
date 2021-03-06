# 실습
# 멀티 레이어
# from tensorflow.keras.datasets import mnist
# acc 0.97이상


from keras.datasets import mnist
import tensorflow as tf
import numpy as np
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import accuracy_score


#1. 데이터
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# print(x_train.shape, y_train.shape) #(60000, 28, 28) (60000,)
# print(x_test.shape, y_test.shape) #(10000, 28, 28) (10000,)

x_train = x_train.reshape(60000, 28*28)  
x_test = x_test.reshape(10000, 28*28)
y_train = y_train.reshape(60000,1)
y_test = y_test.reshape(10000,1)

scaler = StandardScaler()
x_train = scaler.fit_transform(x_train) # 변환
x_test = scaler.transform(x_test)

en = OneHotEncoder()
y_train = en.fit_transform(y_train).toarray()
y_test = en.fit_transform(y_test).toarray()


# print(x_train.shape, y_train.shape) #(60000, 784) (60000, 10)
# print(x_test.shape, y_test.shape) #(10000, 784) (10000, 10)

# 2. 모델링
print(x_train.shape, y_train.shape)

x = tf.compat.v1.placeholder(tf.float32, shape=[None, 28*28])
y = tf.compat.v1.placeholder(tf.float32, shape=[None, 10])

# 히든레이어 1
W1 = tf.Variable(tf.random.normal([28*28, 512]), name='weight')
b1 = tf.Variable(tf.random.normal([512]), name='bias')

layer1 = tf.nn.relu(tf.matmul(x, W1) + b1)

# 히든레이어 2
W2 = tf.Variable(tf.random.normal([512 ,256]), name='weight')
b2 = tf.Variable(tf.random.normal([256]), name='bias')

layer2 = tf.sigmoid(tf.matmul(layer1, W2) + b2)

# 히든레이어 3
W3 = tf.Variable(tf.random.normal([256 ,128]), name='weight')
b3 = tf.Variable(tf.random.normal([128]), name='bias')

layer3 = tf.sigmoid(tf.matmul(layer2, W3) + b3)

# 히든레이어 4
W4 = tf.Variable(tf.random.normal([128 ,64]), name='weight')
b4 = tf.Variable(tf.random.normal([64]), name='bias')

layer4 = tf.sigmoid(tf.matmul(layer3, W4) + b4)

# 아웃풋레이어
W5 = tf.Variable(tf.random.normal([64 ,10]), name='weight')
b5 = tf.Variable(tf.random.normal([1, 10]), name='bias')

hypothesis = tf.nn.softmax(tf.matmul(layer4, W5) + b5) 
# layer = tf.sigmoid(tf.matmul(x, W) + b)

# layers1 = tf.nn.relu(tf.matmul(x_train, W) + b)
# layers2 = tf.nn.elu(tf.matmul(x_train, W) + b)

# layers3 = tf.nn.selu(tf.matmul(x_train, W) + b)
# layers4 = tf.sigmoid(tf.matmul(x_train, W) + b)
# layers = tf.nn.dropout(layers4, keep_prob=0.3)
# hypothesis = tf.nn.relu(tf.matmul(x_train, W) + b)
# hypothesis = tf.nn.elu(tf.matmul(x_train, W) + b)
# hypothesis = tf.nn.selu(tf.matmul(x_train, W) + b)




# cost = tf.reduce_mean(tf.square(hypothesis-y)) # mse
cost = -tf.reduce_mean(y_train*tf.log(hypothesis)+(1-y_train)*tf.log(1-hypothesis)) # binary_crossentropy

optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.00001)
# optimizer = tf.train.GradientDescentOptimizer(learning_rate=1e-5)
train = optimizer.minimize(cost)

# 마지막 레이어 softmax

sess = tf.compat.v1.Session()
sess.run(tf.global_variables_initializer())

for epochs in range(2001):
    cost_val, hy_val, _ = sess.run([cost, hypothesis, train], feed_dict={x:x_train, y:y_train})
    if epochs % 200 == 0:
        print(epochs, cost_val)


# 4. 평가, 예측
predicted = tf.cast(hypothesis > 0.5, dtype=tf.float32)
accuracy = tf.reduce_mean(tf.cast(tf.equal(predicted, y), dtype=tf.float32))
h, c, a = sess.run([hypothesis, predicted, accuracy], feed_dict={x:x_train, y:y_train})

print("==========================================")
print("예측값 : \n", h[0:5], "\n 예측결과값 \n: ", c[0:5], "\n Accuracy \n:", a)


sess.close()


