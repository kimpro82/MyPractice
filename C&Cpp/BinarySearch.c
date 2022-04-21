#include <stdio.h>
#include <stdlib.h>                             // malloc()


typedef struct _tNode                           // It makes using struct easier to declare it with typedef
{
    int value;
    struct _tNode* left;                        // Node* left : why does it not work?
    struct _tNode* right;                       // should be declared as a pointer
} Node;


Node* insert(Node* root, int value)             // The location of '*' doesn't matter
{
    if (root == NULL)
    {
        Node* root = malloc(sizeof(Node));      // malloc : instead of `new` in C++
        root->value = value;
        root->left = NULL;
        root->right = NULL;

        return root;
    }
    else
    {
        if (root->value > value) root->left = insert(root->left, value);
        else root->right = insert(root->right, value);
    }

    return root;
}

Node* delete(Node* root, int value) 
{
    if (root == NULL) return root;

    if (root->value > value) root->left = delete(root->left, value);
    else if (root->value < value) root->right = delete(root->right, value);
    else
    {
        // ing~~~
    }

    return root;
}


void preOrder(Node* root)
{
    if (root == NULL) return;

    printf("%d ", root->value);
    preOrder(root->left);
    preOrder(root->right);
}

void inOrder(Node* root)
{
    if (root == NULL) return;

    inOrder(root->left);
    printf("%d ", root->value);
    inOrder(root->right);
}

void postOrder(Node* root)
{
    if (root == NULL) return;

    postOrder(root->left);
    postOrder(root->right);
    printf("%d ", root->value);
}


int main()
{
    Node* root = NULL;

    int arr[6] = {6, 3, 4, 7, 13, 10};
    int len = sizeof(arr) / sizeof(int);
    for (int i = 0; i < len; i++) root = insert(root, arr[i]);

    printf("Preorder traversal : ");
    preOrder(root);
    putchar('\n');

    printf("Inorder traversal : ");
    inOrder(root);
    putchar('\n');

    printf("Postorder traversal : ");
    postOrder(root);
    putchar('\n');

    return 0;
}