//sec2-Halil-Avcı-22003476

#include "Cage.h"

Cage::Cage(string name, double probability) : 
    name(name), probability(probability), adjacentCageNumber(0) {
}

Cage::~Cage() {
    //default destructor
}

string Cage::getName() const {
    return name;
}

double Cage::getProbability() const {
    return probability;
}

SortedLinkedList<string>& Cage::getAdjacentCages() {
    return adjacentCages;
}

void Cage::addAdjacentCage(string cageName) {
    bool isAdded = false;
    for (int i = 1; i <= adjacentCageNumber; i++) {
        if (cageName < adjacentCages.getEntry(i) && !isAdded) {
            adjacentCages.insert(i, cageName);
            isAdded = true;
        }   
    }

    if (!isAdded) {
        adjacentCages.insert(adjacentCageNumber + 1, cageName);
    }

    adjacentCageNumber++;
}

void Cage::markVisited(bool isVisited) {
    visited = isVisited;
}

bool Cage::isVisited() {
    return visited;
}
