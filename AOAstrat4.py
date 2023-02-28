from queue import PriorityQueue

class House:
    def __init__(self, startdate, enddate):
        self.startdate = startdate
        self.enddate = enddate
        self.painted = False

    def __lt__(self, other): #overriding less than method
        return self.enddate <= other.enddate


def strat4(n, houses): #implementing strat4
    li = [House(h[0], h[1]) for h in houses]
    Q = PriorityQueue()
    res = []
    
    for c in range(1, n+1):
        #print(c)
        while not Q.empty() and Q.queue[0].enddate < c:
            #print('xxx')
            Q.get()
            
        for h in li:
            if not h.painted and h.startdate <= c and h.enddate >= c:
                Q.put(h)
                
        if not Q.empty():
            #print('a')
            x = Q.get()
            x.painted = True
            #print(x.startdate,x.enddate)
            if li.index(x) not in res:
                res.append(li.index(x))

    
    return res

n,m=list(map(lambda x: int(x),input().split()))
house_list=[]
for i in range(m): #taking input
    start,end=list(map(lambda x: int(x),input().split()))
    h=(start,end)
    house_list.append(h)
li=strat4(n,house_list)
for i in li:
    print(i,end=" ")