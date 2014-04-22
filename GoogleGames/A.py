class Solver():
    def __init__(self, f):
        num_cities = int(f.readline())
        pants = {}
        for i in range(num_cities):
            city, color, score = f.readline().split(' ')
            score = int(score.strip())
            if color not in pants:
                pants[color] = {}
            color_p = pants[color]
            if score not in color_p:
                color_p[score] = city
            elif color_p[score] != city:
                color_p[score] = None

        self.pants = pants

    def solve(self):
        num = 0
        for color in self.pants.keys():
            num += sum([0 if x is None else 1 for x in self.pants[color].values()])
        return num



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
