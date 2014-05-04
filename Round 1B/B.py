import math

class Solver():
    def __init__(self, f):
        parts = f.readline().split(' ')
        self.a = int(parts[0])
        self.b = int(parts[1])
        self.k = int(parts[2])

    @staticmethod
    def num_bits(n):
        return int(math.ceil(math.log(n, 2)))


    def zero_parts(self):
        true_k = self.k - 1
        floored = int(math.log(true_k, 2))
        num_perms = floored * (2 ** floored)
        ways_to_get_zero = 0
        return ways_to_get_zero * num_perms

    @staticmethod
    def brute_force(a, b, k):
        poss = 0
        for i in xrange(a):
            for j in xrange(b):
                if i & j < k:
                    poss += 1
        return poss

    @staticmethod
    def brute_force2(a, b, k):
        poss = 0
        if k > a or k > b:
            return 0
        for i in xrange(k, a):
            for j in xrange(k, b):
                if i & j >= k:
                    poss += 1
        return poss


    @staticmethod
    def number_of_pairs(a, b, k):
        if a < b:
            tmp = a
            a = b
            b = tmp
        if k > b:
            return a * b
        elif a > b:
            return Solver.number_of_pairs(b, b, k) * (a - b)
        else:
            pass



    def solve(self):
        return str(self.a * self.b - Solver.brute_force2(self.a, self.b, self.k))


def main():
    with open('input.txt', 'rb') as f:
        num_problems = int(f.readline())
        answers = []
        for i in xrange(num_problems):
            solver = Solver(f)
            answers.append('Case #%d: %s' % (i + 1, solver.solve()))
            print "done with %d" % i
        with open('output.txt', 'w') as fout:
            fout.write('\n'.join(answers))
        print answers


if __name__ == "__main__":
    main()
