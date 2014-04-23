class Solver():
    def __init__(self, f):
        pass

    def solve(self):
        pass



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
