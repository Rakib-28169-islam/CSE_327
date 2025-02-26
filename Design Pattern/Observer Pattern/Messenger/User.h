#pragma once;
#include <bits/stdc++.h>
#include "Observer.h"
using namespace std;
class User:public Observer{
    private:
    string name;
    string id;
    public:
    User(string name,string id);
    void update(string message);
    string getId();
    string getName();

};