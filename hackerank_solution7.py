if __name__ == '__main__':
    N = int(input())
    lists=[]
    for i in range(N):
        name,*line=input().split()
        scores=list(map(int,line))
        if(name=="insert"):
            a,b=scores[0],scores[1]
            lists.insert(a,b)
        if(name=="print"):
            print(lists)
        if(name=="sort"):
            lists.sort()
        if(name=="reverse"):
            lists.reverse()
        if(name=="pop"):
            lists.pop()
        if(name=="append"):
            a=scores[0]
            lists.append(a)
        if(name=="remove"):
            a=scores[0]
            lists.remove(a)

            
