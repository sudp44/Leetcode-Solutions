import scala.collection.mutable.HashMap

object Solution {
    def twoSum(nums: Array[Int], target: Int): Array[Int] = {
        
        val hm = new HashMap[Int, Int]()
        var i = 0
        
        while (i < nums.length){
            val k = target - nums(i)
            if (hm.contains(k)){
                return Array(i, hm(k))
                } else {
                    hm += (nums(i) -> i)
                }
                i += 1
        }
        Array.empty[Int]
    }
}

// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna