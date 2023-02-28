class House:
  def __init__(self,startdate,enddate):
    self.startdate=startdate
    self.enddate=enddate
    self.painted=False

def strat1(n,house_list): #strat1 implementation
  m=0
  res={} # res is resultant dict with day and house just to check
  li=[] #li is resultant list
  c=1
  while c<=n and m<len(house_list):
    #print(c)
    if house_list[m].startdate<=c and house_list[m].enddate>=c and house_list[m].painted==False:
      #print(c,m)
      res[c]=m
      li.append(m)
      house_list[m].painted=True
      m=m+1
      c=c+1
    elif house_list[m].startdate>c and house_list[m].enddate>=c and house_list[m].painted==False:
      c=house_list[m].startdate
    else:
      m=m+1
  #print(res)
  #print(len(res))
  return li

n,m=list(map(lambda x: int(x),input().split()))
house_list=[]
for i in range(m): #taking input
    start,end=list(map(lambda x: int(x),input().split()))
    h=House(start,end)
    house_list.append(h)
li=strat1(n,house_list)
for i in li:
    print(i,end=" ")