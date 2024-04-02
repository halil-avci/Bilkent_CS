
#include "ZooMap.h"

int main() {
ZooMap zm("cage.txt", "zoo.txt");
zm.displayAllCages();
cout << endl;
zm.displayAdjacentCages("E");
cout << endl;
zm.displayAdjacentCages("C");
cout << endl;
/*
zm.displayZooMap();
cout << endl;
zm.findSafestPath("E", "A");
cout << endl;
zm.findSafestPath("D", "C");
cout << endl;
zm.findMostDangerousPath("E", "A");
cout << endl;
zm.findMostDangerousPath("D", "C");
cout << endl;
zm.findMostDangerousPath("C", "F"); */
return 0;
}