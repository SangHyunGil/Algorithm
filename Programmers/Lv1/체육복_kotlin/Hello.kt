import java.util.*

class Solution {
    fun solution(n: Int, lost: IntArray, reserve: IntArray): Int {
        val lostSet = (lost.sorted().toMutableSet() - reserve.sorted().toMutableSet()) as MutableSet<Int>
        val reserveSet = reserve.sorted().toMutableSet() - lost.sorted().toMutableSet()

        for (reserveItem in reserveSet) {
            when {
                reserveItem-1 in lostSet -> lostSet.remove(reserveItem-1)
                reserveItem+1 in lostSet -> lostSet.remove(reserveItem+1)
            }
        }

        return n - lostSet.size
    }
}