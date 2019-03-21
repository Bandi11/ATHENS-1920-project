import pandas as pd
import ML_input as ML


if __name__=='__main__':

    handwritten_binary = ML.handwritten_list()
    generated_binary = ML.generated_list()
    generated_compressed = ML.compressor(generated_binary)
    handwritten_compressed = ML.compressor(handwritten_binary)

    Dataframe =ML.all_dataframe_creator(handwritten_compressed,generated_compressed,
                                        handwritten_binary,generated_binary)

    t_d,t_v,train_d,train_v = ML.sampling(Dataframe,500)

from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import classification_report

tuned_parameters = [{'kernel': ['rbf'],
                     'gamma': [1e-3, 1e-4],
                     'C': [1, 10, 100, 1000]}]

gnb = GaussianNB()
y_pred = gnb.fit(train_d, train_v).predict(t_d)
report = classification_report(t_v, y_pred)
print(report)


