
#creation of heap
class MaxHeap():


    def add(self,e):
        self.data.append(e)
        self.heap_up(len(self.data)-1)
            
    def heap_up(self,k):
    
        while k>0:
            if self.data[k]> self.data[(k-1)//2]:
                self.data[k],self.data[(k-1)//2]=self.data[(k-1)//2],self.data[k]
                k=(k-1)//2
            else:
                break


        #     else:
        #         return(self)

        # return(self)

    def heap_down(self,k):
        while 2*k+2<len(self.data) :
           
            if self.data[2*k+1]<=self.data[2*k+2]:
                if self.data[k]<self.data[2*k+2]:
                    self.data[k],self.data[2*k+2]=self.data[2*k+2],self.data[k]
                    k=2*k+2
                else:
                    break
            else:
                if self.data[k]<self.data[2*k+1]:
                    self.data[k],self.data[2*k+1]=self.data[2*k+1],self.data[k]
                    k=2*k+1
                else:
                    break

            
        while 2*k+2 == len(self.data) :
            if self.data[k]<self.data[2*k+1]:
                self.data[k],self.data[2*k+1]=self.data[2*k+1],self.data[k]
                k=2*k+1
            else:
                break

        

    def know_max(self):
        return self.data[0]
    def extract_max(self):
        if len(self.data)!=1:
            ans=self.data[0]
            u=self.data.pop()
            self.data[0]=u
            self.heap_down(0)
        else:
            ans=self.data[0]
            self.data.pop()

    
        return ans
  
    def __init__(self):
        self.data =[]
    

def findMaxCapacity(n,links,s,t):
    neighbour_list=[]
    for  i in range (0,n):
        neighbour_list.append([])
    for i in range(len(links)):
            neighbour_list[links[i][0]].append((links[i][1],links[i][2]))
            neighbour_list[links[i][1]].append((links[i][0],links[i][2]))
    
    capacity=[]
    path_trace=[]
    place_in_heap=[]
    for i in range (n):
        capacity.append(-1)
        path_trace.append(None)
        place_in_heap.append(1)
    HeapList=MaxHeap()
    capacity[s]=0
    HeapList.add((capacity[s],s))

    while HeapList.know_max()[1] != t:
            (cap,out) = HeapList.extract_max()
           
            place_in_heap[out]=0      
        
            for i in range (0,len(neighbour_list[out])):
                
                if out == s:
                    
                    if place_in_heap[neighbour_list[out][i][0]] ==1:
                        if capacity[neighbour_list[out][i][0]]<neighbour_list[out][i][1] :
                            capacity[neighbour_list[out][i][0]]= neighbour_list[out][i][1]
                            path_trace[neighbour_list[out][i][0]] = out
                            HeapList.add((neighbour_list[out][i][1],neighbour_list[out][i][0]))
                        

                else:
                        
                        if place_in_heap[neighbour_list[out][i][0]] ==1:
                            k = min(cap,neighbour_list[out][i][1])
                            if k> capacity[neighbour_list[out][i][0]] :
                
                                capacity[neighbour_list[out][i][0]]  = k
                                path_trace[neighbour_list[out][i][0]] = out
                                HeapList.add((k,neighbour_list[out][i][0]))
    
    j=t
    
    path=[]
    while True :
        path.append(j)
        j=path_trace[j]
        if j==s:
            path.append(j)
            break

    real_path =[]
    for i in range ((len(path)-1),-1,-1):
        real_path.append(path[i])
    
    return (capacity[t],real_path)



