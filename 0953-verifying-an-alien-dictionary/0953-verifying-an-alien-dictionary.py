class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        order_map = {char: i for i, char in enumerate(order)}

        n = len(words)

        for i in range(n-1):
            word1 = words[i]
            word2 = words[i+1]

            for j in range(len(word1)):
                if j >= len(word2):
                    return False
                if word1[j] != word2[j]:
                    if order_map[word1[j]] > order_map[word2[j]]:
                        return False
                    else:
                        break
        return  True
        


            
            



        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna