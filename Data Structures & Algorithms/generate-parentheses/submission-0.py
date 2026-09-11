class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        path = []
        def dfs(opencount, closecount):
            if len(path) == 2*n:
                res.append("".join(path))
                return
            
            if opencount < n:
                path.append("(")
                dfs(opencount+1,closecount)
                path.pop()
            
            if closecount < opencount:
                path.append(")")
                dfs(opencount,closecount+1)
                path.pop()
            
        dfs(0,0)
        return res