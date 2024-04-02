//sec2-Halil-Avcı-22003476

#include "ZooMap.h"

ZooMap::ZooMap(const string cageFile, const string zooFile) : noOfCages(0) {
    ifstream fileCages(cageFile);
    string strLine;
    while (getline(fileCages, strLine)) {
        addCage(strLine);
    }

    ifstream fileZoo(zooFile);
    while (getline(fileZoo, strLine)) {
        addCagePath(strLine);
    }
}

ZooMap::~ZooMap() {
    //default destructor
}

void ZooMap::displayAllCages() const {
    cout << "The cages in the zoo are:" << endl;

    for (int i = 1; i <= noOfCages; i++) {
        if (i != 1) {
            cout << " ";
        }
        cout << cageList.getEntryReference(i).getName() << ",";
    }

    cout << endl;
}

void ZooMap::displayAdjacentCages(const string cageName) const {
    cout << "The cages adjacent to " << cageName << " are:" << endl;
    cout << cageName << " ->";

    for (int i = 1; i <= noOfCages; i++) {
        if (cageName == cageList.getEntryReference(i).getName()) {
            SortedLinkedList<string>& adjacentCageList = cageList.getEntryReference(i).getAdjacentCages();

            for (int i = 1; i <= adjacentCageList.getLength(); i++) {
                if (i != 1) {
                    cout << " ";
                }
                cout << adjacentCageList.getEntryReference(i) << ",";
            }
        }
    }

    cout << endl;
}

void ZooMap::addCage(string line) {
    string cageName;
    cageName = line[0];
    string strPorbability;
    strPorbability = line.substr(2, 4);
    double probability = stod(strPorbability);
    Cage newCage(cageName, probability);

    bool isAdded = false;
    for (int i = 1; i <= noOfCages; i++) {
        if (cageName < cageList.getEntryReference(i).getName() && !isAdded) {
            cageList.insert(i, newCage);
            isAdded = true;
        }   
    }

    if (!isAdded) {
        cageList.insert(noOfCages + 1, newCage);
    }

    noOfCages++;
}

void ZooMap::addCagePath(string line) {
    string cageFrom;
    cageFrom  = line[0];
    string cageTo;
    cageTo = line[2];

    for (int i = 1; i <= noOfCages; i++) {
        if (cageFrom == cageList.getEntryReference(i).getName()) {
            cageList.getEntryReference(i).addAdjacentCage(cageTo);
        }
    }
}