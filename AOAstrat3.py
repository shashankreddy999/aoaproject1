from queue import PriorityQueue

class House:
    def __init__(self, startdate, enddate):
        self.startdate = startdate
        self.enddate = enddate
        self.duration = enddate - startdate
        self.painted = False

    def __lt__(self, other):
        return self.duration < other.duration


def strat3(n, houses):
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
            if li.index(x) not in res:
                #print(res)
                res.append(li.index(x))
                #print(res)

    
    return res
n,m=list(map(lambda x: int(x),input().split()))
house_list=[]
for i in range(m):
    start,end=list(map(lambda x: int(x),input().split()))
    h=(start,end)
    house_list.append(h)
li=strat3(n,house_list)
for i in li:
    print(i,end=" ")