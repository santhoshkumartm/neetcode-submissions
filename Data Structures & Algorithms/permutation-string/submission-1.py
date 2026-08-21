class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Length mismatch-ae illana, return False
        if len(s1) > len(s2):
            return False
        
        n = len(s1)
        
        # Step 1: s1-oda Frequency Map (Target)
        target = {}
        for c in s1:
            target[c] = target.get(c, 0) + 1
        
        # Step 2: First Window (size n) - s2-oda starting index-la irundhu
        window = {}
        for i in range(n):
            window[s2[i]] = window.get(s2[i], 0) + 1
        
        # Step 3: First window-ai check pannu
        if window == target:
            return True
        
        # Step 4: Window-ai Slide பண்ணு (right side add, left side remove)
        for i in range(n, len(s2)):
            # ----------- ADD (Right side) ----------
            right_char = s2[i]
            window[right_char] = window.get(right_char, 0) + 1
            
            # ----------- REMOVE (Left side) ----------
            left_char = s2[i - n]   # Window-ai vittu veliya pogura character
            window[left_char] -= 1
            if window[left_char] == 0:
                del window[left_char]   # 0-va irundha, map-la irundhu full-aa remove pannidu (comparison clean-aa irukka)
            
            # ----------- CALCULATE / COMPARE ----------
            if window == target:
                return True
        
        return False