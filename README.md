# CPE (Collegiate Programming Examination)
## About Practice
As I know, I have quite more interest in web development. Therefore, I have touched some lanauge are more tend to relevent about web. For instance, javascript, .Net, html, and so on. I think it's time to practice other lanauge. Also, it's great to have some coding certificate for my future degree. In conclusion. I choose CPE as my programming examination.

CPE Link: https://cpe.cse.nsysu.edu.tw/index.php

## Previous exam 

### 11332 Summing Digits
Question:
https://cpe.cse.nsysu.edu.tw/cpe/file/attendance/problemPdf/11332.pdf

Smart Method:
```
int f(int n){
    int sum = 0;
    while(n > 0){
      sum = sum + (n % 10) 
      n = n/10
    }
    if(sum < 10){
      return sum;
    }else{
      return f(sum);
    }
}
```
In function f, we don't need to calculate the length of number. We can simplify using remainder to calculate the last digit in the number, and then we cut out original number's last number.

For example: our original number is 123. We use % to get the remainder 3 also is the last digit, and then we don't need 3 anymore. We use / to cut the last digit out. We got new number 12, and back to the % process, and so on.

And how we know the sum we get it's single digit? And Should we send it back to seperate again or it's what we want?
while sum is > 10 means it's not single digit, so we can use this to decide which step should we do.
