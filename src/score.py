class Calculator(object):
    def __init__(self, problems, answers, full_score=100):
        self.problems = problems
        self.answers = answers
        self.answers_calculated = []
        self._calculate()
        self.full_score = full_score

    def score(self):
        single_score = self.full_score / len(self.problems)
        return round(self.how_many()*single_score, 2)

    def rate(self):
        return round(self.how_many()/len(self.problems), 2)

    def how_many(self):
        i = 0
        for a in self.answers_calculated:
            if a[0] == a[1]:
                i = i + 1
        return i

    def _calculate(self):
        exp = []
        for item in self.problems:
            item = [str(i) for i in item]
            exp.append("".join(item))
        for i in range(len(exp)):
            ans = []
            if self.answers[i] is not None:
                ans.append(self.answers[i])
                ans.append(eval(exp[i]))
            else:
                ans.append(0)
                ans.append(1)
            self.answers_calculated.append(ans)
        print(self.answers_calculated)
