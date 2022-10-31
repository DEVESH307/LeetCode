class Solution {
public:
    int dx[8] = {1, 1, 0, -1, -1, -1, 0, 1};
    int dy[8] = {0, 1, 1, 1, 0, -1, -1, -1};
    void gameOfLife(vector<vector<int>>& board) {
        int m = board.size();        
        int n = board[0].size();
        for(int x = 0; x < m; x++){
            for(int y = 0; y < n; y++){
                int curr_live_neighbours = 0;
                for(int i = 0; i < 8; i++){
                    if(x+dx[i] >= 0 && x+dx[i] < m && y+dy[i] >= 0 && y+dy[i] < n && abs(board[x+dx[i]][y+dy[i]]) == 1){
                        curr_live_neighbours++;
                    }
                }
                if(board[x][y] == 1 && (curr_live_neighbours < 2 || curr_live_neighbours > 3))
                    board[x][y] = -1;  
                if(board[x][y] == 0 && curr_live_neighbours == 3)
                    board[x][y] = 2;
            }
        }
        for(int x = 0; x < m; x++){
            for(int y = 0; y < n; y++){
                if(board[x][y] >= 1)
                    board[x][y] = 1;
                else
                    board[x][y] = 0;
            }
        }
    }
};