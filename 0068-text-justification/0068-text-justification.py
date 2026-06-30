class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        result = []
        n = len(words)
        index = 0
        
        while index < n:
            total_chars = len(words[index])
            last = index + 1
            
            # Determine the last word that fits on the current line
            while last < n:
                if total_chars + 1 + len(words[last]) > maxWidth:
                    break
                total_chars += 1 + len(words[last])
                last += 1
                
            line = []
            diff = last - index - 1  # Number of gaps between words
            
            # If this is the last line or contains only one word, left-justify
            if last == n or diff == 0:
                for i in range(index, last):
                    line.append(words[i])
                    if i < last - 1:
                        line.append(" ")
                
                # Form the string and pad the rest with spaces
                current_line_str = "".join(line)
                remaining_spaces = maxWidth - len(current_line_str)
                current_line_str += " " * remaining_spaces
            else:
                spaces = (maxWidth - total_chars) // diff
                extra_spaces = (maxWidth - total_chars) % diff
                
                for i in range(index, last):
                    line.append(words[i])
                    if i < last - 1:
                        spaces_to_apply = spaces + (1 if (i - index) < extra_spaces else 0)
                        line.append(" " * (spaces_to_apply + 1)) # +1 for basic word separation
                
                current_line_str = "".join(line)
                
            result.append(current_line_str)
            index = last
            
        return result


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna