// ourfunc 定义输入输出
#include <iostream>
void simon(int);

int main()
{
    using namespace std;
    simon(3);
    cout<<" Pick an integer:";
    int count = 100;
    //cin >> count;//如果使用cin 在mac 下需要设置externalConsole": true
    simon(count);
    cout<<"Done!"<<endl;
    return 0;
}

void simon(int n)
{
    using namespace std;
    cout << "Simon says touch your toes" << n <<"times."<<endl;
}