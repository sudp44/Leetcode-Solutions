import scala.collection.mutable._
object Solution {
    def groupAnagrams(strs: Array[String]): List[List[String]] = {
        if (strs.isEmpty){
            return List.empty[List[String]]
        }
        
        val ansMap = HashMap[String, ArrayBuffer[String]]()
        val count = new Array[Int](26)

        
        for (s <- strs){
            java.util.Arrays.fill(count, 0)
            for (c <- s){
                count(c - 'a') += 1
            }
            val sb = new StringBuilder("")

            for (i <- count){
                sb.append("#")
                sb.append(i)
            } 

            val key = sb.toString
            
            if (!ansMap.contains(key)){
                ansMap += (key -> ArrayBuffer[String]())
            }

            ansMap(key).append(s) 
        }

        ansMap.values.map(_.toList).toList        
    }
}

// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna