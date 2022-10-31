class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        vector<int> res;
        int row = matrix.size();
        int col = matrix[0].size();
        int top = 0;
        int bottom = row-1;
        int left = 0;
        int right = col-1;
        
        while(top <= bottom && left <= right && res.size() < row*col ){
            for(int i = left; i <= right && res.size() < row*col; i++){
                res.push_back(matrix[top][i]);
            }
            top++;
            for(int i = top; i <= bottom && res.size() < row*col; i++){
                res.push_back(matrix[i][right]);
            }
            right--;
            for(int i = right; i >= left && res.size() < row*col; i--){
                res.push_back(matrix[bottom][i]);
            }
            bottom--;
            for(int i = bottom; i >= top && res.size() < row*col; i--){
                res.push_back(matrix[i][left]);
            }
            left++;
        }
        return res;
    }
};