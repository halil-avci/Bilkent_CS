//sec2-Halil-Avcı-22003476

#include "Creator.h"
#include <string>
using namespace std;

Creator::Creator(int anId, string aName) : id(anId), name(aName), noOfFollowers(0), noOfContents(0) {
    SortedLinkedList<int> followerIds;
    SortedLinkedList<Content> contents;
}

int Creator::getId() const {
    return id;
}

string Creator::getName() const {
    return name;
}

int Creator::getNoOfFollowers() const {
    return noOfFollowers;
}

int Creator::getNoOfContents() const {
    return noOfContents;
}

void Creator::addContent(Content content) {
    int contentId = content.getId();
    
    bool isInserted = false;
    for (int i = 1; i <= noOfContents; i++) {
        if (contentId < contents.getEntryReference(i).getId() && !isInserted) {
            contents.insert(i, content);
            isInserted = true;
        }   
    }

    if (!isInserted) {
        contents.insert(noOfContents + 1, content);
    }

    noOfContents++;
}

void Creator::addFollower(int followerId) {
    bool isInserted = false;
    for (int i = 1; i <= noOfFollowers; i++) {
        if (followerId < followerIds.getEntryReference(i) && !isInserted) {
            followerIds.insert(i, followerId);
            isInserted = true;
        }   
    }

    if (!isInserted) {
        followerIds.insert(noOfFollowers + 1, followerId);
    }

    noOfFollowers++;
}

void Creator::removeContent(int contentId) {
    bool contentExists = false;
    for (int i = 1; i <= noOfContents; i++) {
        if (contentId == contents.getEntryReference(i).getId()) {
            contents.remove(i);
            noOfContents--;
            contentExists = true;
        }
    }
}
void Creator::removeFollower(int followerId) {
    bool followerExists = false;
    for (int i = 1; i <= noOfFollowers; i++) {
        if (followerId == followerIds.getEntryReference(i)) {
            followerIds.remove(i);
            noOfFollowers--;
            followerExists = true;
        }
    }
}
void Creator::showFollowers() const {
    cout << "Regular users following content creator with ID " << id << ":" << endl;
    if (noOfFollowers == 0) {
        cout << "None" << endl;
    }
    else {
        for (int i = 1; i <= noOfFollowers; i++) {
            cout << followerIds.getEntryReference(i) << endl;
        }
    }
}

void Creator::showContents() const {
    cout << "Contents of content creator with ID " << id << ":" << endl;
    if (noOfContents == 0) {
        cout << "None" << endl;
    }
    else {
        for (int i = 1; i <= noOfContents; i++) {
            cout << contents.getEntryReference(i).getId() << endl;
        }
    }
}

bool Creator::doesContentExist(int contentId) const {
    bool contentExists = false;
    for (int i = 1; i <= noOfContents; i++) {
        if (contentId == contents.getEntryReference(i).getId()) {
            contentExists = true;
        }
    }

    return contentExists;
}

bool Creator::doesUserFollow(int userId) const {
    bool followerExists = false;
    for (int i = 1; i <= noOfFollowers; i++) {
        if (userId == followerIds.getEntryReference(i)) {
            followerExists = true;
        }
    }
    return followerExists;
}