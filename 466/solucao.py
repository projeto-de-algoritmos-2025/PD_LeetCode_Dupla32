class Solution:
    def getMaxRepetitions(self, s1, n1, s2, n2):
        if n1 == 0:
            return 0

        s1_len = len(s1)
        s2_len = len(s2)
        index = 0
        count = 0
        recall = dict()

        for i in range(n1):
            for j in range(s1_len):
                if s1[j] == s2[index]:
                    index += 1
                    if index == s2_len:
                        index = 0
                        count += 1

            if index in recall:
                i_prime, count_prime = recall[index]
                pre_loop = (i_prime, count_prime)
                in_loop = (i - i_prime, count - count_prime)

                loop_count = (n1 - pre_loop[0] - 1) // in_loop[0]
                total = pre_loop[1] + loop_count * in_loop[1]

                rest = (n1 - pre_loop[0] - 1) % in_loop[0]

                for _ in range(rest):
                    for j in range(s1_len):
                        if s1[j] == s2[index]:
                            index += 1
                            if index == s2_len:
                                index = 0
                                total += 1
                return total // n2
            else:
                recall[index] = (i, count)

        return count // n2
