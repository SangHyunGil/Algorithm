class Solution {
    var answer: ArrayList<Int> = arrayListOf()
    var score = intArrayOf(0, 0, 0)
    var method1 = intArrayOf(1, 2, 3, 4, 5)
    var method2 = intArrayOf(2, 1, 2, 3, 2, 4, 2, 5)
    var method3 = intArrayOf(3, 3, 1, 1, 2, 2, 4, 4, 5 , 5)

    fun solution(answers: IntArray): IntArray {
        for (i in answers.indices) {
            score[0] += if (method1[i%5] == answers[i]) 1 else 0
            score[1] += if (method2[i%8] == answers[i]) 1 else 0
            score[2] += if (method3[i%10] == answers[i]) 1 else 0
        }

        val max = score.maxOrNull()
        for (i in score.indices) {
            if (max == score[i])
                answer.add(i+1)
        }
        return answer.toIntArray()
    }
}