//sec2-Halil-Avcı-22003476

#include <string>
#include "Content.h"

Content::Content(int anId, string aTitle) : id(anId), title(aTitle) {
}

int Content::getId() const {
    return id;
}

string Content::getTitle() const {
    return title;
}