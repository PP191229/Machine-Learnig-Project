import joblib
import pandas
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

df = pandas.read_csv(r'D:\Machine Learning python\Machine-Learnig-Project\untitled\Data.csv')
df.shape
df.head()


X = df.drop('Movement Input', axis=1)
Y = df['Movement Input']

x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)

svc = SVC(kernel='linear')

svc.fit(x_train, y_train)

y_pred = svc.predict(x_test)

joblib.dump(svc, open('trained_model.pkl', 'wb'))
svmModel = joblib.load(open('trained_model.pkl', 'rb'))
SVM_results = svmModel.score(x_test, y_test)
print(SVM_results)
