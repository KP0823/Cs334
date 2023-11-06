import sys

def read_from_stdin():

    term = input()
    term= eval(term)

    var = sys.stdin.readline()
    var = eval(var)
    
    sub = sys.stdin.readline()
    sub = eval(sub)

    string = sys.stdin.readline()
    string = eval(string)

    index = sys.stdin.readline()
    index = eval(index)
    return term,var,sub,string,index

term,var,sub,string,index=read_from_stdin()

def apply_single_production_left():
    replace=None
    new_string=""
    for i in range(len(string)):
        if string[i]==' ':
            new_string+=string[i]
        elif string[i] not in term:
            replace=string[i]
            break
        else:
            new_string+=string[i]
    if replace ==None:
        return string
    list_value=sub.get(replace)
    new_string+=list_value[index]
    for k in range(i+1,len(string)):
        new_string+=string[k]
    return new_string

st=apply_single_production_left()
print(st)

