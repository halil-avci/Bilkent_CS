//sec2-Halil-Avcı-22003476

#ifndef CAGE_H
#define CAGE_H

#include <string>
#include "SortedLinkedList.h"

class Cage {
public:
    Cage(string name, double probability);
    ~Cage();

    string getName() const;
    SortedLinkedList<string>& getAdjacentCages();
    double getProbability() const;
    void addAdjacentCage(string cageName);
    void markVisited(bool isVisited);
    bool isVisited();

private:
    string name;
    SortedLinkedList<string> adjacentCages;
    double probability;
    int adjacentCageNumber;
    bool visited;
};

#endif