#include "Issue.h"

Issue::Issue(){
    this->issueId = 0;
    this->description = "";
    this->assigneeName = "";
}

Issue::Issue(int issueId, string description, string assigneeName){
    this->issueId = issueId;
    this->description = description;
    this->assigneeName = assigneeName;
}

void Issue::setDescription(string description){
    this->description = description;
}

string Issue::getDescription(){
    return description;
}

void Issue::setAssigneeName(string assigneeName){
    this->assigneeName = assigneeName;
}

string Issue::getAssigneeName(){
    return assigneeName;
}

void Issue::setIssueId(int issueId){
    this->issueId = issueId;
}

int Issue::getIssueId(){
    return issueId;
}

Issue &Issue::operator=(const Issue &other){
    if(this != &other){
        issueId = other.issueId;
        description = other.description;
        assigneeName = other.assigneeName;
        
    }
    return *this;
}
