#include <iostream>
#include <cmath>
using namespace std;


int f(int n){
	int sum = 0;
	while(n > 0){
		sum += n% 10;
		n /= 10;
	}
	if(sum < 10){
		return sum;
	}else{
		return f(sum);
	}
}

int main(int argc, char** argv){
	int output[99]={0};
	int count = 0;
	int r[0];
	int n;
	while(cin >> n && n){
		output[count] = f(n);
		count++;
	} 
	for(int i=0;i<count;i++){
		cout << output[i]<<endl;
	}	
	return 0;
}
