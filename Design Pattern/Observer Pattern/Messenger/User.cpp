#pragma once

#include <bits/stdc++.h>
using namespace std;
#include "User.h"
#include "Observer.h"

User::User(string name,string id){
    this->name = name;
    this->id = id;
}
void User::update(string message)
{
    cout <<name<<id<<": "<<message<<endl;


}
string User::getId()
{
     return id;
}
string User::getName()
{
     return name;
}