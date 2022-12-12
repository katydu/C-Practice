#include <iostream>
#include <string.h> // strtok

using namespace std;

int main()
{
    char BitrhDay;
    char CurrentDay;
    char str[] = {0};
    cin >> BitrhDay;
    //cin >> CurrentDay;
    cout << "BitrhDay:" << BitrhDay << endl;
    //cout << "CurrentDay" << CurrentDay;
    char str[] = BitrhDay;
    const char* d = "/";
    char *p;
    p = strtok(str, d);
    while (p != NULL) {
        printf("%s\n", p);
        p = strtok(NULL, d);		   
    }

    return 0;
}