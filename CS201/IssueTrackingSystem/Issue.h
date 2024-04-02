#ifndef ISSUE_H
#define ISSUE_H

#include <iostream>
#include <stdio.h>
using namespace std;

class Issue{
private:
   string description;
   string assigneeName;
   int issueId;
public:
   Issue();
   Issue(int issueId, string description, string assigneeName);
   void setDescription(string description);
   string getDescription();
   void setAssigneeName(string assigneeName);
   string getAssigneeName();
   void setIssueId(int issueId);
   int getIssueId();
   Issue& operator=(const Issue& other);
};
#endif