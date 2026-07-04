import scala.collection.mutable

class TimeMap() {
    // Maps a String key to a mutable TreeMap that sorts keys in ascending order
    private val map = mutable.Map[String, mutable.TreeMap[Int, String]]()

    def set(key: String, value: String, timestamp: Int): Unit = {
        // Retrieve the tree map or initialize a new one if it doesn't exist
        val treeMap = map.getOrElseUpdate(key, mutable.TreeMap[Int, String]())
        treeMap.put(timestamp, value)
    }

    def get(key: String, timestamp: Int): String = {
        map.get(key) match {
            case None => ""
            case Some(treeMap) =>
                // maxBefore returns an Option[(Int, String)] for the largest key <= timestamp
                treeMap.maxBefore(timestamp + 1) match {
                    case None => ""
                    case Some((_, value)) => value
                }
        }
    }
}


/**
 * Your TimeMap object will be instantiated and called as such:
 * val obj = new TimeMap()
 * obj.set(key,value,timestamp)
 * val param_2 = obj.get(key,timestamp)
 */

// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna