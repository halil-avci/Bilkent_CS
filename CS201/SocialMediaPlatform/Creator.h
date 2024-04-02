//sec2-Halil-Avcı-22003476

#ifndef CREATOR_H
#define CREATOR_H

#include <string>
#include "SortedLinkedList.h"
#include "Content.h"
#include <iostream>
using namespace std;

class Creator {

private:
    int id;
    string name;
    SortedLinkedList<int> followerIds;
    SortedLinkedList<Content> contents;
    int noOfFollowers;
    int noOfContents;

public:
    Creator(int anId, string aName);

    int getId() const;
    string getName() const;
    int getNoOfFollowers() const;
    int getNoOfContents() const;
    void addContent(Content content);
    void addFollower(int followerId);
    void removeContent(int contentId);
    void removeFollower(int followerId);
    void showFollowers() const;
    void showContents() const;
    bool doesContentExist(int contentId) const;
    bool doesUserFollow(int userId) const;
};

#endif