
import sys,itertools

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
       dic[i]=[0]
   


def main():
    read_from_stdin()
    NFA()

if __name__=="__main__":
    main()
