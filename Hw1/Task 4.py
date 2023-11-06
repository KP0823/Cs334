
import sys,itertools

def state_to_go_to(target_spec, index):
    #0 works if its null and episillion
    if target_spec[0]!=[] and len(target_spec[0])>index:
        return(target_spec[0][index],True)
    else:
        return(target_spec[1][0],False)

def flatten(l):
    return [item for sublist in l for item in sublist]

def convert(an,choice,states):
    if an==[]:
        return 
    else:
        if len(an)==3 and isinstance(an[2],bool) and (an[2]==True or an[2]==False):
            choice+=(an[0],)
            states+=(an[1],)
            print("("+str(choice)+", "+str(states)+") --> "+str(an[2]))
        else:
            if(an[0]!=None and states[0]!=None):
                choice+=(an[0],)
                states+=(an[1],)
            for i in an:
                if isinstance(i, list):
                    convert(i,choice,states)

    return
    

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
    

        
    def follow_choice(self,choice_sequence, input_string):
        counter=0
        current_state=0
        places=[0]
        convert=self.convert_delta()
        final_state=None
        for i in choice_sequence:
            values= convert[(current_state,input_string[counter])]
            result=state_to_go_to(values,i)
            if result[1]==True:
                counter+=1
            current_state=result[0]
            places+=[current_state]
        if counter==len(input_string) and current_state==self.F[0]:
            final_state=True
        else:
            final_state=False
        return[places,final_state]

    def gen(self,choice,current,tape, an):
        if tape=='' and current==self.F[0]:
            an.append([choice,current,True])
            return
        if tape=='' and current!=self.F[0]:
            an.append([choice,current,False])
            return
        dlt= self.convert_delta()
        list_of_states=dlt[current,tape[0]]
        if(list_of_states==[[],[]]):
            an.append([choice,current,False])
            return
        an.append([choice,current])
        for i in range(len(list_of_states[0])):
            self.gen(i,list_of_states[0][i],tape[1::],an[-1])
        for k in range(len(list_of_states[1])):
            if list_of_states[0]==[]:
                self.gen(k,list_of_states[1][k],tape,an[-1])
            else:
                self.gen(len(list_of_states[0]),list_of_states[1][k],tape,an[-1])
        return

    def generate_all_processing_path(self,tape):
        an=[]
        dlt=self.convert_delta()
        list_of_states=dlt[0,tape[0]]
        for i in range(len(list_of_states[0])):
            an.append([0])
            self.gen(i,list_of_states[0][i],tape[1::],an[-1])
        for k in range(len(list_of_states[1])):
            an.append([0])
            self.gen(k,list_of_states[1][k],tape,an[-1])
        for l in an:
           choices=()
           states=(0,)
           convert(flatten(l[1::]),choices,states)
        return an
    
def read_choice_input():
    input_string=sys.stdin.readline()
    input_string=eval(input_string)
    return input_string

def main():
    first=NDFA()
    first.read_from_stdin()
    input_string=read_choice_input()
    transits=first.generate_all_processing_path(input_string)
  
if __name__=="__main__":
    main()
