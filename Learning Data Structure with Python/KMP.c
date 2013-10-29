#include <stdio.h>

/*
SString是与算法相关的数据结构。
SString的0位，存储该字符串的长度。
其余存储该字符串的值。
*/
typedef char* SString;

/*============================================*/
/*与字符串相关的函数*/
/*============================================*/
/*计算给予的字符串S的长度*/
int strlen(char* S)
{
	int i=0;

	while(S[i]!='\0')
		i++;
	return i;
}
/*============================================*/
/*与算法相关的数据结构*/
/*============================================*/
/*
genSString(char* S)生成与算法相关的数据结构SString。
它将char *S转换为生成SString结构的字符串。
*/
SString genSString(char* S)
{
	int Slen=strlen(S);
	int i=0;
	SString s=(SString)malloc(sizeof(char)*(Slen+2));
	s[0]=Slen;
	
	//i=0
	while(S[i]!='\0')
	{
		s[i+1]=S[i];
		i++;
	}
	s[i+1]='\0';

	return s;
}
/*============================================*/
/*与算法相关的函数*/
/*============================================*/
int* getNext(SString S)
{
	int i=1;
	int j=0;
	int* next=(int *)malloc(sizeof(int)*((int)S[0]+1));
	next[0]=(int)S[0]+1;
	next[1]=0;
	
	//printf("%s,%d ",__FUNCTION__,next[0]);
	
	while(i<(int)S[0])
	{
		if(j==0||S[i]==S[j])
		{
			++i;
			++j;
			next[i]=j;
		}
		else
		{
			j=next[j];
		}
	}
	
	printf("\n");
	for(i=1;i<next[0];i++)
		printf("%d ",next[i]);
	printf("\n");
	return next;

}

int Index_KMP(SString S,SString T,int POS)
{
	int i=POS;
	int j=1;
	int *next=getNext(T);
	
	while(i<=S[0] && j<=T[0])
	{
		if(j==0||S[i]==T[j])
		{
			++i;
			++j;
		}
		else
		{
			j=next[j];
		}
	}
	
	if(j>T[0])
		return i-T[0];
	else
		return 0;
}

/*============================================*/
/*主函数*/
/*============================================*/
int main(int argc,char *argv[])
{
	char *s="ababcabdddabss";
	char *t="dddab";
	SString ss=NULL;
	SString st=NULL;
	
	ss=genSString(s);
	st=genSString(t);

	
	printf("%s:%s  %s",__FUNCTION__,ss,st);
	printf("%d",Index_KMP(ss,st,1));
	return 0;
}