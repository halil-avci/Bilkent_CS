#ifndef EMPLOYEE_H
#define EMPLOYEE_H

#include <iostream>
#include "Issue.h"
using namespace std;

class Employee{
private:
    string name;
    string title;
    Issue* issuesOfEmployee;
    int numberOfIssuesOfEmployee;
public:
    Employee();
    Employee(string name, string title);
    ~Employee();
    void assignIssue(const int id, const string description);
    void unassignIssue(const int it);
    void transferIssues(Employee &newAssignee);
    void setName(string name);
    string getName();
    void setTitle(string title);
    string getTitle();
    void setIssuesOfEmp(Issue* issuesOfEmp);
    Issue* getIssuesOfEmp();
    void setNumberOfIssuesOfEmp(int numberOfIssuesOfEmp);
    int getNumberOfIssuesOfEmp();
    Employee& operator=(const Employee& other);
};
#endif
