from queue import PriorityQueue

class House:
    def __init__(self, startdate, enddate, idx):
        self.startdate = startdate
        self.enddate = enddate
        self.painted = False
        self.idx = idx
        
    def __lt__(self, other): #less than override
        return self.enddate <= other.enddate

def strat5(n, m, houses): #implementing strat 5
    li = [House(h[0], h[1], i) for i, h in enumerate(houses)]
    Q = PriorityQueue()
    res = []
    c = 1

    while len(res) < m:
        if c>n:
          break
        print(c)
        while not Q.empty() and Q.queue[0].enddate < c:
            x = Q.get()
            if x.painted and x.idx not in res:
                res.append(x.idx)

        while i + 1 < m and li[i+1].startdate <= c:
            i += 1
            Q.put(li[i])

        if not Q.empty():
            x = Q.get()
            x.painted = True
            if x.idx not in res:
                res.append(x.idx)

        if c<=m:
            c += 1

    return res

n,m=list(map(lambda x: int(x),input().split()))
house_list=[]
for i in range(m): #taking input
    start,end=list(map(lambda x: int(x),input().split()))
    h=(start,end)
    house_list.append(h)
li=strat5(n,m,house_list)
for i in li:
    print(i,end=" ")