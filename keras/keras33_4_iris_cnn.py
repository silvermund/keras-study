from tensorflow.keras.models import Sequential, Model
from tensorflow.keras.layers import Dense, Input, concatenate, Concatenate, Conv1D, Flatten, MaxPool1D, Dropout, GlobalAveragePooling1D
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.utils import to_categorical
from sklearn.datasets import load_iris
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, MaxAbsScaler, RobustScaler, StandardScaler, QuantileTransformer, PowerTransformer
from sklearn.preprocessing import OneHotEncoder
import time

datasets = load_iris()

print(datasets.DESCR)
print(datasets.feature_names)

#1. 데이터
x = datasets.data
y = datasets.target

print(x.shape, y.shape) #(150, 4) (150,)

# print(y) # y가 0,1,2
# print(np.unique(y))

# 원핫인코딩 One-Hot-Encoding (150,) -> (150, 3)
# 0 -> [1, 0, 0]
# 1 -> [0, 1, 0]
# 2 -> [0, 0, 1]

# [0, 1, 2, 1, 2] ->
# [[1, 0, 0]
#  [0, 1, 0]
#  [0, 1, 0]]    (4,) -> (4, 3)
y = to_categorical(y)
print(y.shape) # (150, 3)

# 데이터 전처리
x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.7, shuffle=True, random_state=66)

scaler = StandardScaler()
scaler.fit(x_train) # 훈련
x_train = scaler.transform(x_train) # 변환
x_test = scaler.transform(x_test)

x_train = x_train.reshape(x_train.shape[0], x_train.shape[1], 1)
x_test = x_test.reshape(x_test.shape[0], x_test.shape[1], 1)

print(x_train.shape) #(105, 4, 1)
print(x_test.shape) #(45, 4, 1)


#2. 모델 구성
model = Sequential()
model.add(Conv1D(filters=8, kernel_size=2, padding='same', input_shape=(4,1)))
model.add(Dropout(0.2))
model.add(Conv1D(8, 2, padding='same', activation='relu'))   
model.add(MaxPool1D())

model.add(Conv1D(32, 2, padding='same', activation='relu')) 
model.add(Dropout(0.2))
model.add(Conv1D(32, 2, padding='same', activation='relu')) 
model.add(MaxPool1D())

model.add(Conv1D(128, 2, padding='same', activation='relu'))
model.add(Dropout(0.2))
model.add(Conv1D(128, 2, padding='same', activation='relu'))  
# model.add(MaxPool1D())

# model.add(Flatten())    
# model.add(Dense(128, activation='relu')) 
# model.add(Dropout(0.2))
# model.add(Dense(128, activation='relu'))  
# model.add(Dropout(0.2))
# model.add(Dense(128, activation='relu')) 
model.add(GlobalAveragePooling1D())
model.add(Dense(3, activation="softmax"))

#3. 컴파일, 훈련
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics='acc')

es = EarlyStopping(monitor='loss', patience=5, mode='min', verbose=1)

start_time = time.time()
model.fit(x_train, y_train, epochs=1000, batch_size=4, validation_split=0.25, callbacks=[es])
end_time = time.time() - start_time



# 4. 평가 예측
loss = model.evaluate(x_test, y_test)
print("time : ", end_time)
print('loss : ', loss[0])
print('acc : ', loss[1])



'''
dnn
loss :  1.138843059539795
accuracy :  0.9333333373069763

cnn
time :  5.808387517929077
loss :  0.11911186575889587
acc :  0.9777777791023254
'''