import java.util.*

class Failure(
    val rate: Double,
    val level: Int
) {
}

class Solution {
    fun solution(N: Int, stages: IntArray): IntArray {
        val numOfClearMember = IntArray(N)
        stages.forEach {
            numOfClearMember[it-1] += 1
        }

        val answer = ArrayList<Failure>(N)
        val participant = stages.size
        for (level in numOfClearMember.indices) {
            if (participant > 0) {
                answer.add(Failure(numOfClearMember[level].toDouble()/participant, level))
            } else {
                answer.add(Failure(0.0, level))
            }
        }

        println(answer)

        return answer
            .sortedWith(Comparator.comparing(Failure::rate).reversed().thenComparing(Failure::level))
            .map { it.level }
            .toIntArray()
    }
}
