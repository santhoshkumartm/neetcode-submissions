class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Step 1: Target frequency map (DO NOT change this)
        target = {}
        for c in t:
            target[c] = target.get(c, 0) + 1
        
        # Step 2: Window frequency map
        window = {}
        
        # Step 3: Pointers and counters
        left = 0
        have = 0           # How many unique characters in target are FULLY matched
        need = len(target) # Total unique characters needed
        
        # Step 4: Track the best answer
        start_idx = 0
        min_len = float('inf')
        
        # Step 5: Slide the right pointer
        for right in range(len(s)):
            right_char = s[right]
            
            # Add current character to window
            window[right_char] = window.get(right_char, 0) + 1
            
            # If this character is in target AND we just reached the required count
            if right_char in target and window[right_char] == target[right_char]:
                have += 1
            
            # Step 6: While the window is VALID (we have all chars)
            while have == need:
                # Update answer if this window is smaller
                curr_len = right - left + 1
                if curr_len < min_len:
                    min_len = curr_len
                    start_idx = left
                
                # Step 7: Shrink from the LEFT
                left_char = s[left]
                window[left_char] -= 1
                
                # If the left char was crucial and now we don't have enough of it
                if left_char in target and window[left_char] < target[left_char]:
                    have -= 1
                
                # Move the left pointer forward
                left += 1
        
        # Return the result
        return s[start_idx:start_idx + min_len] if min_len != float('inf') else ""