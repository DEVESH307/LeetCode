class Solution {
public:
    int row[4] = {1, 0, -1, 0};    
    int col[4] = {0, 1, 0, -1};
    bool wordSearchExistHelper(vector<vector<char>>& board, string &word, int i, int j, int N, int M, int k){
        if(k >= word.size())
            return true;
        if(i < 0 || i >= N || j < 0 || j >= M || board[i][j] == '.' || word[k] != board[i][j])
            return false;
        // if(word.size() == 1 && word[k] == board[i][j]) 
        //     return true;
        board[i][j] = '.';
        int ans = false;
        for(int index = 0; index < 4; index++)
            ans |= wordSearchExistHelper(board, word, i+row[index], j+col[index], N, M, k+1);
        board[i][j] = word[k];
        return ans;
    }
    bool exist(vector<vector<char>>& board, string word) {
        int N = board.size();    
        // if(N == 0) return false;
        int M = board[0].size();
        int k = word.size();
        // if(k == 0) return false;
        for(int i = 0; i < N; i++)
            for(int j = 0; j < M; j++)
                if(board[i][j] == word[0])
                    if(wordSearchExistHelper(board, word, i, j, N, M, 0))
                        return true;
        return false;
    }
};