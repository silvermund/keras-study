# save_dir 설명
# flow 또는 flow_directory의 iterator 구조 + 

from tensorflow.keras.datasets import fashion_mnist
from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, Embedding, LSTM, Flatten, Dropout, Bidirectional, MaxPooling2D
from tensorflow.keras.callbacks import EarlyStopping
import matplotlib.pyplot as plt
import numpy as np
import time

(x_train, y_train), (x_test, y_test) = fashion_mnist.load_data()


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
# train_datagen = ImageDataGenerator(rescale=1./255)

# xy_train = train_datagen.flow_from_directory(
#     '../_data/brain/train',
#     target_size=(150, 150),
#     batch_size=5,
#     class_mode='binary',
#     shuffle=True
# )

# 1. ImageDataGenerator를 정의
# 2. 파일에서 땡겨오려면 -> flow_from_directory() // x, y가 튜플 형태로 뭉쳐있어
# 3. 데이터에서 땡겨오려면 -> flow()              // x, y가 나눠있어

augment_size=10

randidx = np.random.randint(x_train.shape[0], size=augment_size)
print(x_train.shape[0])     #60000
print(randidx)              # [59679  9431   940 ... 54751 36349  4697]
print(randidx.shape)        #(40000,)

x_augmented = x_train[randidx].copy()
y_augmented = y_train[randidx].copy()

print(x_augmented.shape) #(40000, 28, 28)


x_augmented = x_augmented.reshape(x_augmented.shape[0], 28, 28, 1)
x_train = x_train.reshape(x_train.shape[0], 28, 28, 1)
x_test = x_test.reshape(x_test.shape[0], 28, 28, 1)


####################################################################################

start_time = time.time()
x_augmented = train_datagen.flow(x_augmented, np.zeros(augment_size),
                                batch_size=augment_size, shuffle=False,
                                save_to_dir='../temp/'  # 이번파일은 요놈이 주인공!!
                                )#.next()[0]
end_time = time.time() - start_time

# print(x_augmented.shape) #(40000, 28, 28, 1)
print(x_augmented[0][0].shape)

# x_train = np.concatenate((x_train, x_augmented))
# y_train = np.concatenate((y_train, y_augmented))

# print(x_train.shape, y_train.shape) #(100000, 28, 28, 1) (100000,)

print("걸린시간: ", end_time)



