#include<bits/stdc++.h>
#include "GroupChat.cpp"
#include "GroupChat.h"
#include "User.cpp"
#include "User.h"
using namespace std;
int main()
{
    GroupChat chat;
    User user1("User1","@user1"),user2("User2","@user2"),user3("User3","@user3");
    chat.registerUser(&user1);
    chat.registerUser(&user2);
    chat.registerUser(&user3);
    chat.sendMessage("Hello everyone!");

}