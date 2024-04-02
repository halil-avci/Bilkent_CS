//sec2-Halil-Avcı-22003476

#ifndef PATHSTACK_H
#define PATHSTACK_H

#include "Node.h"
#include "Cage.h"

class PathStack {
public:
    PathStack();
    PathStack(const PathStack& aStack);
    ~PathStack();

    bool isEmpty() const;
    bool push(const Cage& newCage);
    bool pop();
    Cage& peek();

private:
    Node<Cage>* topPtr;
};

#endif