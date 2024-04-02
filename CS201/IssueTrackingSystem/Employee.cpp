#include <iostream>
#include "Employee.h"
using namespace std;

Employee::Employee(){
    this->name = "";
    this->title = "";
    this->issuesOfEmployee = nullptr;
    this->numberOfIssuesOfEmployee = 0;
}

Employee::Employee(string name, string title){
    this->name = name;
    this->title = title;
    this->issuesOfEmployee = nullptr;
    this->numberOfIssuesOfEmployee = 0;
}

Employee::~Employee(){
    delete[] issuesOfEmployee;
}

void Employee::assignIssue(const int id, const string description){
    Issue* issuesOfEmployeeResized = new Issue[numberOfIssuesOfEmployee + 1];
    for(int i = 0; i < numberOfIssuesOfEmployee; i++){
        issuesOfEmployeeResized[i] = issuesOfEmployee[i];
    }
    Issue issue(id, description, name);
    numberOfIssuesOfEmployee++;
    issuesOfEmployeeResized[numberOfIssuesOfEmployee - 1] = issue;
    if(issuesOfEmployee != nullptr){
        delete[] issuesOfEmployee;
    }
    issuesOfEmployee = issuesOfEmployeeResized;
}

void Employee::unassignIssue(const int id){
    int indexToRemove = -1;
    for(int i = 0; i < numberOfIssuesOfEmployee; i++){
        if(issuesOfEmployee[i].getIssueId() == id){ 
            indexToRemove = i;
            break;
        }
    }
    Issue* issuesOfEmployeeResized2 = new Issue[numberOfIssuesOfEmployee - 1];
    for(int i = 0; i < indexToRemove; i++){
        issuesOfEmployeeResized2[i] = issuesOfEmployee[i];
    }
    for(int i = 0; i < numberOfIssuesOfEmployee - 1; i++){
        issuesOfEmployeeResized2[i] = issuesOfEmployee[i + 1];
    }
    /*if(numberOfIssuesOfEmployee < 1){
        delete[] issuesOfEmployee;
        issuesOfEmployee = nullptr;
        numberOfIssuesOfEmployee = 0;
        return;
    }*/
    if(issuesOfEmployee != nullptr){
        delete[] issuesOfEmployee;  
    }
    issuesOfEmployee = issuesOfEmployeeResized2;
    numberOfIssuesOfEmployee--; 
}

void Employee::transferIssues(Employee &newAssignee){
    for(int i = 0; i < numberOfIssuesOfEmployee; i++){
        newAssignee.assignIssue(issuesOfEmployee[i].getIssueId(), issuesOfEmployee[i].getDescription());
        unassignIssue(issuesOfEmployee[i].getIssueId());
    }
    if(issuesOfEmployee != nullptr){
        delete[] issuesOfEmployee;
    }
    issuesOfEmployee = nullptr;
    numberOfIssuesOfEmployee = 0;
}

void Employee::setName(string name){
    this->name = name;
}

string Employee::getName(){
    return name;
}

void Employee::setTitle(string title){
    this->title = title;
}

string Employee::getTitle(){
    return title;
}

void Employee::setIssuesOfEmp(Issue *issuesOfEmployee){
    this->issuesOfEmployee = issuesOfEmployee;
}

Issue *Employee::getIssuesOfEmp(){
    return issuesOfEmployee;
}

void Employee::setNumberOfIssuesOfEmp(int numberOfIssuesOfEmployee){
    this->numberOfIssuesOfEmployee = numberOfIssuesOfEmployee;
}

int Employee::getNumberOfIssuesOfEmp(){
    return numberOfIssuesOfEmployee;
}

Employee& Employee::operator=(const Employee& other){
    if(this != &other){
        name = other.name;
        title = other.title;
        numberOfIssuesOfEmployee = other.numberOfIssuesOfEmployee;
        issuesOfEmployee = new Issue[numberOfIssuesOfEmployee];
        for(int i = 0; i < other.numberOfIssuesOfEmployee; i++){
            issuesOfEmployee[i] = other.issuesOfEmployee[i];
        }
    }
    return *this;
}