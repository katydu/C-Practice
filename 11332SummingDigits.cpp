#include <iostream>
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

void calculateDigit(int num,int len){
	int digit;
	int sum = 0;
	for(int i=len;i>0;i--)
	{
		//when check the first number only need to divided
		if(i == len)
		{
			double a = pow(10,len-1);
			digit = num/a;
		}
		//when check the last number only need to check remainder
		else if(i == 1)
		{
			digit = num%10;
		}
		// when check other place then need to check remainder first then do divided
		else
		{
			int divided = pow(10,i);
			int remainder = pow(10,i-1);
			int process = num%divided;
			digit = process/remainder;
		}
		// sum the each digit we seperate out
		sum = sum + digit;	
	}
	// when the sum still > 10 means the sum need to do the seperate process again
	if(sum>=10)
	{
		len = calculateLength(sum);
		calculateDigit(sum,len);
	}
	// <10 means it the final answer we want
	else
	{
		cout << "output:" << sum <<endl;
	}
}


int main(int argc, char** argv){
	int input;
	int length;
	int inputArray[99] = {0};
	// calculate array index
	int count=0;
	while(1){
		cout << "Please Enter:";
		cin >> input;
		//user enter 0 then break 
		if(input==0){
			break;
		}else{
			inputArray[count] = input;
			count = count +1;
		}
	}
	// start
	for(int i=0;i<count;i++){
		length = calculateLength(inputArray[i]);
		calculateDigit(inputArray[i],length);
	}
	return 0;
}
