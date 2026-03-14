def jump(nums):
    jumps= 0
    end = 0
    max_pos = 0

    for i in range(len(nums)-1):
        max_pos = max(max_pos, nums[i] + i)
        if i == end:
            jumps += 1
            end = max_pos
        
    return jumps

print(jump([1, 3, 5]))