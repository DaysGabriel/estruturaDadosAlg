#ifndef BST_HPP
#define BST_HPP

#include "node.hpp"

class BST
{
private:
    Node* root;
public:
    BST(int _info);
    //Various versions of the insert method
    insert(int _info, Node* &root);
    insert(int _info, Node** root);
    insertPrivate(int _info);
private:
    _insertPrivate(int _info, Node* root);
};

#endif