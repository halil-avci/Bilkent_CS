//sec2-Halil-Avcı-22003476

#ifndef USER_H
#define USER_H

#include <string>
using namespace std;

class User {

private:
    int id;
    string name;

public:
    User(int anId, string aName);

    int getId() const;
    string getName() const;
};

#endif