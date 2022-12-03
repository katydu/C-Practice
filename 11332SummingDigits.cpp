#include <iostream>
#include <cstring>
#include <string>
#include <cmath>
using namespace std;

int calculateLength(int num){
	if(num/10 > 0){
		if(num/100 > 0){
			if(num/1000 > 0){
				if(num/10000 > 0){
					if(num/100000 > 0){
						if(num/1000000 > 0){
							if(num/10000000 > 0){
								if(num/100000000 > 0){
									if(num/1000000000 > 0){
										return 10;
									}
									return 9;
								}
								return 8;
							}
							return 7;
						}
						return 6;
					}
					return 5;
				}
				return 4;
			}
			return 3;
		}
		return 2;
	}
	return 1;
}

int calculateDigit(int num,int len){
	int digit;
	int sum = 0;
	for(int i=len;i>0;i--){
		if(i == len){
			double a = pow(10,len-1);
			digit = num/a;
			cout << "digit:" << digit << endl; 
		}else if(i == 1){
			digit = num%10;
			cout << "digit:" << digit << endl; 
		}else{
			int c = pow(10,i);
			int d = pow(10,i-1);
			int process = num%c;
			digit = process/d;
			cout << "digit:" << digit << endl; 
		}
		sum = sum + digit;
		cout << "sum:" << sum << endl; 
		
	}
	return sum;
}


int main(int argc, char** argv){

	int input;
	int length;
	cout << "請輸入數值:";
	cin >> input;
	while(1){
		length = calculateLength(input);
		cout << "長度" << length << endl; 
		if(length == 1){
			cout << "outcome:" << input << endl; 
			return 0;
		}else{
			input = calculateDigit(input,length);
		}
	}
	
	
	return 0;
}
