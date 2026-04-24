class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        # Count occurrences using the built-in count method
        l_count = moves.count('L')
        r_count = moves.count('R')
        under_count = moves.count('_')
        
        # The trick: (Absolute difference of L and R) + all underscores
        # Because underscores can always extend the path of the majority direction
        return abs(l_count - r_count) + under_count