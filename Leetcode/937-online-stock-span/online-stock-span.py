class StockSpanner:
    def __init__(self):
        # Initialize your monotonic stack here to persist across calls
        self.stack = [] # Stores tuples of (price, span)

    def next(self, price: int) -> int:
        span = 1
        # Look back at previous days stored in your persistent stack
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]
            
        self.stack.append((price, span))
        return span