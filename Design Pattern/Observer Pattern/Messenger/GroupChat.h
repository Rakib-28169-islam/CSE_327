
#pragma once
#include <bits/stdc++.h>
#include<bits/stdc++.h>
#include "Subject.h"
#include "Observer.h"
class GroupChat:public Subject{

    private:
    vector<Observer *>users;
    vector<string>messages;

    public:
    GroupChat();
    void registerUser(Observer *observer);
    void removeUser(Observer *observer);
    void sendMessage(string message);
    void notify();



};