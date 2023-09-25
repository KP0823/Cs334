
import sys,itertools,pprint

class NDFA:
    def __init__(self):
        self.states=None
        self.sigma=None
        self.dlt=None
        self.qs=None
        self.F=None

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
        if index==1:
            if target_spec[index]==[] and target_spec[0]!=[]:
                return (target_spec[0][-1],False)
            else:
                return (target_spec[index],True)
        if index==0:
            if target_spec[index]==[] and target_spec[1]!=[]:
                return (target_spec[1][-1],False)
            else:
                return (target_spec[index],True)
    
    
def main():
    first=NDFA()
    first.read_from_stdin()
    result=first.convert_delta()
    last_key=list(result)[-1]

if __name__=="__main__":
    main()
