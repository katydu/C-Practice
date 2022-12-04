#include <iostream>
using namespace std;


int f(int n){
	int sum = 0;
	while(n > 0){
		//sum = sum + (n % 10) 
		sum += n% 10;
		// n = n/10
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
	int n;
	// while cin the n also check n is >0, cin >> n && n > 0
	while(cin >> n && n){
		// put output in the array
		output[count] = f(n);
		// count how many output we have, avoid other 0 in array will cause wrong answer
		count++;
	} 
	for(int i=0;i<count;i++){
		cout << output[i]<<endl;
	}	
	return 0;
}
