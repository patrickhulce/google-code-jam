class Solver():
    def __init__(self, f):
        n = f.readline()
        self.n = int(n)

        words = []
        for i in range(self.n):
            words.append(f.readline().strip())
        self.words = words

        sequences = []
        for word in words:
            sequence = [(word[0], 1)]
            for i, c in enumerate(word[1:]):
                if word[i] != c:
                    sequence.append((c, 1))
                else:
                    sequence[-1] = (sequence[-1][0], sequence[-1][1] + 1)
            sequences.append(sequence)

        self.sequences = sequences
        print self.sequences


    def solve(self):
        raw_sequences = [[x[0] for x in row] for row in self.sequences]
        #print raw_sequences
        is_possible = reduce(lambda acc, y: acc and y == raw_sequences[0], raw_sequences, True)
        if not is_possible:
            return "Fegla Won"
        raw_numbers = [[x[1] for x in row] for row in self.sequences]
        #print raw_numbers
        transposed = map(list, zip(*raw_numbers))
        averages = [sum(col) / len(col) for col in transposed]
        #print averages
        diffs = [[abs(averages[i] - x) for i, x in enumerate(row)] for row in raw_numbers]
        #print diffs
        total_diffs = [sum(row) for row in diffs]
        #print total_diffs
        return str(sum(total_diffs))




def main():
    with open('input.txt', 'rb') as f:
        num_problems = int(f.readline())
        answers = []
        for i in xrange(num_problems):
            solver = Solver(f)
            answers.append('Case #%d: %s' % (i + 1, solver.solve()))
        with open('output.txt', 'w') as fout:
            fout.write('\n'.join(answers))
        print answers


if __name__ == "__main__":
    main()
