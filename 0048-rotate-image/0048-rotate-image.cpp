class Solution {
public:
    void transpose(vector<vector<int>>& matrix, int n){
        int row = n;
        int col = n;
        for(int i = 0; i < row; i++){
            for(int j = i+1; j < col; j++){
                swap(matrix[i][j], matrix[j][i]);
            }
        }
    }
    void reverse(vector<vector<int>>& matrix, int n){
        int row = n;
        int col = n;
        for(int i = 0; i < row; i++){
            for(int j = 0; j < col/2; j++){
                swap(matrix[i][j], matrix[i][col-j-1]);
            }
        }        
    }
    void rotate(vector<vector<int>>& matrix) {
        int n = matrix.size();
        transpose(matrix, n);
        reverse(matrix, n);
    }
};