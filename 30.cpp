#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int trapped(vector<int> emap){
	if(emap.size()<3)
		return 0;

	int total=0;
	int lmax=emap[0];
	int rmax=emap[emap.size()-1];
	int l=0;
	int r=emap.size()-1;

	while(l<r){
		if(emap[i-1]-emap[i]>=0 || emap[i+1]-emap[i] >=0)
			continue;
		temp = min(emap[i-1]-emap[i],emap[i+1]-emap[i]);
	}

	return total;
}


int main(){
	vector<int> list = {0,1,2,3,4};

	cout << trapped(list) << endl;
}
