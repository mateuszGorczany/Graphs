from copy import copy

class SequenceChecker:    
    def __init__(self):
        self.seq = []

    def check_sequence(self, seq):
        self.seq = copy(seq)
        self.seq = sorted(self.seq)
        self.seq.reverse()
        
        if not self.is_uneven_even():
            return False

        while True:
            if self.is_all_zero():
                return True
            if self.seq[0] < 0 or self.seq[0] >= len(self.seq) or self.is_smth_negative():
                return False
            for i in range(1, self.seq[0]+1):
                self.seq[i] = self.seq[i] - 1
            self.seq[0] = 0
            self.seq = sorted(self.seq)
            self.seq.reverse()

    def is_all_zero(self):
        for val in self.seq:
            if val != 0:
                return False
        return True

    def is_smth_negative(self):
        n = len(self.seq)
        for i in range(1, n):
            if self.seq[i] < 0:
                return True
        return False

    def is_uneven_even(self):
        count = 0
        for val in self.seq:
            if val%2 == 1:
                count += 1
        if count %2 == 0:
            return True
        return False
