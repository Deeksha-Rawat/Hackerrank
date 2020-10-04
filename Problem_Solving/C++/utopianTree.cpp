/* https://www.hackerrank.com/challenges/utopian-tree/problem  */

#include<bits/stdc++.h>
using namespace std;

int utopianTree()
{
  int n ;
  cin >> n ;
  int h=1 ;
  for(int i=1; i<=n ; i++)
  {
    if(i%2==0)
    {
      h++ ;
    }
    else
    {
      h = 2*h ;
    }
  }
  cout<< h ;
  
  return 0 ;
}
