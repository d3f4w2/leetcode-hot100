
class MinStack:
    def __init__(self):
        self.stack = []
        self.minstack = []
        
    def push(self, val):
        self.stack.append(val)
        if not self.minstack or val <= self.minstack[-1]:
            self.minstack.append(val)
    
    def pop(self):
        if self.stack.pop() == self.minstack[-1]:
            self.minstack.pop()
    
    def top(self):
        return self.stack[-1]
    
    def getMin(self):
        return self.minstack[-1]

    
if __name__ == "__main__":
    minStack = MinStack()
    
    print("操作: push(-2)")
    minStack.push(-2)
    
    print("操作: push(0)")
    minStack.push(0)
    
    print("操作: push(-3)")
    minStack.push(-3)
    
    # 此时最小值应该是 -3
    current_min = minStack.getMin()
    print(f"getMin() -> {current_min} (期望: -3) {'✅' if current_min == -3 else '❌'}")
    
    print("操作: pop() (弹出 -3)")
    minStack.pop()
    
    # 此时栈顶应该是 0
    top_val = minStack.top()
    print(f"top() -> {top_val} (期望: 0) {'✅' if top_val == 0 else '❌'}")
    
    # 此时最小值应该回退到 -2
    current_min = minStack.getMin()
    print(f"getMin() -> {current_min} (期望: -2) {'✅' if current_min == -2 else '❌'}")

    # --- 额外测试：重复最小值的情况 ---
    print("\n--- 额外测试：重复最小值 ---")
    minStack2 = MinStack()
    minStack2.push(5)
    minStack2.push(5) # 压入相同的最小值
    minStack2.push(3) # 压入更小的
    
    print(f"getMin() -> {minStack2.getMin()} (期望: 3)")
    
    minStack2.pop() # 弹出 3
    print(f"getMin() -> {minStack2.getMin()} (期望: 5)")
    
    minStack2.pop() # 弹出一个 5
    # 关键点：因为还有一个 5 在栈里，最小值应该还是 5
    print(f"getMin() -> {minStack2.getMin()} (期望: 5) {'✅' if minStack2.getMin() == 5 else '❌'}")
    
    minStack2.pop() # 弹出最后一个 5
    # 栈空了，通常题目保证不会对空栈调用 getMin，但逻辑上最小栈也应空
    print(f"栈是否为空: {len(minStack2.stack) == 0}")