#include "BST.hpp"

BST::BST(int _info)
{
    root = new Node(_info);
}

void BST::insert(int _info, Node* &root)
{
    if (root == nullptr)
        root = new Node(_info);
    else if (_info > root->info)
        insert(_info, root->right);
    else
        insert(_info, root->left);
}

void BST::insert(int _info, Node** root)
{
    if (*root == nullptr)
        *root = new Node(_info);
    else if (_info > (*root)->info)
        insert(_info, &(*root)->right);
    else
        insert(_info, &(*root)->left);
}

void BST::insertPrivate(int _info)
{
    root = _insertPrivate(_info, root);
}

Node* BST::_insertPrivate(int _info, Node* root)
{
    if (root == nullptr)
        root = new Node(_info);
    else if (_info > root->info)
        root->right = _insertPrivate(_info, root->right);
    else
        root->left = _insertPrivate(_info, root->left);
    return root;
}