def combinationSum(candidates, target):
    result = []
    candidates.sort()
    def backtrace(start, path, cur_sum):
        if cur_sum == target:
            result.append(path.copy())
            return
        for i in range(start, len(candidates)):
            if cur_sum + candidates[i] > target:
                break
            path.append(candidates[i])
            backtrace(i, path, cur_sum + candidates[i])
            path.pop()

    backtrace(0, [], 0)
    return result


print(combinationSum([2,3,6,7], 7))