#include "GroupChat.h"

GroupChat::GroupChat(){}
void GroupChat::registerUser(Observer *observer){
    users.push_back(observer);
}
void GroupChat::removeUser(Observer *observer)
{
    auto it = find(users.begin(),users.end(),observer);
    if( it != users.end())
    {
        users.erase(it);
    }
}
void GroupChat::sendMessage(string message)
{
    messages.push_back(message);
    GroupChat::notify();
}
void GroupChat::notify()
{
    for (auto &user : users)
    {
        user->update(messages.back());
    }
}