def countTriangles(sticks):
    sticks.sort()
    triangles = 0
    n = len(sticks)
    
    for big in range(n - 1, 1, -1):
        left, right = 0, big - 1
        while left < right:
            if sticks[left] + sticks[right] > sticks[big]:
                triangles += (right - left)
                right -= 1
            else:
                left += 1
                
    return triangles

# Test cases
print(countTriangles([2, 2, 3, 4]))  
print(countTriangles([4, 2, 3, 4])) 
