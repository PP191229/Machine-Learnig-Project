import joblib
import pandas
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

df = pandas.read_csv(r'D:\Machine Learning python\Machine-Learnig-Project\untitled\Data.csv')
df.shape
df.head()

# axis 1 = columns, axis 0 = row
X = df.drop('Movement Input', axis=1)
Y = df['Movement Input']

X_train, X_test, Y_train, y_test = train_test_split(X, Y, test_size=0.2)

svc = SVC(kernel='linear')

svc.fit(X_train, Y_train)

y_pred = svc.predict(X_test)

acc = metrics.accuracy_score(y_test, y_pred)
print(acc)
joblib.dump(svc, 'trained_model.pkl')
