//sec2-Halil-Avcı-22003476

#ifndef ZOOMAP_H
#define ZOOMAP_H

#include "Cage.h"
#include "PathStack.h"
#include <fstream>
#include <iostream>
#include <string>
using namespace std;

class ZooMap {
public:
    ZooMap(const string cageFile, const string zooFile);
    ~ZooMap();
    void displayAllCages() const;
    void displayAdjacentCages(const string cageName) const;
    //void displayZooMap() const;
    //void findSafestPath(const string startCage, const string endCage);
    //void findMostDangerousPath(const string startCage, const string endCage);

private:
    SortedLinkedList<Cage> cageList;
    int noOfCages;
    PathStack pathStack;

    void addCage(string textLine);
    void addCagePath(string textLine);
    //void markVisited(string cageName);
    //void unvisitAllCages();
    //Cage getNextAdjacentCage(Cage fromCage);

};

#endif