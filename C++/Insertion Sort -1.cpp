#include <bits/stdc++.h>

using namespace std;

int main()
{
    int i,j,x;
    int n;
    int temp;
    cin>>n;
    int a[n];
    for(i=0;i<n;i++)
    {
        cin>>a[i];
    }
for(i = 1; i <= n - 1; i++)
    {
        for(j = i; j > 0 ; j--)
        {
            if (a[j - 1] > a[j])
            {
                temp = a[j];
                a[j] = a[j - 1];
               

            for(x=0;x<n;x++)
            {
                cout<<a[x]<< " ";
            
            }
           cout<<endl; 
            a[j - 1] = temp;
            }
            
        }
        
    }
            
            for(i=0;i<n;i++)  {
                cout<<a[i]<<" ";
                
            }
            


}
