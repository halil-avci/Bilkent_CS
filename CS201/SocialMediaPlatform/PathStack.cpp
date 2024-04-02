//sec2-Halil-Avcı-22003476

#include "PathStack.h"

PathStack::PathStack() : topPtr(nullptr) {
}

PathStack::PathStack(const PathStack& aStack) {
    Node<Cage>* origChainPtr = aStack.topPtr;
    if (origChainPtr == nullptr) {
        topPtr = nullptr;
    }
    else {
        topPtr = new Node<Cage>(origChainPtr->getItem());

        Node<Cage>* newChainPtr = topPtr;
        origChainPtr = origChainPtr->getNext();

        while (origChainPtr != nullptr) {
            Cage nextCage = origChainPtr->getItem();
            Node<Cage>* newNodePtr = new Node<Cage>(nextCage);
            newChainPtr->setNext(newNodePtr);
            newChainPtr = newChainPtr->getNext();
            origChainPtr = origChainPtr->getNext();
        }
        newChainPtr->setNext(nullptr);
    }
}

PathStack::~PathStack() {
    while(!isEmpty()) {
        pop();
    }
}

bool PathStack::push(const Cage& newCage) {
    Node<Cage>* newNodePtr = new Node<Cage>(newCage, topPtr);
    topPtr = newNodePtr;
    newNodePtr = nullptr;
    return true;
}

bool PathStack::pop() {
    bool result = false;
    if (!isEmpty()) {
        Node<Cage>* nodeToDeletePtr = topPtr;
        topPtr = topPtr->getNext();

        nodeToDeletePtr->setNext(nullptr);
        delete nodeToDeletePtr;
        nodeToDeletePtr = nullptr;

        result = true;
    }

    return result;
}

Cage& PathStack::peek() {
        return topPtr->getItemReference();
}

bool PathStack::isEmpty() const {
    return topPtr == nullptr;
}