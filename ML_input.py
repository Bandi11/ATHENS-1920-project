"""ML pipeline"""
import pandas as pd
import random
import BinSeqGenerator as Bingen
#from sklearn.naive_bayes import GaussianNB
#from sklearn.metrics import classification_report

def df_read(location):
  dataframe = pd.read_csv(location,sep=' ')
  #dataframe = dataframe.set_index('Unnamed: 0')
  return dataframe

def handwritten_list():
    handwritten_temp = df_read('lifespan.csv')['toss'].head(500)
    handwritten_binary = []
    for line in handwritten_temp:
        new_line = str(line)
        if len(str(line)) < 12:
            i = 12 - len(str(line))
            new_line = '0' * i + str(line)
        handwritten_binary.append(new_line)
    return handwritten_binary

def generated_list():
    list =[]
    for i in range(0,500):
        list.append(str(bin(random.getrandbits(12))[2:]))
    return list


def re_categorisation(allcommit):
  cat = []
  for index, row in allcommit.iterrows():
    if (row['category'] == 'whatever')or(row['category'] == 'bugfix'):
      cat.append('good')
    else:
      cat.append('bug')
      
  allcommit['cat.'] = cat
    
def sampling(allcommit,ammount):
  
  bug = allcommit[allcommit['cat.']=='bug'][:ammount]
  non_bug = allcommit[allcommit['cat.']=='good'][:ammount]
  
  test_bug = bug.sample(frac=0.3)
  test_nonbug = non_bug.sample(frac=0.3)
  
  test_df = pd.concat([test_bug,test_nonbug])
  test_vector = test_df['cat.']
  test_df = test_df.drop(['cat.','category'], axis=1)

  
  train_bug = bug.drop(list(test_bug.index))
  train_nonbug = non_bug.drop(list(test_nonbug.index))
  
  train_df = pd.concat([train_bug,train_nonbug])
  train_vector = train_df['cat.']
  train_df = train_df.drop(['cat.','category'], axis=1)
  
  return test_df, test_vector, train_df, train_vector

if __name__ == '__main__':
  DF = df_read('hive__all_Commit_Table_CSV')
  re_categorisation(DF)
  test_DF,test_V,train_DF,train_V = sampling(DF)
  
  Gauss_input_test = test_DF.drop(['author','authordate',
                             'changed files','changed lines',
                             'commitdate','commitdate==authordate',
                             'committer', 'committer==author',
                             'insertions','message',
                                      'not test file','renamed files'], axis = 1)
  
  Gauss_input_train = train_DF.drop(['author','authordate',
                             'changed files','changed lines',
                             'commitdate','commitdate==authordate',
                             'committer', 'committer==author',
                             'insertions','message',
                                      'not test file','renamed files'], axis = 1)
  
  
  gnb = GaussianNB()
  y_pred = gnb.fit(Gauss_input_train, train_V).predict(Gauss_input_test)
  report = classification_report(test_V, y_pred)
