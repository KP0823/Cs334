
import sys,itertools,pprint

global states,sigma, dlt, qs,F

def read_from_stdin():
    global states,sigma, dlt, qs,F

    states = input()
    states= eval(states)

    sigma = sys.stdin.readline()
    sigma = eval(sigma)
    
    dlt = sys.stdin.readline()
    dlt = eval(dlt)

    qs = sys.stdin.readline()
    qs = eval(qs)

    F = sys.stdin.readline()
    F = eval(F)

    return states, sigma, dlt, qs, F

def NFA():
    global states,sigma, dlt, qs,F
    dic ={}
    keys=list(itertools.product(states,sigma))
    for i in keys:
        dic[i]=[]
    for key, value in dlt.items():
        if key[1]=='E':
            dic[(key[0],'0')]+=[value]
            dic[(key[0],'1')]+=[value]

        else:
            dic[key]+=[value]
    return dic

def main():
    read_from_stdin()
    result=NFA()
    last_key=list(result)[-1]
    for key,value in result.items():
        if(key!=last_key):
            print(str(key) +": "+str(value)+",")
        else:
             print(str(key) +": "+str(value)+"")
    

if __name__=="__main__":
    main()
