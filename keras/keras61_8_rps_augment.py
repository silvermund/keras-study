# 훈련데이터를 기존데이터 20% 더 할 것
# 성과 비교
# save_dir도 temp에 넣을 것
# 증폭데이터는 temp에 저장 후 훈련 끝난 후 결과 본 뒤 삭제

# 훈련데이터를 기존데이터 20% 더 할 것
# 성과 비교
# save_dir도 temp에 넣을 것
# 증폭데이터는 temp에 저장 후 훈련 끝난 후 결과 본 뒤 삭제

from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, Embedding, LSTM, Flatten, Dropout, Bidirectional, MaxPool2D
from tensorflow.keras.callbacks import EarlyStopping
from sklearn.preprocessing import OneHotEncoder
import matplotlib.pyplot as plt
import numpy as np
import time

train_datagen = ImageDataGenerator(
    rescale=1./255, 
    horizontal_flip=True,
    vertical_flip=False,
    width_shift_range=0.1,
    height_shift_range=0.1,
    rotation_range=5,
    zoom_range=0.1,
    shear_range=0.5,
    fill_mode='nearest'
)

test_datagen = ImageDataGenerator(rescale=1./255)

x_train = np.load('./_save/_npy/k59_6_train_x.npy')
y_train = np.load('./_save/_npy/k59_6_train_y.npy')
x_test = np.load('./_save/_npy/k59_6_test_x.npy')
y_test = np.load('./_save/_npy/k59_6_test_y.npy')


print(x_train.shape, y_train.shape) #(2520, 150, 150, 3) (2520, 3)
print(x_test.shape, y_test.shape) #(2520, 150, 150, 3) (2520, 3)


augment_size = 520

randidx = np.random.randint(x_train.shape[0], size=augment_size)
print(x_train.shape[0])     #2520
# print(randidx)    
print(randidx.shape)        #(520,)

x_augmented = x_train[randidx].copy()
y_augmented = y_train[randidx].copy()

print(x_augmented.shape) #(520, 150, 150, 3)


x_augmented = x_augmented.reshape(x_augmented.shape[0], 150, 150, 3)
x_train = x_train.reshape(x_train.shape[0], 150, 150, 3)
x_test = x_test.reshape(x_test.shape[0], 150, 150, 3)

x_augmented = train_datagen.flow(x_augmented, np.zeros(augment_size),
                                batch_size=augment_size, shuffle=False,
                                #save_to_dir='../temp/'
                                ).next()[0]

print(x_augmented.shape) #(520, 150, 150, 3)

x_train = np.concatenate((x_train, x_augmented))
y_train = np.concatenate((y_train, y_augmented))

print(x_train.shape, y_train.shape) #(3040, 150, 150, 3) (3040, 3)


print(np.unique(y_train)) #[0. 1.]

model = Sequential()
model.add(Conv2D(filters = 16, kernel_size=(3,3), input_shape =(150,150,3), activation= 'relu'))
model.add(Conv2D(filters = 16, kernel_size=(3,3),  activation= 'relu'))
# model.add(MaxPooling2D(2,2))
model.add(Dropout(0.2))
model.add(Conv2D(filters = 64, kernel_size=(2,2),  activation= 'relu'))
model.add(Conv2D(filters = 64, kernel_size=(2,2),  activation= 'relu'))
# model.add(MaxPooling2D(2,2))
model.add(Dropout(0.2))
model.add(Flatten())
model.add(Dense(64, activation= 'relu'))
model.add(Dense(16, activation= 'relu'))
model.add(Dense(3, activation= 'softmax'))


# 3. 컴파일, 훈련
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['acc'])

# hist = model.fit_generator(xy_train, epochs=50, steps_per_epoch=32, #160/5=32
#                             validation_data=xy_test,  
#                             validation_steps=4)  

es = EarlyStopping(monitor='val_loss', patience=20, verbose=1, mode='auto', restore_best_weights=True)


start_time = time.time()
# hist = model.fit(x_train, y_train, epochs=100, verbose=1, validation_split=0.2, 
#             callbacks=[es], steps_per_epoch=32, validation_steps=4)

hist = model.fit(x_train, y_train, epochs=100, batch_size=64, validation_split=0.2, callbacks=[es])
end_time = time.time() - start_time


# 4. 평가, 예측
acc = hist.history['acc']
val_acc = hist.history['val_acc']
loss = hist.history['loss']
val_loss = hist.history['val_loss']
results = model.evaluate(x_test, y_test)

print('걸린 시간 : ', end_time)
print("acc : ", acc[-1])
print("val_acc : ", val_acc[-1])

# 걸린 시간 :  268.86843967437744
# acc :  0.9717364311218262
# val_acc :  0.5540287494659424

# after aug
# 걸린 시간 :  171.07495641708374
# acc :  0.9712170958518982
# val_acc :  0.38486841320991516
 