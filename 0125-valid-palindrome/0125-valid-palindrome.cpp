class Solution {
public:
    bool isPalindrome(string s) {
        string str;
        for(int i = 0; i < s.size(); i++){
            if(s[i] >= 'a' && s[i] <= 'z' || s[i] >= '0' && s[i] <= '9'){
                str.push_back(s[i]);
            }
            else if(s[i] >= 'A' && s[i] <= 'Z'){
                str.push_back(s[i]+32);
            }
            else{
                continue;
            }
        }
        int start = 0;
        int end = str.size()-1;
        while(start <= end){
            if(str[start] != str[end]){
                return false;
            }
            else{
                start++;
                end--;
            }
        }
        return true;
    }
};