# -*- coding: cp936 -*-
'''
用pytho实现图的常用算法
'''
import random
import copy

MaxLen=10000#MaxLen表示不可到达的点
visited=[]#定义一个列表来存储已经访问的顶点

class Graph:
    def __init__(self):
        '''初始化Graph，其中Graph的顶点数为0，邻接矩阵为空'''
        self.vexnum=0
        self.graph=[]
        
    def getRandGraph(self,size):
        '''得到一个随机图'''
        choice=[111,211,311,411,511,MaxLen]
        self.vexnum=size
        for i in range(size):
            lst=[x for x in range(size)]
            for j in range(1,size):
                lst[j]=random.choice(choice)
            lst[0],lst[i]=lst[i],lst[0]
            self.graph.append(copy.deepcopy(lst))
            
    def visit(self,i):
        '''访问索引为i的节点并打印'''
        adjustLst=["G"+str(x) for x in range(self.vexnum)]
        print adjustLst[i],
        
    def VexConnect(self,v):
        '''返回与V结点连接的所有结点'''
        for x in range(self.vexnum):
           if self.graph[v][x]!=0 and self.graph[v][x]!=MaxLen:
               yield x
               
    def __str__(self):
        '''打印图的节点数和邻接矩阵'''
        print "The Graph vexnum:",self.vexnum
        print "The Graph Matrix:"
        for i in range(self.vexnum):
            for j in range(self.vexnum):
                if self.graph[i][j]!=MaxLen and self.graph[i][j]!=0:
                    print self.graph[i][j],
                elif self.graph[i][j]==0:
                    print "000",
                else:
                    print "Max",
            print 
        return ""

def DFS(G,v):
    '''深度遍历的递归函数'''
    visited[v]=True
    G.visit(v)
    VConnect=G.VexConnect(v)#获得顶点V连接的所有顶点
    for i in VConnect:
        if visited[i]!=True:
            DFS(G,i)
        
def DFSTraverse(G):
    '''图的深度遍历'''
    global visited
    visited=[False for i in range(G.vexnum)]#初始化已访问的数组
    
    for i in range(G.vexnum):
        if visited[i]!=True:
            DFS(G,i)

def BFSTraverse(G):
    '''图的广度遍历'''
    global visited
    visited=[False for i in range(G.vexnum)]#初始化已访问的数组
    for i in range(G.vexnum):
        if visited[i]!=True:
            visited[i]=True
            G.visit(i)
        Queue=[i]
        for Qe in Queue:
            if visited[Qe]!=True:
                visited[Qe]=True
                G.visit(Qe)
            VConnect=G.VexConnect(Qe)
            for j in VConnect:
                if visited[j]!=True:
                    Queue.append(j)

def prim(G,root):    
    lowcost=[x for x in G.graph[root]]#初始化最低权值列表
    lowcost[root]=0#将root节点标记为U集合顶点,其余非0节点为V-U集合的顶点
    VexLst=[root for x in range(G.vexnum)]#初始化最短顶点地址列表
    result=[]#初始化保存结果的数组

    def minmun(lowcost):
        '''从V-U集合中得到与U集合路径最短的点'''
        min_index=0
        min_value=MaxLen
        for x in range(G.vexnum):
            if lowcost[x]==0 or lowcost[x]==MaxLen:
                continue
            elif lowcost[x]<min_value:
                min_index=x
                min_value=lowcost[x]
        return min_index

    def PrintResult(result):
        '''打印结果'''
        total=0
        print ''
        print 'Root:%d'%root
        for r in result:
            total+=r[2]
            print "%d --> %d weight:%d"%r
        print "Total:%d"%(total)
        print ''

    for i in range(1,G.vexnum):
        min=minmun(lowcost)#从V-U集合中得到与U集合路径最短的点
        result.append((VexLst[min],min,lowcost[min]))#将结果保存
        lowcost[min]=0#将从V-U集合中得到与U集合路径最短的点标记为U集合的点
        for j in range(0,G.vexnum):
            if lowcost[j]!=0 and G.graph[min][j]<lowcost[j]:
                lowcost[j]=G.graph[min][j]
                VexLst[j]=min
    PrintResult(result)
    return result

if __name__=="__main__":
    g=Graph()
    g.getRandGraph(5)
    print g
    #print visited
    DFSTraverse(g)
    print ''
    BFSTraverse(g)
    print ''
    print ''
    for x in range(g.vexnum):
        prim(g,x)


    
    
    
