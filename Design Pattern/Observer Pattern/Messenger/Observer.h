#pragma once
#include <bits/stdc++.h>
using namespace std;

class Observer
{
    public:
     virtual ~Observer() = default;
     virtual void update(string message) =0;

};