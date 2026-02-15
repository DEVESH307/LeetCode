// class Solution {
// public:
//     int row[4] = {1, 0, -1, 0};
//     int col[4] = {0, 1, 0, -1};
//     int orangesRotting(vector<vector<int>>& grid) {
//         int time = 0;
//         int n = grid.size();
//         int m = grid[0].size();
//         queue<pair<int, int>> Q;
//         for(int i = 0; i < n; i++){
//             for(int j = 0; j < m; j++){
//                 if(grid[i][j] == 2){
//                     Q.push({i, j});
//                 }
//             }
//         }
//         Q.push({-1, -1});
//         // return time;
//         while(Q.size() > 1){
//             auto frontElem = Q.front();
//             Q.pop();
//             for(int i  = 0; i < 4; i++){
//                 int x = frontElem.first+row[i];
//                 int y = frontElem.second+col[i];
//                 if(x >= 0 && x < n && y >= 0 && y < m && grid[x][y] == 1){
//                     grid[x][y] = 2;
//                     Q.push({x, y});
//                 }
//             }
//             if (frontElem.first == -1 && frontElem.second == -1){
//                 Q.push({-1, -1});
//                 time++;
//                 continue;
//             }  
//         }
//         // return time;
//         for(int i = 0; i < n; i++){
//             for(int j = 0; j < m; j++){
//                 if(grid[i][j] == 1){
//                     return -1;
//                 }
//             }
//         }
//         return time;
//     }
// };


class Solution {
public:
    int row[4] = {1, 0, -1, 0};
    int col[4] = {0, 1, 0, -1};
    int orangesRotting(vector<vector<int>>& grid) {
        int time = 0;
        int n = grid.size();
        int m = grid[0].size();
        queue<pair<int, int>> Q;
        for(int i = 0; i < n; i++){
            for(int j = 0; j < m; j++){
                if(grid[i][j] == 2){
                    Q.push({i, j});
                }
            }
        }
        while(!Q.empty()){
            int size = Q.size();
            int can_rot = 0;
            for(int i = 0; i < size; i++){
                auto frontElem = Q.front();
                Q.pop();
                for(int j  = 0; j < 4; j++){
                    int x = frontElem.first+row[j];
                    int y = frontElem.second+col[j];
                    if(x >= 0 && x < n && y >= 0 && y < m && grid[x][y] == 1){
                        grid[x][y] = 2;
                        Q.push({x, y});
                        can_rot = 1;
                    }
                }
            }
            time += can_rot;
        }
        for(int i = 0; i < n; i++){
            for(int j = 0; j < m; j++){
                if(grid[i][j] == 1){
                    return -1;
                }
            }
        }
        return time;
    }
};