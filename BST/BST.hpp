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
    void insert(myType info)
    {
        root = _insert(info, root);
    }

private:
    Node<myType>* _insert(myType info, Node<myType>*node)
    {
        if (node == nullptr)
            node = new Node(info);
        else if (info > node->info)
            node->right = _insert(info, node->right);
        else
            node->left = _insert(info, node->left);
        return node;
    }
};

#endif
