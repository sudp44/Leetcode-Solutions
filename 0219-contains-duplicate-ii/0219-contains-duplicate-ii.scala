import scala.collection.mutable.HashSet
object Solution {
    def containsNearbyDuplicate(nums: Array[Int], k: Int): Boolean = {
        val n = nums.length
        val hs = HashSet[Int]()
        var i = 0
        while(i < n){
            if (hs.contains(nums(i))){
                return true
            } else {
                hs += nums(i)
            }
            if (hs.size > k){
                hs -= nums(i-k)
            }
            i += 1
        }
        return false
    }
}
//TC, SC: O(n)

// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna