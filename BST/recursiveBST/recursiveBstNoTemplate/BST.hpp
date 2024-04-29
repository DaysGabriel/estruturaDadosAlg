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
    void insert(int _info, Node* &root);
    void insert(int _info, Node** root);
    void insertPrivate(int _info);
private:
    Node* _insertPrivate(int _info, Node* root);
};

#endif