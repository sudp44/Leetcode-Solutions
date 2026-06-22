import scala.collection.mutable.HashSet
object Solution {
    def containsDuplicate(nums: Array[Int]): Boolean = {

        val n = nums.length
        var i = 0
        val hs = HashSet[Int]()

        while(i < n){
            if (hs.contains(nums(i))){
                return true
            } else{
                hs += nums(i)
            }
            i += 1
        }
        return  false
    }
}

// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna