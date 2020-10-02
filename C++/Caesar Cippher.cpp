#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
int n, k, i = 0;
char ch;
string s;
cin >> n >> s >> k;
    while(i < n){
 ch = s[i];
 if(ch < 91 && ch > 64){
 ch += k%26;
 if(ch > 90){
 ch -= 26;
 }
}else if(ch > 96 && ch < 123){
 ch -= 96;
ch += k%26;
if(ch > 26){
 ch -= 26;
 }
  ch += 96;
  }
  s[i] = ch;
   i++;
   }
   cout << s;
    return 0;
}
