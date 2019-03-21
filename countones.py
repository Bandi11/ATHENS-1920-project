

def percentageofones(listSQ):
    
    listPer=[]
    for i in listSQ:
        c = i.count("1")
        p = c/12*100
        listPer.append(p)
    
    return listPer


def savedbits(listSQ,listCompressed):
    
    listbits=[]
    
    for i,j in zip(listSQ,listCompressed): 
        
        listbits.append(len(i)-len(j.replace(' ','')))
        
    return listbits
    

