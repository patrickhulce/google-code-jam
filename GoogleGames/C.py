import math

class Solver():
    def __init__(self, f):
        parts = f.readline().split(' ')
        self.num_sides = int(parts[0])
        self.target_score = float(parts[1])
        self.table = {}

    def probability(self, sum, number):
        if sum in self.table and number in self.table[sum]:
            return self.table[sum][number]
        if number == 1:
            ans = min(1.0, sum / self.num_sides)
            if sum not in self.table:
                self.table[sum] = {}
            self.table[sum][number] = ans
            return ans
        if sum < 1:
            return 1.0
        ans = 0.0
        for i in range(1, min(self.num_sides, int(number))):
            ans += self.probability(sum - i, number - 1) * (1.0 / self.num_sides)
        if sum not in self.table:
            self.table[sum] = {}
        self.table[sum][number] = ans
        print "%f - %d : %f" % (sum, number, ans)
        return ans

    def solve(self):
        self.probability(self.target_score, 1)
        print self.table
        return 0.0




def main():
    with open('input.txt','rb') as f:
        num_problems = int(f.readline())
        answers = []
        for i in xrange(num_problems):
            solver = Solver(f)
            answers.append('Case #%d: %s' % (i+1, solver.solve()))
        with open('output.txt', 'w') as fout:
            fout.write('\n'.join(answers))
        print answers


if __name__ == "__main__":
    main()
