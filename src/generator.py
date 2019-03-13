from src.config import Ledt, Chkb
import random


class Generator(object):
    def __init__(self, args):
        self.amount = args[Ledt.ledt_amount]
        self.less_than = args[Ledt.ledt_less_than]
        self.item_num = args[Ledt.ledt_item_num]
        self.operators = list(set(args[Ledt.ledt_operator]))
        self.operators_set = ['+', '-', '*', '/', '%']
        self.decimal = args[Chkb.chkb_decimal]
        self.decimals = args[Ledt.ledt_decimal]

    def generate(self):
        exp_all = []
        for a in range(self.amount):
            tmp = []
            op = self.operators[random.randint(0, len(self.operators) - 1)]
            for item in range(self.item_num):
                num = None
                if not self.decimal or op == '%':
                    num = random.randint(1, self.less_than)
                else:
                    num = round(random.uniform(1, self.less_than), self.decimals)
                tmp.append(num)
                tmp.append(op)
            exp_all.append(tmp[:-1])
        return exp_all
