class Solution {
public:
    // int fib(int n) {
    //     if(n <= 1)
    //         return n;
    //     int F0 = 0;
    //     int F1 = 1;
    //     int F2 = 0;
    //     for(int i = 2; i <= n; i++){
    //         F2 = F1 + F0;
    //         F0 = F1;
    //         F1 = F2;
    //     }
    //     return F2;
    // }
    int fib(int n) {
       if(n <= 1) return n;
        
        return fib(n-1)+fib(n-2);
    }

};