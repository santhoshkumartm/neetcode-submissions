class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prevMap={i:[] for i in range(numCourses)}

        for crs ,pre in prerequisites:
            prevMap[crs].append(pre)

        visited=set()

        def dfs(crs):
            if prevMap[crs]==[]:
                return True
            if crs in visited:
                return False
            visited.add(crs)
            for pre in prevMap[crs]:
                if not dfs(pre):return False
            visited.remove(crs)
            prevMap[crs]=[]
            return True

        for crs in range(numCourses):
            if not dfs(crs):return False
        return True


        