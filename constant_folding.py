import re
def constant_folding(filename):
    f=open(filename,'r+')
    
    s="([a-z]|[A-Z]|_)+([a-z]|[A-Z]|_|\d)*=\d+$|([a-z]|[A-Z]|_)+([a-z]|[A-Z]|_|\d)*=\"\w+\"$|([a-z]|[A-Z]|_)+([a-z]|[A-Z]|_|\d)*=\'\w+\'$"
    s=re.compile(s)
    #line nums
    ln=[]
    assign=[]
    for line_i, line in enumerate(f, 1):
            # check if we have a regex match
            if s.search(line):
                # if so, note down line number 
                ln.append(line_i)
                assign.append(line[:-1])
    print("Assingments( line no) | lhs | rhs")
    for i in range(0,len(ln)):
        a=assign[i].split('=')
        lhs=a[0]
        rhs=a[1]
        print(ln[i],lhs,rhs)
        identifier="\w=((\w+|\d+)(\+|\-|\*|\/|\^))*"+lhs+"((\+|\-|\*|\/|\^)(\w+|\d+))*$"
        identifier=re.compile(identifier)
        f.seek(0)
        line=f.readlines()
        before=re.compile("(=|\+|\-|\*|\/|\^)+"+lhs+"[^\w]((\+|\-|\*|\/|\^)){0,1}")
        after=re.compile("(=|\+|\-|\*|\/|\^)+"+rhs+"[^\w]((\+|\-|\*|\/|\^)){0,1}")
        for j in range(ln[i],line_i):
            if re.match(s,line[j]):
                if line[j].split('=')[0]==lhs:
                    break
            if re.match(identifier,line[j]):
                print("Reuse",lhs,"at line number",j+1)
                #h=re.sub(before,after,line[j])  
    
    f.close()
constant_folding('test.py')