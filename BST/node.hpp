#ifndef NODE_HPP
#define NODE_HPP

template <typename myType>

class Node
{
private:
    myType info;
    Node<myType>* left;
    Node<myType>* right;
public:
    Node(myType _info): info(_info), left(nullptr), right(nullptr); 
};

#endif
