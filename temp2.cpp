#include<iostream>
#include<string>
#include<vector>
using namespace std;




int main(){
    // string ans;

    // getline(cin, ans);
    // cout<<ans;

    vector<int> arry;

    arry.push_back(2);
    arry.push_back(4);

    cout<<arry.size()<<endl;

    int n = 5;

    // for (int i =0; i<n; i++){
    //     int data;
    //     cin>>data;
    //     arry.push_back(data);
    // }

    for (int i =0; i<n; i++){
        int data;
        cout<<" enter data : ";
        cin>>data;
        arry.push_back(data);
    }

    // int ary[6];

    // for(int i =0; i<6; i++){
    //     cin>>ary[i];
    // }

    arry.pop_back();

    for( int i =0; i<arry.size(); i++){
        // cout<<arry[i]<<" ";
        cout<<arry.at(i)<<" ";
    }
    
    
    return 0;
}