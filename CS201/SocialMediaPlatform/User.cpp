//sec2-Halil-Avcı-22003476

#include "User.h"

User::User(int anId, string aName) : id(anId), name(aName) {
}

int User::getId() const {
    return id;
}

string User::getName() const {
    return name;
}