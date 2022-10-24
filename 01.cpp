#include <iostream>
#include <vector>
#include <set>

using namespace std;

bool addUp(vector<int> arr, int k){
	set<int> needed;

	for(int i=0;i<arr.size();i++){
		if(needed.find(arr[i]) != needed.end()){
			needed.insert(k-arr[i]);
		}
		else{ 
			return true;
		}
	}

	return false;
}

int main(){
	vector<int> in ={10,15,3,7};

	if(addUp(in, 17))
	    cout << "true"<<endl;
	else
	    cout << "false"<<endl;

	return 0;
}