from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense
import numpy as np
from keras.utils import to_categorical

(x_train,y_train),(x_test,y_test)=mnist.load_data()
x_train=x_train[:10000]
y_train=y_train[:10000]
x_test=x_test[:2000]
y_test=y_test[:2000]

x_train=x_train.reshape(x_train.shape[0],28*28).astype("float32")/255
x_test=x_test.reshape(x_test.shape[0],28*28).astype("float32")/255

y_train=to_categorical(y_train,10)
y_test=to_categorical(y_test,10)

model=Sequential()
model.add(Dense(64,activation="relu",input_shape=(784,)))
model.add(Dense(32,activation="relu"))
model.add(Dense(10,activation="softmax"))
model.compile(optimizer="adam",loss="categorical_crossentropy",metrics=["accuracy"])

model.fit(x_train,y_train,epochs=2,batch_size=64,validation_split=0.1)

loss,acc=model.evaluate(x_test,y_test)
print("accuracy",acc)
print(loss)