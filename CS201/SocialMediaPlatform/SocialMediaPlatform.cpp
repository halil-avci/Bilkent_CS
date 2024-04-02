//sec2-Halil-Avcı-22003476

#include <string>
#include <iostream>
#include "SocialMediaPlatform.h"
using namespace std;

SocialMediaPlatform::SocialMediaPlatform() : noOfCreators(0), noOfUsers(0) {
    SortedLinkedList<Creator> creators;
    SortedLinkedList<User> users;
}

SocialMediaPlatform::~SocialMediaPlatform() {
    //default destructor
}

void SocialMediaPlatform::addRegularUser( const int regularUserId, const string name ) {
    bool userExists = false;
    for (int i = 1; i <= noOfUsers; i++) {
        if (regularUserId == users.getEntryReference(i).getId()) {
            userExists = true;
        }
    }

    if (userExists) {
        cout << "Cannot add regular user. There is already a regular user with ID " << regularUserId
                << "." << endl;
    }
    else {
        User newUser(regularUserId, name);

        bool isInserted = false;
        for (int i = 1; i <= noOfUsers; i++) {
            if (regularUserId < users.getEntryReference(i).getId() && !isInserted) {
                users.insert(i, newUser);
                isInserted = true;
            }   
        }

        if (!isInserted) {
            users.insert(noOfUsers + 1, newUser);
        }

        noOfUsers++;
        cout << "Added regular user " << regularUserId << "." << endl;
    }
}

void SocialMediaPlatform::removeRegularUser( const int regularUserId ) {
    bool userExists = false;
    for (int i = 1; i <= noOfUsers; i++) {
        if (regularUserId == users.getEntryReference(i).getId()) {
            users.remove(i);
            noOfUsers--;
            userExists = true;
            cout << "Removed regular user " << regularUserId << "." << endl;
        }
    }

    if (userExists) {
        for (int i = 1; i <= noOfCreators; i++) {
            creators.getEntryReference(i).removeFollower(regularUserId);
        }
    }
    else {
        cout << "Cannot remove regular user. There is no regular user with ID " << regularUserId
                << "." << endl;
    }
}

void SocialMediaPlatform::addContentCreator( const int contentCreatorId, const string name ) {
    bool creatorExists = false;
    for (int i = 1; i <= noOfCreators; i++) {
        if (contentCreatorId == creators.getEntryReference(i).getId()) {
            creatorExists = true;
        }
    }

    if (creatorExists) {
        cout << "Cannot add content creator. There is already a content creator with ID " << contentCreatorId
                << "." << endl;
    }
    else {
        Creator newCreator(contentCreatorId, name);

        bool isInserted = false;
        for (int i = 1; i <= noOfCreators; i++) {
            if (contentCreatorId < creators.getEntryReference(i).getId() && !isInserted) {
                creators.insert(i, newCreator);
                isInserted = true;
            }   
        }

        if (!isInserted) {
            creators.insert(noOfCreators + 1, newCreator);
        }

        noOfCreators++;
        cout << "Added content creator " << contentCreatorId << "." << endl;
    }
}

void SocialMediaPlatform::removeContentCreator( const int contentCreatorId ) {
    bool creatorExists = false;
    for (int i = 1; i <= noOfCreators; i++) {
        if (contentCreatorId == creators.getEntryReference(i).getId()) {
            creators.remove(i);
            noOfCreators--;
            creatorExists = true;
        }
    }

    if (!creatorExists) {
        cout << "Cannot remove content creator. There is no content creator with ID " << contentCreatorId
                << "." << endl;
    }
    else {
        cout << "Removed content creator " << contentCreatorId << "." << endl;
    }
}

void SocialMediaPlatform::addContent( const int contentCreatorId, const int contentId, const string title ) {
    bool contentExists = false;
    bool creatorExists = false;
    int creatorIndex = 0;
    for (int i = 1; i <= noOfCreators; i++) {
        if (!creatorExists && contentCreatorId == creators.getEntryReference(i).getId()) {
            creatorExists = true;
            creatorIndex = i;
        }
        if (!contentExists && creators.getEntryReference(i).doesContentExist(contentId)) {
            contentExists = true;
        }
    }

    if (contentExists) {
        cout << "Cannot add content. There is already a content with ID " << contentId
                << "." << endl;
    }
    else if (!creatorExists) {
        cout << "Cannot add content. There is no content creator with ID " << contentCreatorId
                << "." << endl;
    }
    else {
        Content newContent(contentId, title);
        creators.getEntryReference(creatorIndex).addContent(newContent);
        cout << "Added content " << contentId << "." << endl;
    }
}

void SocialMediaPlatform::removeContent( const int contentCreatorId, const int contentId ) {
    bool contentExists = false;
    bool creatorExists = false;
    int creatorIndex = 0;
    for (int i = 1; i <= noOfCreators; i++) {
        if (contentCreatorId == creators.getEntryReference(i).getId()) {
            creatorExists = true;
            creatorIndex = i;
        } 
        if (creators.getEntryReference(i).doesContentExist(contentId)) {
            contentExists = true;
        } 
    }

    if (!creatorExists) {
        cout << "Cannot remove content. There is no content creator with ID " << contentCreatorId
                << "." << endl;
    }
    else if (!contentExists) {
        cout << "Cannot remove content. There is no content with ID " << contentId
                << " shared by content creator with ID " << contentCreatorId << "." << endl;
    }
    else {
        creators.getEntryReference(creatorIndex).removeContent(contentId);

        cout << "Removed content " << contentId << "." << endl;
    }
}

void SocialMediaPlatform::followContentCreator( const int regularUserId, const int contentCreatorId ) {
    bool creatorExists = false;
    int creatorIndex = 0;
    for (int i = 1; i <= noOfCreators; i++) {
        if (contentCreatorId == creators.getEntryReference(i).getId()) {
            creatorExists = true;
            creatorIndex = i;
        } 
    }

    bool userExists = false;
    for (int i = 1; i <= noOfUsers; i++) {
        if (regularUserId == users.getEntryReference(i).getId()) {
            userExists = true;
        }
    }

    if (!creatorExists || !userExists) {
        cout << "Cannot follow. Regular user and/or content creator ID does not exist." << endl;
    }
    else if (creators.getEntryReference(creatorIndex).doesUserFollow(regularUserId)) {
        cout << "Cannot follow. The user is already following the content creator." << endl; 
    }
    else {
        creators.getEntryReference(creatorIndex).addFollower(regularUserId);

        cout << "Regular user with ID " << regularUserId << " followed content creator with ID "
                << contentCreatorId << "." << endl;
    }
}

void SocialMediaPlatform::unfollowContentCreator( const int regularUserId, const int contentCreatorId) {
    bool creatorExists = false;
    int creatorIndex = 0;
    for (int i = 1; i <= noOfCreators; i++) {
        if (contentCreatorId == creators.getEntryReference(i).getId()) {
            creatorExists = true;
            creatorIndex = i;
        } 
    }

    bool userExists = false;
    for (int i = 1; i <= noOfUsers; i++) {
        if (regularUserId == users.getEntryReference(i).getId()) {
            userExists = true;
        }
    }

    if (!creatorExists || !userExists) {
        cout << "Cannot unfollow. Regular user and/or content creator ID does not exist." << endl;
    }
    else if (!creators.getEntryReference(creatorIndex).doesUserFollow(regularUserId)) {
        cout << "Cannot unfollow. The user is not following the content creator." << endl;
    }
    else {
        creators.getEntryReference(creatorIndex).removeFollower(regularUserId);

        cout << "Regular user with ID " << regularUserId << " unfollowed content creator with ID "
                << contentCreatorId << "." << endl;
    }
}

void SocialMediaPlatform::showFollowersOf( const int contentCreatorId ) const {
    bool creatorExists = false;
    int creatorIndex = 0;
    for (int i = 1; i <= noOfCreators; i++) {
        if (contentCreatorId == creators.getEntryReference(i).getId()) {
            creatorExists = true;
            creatorIndex = i;
        } 
    }

    if (!creatorExists) {
        cout << "Cannot show. There is no content creator with ID " << contentCreatorId
                << "." << endl;
    }
    else {
        creators.getEntryReference(creatorIndex).showFollowers();
    }
}

void SocialMediaPlatform::showContentsOf( const int contentCreatorId ) const {
    bool creatorExists = false;
    int creatorIndex = 0;
    for (int i = 1; i <= noOfCreators; i++) {
        if (contentCreatorId == creators.getEntryReference(i).getId()) {
            creatorExists = true;
            creatorIndex = i;
        } 
    }

    if (!creatorExists) {
        cout << "Cannot show. There is no content creator with ID " << contentCreatorId
                << "." << endl;
    }
    else {
        creators.getEntryReference(creatorIndex).showContents();
    }
}

void SocialMediaPlatform::showAllRegularUsers( ) const {
    cout << "Regular users in the social media platform:" << endl;
    
    if (noOfUsers == 0) {
        cout << "None" << endl;
    }
    else {
        for (int i = 1; i <= noOfUsers; i++) {
            cout << users.getEntryReference(i).getId() << ", " << users.getEntryReference(i).getName() << endl;
        }
    }
}

void SocialMediaPlatform::showAllContentCreators( ) const {
    cout << "Content creators in the social media platform:" << endl;
    
    if (noOfCreators == 0) {
        cout << "None" << endl;
    }
    else {
        for (int i = 1; i <= noOfCreators; i++) {
            cout << creators.getEntryReference(i).getId() << ", " << creators.getEntryReference(i).getName() << ", ";
            cout << creators.getEntryReference(i).getNoOfFollowers() << " follower(s), ";
            cout << creators.getEntryReference(i).getNoOfContents() << " content(s)" << endl;
        }
    }
}