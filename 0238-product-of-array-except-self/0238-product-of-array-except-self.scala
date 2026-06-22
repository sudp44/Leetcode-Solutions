object Solution {
    def productExceptSelf(nums: Array[Int]): Array[Int] = {
        val n = nums.length

        val result = new Array[Int](n)
        java.util.Arrays.fill(result, 1)

        var pre = 1
        var post = 1

        for (i <- nums.indices){
            result(i) = pre
            pre = pre * nums(i)
        }

        for (i <- nums.indices.reverse){
            result(i) = post * result(i)
            post = post * nums(i)
        }

        return result
    }
}

// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna