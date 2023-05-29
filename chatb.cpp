#include<bits/stdc++.h>
using namespace std;
int main()
{
    map<string,string> m;
    m["Hello"]="How may I help you?";
    m["Hi"]="How may I help you?";
    m["How are you?"]="I am good what about you?";
    m["I am fine."]="Thats great! How may I help you?";

    m["Recharge plans"]="There are some popular combo plans:\nRs 299 ------------>  Unlimited calls + 1.5gb data/day for 28 days\nRs 799 ------------>  Unlimited calls + 1.5gb data/day for 84 days \nRs 399 ------------>  Unlimited calls + 2.5gb data/day for 28 days \nRs 499 ------------>  Unlimited calls + 3gb data/day for 28 days";

    m["Data plans"]="There are some popular data plans:\nRs 151 ------------>  8 gb for 28 days\nRs 108 ------------>  6 gb for 15 days\nRs 58 ------------>  3 gb for 28 days\nRs 38 ------------>  3 gb for 18 days";

    m["Validity plans"]="There are some plans:\nRs 99 ------------> Rs 99 talktime + 200 mb for 28 days\nRs 279 ------------> Rs 279 talktime + 500 mb for 90 days\nRs 107 ------------> Rs 107 talktime + 200 mb for 28 days\nRs 111 ------------> Rs 111 talktime + 100 mb for 31 days";

    m["Yearly plan"]="There are some yearly plans:\nRs 2099 ------------>  Unlimited calls + 3gb data/day for 365 days\nRs 1899 ------------>  Unlimited calls + 2.5gb data/day for 365 days\nRs 1799 ------------>  Unlimited calls + 1.5gb data/day for 3658 days";

    m["Thank you"]="Welcome";
    string s;
    cout<<"\nEnter something to talk with chatbot\n";
    while(true)
    {
        cout<<"\nYou : ";
        getline(cin,s);
        if(s=="quit"||s=="Quit"||s=="Exit"||s=="exit")
        {
            cout<<"\nChatbot: Thank you...";
            return 1;
        }
        if(m.find(s)==m.end()||s=="")
        {
            cout<<"\nChatbot : Sorry for inconvenience I can only answer:\n Recharge plans\nYearly plan\nData plans\nValidity plans";
        }
        else
        {
            cout<<"\nChatbot : "<<m[s]<<endl;
        }
    }
}