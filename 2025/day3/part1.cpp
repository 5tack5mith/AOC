#include<iostream>
#include<fstream>
#include<string>
using namespace std;
int main(){
    ifstream file;
    file.open("input.txt");
    if(!file.is_open()){
        cout<<"Error opening file\n";
        return 1;
    }
    string line;
    int sum =0;
    while(getline(file,line)){
        char max1='0',max2='0';
        int j;
        int n=line.length();
        for(int i=0;i<n-1;i++){
            if(max1<line[i]){
                max1=line[i];
                j=i;
            }
        }
        for(int i=j+1;i<n;i++){
            if(max2<line[i]){
                max2=line[i];
            }
        }
        cout<<max1<<" and "<<max2<<endl;
        int num = ((max1-'0')*10)+(max2-'0');
        //cout<<num<<endl;
        sum+=num;
        //cout<<sum<<endl;
    }
    cout<<sum;
    return 0;
}