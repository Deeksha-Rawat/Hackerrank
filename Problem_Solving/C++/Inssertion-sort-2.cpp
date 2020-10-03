#include <bits/stdc++.h>

using namespace std;

int main()
{
    int i,j;
    int n;
    int temp;
    cin>>n;
    int arr[n];
    for(i=0;i<n;i++)
    {
        cin>>arr[i];
    }
for(int j = 1; j<n; j++){
int c = arr[j];
int k = j+1;
while(arr[k-2]> c){
        arr[k-1] = arr[k-2];
        k--;
    }
arr[k-1] = c;
for(int i = 0; i < n; i++){
    cout << arr[i] << " ";
    }
    cout << endl;
}
}

