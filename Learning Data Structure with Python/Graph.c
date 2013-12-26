#include <stdio.h>

#define MaxSize 20

typedef struct EdgeNode
{
	int vexName;
	struct EdgeNode *next;
}EdgeNode;

typedef struct VexNode
{
	int data;
	struct EdgeNode *first;
}VexList[MaxSize];

typedef struct Graph
{
	VexList vexlist;
	int vexNum,edgeNum;
}Graph;

int CreateGraph(Graph *G)
{
	int i,j,k;
	EdgeNode *ePtr;
	EdgeNode *e;
	G->vexNum=5;
	G->edgeNum=5;
	
	//给图G的顶点列表初始化。
	for(i=0;i<G->vexNum;i++)
	{
		G->vexlist[i].data=i;
		G->vexlist[i].first=NULL;
	}
	
	ePtr=G->vexlist[0].first;//将边指针指向0号顶点的第一条边
	
	//建立vexNum-1个边节点与0号顶点连接。
	for(j=1;j<G->edgeNum;j++)
	{
		
		
		e=(EdgeNode *)malloc(sizeof(EdgeNode));
		e->vexName=j;
		
		while(ePtr!=NULL)
		{
			ePtr=ePtr->next;
		}
		
		ePtr=e;
	}
	
	ePtr=G->vexlist[1].first;
	e=(EdgeNode *)malloc(sizeof(EdgeNode));
	e->vexName=3;
	ePtr=e;
	
	return 0;
}
//======================================================
int Visit(Graph *G,int vex)
{
	printf("->%d",G->vexlist[vex].data);
	return 0;
}

int Visited[5]={0,0,0,0,0};
int DFS(Graph *G,int vex)
{
	EdgeNode *e;
	Visited[vex]=1;
	Visit(G,vex);
	
	e=G->vexlist[vex].first;
	
	while(e!=NULL)
	{
		if(Visited[e->vexName]==0)
			DFS(G,e->vexName);
		e=e->next;
	}
	
	return 0;
}

int main(int argc,char *argv[])
{
	Graph G;
	CreateGraph(&G);
	DFS(&G,0);
	return 0;
}