from sklearn import svm
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

iris = datasets.load_iris()
print(type(iris))
print(iris.data)
print(iris.feature_names)
print(iris.target)
print(iris.target_names)
x=iris.data[:,2]
y=iris.target
x_train,x_test, y_train, y_test=train_test_split(x,y,test_size=0.2, random_state=4)

x_train_1d=x_train.reshape(-1,1)
x_test_1d=x_test.reshape(-1,1)
y_train_1d=y_train.reshape(-1,1)
y_test_1d=y_test.reshape(-1,1)
model = svm.SVC(kernel='linear')
model.fit(x_train_1d, y_train_1d)
y_pred_mod=model.predict(x_test_1d)
print(accuracy_score(y_test_1d, y_pred_mod))
