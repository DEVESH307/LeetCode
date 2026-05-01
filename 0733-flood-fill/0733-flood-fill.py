class Solution:
    def floodFill(self, image, sr, sc, color):
        n = len(image)
        m = len(image[0])

        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        initial_color = image[sr][sc]

        if initial_color == color:
            return image

        def dfs(r, c):
            # boundary + color check
            if r < 0 or r >= n or c < 0 or c >= m:
                return
            if image[r][c] != initial_color:
                return

            image[r][c] = color

            for dr, dc in directions:
                dfs(r + dr, c + dc)

        dfs(sr, sc)
        return image