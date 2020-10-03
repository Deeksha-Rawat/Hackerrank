#include <bits/stdc++.h>
#include<string>
using namespace std;

// Complete the camelcase function below.
int camelcase(string s) 
{
int i;
int count=0;
int x=s.length();
for(i=0; i<=x;i++)
{
    if (s[i]>=65 && s[i]<=90)
    {
        count++;
    }
    
}
return count+1;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string s;
    getline(cin, s);

    int result = camelcase(s);

    fout << result << "\n";

    fout.close();

    return 0;
}
