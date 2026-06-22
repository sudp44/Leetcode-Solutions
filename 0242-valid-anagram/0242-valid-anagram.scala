object Solution {
    def isAnagram(s: String, t: String): Boolean = {
        if (s.length != t.length){
            return false
        }
        val charCount = new Array[Int](26)
        for (i <- 0 until s.length){
            charCount(s(i) - 'a') += 1
            charCount(t(i) - 'a') -= 1
        }
        var c = 0
        while (c < 26){
            if (charCount(c) != 0){
                return false
            }
            c += 1
        }
        return  true
    }
}
// TC: O(n), SC: O(1)

// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna