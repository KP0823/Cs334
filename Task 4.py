
import sys,itertools

def state_to_go_to(target_spec, index):
    #0 works if its null and episillion
    if target_spec[0]!=[] and len(target_spec[0])>index:
        return(target_spec[0][index],True)
    else:
        return(target_spec[1][0],False)
    
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
    
    # def generate_all_helper(self, current_choice, current_state, tape_index,tape,):
    #     result=[]
    #     if tape_index==len(tape) and self.F==current_state:
    #         return [current_choice,current_state,True]
    #     if tape_index==len(tape) and self.F!=current_state:
    #         return [current_choice,current_state,False]
    #     current_choice=0
    #     transitions=self.convert_delta()
    #     moves=transitions[(current_state,tape[tape_index])]

    #     if moves==[[],[]]:
    #         #return[current_choice,current_state,False]
    #         return result
    #     if moves[0]!=[]:
    #         for i in range(len(moves[0])):
    #             future_moves=state_to_go_to(moves,current_choice)
    #             print(result)
    #             if future_moves[1]==False:
    #                 #result= [current_choice,current_state,tape[tape_index::]]
    #                 result+= self.generate_all_helper(0,future_moves[0],tape_index,tape)
    #             elif future_moves[1]==True:
    #                 #result= [current_choice,current_state,tape[tape_index::]]
    #                 result+= [self.generate_all_helper(0,future_moves[0],tape_index+1,tape)]
    
    #             #result = [current_choice,current_state,tape[tape_index::]]
    #             result += [self.generate_all_helper(current_choice+1,current_state, tape_index+1 ,tape)]
    #     # elif moves[0]==[] and moves[1]!=[]:
    #     #     result = [current_choice,current_state,tape[tape_index::]]
    #     #     result+= [self.generate_all_helper(0,moves[1][0],tape_index,tape)]
    #     return result


    def gen_all_helper(self,current_choice,current_state,tape):
        if tape=='' and current_state==self.F[0]:
            return [current_choice,current_state,True]
        if tape=='' and current_state!=self.F[0]:
            return [current_choice,current_state,False]
        delta=self.convert_delta()
        list_of_states=delta[(current_state,tape[0])]
        result=[current_choice,current_state,tape]
        if list_of_states==[[],[]]:
            return [current_choice,current_state,False]
        if current_choice>=len(list_of_states[0]) and list_of_states[1]==[]:
            return []
        else:
            goto=state_to_go_to(list_of_states, current_choice)
            if(goto[1]==True):
                result+=[self.gen_all_helper(0,goto[0],tape[1::])]
            if(goto[1]==False):
                result+=[self.gen_all_helper(0,goto[1],tape)]
            result+=[self.gen_all_helper(current_choice+1,current_state,tape[1::])]
        return result
    #loop to the end moves[0]
    #then try the moves[1]
    def generate_all_processing_path(self,tape):
        current_choice=0
        current_state=0
        tape_index=0
        #return self.generate_all_helper(current_choice,current_state,tape_index,tape)
        return self.gen_all_helper(current_choice,current_state,tape)
    
def read_choice_input():
    input_string=sys.stdin.readline()
    input_string=eval(input_string)
    return input_string

def main():
    first=NDFA()
    first.read_from_stdin()
    input_string=read_choice_input()
    transits=first.generate_all_processing_path(input_string)
    print(transits)

if __name__=="__main__":
    main()
