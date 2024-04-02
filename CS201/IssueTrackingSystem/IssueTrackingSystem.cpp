#include "IssueTrackingSystem.h"
//g++ Issue.cpp Employee.cpp IssueTrackingSystem.cpp main.cpp -o test1
IssueTrackingSystem::IssueTrackingSystem(){
    employees = nullptr;
    numberOfEmployees = 0;
    issues = nullptr;
    numberOfIssues = 0;
}

IssueTrackingSystem::~IssueTrackingSystem(){
    delete[] employees;
    delete[] issues;
}

void IssueTrackingSystem::addEmployee(const string name, const string title){
    for(int i = 0; i < numberOfEmployees; i++){
        if(employees[i].getName() == name){
            cout << "Cannot add employee. Employee with name " << name << " already exists." << endl;
            return;
        }
    }
    Employee* employeeListResized = new Employee[numberOfEmployees + 1];
    for(int i = 0; i < numberOfEmployees; i++){
        employeeListResized[i] = employees[i];
    }
    Employee* emp = new Employee (name, title);
    numberOfEmployees++;
    employeeListResized[numberOfEmployees-1] = *emp;
    if(employees != nullptr){
        delete[] employees;
    }
    employees = employeeListResized;
    
    cout << "Added employee " << name << "." << endl;
}

void IssueTrackingSystem::removeEmployee(const string name){
    int indexToRemove = -1;
    for(int i = 0; i < numberOfEmployees; i++){
        if(employees[i].getName() == name){
            indexToRemove = i;
            break;
        }
    }
    if(indexToRemove == -1){
        cout << "Cannot remove employee. There is no employee with name " << name << "." << endl;
        return;
    }
    if(employees[indexToRemove].getNumberOfIssuesOfEmp() > 0){
        cout << "Cannot remove employee. " << employees[indexToRemove].getName() << " has assigned issues." << endl;
        return;
    }

    Employee* employeesResized = new Employee[numberOfEmployees - 1];
    for(int i = 0; i < indexToRemove; i++){
        employeesResized[i] = employees[i];
    }
    for(int i = indexToRemove; i < numberOfEmployees - 1; i++){
        employeesResized[i] = employees[i + 1];
    }
    if(employees != nullptr){
        delete[] employees;
    }
    employees = employeesResized;
    numberOfEmployees--;
    cout << "Removed employee " << name << "." << endl;
}

void IssueTrackingSystem::addIssue(const int issueId, const string description, const string assigneeName){
    for(int i = 0; i < numberOfEmployees; i++){
        if(employees[i].getName() == assigneeName){
            employees[i].assignIssue(issueId, description);
            Issue* issueListResized = new Issue[numberOfIssues + 1];
            for(int i = 0; i < numberOfIssues; i++){
                issueListResized[i] = issues[i];
            }
            Issue issue(issueId, description, assigneeName);
            issueListResized[numberOfIssues] = issue;
            numberOfIssues++;
            if(issues != nullptr){   
                delete[] issues; 
            }    
            issues = issueListResized;
            cout << "Added issue " << issueId << "." << endl;
            return;
        }
        else{
            for(int i = 0; i < numberOfIssues; i++){
                if(issues[i].getIssueId() == issueId){
                    cout << "Cannot add issue. Issue with Id " << issueId <<  " already exists." << endl;
                    return;
                }
            }
        }
    }
}

void IssueTrackingSystem::removeIssue(const int issueId){
    int indexToRemove = -1;
    for(int i = 0; i < numberOfIssues; i++){
        if(issues[i].getIssueId() == issueId){
            indexToRemove = i;
            break;
        }
    }
    if(indexToRemove == -1){
        cout << "Cannot remove issue. There is no issue with ID " << issueId << "." << endl;
        return;
    }
    for(int i = 0; i < numberOfEmployees; i++){
        for(int j = 0; j < employees[i].getNumberOfIssuesOfEmp(); j++){
            if(employees[i].getIssuesOfEmp()[j].getIssueId() == issueId){
                employees[i].unassignIssue(issueId);
                cout << "Removed issue " << issueId << "." << endl;
                break;
            }
        }
    }
    Issue* issueListResized = new Issue[numberOfIssues - 1];
    for(int i = 0; i < indexToRemove; i++){
        issueListResized[i] = issues[i];
    }
    for(int i = indexToRemove; i < numberOfIssues - 1; i++){
        issueListResized[i] = issues[i + 1];
    }
    if(issues != nullptr){
        delete[] issues;
    }
    issues = issueListResized;
    numberOfIssues--;
    
}

void IssueTrackingSystem::changeAssignee(const string previousAssignee, const string newAssignee){
    for(int i = 0; i < numberOfEmployees; i++){
        for(int j = 0; j < numberOfEmployees; j++){
            if(employees[i].getName() == previousAssignee && employees[j].getName() == newAssignee){
                employees[i].transferIssues(employees[j]);
                cout << employees[i].getName() << "’s issues are transferred to " << employees[j].getName() << endl;
                return;
            }
        }
    }
    cout << "Cannot change assignee. Previous or/and new assignee does not exist." << endl;
}

void IssueTrackingSystem::showAllEmployees() const{
    if(employees != nullptr){
        cout << "Employees in the system:" << endl;
        for(int i = 0; i < numberOfEmployees; i++){
            cout << employees[i].getName() << ", " << employees[i].getTitle() << ", " << employees[i].getNumberOfIssuesOfEmp() << " issue(s)." << endl;
        }
    }
    else{
        cout << "None" << endl;
    }
}

void IssueTrackingSystem::showAllIssues() const{
    if(employees != nullptr && issues != nullptr){
        cout << "Issues:" << endl;
        for(int i = 0; i < numberOfEmployees; i++){
            for(int j = 0; j < employees[i].getNumberOfIssuesOfEmp(); j++){
                cout << employees[i].getIssuesOfEmp()[j].getIssueId() << ", " << employees[i].getIssuesOfEmp()[j].getDescription() << ", " << employees[i].getIssuesOfEmp()[j].getAssigneeName() << "." << endl;
            }
        }
    }
    else{
        cout << "No Issues." << endl;
    }
}

void IssueTrackingSystem::showEmployee(const string name) const{
    for(int i = 0; i < numberOfEmployees; i++){
        if(employees[i].getName() == name){
            cout << employees[i].getName() << ", " << employees[i].getTitle() << ", " << employees[i].getNumberOfIssuesOfEmp() << " issue(s)." << endl;
            return;
        }
    }
    cout << "Cannot show employee. There is no employee with name " << name << "." << endl;
}

void IssueTrackingSystem::showIssue(const int issueId) const{
    for(int i = 0; i < numberOfIssues; i++){
        if(issues[i].getIssueId() == issueId){
            cout << issues[i].getIssueId() << ", " << issues[i].getDescription() << ", " << issues[i].getAssigneeName() << "." << endl;
            return;
        }
    }
    cout << "Cannot show issue. There is no issue with ID " << issueId << "." << endl;
}

/*int indexToRemove = -1;
    for(int i = 0; i < numberOfEmployees; i++){
        if(employees[i].getName() == name){
            indexToRemove = i;
            break;
     }
    }
    if(indexToRemove == -1){
        cout << "Cannot remove employee. There is no employee with name " << name << "." << endl;
        return;
    }
    if(employees[indexToRemove].getNumberOfIssuesOfEmp() > 0){
        cout << "Cannot remove employee. " << employees[indexToRemove].getName() << " has assigned issues." << endl;
        return;
    }

    Employee* employeesResized = new Employee[numberOfEmployees - 1];
    for(int i = 0; i < indexToRemove; i++){
        employeesResized[i] = employees[i + 1];
    }
    for(int i = indexToRemove; i < numberOfEmployees - 1; i++){
        employeesResized[i] = employees[i + 1];
    }
    delete[] employees;
    employees = employeesResized;
    numberOfEmployees--;
    cout << "Removed employee " << name << "." << endl;*/

    /*int indexToRemove = -1;
    for(int i = 0; i < numberOfEmployees; i++){
        if(employees[i].getName() == name){
            indexToRemove = i;
        }
    }
    if(indexToRemove < 0){
        cout << "Cannot remove employee. There is no employee with name " << name << "." << endl;
        return;
    }
    if(employees[indexToRemove].getNumberOfIssuesOfEmp() > 0 && employees[indexToRemove].getIssuesOfEmp() != nullptr){
        cout << "Cannot remove employee. " << employees[indexToRemove].getName() <<  " has assigned issues." << endl;
        return;
    }
    Employee *employeesResized = new Employee[numberOfEmployees - 1];
    for(int i = 0; i < indexToRemove; i++){
        Employee emp(employees[i].getName(), employees[i].getTitle());
        employeesResized[i] = emp;
        if(employees[i].getNumberOfIssuesOfEmp() != 0){
            employeesResized[i].setIssuesOfEmp(new Issue[employees[i].getNumberOfIssuesOfEmp()]);
            for(int j = 0; j < employees[i].getNumberOfIssuesOfEmp(); j++){
                Issue issue(employees[i].getIssuesOfEmp()[j].getIssueId(), employees[i].getIssuesOfEmp()[j].getDescription(), employees[i].getIssuesOfEmp()[j].getAssigneeName());
                employeesResized[i].getIssuesOfEmp()[j] = issue;
                employeesResized[i].setNumberOfIssuesOfEmp(employeesResized[i].getNumberOfIssuesOfEmp() + 1);
            }
        }
    }
    for(int i = indexToRemove; i < numberOfEmployees-1; i++){
        Employee emp(employees[i + 1].getName(), employees[i + 1].getTitle());
        employeesResized[i] = emp;
        if (employees[i + 1].getNumberOfIssuesOfEmp() != 0){
            employeesResized[i].setIssuesOfEmp(new Issue[employees[i + 1].getNumberOfIssuesOfEmp()]);
            for(int j = 0; j < employees[i + 1].getNumberOfIssuesOfEmp(); j++){
                Issue issue(employees[i + 1].getIssuesOfEmp()[j].getIssueId(), employees[i + 1].getIssuesOfEmp()[j].getDescription(), employees[i + 1].getIssuesOfEmp()[j].getAssigneeName());
                employeesResized[i].getIssuesOfEmp()[j] = issue;
                employeesResized[i].setNumberOfIssuesOfEmp(employeesResized[i].getNumberOfIssuesOfEmp() + 1);
            }
        }
    }
    numberOfEmployees--;
    if(employees != nullptr){
        delete[] employees;
    }
    employees = employeesResized;
    cout << "Removed employee " << name << "." << endl;*/