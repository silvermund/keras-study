# 실습, 모델 구성하고 완료하시오.
from sklearn.utils import all_estimators

from sklearn.svm import LinearSVC, SVC
from sklearn.neighbors import KNeighborsClassifier, KNeighborsRegressor
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

from tensorflow.keras.models import Sequential, Model
from tensorflow.keras.layers import Dense, Input, concatenate, Concatenate
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.utils import to_categorical
import numpy as np
import pandas as pd
# from sklearn import datasets
from sklearn.metrics import r2_score, accuracy_score
from sklearn.model_selection import train_test_split, KFold, cross_val_score
from sklearn.preprocessing import MinMaxScaler, StandardScaler, QuantileTransformer, PowerTransformer
from sklearn.datasets import load_wine
from sklearn.preprocessing import OneHotEncoder
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

datasets = pd.read_csv('../_data/winequality-white.csv', sep=';', index_col=None, header=0)

# ./  : 현재폴더
# ../ : 상위폴더

# print(datasets)
# print(datasets.shape) # (4898, 12)

# 11개까지 x, 마지막 1개 quality가 y

# print(datasets.info())
# print(datasets.describe())

# 다중분류
# 모델링하고
# 0.8 이상 완성!!!


#1. 데이터
np = datasets.values


x = np[:,:11]
y = np[:,11:]

print(x)
print('-----------------------------------------')
print(y)

#1. 판다스 -> 넘파이
#2. x와 y를 분리
#3. sklearn의 onehot??? 사용할 것 
#4. y의 라벨을 확인 np.unique(y)
#5. y의 shape 확인 (4898, ) -> (4898,7)


print(x.shape, y.shape) # (4898, 11) (4898, 1)

print(y) # y가 0,1,2
# print(np.unique(y))

ohe = OneHotEncoder(sparse=False)
y = ohe.fit_transform(y)

# y = to_categorical(y)

print(y[:5])
print(y.shape) # (4898, 7)

print(type(x), type(y))


# 데이터 전처리
# x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.7, shuffle=True, random_state=66)
n_splits=5
kfold = KFold(n_splits=n_splits, shuffle=True, random_state=66)


# scaler = PowerTransformer()
# scaler.fit(x_train) # 훈련
# x_train = scaler.transform(x_train) # 변환
# x_test = scaler.transform(x_test)

#2. 모델 구성
allAlgorithms = all_estimators(type_filter='classifier')
# allAlgorithms = all_estimators(type_filter='regressor')
# print(allAlgorithms)
print("모델의 갯수 : ", len(allAlgorithms)) #41

for (name, algorithm) in allAlgorithms:
    try :
        model = algorithm()

        scores = cross_val_score(model, x, y, cv=kfold)

        print(name, scores)
    except:
        # continue
        print(name, 'is N/A')
        
# model = LinearSVC()

# model = SVC()

# model = KNeighborsClassifier()
# accuracy_score :  0.5054421768707483

# model = KNeighborsRegressor()

# model = LogisticRegression()

# model = RandomForestClassifier()
# accuracy_score :  0.5414965986394558

# model = DecisionTreeClassifier()
# accuracy_score :  0.5918367346938775


# model = Sequential()
# model.add(Dense(128, activation='relu', input_shape=(11,))) 
# model.add(Dense(64, activation='relu'))
# model.add(Dense(64, activation='relu'))
# model.add(Dense(64, activation='relu'))
# model.add(Dense(64, activation='relu'))
# model.add(Dense(7, activation='softmax'))

#3. 컴파일, 훈련
# model.fit(x_train, y_train)
# model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# es = EarlyStopping(monitor='loss', patience=5, mode='min', verbose=1)

# hist = model.fit(x_train, y_train, epochs=100, batch_size=16, validation_split=0.2, callbacks=[es])

# print(hist.history.keys())
# print("================================")
# print(hist.history['loss'])
# print("================================")
# print(hist.history['val_loss'])
# print("================================")



#4. 평가, 예측
# results = model.score(x_test, y_test)
# print(results)
# y_predict = model.predict(x_test)
# acc = accuracy_score(y_test, y_predict)
# print("accuracy_score : ", acc)



# print("=================예측===============")
# print(y_test[:5])
# y_predict2 = model.predict(x_test[:5])
# print(y_predict2)


# print("==============평가, 예측=============")
# loss = model.evaluate(x_test, y_test)
# print('loss : ', loss[0])
# print('accuracy : ', loss[1])

# print("=================예측===============")
# print(y_test[:5])
# y_predict = model.predict(x_test[:5])
# print(y_predict)

# plt.plot(hist.history['loss'])  # x:epoch, / y:hist.history['loss']
# plt.plot(hist.history['val_loss'])

# plt.title("loss, val_loss")
# plt.xlabel('epoch')
# plt.ylabel('loss, val_loss')
# plt.legend(['train loss','val loss'])
# plt.show()
'''
loss :  1.8325819969177246
accuracy :  0.5442177057266235

원핫인코더
loss :  1.6113581657409668
accuracy :  0.5673469305038452

StandardScaler
loss :  2.4856913089752197
accuracy :  0.5965986251831055

PowerTransformer
loss :  2.5612287521362305
accuracy :  0.6000000238418579
'''

# 모델의 갯수 :  41
# AdaBoostClassifier [nan nan nan nan nan]
# BaggingClassifier [nan nan nan nan nan]
# BernoulliNB [nan nan nan nan nan]
# CalibratedClassifierCV [nan nan nan nan nan]
# CategoricalNB [nan nan nan nan nan]
# ClassifierChain is N/A
# ComplementNB [nan nan nan nan nan]
# DecisionTreeClassifier [0.62755102 0.6        0.60306122 0.59959142 0.60572012]
# DummyClassifier [0. 0. 0. 0. 0.]
# ExtraTreeClassifier [0.63061224 0.59591837 0.6        0.61797753 0.61389173]
# ExtraTreesClassifier [0.59795918 0.53979592 0.55306122 0.57711951 0.57711951]
# GaussianNB [nan nan nan nan nan]
# GaussianProcessClassifier [nan nan nan nan nan]
# GradientBoostingClassifier [nan nan nan nan nan]
# HistGradientBoostingClassifier [nan nan nan nan nan]
# KNeighborsClassifier [0.40612245 0.40816327 0.39693878 0.38508682 0.37282942]
# LabelPropagation [nan nan nan nan nan]
# LabelSpreading [nan nan nan nan nan]
# LinearDiscriminantAnalysis [nan nan nan nan nan]
# LinearSVC [nan nan nan nan nan]
# LogisticRegression [nan nan nan nan nan]
# LogisticRegressionCV [nan nan nan nan nan]
# MLPClassifier [0.29081633 0.08877551 0.29591837 0.18590398 0.22982635]
# MultiOutputClassifier is N/A
# MultinomialNB [nan nan nan nan nan]
# NearestCentroid [nan nan nan nan nan]
# NuSVC [nan nan nan nan nan]
# OneVsOneClassifier is N/A
# OneVsRestClassifier is N/A
# OutputCodeClassifier is N/A
# PassiveAggressiveClassifier [nan nan nan nan nan]
# Perceptron [nan nan nan nan nan]
# QuadraticDiscriminantAnalysis [nan nan nan nan nan]
# RadiusNeighborsClassifier [nan nan nan nan nan]
# RandomForestClassifier [0.58877551 0.53979592 0.55918367 0.57303371 0.56690501]
# RidgeClassifier [nan nan nan nan nan]
# RidgeClassifierCV [nan nan nan nan nan]
# SGDClassifier [nan nan nan nan nan]
# SVC [nan nan nan nan nan]
# StackingClassifier is N/A
# VotingClassifier is N/A