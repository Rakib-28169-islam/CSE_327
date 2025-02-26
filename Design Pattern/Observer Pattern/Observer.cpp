#include <bits/stdc++.h>
using namespace std;

class Observer
{
public:
    virtual ~Observer() = default;
    virtual void notify(float temperature, float humidity, float pressure) = 0;
};

class Subject
{

public:
    virtual ~Subject() = default;
    virtual void registerUser(Observer *observer)  = 0;
    virtual void removeUser(Observer *observer)  = 0;
    virtual void updateData()  = 0;
};
class User : public Observer
{

private:
    string id;

public:
    User(string id,Subject &subject)
    {
        subject.registerUser(this);
        this->id = id;
    }
    void notify(float temperature, float humidity, float pressure)
    {
        cout <<  id << " received update: " << temperature << "C, " << humidity << "%, " << pressure << "Pa" << endl;
    }
    string getId()
    {
        return id;
    }
};
class WeatherStation : public Subject
{
private:
    list<Observer *> users;
    float temperature;
    float humidity;
    float pressure;

public:
    WeatherStation()
    {

        temperature = 0.0f;
        humidity = 0.0f;
        pressure = 0.0f;
    }
    void registerUser(Observer *observer)
    {
        users.push_back(observer);
    }
    void removeUser(Observer *observer)
    {

        users.remove(observer);
    }
    void updateData()
    {
        for (auto &user : users)
        {
            user->notify(temperature, humidity, pressure);
        }
        cout<<endl;
    }
    void setInformation(float temperature, float humidity, float pressure)
    {
        this->temperature = temperature;
        this->humidity = humidity;
        this->pressure = pressure;
        updateData();
    }
};
int main()
{

    WeatherStation weatherStation;
    User user1("#XYZ",weatherStation);
    User user2("#QAQ",weatherStation);
    User user3("#QWE",weatherStation);

    // weatherStation.registerUser(&user1);
    // weatherStation.registerUser(&user2);
    // weatherStation.registerUser(&user3);
    weatherStation.setInformation(25.01f, 50.0f, 1013.0f);
    weatherStation.removeUser(&user3);
    weatherStation.setInformation(30.0f, 60.0f, 1014.0f);

    delete &user1;
    delete &user2;
    delete &user3;
    
    return 0;



    
}