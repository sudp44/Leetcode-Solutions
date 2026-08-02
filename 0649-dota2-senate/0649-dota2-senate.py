class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        # Two queues to hold the indices of Radiant and Dire senators
        radiant = deque()
        dire = deque()

        # Populate the queues
        for i, ch in enumerate(senate):
            if ch == 'R':
                radiant.append(i)
            else:
                dire.append(i)

        # Simulate the voting process
        while radiant and dire:
            r_idx = radiant.popleft()   # next Radiant senator
            d_idx = dire.popleft()      # next Dire senator

            # The senator with the smaller index acts first and bans the opponent.
            # The winner re-queues with an index that puts them after all current senators.
            if r_idx < d_idx:
                radiant.append(r_idx + n)
            else:
                dire.append(d_idx + n)

        return "Radiant" if radiant else "Dire"
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna