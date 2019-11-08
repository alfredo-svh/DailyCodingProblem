#include <iostream>

using namespace std;

class Node{
public:
    Node(string Val, Node* Left=NULL, Node* Right=NULL){val=Val;left=Left;right=Right;}
    
    string val;
    Node* left;
    Node* right;
};

string serialize(Node* root){
    if(root==NULL)
        return "";
    
    return root->val +" "+ serialize(root->left) + " " +serialize(root->right);
    
}

Node *deserialize(string s){
    Node *tree;
    int i=0;
    string s2;
    
    while(s[i]!=" "){
        i++;
    }
    
    tree.val = s2(s, s.begin(), s.begin()+i);
    
    if()
        tree.left = deserialize(s2(s, s.begin()+i, s.end()));
    if()
        tree.right = deserialize(s2(s, s.begin()+i, s.end()));
    
    return tree;
}

int main()
{
    Node node = Node("root", new Node("left", new Node("left.left")), new Node("right"));
    
    cout << serialize(&node)<<endl;

    return 0;
}