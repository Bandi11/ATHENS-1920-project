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

    print(t_d)
    print(t_v)
    print(train_d)
    print(train_v)
