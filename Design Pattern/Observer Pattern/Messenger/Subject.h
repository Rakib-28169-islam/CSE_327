#pragma once

#include <bits/stdc++.h>
#include "Observer.h"
using namespace std;    

class Subject{
    public:
    virtual void registerUser(Observer *observer)  = 0;
    virtual void removeUser(Observer *observer) = 0;
    virtual void notify() = 0;
    virtual ~Subject() = default;


};