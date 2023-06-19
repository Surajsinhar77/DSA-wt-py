#include<iostream>
#include<string>
using namespace std;

// int TrimSpace(char input[],char newinput[])
// {
//     cout<<"mai aagaya "<<endl;
//     int x=0,y=0;
//     while(input[x]!='\0')
//     {
//         while(input[x]!=' ' && input[x] != '\0')
//         {
//             cout<<"hu kya mai "<<endl;
//             newinput[y] = input[x];
//             x++;
//             y++;
//         }
//         x++;
//     }
//     int small = y;
//     return small;
// }

// int main()
// {
//     char input[100];
//     char newinput[100];
//     cin.getline(input,100);
//     int smallLength = TrimSpace(input,newinput);
//     cout<<smallLength<<endl;
//     for(int i=0;i<smallLength;i++)
//     {
//         cout<<newinput[i];
//     }

//     cout<<endl;
//     return 0;
// }


// char * TrimSpace(char input[])
// {
//     int x=0,y=0;
//     char * newinput = new char[100];
//     while(input[x]!= '\0'){
//         if(input[x]==' ')
//         {  
//             x++;
//         }
//         else
//         {
//             newinput[y] = input[x];
//             x++;
//             y++;
//         }
//     }
//     newinput[y] = '\0';
//     return newinput;
// }



// int main(){

//     char input[100];
//     cin.getline(input,100);
//     char * smallInput = TrimSpace(input);
    
//     cout<<smallInput<<endl;
//     cout<<&smallInput<<endl;
//     int i = 0;


//     // while(smallInput[i] != '\0'){
//     //     cout<<smallInput[i];
//     //     i++;
//     // }
//     cout<<endl;
//     delete[] smallInput;
//     return 0;

// }

// void ReverseString(char input[],int &x,int &y)
// {
//     cout<<"hello"<<endl;// infinite loop chal raha hai
//     if(x>=y)
//     {
//         return;
//     }

//     if(x<y)
//     {
//         char temp = input[x];
//         input[x] = input[y];
//         input[y] = temp;
//     }
//     x++;
//     y--;
//     ReverseString(input,x, y);
//     cout<<"hello"<<endl;
// }


// int getLength(char arr[]){
//     int i =0;
//     while(arr[i] != '\0'){
//         i++;
//     }
//     return i;
// }



// int main()
// {
//     char input[100];
//     cin.getline(input,100);
//     int size = getLength(input);
//     int start = 0;
//     ReverseString(input, start, size);
//     cout<<input<<endl;
//     return 0;
// }

int length(char input[])
{
    int count=0;
    for(int i=0;input[i]!='\0';i++)
    {
        count+=1;
    }
    return count;
}

void shift(char input[], int size)
{
    bool flag = false;
    int y = size-1;
    while(y > 0 )
    {                          // 12345  1234 5
        input[y+2] = input[y]; // abhay
        input[y+1] = ' ';
        y--;
    }
    input[size+(size-1)] = '\0';
}

// void spaceBEletter(char input[])
// {
//     int x1=0;
//     int size1 = length(input);
//     // while(x1 <= size1-1)
//     // {
//     //     if(input[x1]!=' ')
//     //     {
//     //         shift(input,x1,size1);
//     //         size1 = smallSize;
//     //     }
//     //     x1++;
//     // }
// }

int main()
{
    char input[100];
    cin.getline(input,100);
    int size =  length(input);
    // spaceBEletter(input);
    shift(input, size);
    for(int i=0;input[i]!='\0';i++)
    {
        cout<<input[i];
    }
    cout<<endl;
    return 0;
}