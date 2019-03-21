"""ML pipeline"""
import pandas as pd
from CopyDetection import Encode
import random
import countones as c
from PrefixInt import DoublingLengthCode as Code
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
    return list(handwritten_binary)

def generated_list():
    list =[]
    generated_binary = []
    for i in range(0,500):
        list.append(str(bin(random.getrandbits(12))[2:]))
    for line in list:
        new_line = str(line)
        if len(str(line)) < 12:
            i = 12 - len(str(line))
            new_line = '0' * i + str(line)
        generated_binary.append(new_line)

    return generated_binary

def compressor(binary_list):
    compressed_list = []

    for element in binary_list:
        compressed_list.append(Encode(element))

    return compressed_list

def all_dataframe_creator(handwritten_compressed, compressed_list2, handwritten_binary, binarylist2):
    percent =[]
    savedbits = []
    category_list =[]
    percent += c.percentageofones(handwritten_binary)
    savedbits += c.savedbits(handwritten_binary,handwritten_compressed)
    category_list += categorisation(handwritten_binary,'handwritten')

    percent += c.percentageofones(binarylist2)
    savedbits += c.savedbits(binarylist2, compressed_list2)
    category_list += (categorisation(binarylist2,'generated'))

    dictionary = {'percent': percent,'saved_bits': savedbits,'type':category_list}
    Dataframe = pd.DataFrame.from_dict(dictionary)

    return Dataframe


def categorisation(binary_list, type):
  cat = []
  for element in binary_list:
    if type == 'handwritten':
        cat.append('handwritten')
    else:
        cat.append('generated')
  return cat
    
def sampling(dataframe, ammount):
  
  hand_all = dataframe[dataframe['type'] == 'handwritten'][:ammount]
  generated_all= dataframe[dataframe['type'] == 'generated'][:ammount]
  
  test_generated = generated_all.sample(frac=0.3)
  test_hand = hand_all.sample(frac=0.3)
  
  test_df = pd.concat([test_generated,test_hand])
  test_vector = test_df['type']
  test_df = test_df.drop(['type'], axis=1)
  train_generated = generated_all.drop(list(test_generated.index),axis=0)
  train_hand = hand_all.drop(list(test_hand.index),axis=0)

  train_df = pd.concat([train_hand,train_generated])

  train_vector = train_df['type']
  train_df = train_df.drop(['type'], axis=1)
  
  return test_df, test_vector, train_df, train_vector

if __name__ == '__main__':
    pass