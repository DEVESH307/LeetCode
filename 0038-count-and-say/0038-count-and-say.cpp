class Solution {
public:
    string countAndSay(int n) {
        if(n == 1) return "1";
        if(n == 2) return "11";
        
        string str = "11";
        for(int i = 3; i <= n; i++){
            string temp = "";
            str = str+"$";
            int cnt = 1;
            for(int j = 1; j < str.size(); j++){
                if(str[j-1] == str[j]){
                    cnt++;
                }
                else{
                    temp += to_string(cnt);
                    temp += str[j-1];
                    cnt = 1;
                }
            }
            str = temp;
        }
        return str;
    }
};