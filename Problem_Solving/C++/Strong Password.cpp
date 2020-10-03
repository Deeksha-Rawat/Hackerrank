#include <bits/stdc++.h>
#include<string>
using namespace std;

int main() { int n,no=0,no2=0,ch=0,rub=0,count=0,i,z=0;

string s;

cin>>n>>s;

for(i=0;i<n;i++)
{
    if(int(s[i])>=65&&int(s[i])<=90)
    no++;
    else if(int(s[i])>=97&&int(s[i])<=122)
    no2++;
    else if(int(s[i])>=48&&int(s[i])<=57)
    ch++;
    else if(s[i]=='+'||s[i]=='-'||s[i]=='!'||s[i]=='@'||s[i]=='#'||s[i]=='%'||s[i]=='^'||s[i]=='&'||s[i]=='*'||s[i]=='('||s[i]==')')
     rub++;
}
if(rub==0)
    count++;
if(ch==0)
    count++;
if(no==0)
    count++;
if(no2==0)
    count++;
if(n>=6&&count==0)
    cout<<0;
else if(n>=6&&count!=0)
    cout<<count;
else if(n<6&&count==0)
    cout<<(6-n);
else
{
if(rub==0)
    z++;
if(ch==0)
    z++;
if(no==0)
    z++;
if(no2==0)
    z++;
if((n+z)>=6)
    cout<<z;
else
{
    cout<<(6-n);
}               
}   
return 0;
}
