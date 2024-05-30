#include <iostream>
#include <vector>
#include <random>
#include <time.h>
using namespace std;
vector<int> a[9];
bool vis[20000];
int main(){
	srand(time(NULL));
	freopen("data_10552.txt","r",stdin);
	int n,lv,r;
	cin>>n;
	for (int i=1000;i<=n;i++) {	
		cin>>lv;
		a[lv].push_back(i);
	}
	freopen("CON","r",stdin);
	cout<<"欢迎使用洛谷挑题机，请输入您想要的难度与数量\n0:入门\n1：普及-\n2:普及提高-\n3:普及+提高\n4:提高+省选-\n5:省选NOI-\n6:NOI\n7:暂无评定\n8:其他（无权访问）\n";
	cout<<"例：输入0 5表示挑选5道入门题"<<endl;
	cin>>lv>>n;
	while (n--){
		r=rand()%a[lv].size();
		while (vis[a[lv][r]]) r=rand()%a[lv].size();
		cout<<"P"<<a[lv][r]<<endl;
		vis[a[lv][r]]=1;
	}
	return 0;
}
