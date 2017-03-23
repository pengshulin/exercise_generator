"""Decorators used in Sudoku"""

def check_length(func):
    """Ensures that the provided list of values has a valid length"""

    def wrapped(self, num, values):
        if len(values) == self.side_length:
            return func(self, num, values)
        else:
            raise ValueError('Invalid values.  Please specify a list of %i values.' % self.side_length)
    return wrapped

def handle_negative(func):
    """Handles negative values for get_row and get_col"""

    def wrapped(self, num):
        if num < 0:
            num = self.side_length + num
        return func(self, num)
    return wrapped

def requires_solution(func):
    """Solves the puzzle before returning"""

    def wrapped(self, *args, **kwargs):
        if None in self.solution:
            self.solve()

        return func(self, *args, **kwargs)
    return wrapped

