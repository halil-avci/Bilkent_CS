//sec2-Halil-Avcı-22003476

#ifndef CONTENT_H
#define CONTENT_H

#include <string>
using namespace std;

class Content {

private:
    int id;
    string title;

public:
    Content(int anId, string aTitle);

    int getId() const;
    string getTitle() const;
};

#endif