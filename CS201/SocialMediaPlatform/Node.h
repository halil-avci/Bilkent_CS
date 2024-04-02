//sec2-Halil-Avcı-22003476

#ifndef NODE_H
#define NODE_H

template<class Type>
class Node {

private:
    Type item;
    Node<Type>* next;

public:
    Node(const Type& anItem);
    Node(const Type& anItem, Node<Type>* nextNodePtr);
    void setItem(const Type& anItem);
    void setNext(Node<Type>* nextNodePtr);
    Type getItem() const;
    Type& getItemReference();
    Node<Type>* getNext() const;
};

#include <cstddef>

template<class Type>
Node<Type>::Node(const Type& anItem) : item(anItem), next(nullptr) 
{}

template<class Type>
Node<Type>::Node(const Type& anItem, Node<Type>* nextNodePtr) : 
                    item(anItem), next(nextNodePtr)
{}

template<class Type>
void Node<Type>::setItem(const Type& anItem) {
    item = anItem;
}

template<class Type>
void Node<Type>::setNext(Node<Type>* nextNodePtr) {
    next = nextNodePtr;
}

template<class Type>
Type Node<Type>::getItem() const {
    return item;
}

template<class Type>
Type& Node<Type>::getItemReference() {
    return item;
}

template<class Type>
Node<Type>* Node<Type>::getNext() const {
    return next;
}

#endif