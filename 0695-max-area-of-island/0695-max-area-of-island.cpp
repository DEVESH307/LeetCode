class Solution {
public:
    int row[4] = {1, 0, -1, 0};
    int col[4] = {0, 1, 0, -1};
    int areaOfIsland(vector<vector<int>>& grid, int r, int c){
        if(r < 0 || r >= grid.size() || c < 0 || c >= grid[0].size() || grid[r][c] == 0)
            return 0;
        grid[r][c] = 0;
        int ans = 1;
        for(int i = 0; i < 4; i++)
            ans += areaOfIsland(grid, r+row[i], c+col[i]);
        return ans;
    }
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        int maxArea = 0;
        for(int r = 0; r < grid.size(); r++)
            for(int c = 0; c < grid[0].size(); c++)
                if(grid[r][c] == 1)
                    maxArea = max(maxArea, areaOfIsland(grid, r, c));
        return maxArea;
    }
};