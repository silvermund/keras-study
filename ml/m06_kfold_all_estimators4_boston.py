# 실습, 모델 구성하고 완료하시오.
# 회귀 데이터를 Classifier로 만들었을 경우에 에러 확인!!!
from sklearn.utils import all_estimators

from sklearn.svm import LinearSVC, SVC # 먹히는지 확인
from sklearn.neighbors import KNeighborsClassifier, KNeighborsRegressor
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor


from tensorflow.keras.models import Sequential, Model
from tensorflow.keras.layers import Dense, Input, concatenate, Concatenate
import numpy as np
from sklearn import datasets
from sklearn.metrics import r2_score, accuracy_score
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split, KFold, cross_val_score
from sklearn.preprocessing import MaxAbsScaler, RobustScaler, QuantileTransformer, PowerTransformer
import warnings
warnings.filterwarnings('ignore')

datasets = load_boston()

#1. 데이터
x = datasets.data
y = datasets.target

# x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, shuffle=True, random_state=5)
n_splits=5
kfold = KFold(n_splits=n_splits, shuffle=True, random_state=66)

# print(x.shape)
# print(y.shape)
# print(datasets.feature_names) ## ['CRIM' 'ZN' 'INDUS' 'CHAS' 'NOX' 'RM' 'AGE' 'DIS' 'RAD' 'TAX' 'PTRATIO' 'B' 'LSTAT'] 13의 요소
# print(datasets.DESCR)

# scaler = PowerTransformer()
# scaler.fit(x_train) # 훈련
# x_train = scaler.transform(x_train) # 변환
# x_test = scaler.transform(x_test)

# model = Sequential()
# model.add(Dense(55, input_dim=13)) #위의 종류만큼 input
# model.add(Dense(44))
# model.add(Dense(33))
# model.add(Dense(22))
# model.add(Dense(11))
# model.add(Dense(1))

#2. 모델구성
allAlgorithms = all_estimators(type_filter='classifier')
# allAlgorithms = all_estimators(type_filter='regressor')
# print(allAlgorithms)
print("모델의 갯수 : ", len(allAlgorithms)) #41

for (name, algorithm) in allAlgorithms:
    try :
        model = algorithm()

        scores = cross_val_score(model, x, y, cv=kfold)

        # model.fit(x_train, y_train)

        # y_predict = model.predict(x_test)
        # acc = accuracy_score(y_test, y_predict)
        print(name, scores)
    except:
        # continue
        print(name, 'is N/A')

# input1 = Input(shape=(13,))
# dense1 = Dense(64)(input1)
# dense2 = Dense(32, activation='relu')(dense1)
# dense3 = Dense(32, activation='relu')(dense2)
# dense4 = Dense(32, activation='relu')(dense3)
# dense5 = Dense(32, activation='relu')(dense4)
# dense6 = Dense(32, activation='relu')(dense5)
# dense7 = Dense(8, activation='relu')(dense6)
# output1 = Dense(1)(dense7)

# model = Model(inputs=input1, outputs=output1)
# model.summary()
# model.compile(loss='mse', optimizer='adam')


# model = LinearSVC()

# model = SVC()

# model = KNeighborsClassifier()

# model = KNeighborsRegressor()

# model = LogisticRegression()

# model = RandomForestClassifier()

# model = RandomForestRegressor

# model = DecisionTreeClassifier()

# model = DecisionTreeRegressor()



# model.fit(x_train, y_train)
# model.fit(x_train, y_train, epochs=100, batch_size=1, validation_split=0.3, shuffle=True)


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

'''
loss = model.evaluate(x_test, y_test)
print('loss : ', loss)

y_predict = model.predict(x_test)
# print('x_predict의 예측값 : ', y_predict)

r2 = r2_score(y_test, y_predict)

print("r2스코어 :", r2)

MaxAbsScaler 선택
loss :  9.979451179504395
r2스코어 : 0.8725385393698488

RobustScaler 선택
loss :  15.675557136535645
r2스코어 : 0.799785640021273

QuantileTransformer 선택
loss :  15.128388404846191
r2스코어 : 0.8067742871910053

PowerTransformer 선택
loss :  15.489265441894531
r2스코어 : 0.8021650131526875

'''

# 모델의 갯수 :  41
# AdaBoostClassifier [nan nan nan nan nan]
# BaggingClassifier [nan nan nan nan nan]
# BernoulliNB [nan nan nan nan nan]
# CalibratedClassifierCV [nan nan nan nan nan]
# CategoricalNB [nan nan nan nan nan]
# ClassifierChain is N/A
# ComplementNB [nan nan nan nan nan]
# DecisionTreeClassifier [nan nan nan nan nan]
# DummyClassifier [nan nan nan nan nan]
# ExtraTreeClassifier [nan nan nan nan nan]
# ExtraTreesClassifier [nan nan nan nan nan]
# GaussianNB [nan nan nan nan nan]
# GaussianProcessClassifier [nan nan nan nan nan]
# GradientBoostingClassifier [nan nan nan nan nan]
# HistGradientBoostingClassifier [nan nan nan nan nan]
# KNeighborsClassifier [nan nan nan nan nan]
# LabelPropagation [nan nan nan nan nan]
# LabelSpreading [nan nan nan nan nan]
# LinearDiscriminantAnalysis [nan nan nan nan nan]
# LinearSVC [nan nan nan nan nan]
# LogisticRegression [nan nan nan nan nan]
# LogisticRegressionCV [nan nan nan nan nan]
# MLPClassifier [nan nan nan nan nan]
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
# RandomForestClassifier [nan nan nan nan nan]
# RidgeClassifier [nan nan nan nan nan]
# RidgeClassifierCV [nan nan nan nan nan]
# SGDClassifier [nan nan nan nan nan]
# SVC [nan nan nan nan nan]
# StackingClassifier is N/A
# VotingClassifier is N/A