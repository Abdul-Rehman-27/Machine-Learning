from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense 
import numpy as np

X=np.array([[0,0],[0,1],[1,0],[1,1]])
y=np.array([[0],[0],[0],[1]])

model=Sequential()
model.add(Dense(1,input_dim=2,activation="sigmoid"))
model.compile(optimizer="sgd",loss="binary_crossentropy",metrics=['accuracy'])
model.fit(X,y,epochs=100,verbose=0)

loss,acc=model.evaluate(X,y,verbose=0)
print("Accuracy:",acc)
print("prediction:",model.predict(X).round())