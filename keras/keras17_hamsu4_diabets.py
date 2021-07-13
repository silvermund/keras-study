# diabetes를 함수형으로 구현하시오.
# 서머리 확인

from tensorflow.keras.models import Sequential, Model
from tensorflow.keras.layers import Dense, Input
import numpy as np
import pandas as pd
from sklearn.datasets import load_diabetes
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split

datasets = load_diabetes()

x = datasets.data
y = datasets.target

print(x.shape, y.shape) #(442,10) (442,)

print(datasets.feature_names) #['age', 'sex', 'bmi', 'bp', 's1', 's2', 's3', 's4', 's5', 's6']

print(datasets.DESCR)

print(y[:30])
print(np.min(y), np.max(y))

x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.7, shuffle=True, random_state=5)

#2. 모델구성

input1 = Input(shape=(10,))
dense1 = Dense(2048)(input1)
dense2 = Dense(1024, activation='relu')(dense1)
dense3 = Dense(512, activation='relu')(dense2)
dense4 = Dense(256, activation='relu')(dense3)
dense5 = Dense(128, activation='relu')(dense4)
dense6 = Dense(64, activation='relu')(dense5)
dense7 = Dense(8, activation='relu')(dense6)
output1 = Dense(1)(dense7)

model = Model(inputs=input1, outputs=output1)
model.summary()


# model = Sequential()
# model.add(Dense(2048, input_dim=10)) 
# model.add(Dense(1024, activation='relu'))
# model.add(Dense(512, activation='relu'))
# model.add(Dense(256, activation='relu'))
# model.add(Dense(128, activation='relu'))
# model.add(Dense(64, activation='relu'))
# model.add(Dense(8, activation='relu'))
# model.add(Dense(1))

#3. 컴파일, 훈련

model.compile(loss='mse', optimizer='adam')

model.fit(x_train, y_train, epochs=100, batch_size=1, validation_split=0.2, shuffle=True)

#4. 평가, 예측
# mse, R2
loss = model.evaluate(x, y)
print('loss : ', loss)

y_predict = model.predict(x)
print('x_predict의 예측값 : ', y_predict)

r2 = r2_score(y, y_predict)

print("r2스코어 :", r2)

#과제1
#0.62 까지 올릴것!!!
#깃헙 주소를 메일에 보낼 것!
'''
r2스코어 : 0.586778592520653
'''

