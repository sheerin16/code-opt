import re
def constant_folding(filename):
    f=open(filename,'r+')
    s="for ([a-z]|[A-Z]|_)+([a-z]|[A-Z]|_|\d)* in ([a-z]|[A-Z]|_)+([a-z]|[A-Z]|_|\d)*|range\((\d+|len\(([a-z]|[A-Z]|_)+([a-z]|[A-Z]|_|\d)*\))\):$"
    s=re.compile(s)
    #line numbers
    l=[]
    forloops=[]
    print("For Loops\nLine# | Limit | Data Structure")

    for line_i, line in enumerate(f, 1):
            # check if we have a regex match
            if s.search(line):
                # if so, note down line number
                if line[:-1].split(' ')[3][:5]=="range":
                    print(line_i,"\t",(line[:-1].split(' ')[3][6:-2]),"\t ")
                else:
                    print(line_i,"\t\t",(line[:-1].split(' ')[3][:-1]))
    
    f.close()
constant_folding('test.py')