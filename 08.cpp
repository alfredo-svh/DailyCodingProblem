/* 
	Problem:
	A unival tree (which stands for "universal value") is a tree where all nodes
	under it have the same value.
	Given the root to a binary tree, count the number of unival subtrees.
 */


#include <iostream>

using namespace std;


class Node{
public:
    Node(int Val=0, Node* Left=NULL, Node* Right=NULL){val=Val;left=Left;right=Right;}
    int val;
    Node* left;
    Node* right;
};

bool isUnival(Node* nd, int vl){
    if(nd==NULL)
        return true;
    
    if(isUnival(nd->left, vl) && isUnival(nd->right, vl) && nd->val==vl)
        return true;
        
    return false;
    
}

int count(Node* root){
    int cnt=0;
    
    if(root==NULL)
        return cnt;

    if(isUnival(root, root->val)){
        cnt++;
    }
    
    cnt+=count(root->left);
    cnt+=count(root->right);
        
    return cnt;
}


int main()
{
    //Node root(0, new Node(1), new Node(0, new Node(1, new Node(1), new Node(1)), new Node(0))); //5
    
    //Node root(1, new Node(1), new Node(1, new Node(1), new Node(1, NULL, new Node(0)))); //3
    
    Node root(1, new Node(3), new Node(2, new Node(2), new Node(2, NULL, new Node(2)))); //5
    
    cout<< count(&root)<<endl;

    return 0;
}