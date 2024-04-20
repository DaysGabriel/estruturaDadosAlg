#ifndef BST_HPP
#define BST_HPP

#include "node.hpp"

template <typename myType>

class BST
{
private:
    Node<myType>* root;
public:
    BST(myType info)
    {
        root = new Node<myType>(info);
    }
    BST(Node<myType>* node=nullptr)
    {
        root = node;
    }
};

#endif
