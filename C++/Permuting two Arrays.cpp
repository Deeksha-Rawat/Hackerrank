#include <bits/stdc++.h>

using namespace std;

int main(){
    long long int t;
    cin>>t;
    while(t--){
long long int n,k,c=0;
cin>>n>>k;
long long int a[n],b[n];
for(long long int i=0;i<n;i++){
    cin>>a[i];
}
for(long long int i=0;i<n;i++){
    cin>>b[i];
}
sort(a,a+n);sort(b,b+n);
for(long long int i=0;i<n;i++){
    for(long long int j=0;j<n;j++){
        if(a[i]+b[j]>=k){
            b[j]=0;
            c++;
            break;
        }

    }
}
if(c==n){
    cout<<"YES"<<endl;
}
else cout<<"NO"<<endl;
}
}
