class Solution {
public:
    bool isPalindrome(int n) {
        long reverse = 0;
        int temp = n;
        if(temp < 0) return false;
        while(temp){
            reverse = reverse*10+temp%10;
            temp /= 10;
        }
        // if(n < 0) reverse *= -1;
        // cout<<reverse<<endl;
        if(reverse == n) return true;
        else return false;
    }
};