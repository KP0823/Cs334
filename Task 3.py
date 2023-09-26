
import sys,itertools

class NDFA:
    def __init__(self):
        self.states=None
        self.sigma=None
        self.dlt=None
        self.qs=None
        self.F=None
        self.choice_sequence=None
        self.input_string=None

    def read_from_stdin(self):

        self.states = input()
        self.states= eval(self.states)

        self.sigma = sys.stdin.readline()
        self.sigma = eval(self.sigma)
        
        self.dlt = sys.stdin.readline()
        self.dlt = eval(self.dlt)

        self.qs = sys.stdin.readline()
        self.qs = eval(self.qs)

        self.F = sys.stdin.readline()
        self.F = eval(self.F)

        self.choice_sequence=sys.stdin.readline()
        self.choice_sequence=eval(self.choice_sequence)

        self.input_string=sys.stdin.readline()
        self.choice_sequence=eval(self.choice_sequence)

#       return states, sigma, dlt, qs, F

    def convert_delta(self):
        dic ={}
        state=self.states
        sigma=self.sigma
        dlt=self.dlt 
        keys=list(itertools.product(state,sigma))
        for i in keys:
            dic[i]=[]
        for key, value in dlt.items():
            if key[1]=='E':
                dic[(key[0],'0')]+=[value]
                dic[(key[0],'1')]+=[value]

            else:
                dic[key]+=[value]
        return dic
    
    @staticmethod
    def state_to_go_to(target_spec, index):
        #0 works if its null and episillion
        if target_spec[0]!=[] and len(target_spec[0])>index:
            return(target_spec[0][index],True)
        else:
            return(target_spec[1][0],False)
        
    def follow_choice(self,choice_sequence, input_string):
        

    
def main():
    first=NDFA()
    first.read_from_stdin()
    result=first.convert_delta()
    last_key=list(result)[-1]
    index=0
    for key,values in result.items():
        if values==[[],[]]:
           continue
        else:
            while index<(len(values[0]) +len(values[1])) :
                add=first.state_to_go_to(values,index)
                print(str(key)+", "+str(index)+", "+ str(add)+"")
                index+=1
            index=0
if __name__=="__main__":
    main()
