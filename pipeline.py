import pandas as pd
import ML_input as ML

if __name__=='__main__':


   handwritten_temp = ML.df_read('lifespan.csv')['toss'].head(500)
   handwritten_binary = []
   for line in handwritten_temp:
       new_line=str(line)
       if len(str(line)) < 12:
           i=12-len(str(line))
           new_line = '0'*i+str(line)
       handwritten_binary.append(new_line)
