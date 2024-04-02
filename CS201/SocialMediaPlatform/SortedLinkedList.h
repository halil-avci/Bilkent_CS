//sec2-Halil-Avcı-22003476

#ifndef SORTED_LINKED_LIST_H
#define SORTED_LINKED_LIST_H
#include "Node.h"
#include <string>

template<class Type>
class SortedLinkedList {

private:
    Node<Type>* headPtr;
    int itemCount;
    Node<Type>* getNodeAt(int pos) const;

public:
    SortedLinkedList();
    ~SortedLinkedList();

    bool isEmpty() const;
    int getLength() const;
    bool insert(int newPosition, const Type& newEntry);
    bool remove(int position);
    void clear();
    Type getEntry(int position) const;
    Type& getEntryReference(int position) const;
};

using namespace std;

template<class Type>
SortedLinkedList<Type>::SortedLinkedList() : headPtr(nullptr), itemCount(0) {
}

template<class Type>
SortedLinkedList<Type>::~SortedLinkedList() {
    clear();
}

template<class Type>
Type SortedLinkedList<Type>::getEntry(int position) const {
    bool ableToGet = (position >= 1) && (position <= itemCount);
    if (ableToGet) {
        Node<Type>* nodePtr = getNodeAt(position);
        return nodePtr->getItem();
    }
}

template<class Type>
Type& SortedLinkedList<Type>::getEntryReference(int position) const {
    bool ableToGet = (position >= 1) && (position <= itemCount);
    if (ableToGet) {
        Node<Type>* nodePtr = getNodeAt(position);
        return nodePtr->getItemReference();
    }
}

template<class Type>
Node<Type>* SortedLinkedList<Type>::getNodeAt(int position) const {
    Node<Type>* curPtr = headPtr;
    for (int skip = 1; skip < position; skip++)
        curPtr = curPtr->getNext();
    
    return curPtr;
}

template<class Type>
bool SortedLinkedList<Type>::insert(int newPosition, const Type& newEntry) {
    bool ableToInsert = (newPosition >= 1) && (newPosition <= itemCount + 1);
    if (ableToInsert) {
        Node<Type>* newNodePtr = new Node<Type>(newEntry);

        if (newPosition == 1) {
            newNodePtr->setNext(headPtr);
            headPtr = newNodePtr;
        }
        else {
            Node<Type>* prevPtr = getNodeAt(newPosition - 1);

            newNodePtr->setNext(prevPtr->getNext());
            prevPtr->setNext(newNodePtr);
        }

        itemCount++;
    }

    return ableToInsert;
}

template<class Type>
bool SortedLinkedList<Type>::remove(int position) {
    bool ableToRemove = (position >= 1) && (position <= itemCount);
    if (ableToRemove) {
        Node<Type>* curPtr = nullptr;
        if (position == 1) {
            curPtr = headPtr;
            headPtr = headPtr->getNext();
        }
        else {
            Node<Type>* prevPtr = getNodeAt(position - 1);
            curPtr = prevPtr->getNext();
            prevPtr->setNext(curPtr->getNext());
        }

        curPtr->setNext(nullptr);
        delete curPtr;
        curPtr = nullptr;

        itemCount--;
    }

    return ableToRemove;
}

template<class Type>
void SortedLinkedList<Type>::clear() {
    while (!isEmpty())
    remove(1);
}

template<class Type>
bool SortedLinkedList<Type>::isEmpty() const {
    if (itemCount == 0) {
        return true;
    }
    return false;
}

template<class Type>
int SortedLinkedList<Type>::getLength() const {
    return itemCount;
}
#endif