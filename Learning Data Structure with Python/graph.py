# -*- coding: cp936 -*-
'''
��pythoʵ��ͼ�ĳ����㷨
'''
import random
import copy

MaxLen=10000#MaxLen��ʾ���ɵ���ĵ�
visited=[]#����һ���б����洢�Ѿ����ʵĶ���

class Graph:
    def __init__(self):
        '''��ʼ��Graph������Graph�Ķ�����Ϊ0���ڽӾ���Ϊ��'''
        self.vexnum=0
        self.graph=[]
        
    def getRandGraph(self,size):
        '''�õ�һ�����ͼ'''
        choice=[111,211,311,411,511,MaxLen]
        self.vexnum=size
        for i in range(size):
            lst=[x for x in range(size)]
            for j in range(1,size):
                lst[j]=random.choice(choice)
            lst[0],lst[i]=lst[i],lst[0]
            self.graph.append(copy.deepcopy(lst))
            
    def visit(self,i):
        '''��������Ϊi�Ľڵ㲢��ӡ'''
        adjustLst=["G"+str(x) for x in range(self.vexnum)]
        print adjustLst[i],
        
    def VexConnect(self,v):
        '''������V������ӵ����н��'''
        for x in range(self.vexnum):
           if self.graph[v][x]!=0 and self.graph[v][x]!=MaxLen:
               yield x
               
    def __str__(self):
        '''��ӡͼ�Ľڵ������ڽӾ���'''
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
    '''��ȱ����ĵݹ麯��'''
    visited[v]=True
    G.visit(v)
    VConnect=G.VexConnect(v)#��ö���V���ӵ����ж���
    for i in VConnect:
        if visited[i]!=True:
            DFS(G,i)
        
def DFSTraverse(G):
    '''ͼ����ȱ���'''
    global visited
    visited=[False for i in range(G.vexnum)]#��ʼ���ѷ��ʵ�����
    
    for i in range(G.vexnum):
        if visited[i]!=True:
            DFS(G,i)

def BFSTraverse(G):
    '''ͼ�Ĺ�ȱ���'''
    global visited
    visited=[False for i in range(G.vexnum)]#��ʼ���ѷ��ʵ�����
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
    lowcost=[x for x in G.graph[root]]#��ʼ�����Ȩֵ�б�
    lowcost[root]=0#��root�ڵ���ΪU���϶���,�����0�ڵ�ΪV-U���ϵĶ���
    VexLst=[root for x in range(G.vexnum)]#��ʼ����̶����ַ�б�
    result=[]#��ʼ��������������

    def minmun(lowcost):
        '''��V-U�����еõ���U����·����̵ĵ�'''
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
        '''��ӡ���'''
        total=0
        print ''
        print 'Root:%d'%root
        for r in result:
            total+=r[2]
            print "%d --> %d weight:%d"%r
        print "Total:%d"%(total)
        print ''

    for i in range(1,G.vexnum):
        min=minmun(lowcost)#��V-U�����еõ���U����·����̵ĵ�
        result.append((VexLst[min],min,lowcost[min]))#���������
        lowcost[min]=0#����V-U�����еõ���U����·����̵ĵ���ΪU���ϵĵ�
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


    
    
    
