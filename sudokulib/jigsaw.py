import sys

from decorators import requires_solution
from sudoku import Sudoku

class JigsawSudoku(Sudoku):
    VALID_SIZES = (3,)
    REGIONS = (
        ( 0, 1, 2, 9,10,11,18,27,28),
        ( 3,12,13,14,23,24,25,34,35),
        ( 4, 5, 6, 7, 8,15,16,17,26),
        (19,20,21,22,29,36,37,38,39),
        (30,31,32,33,40,47,48,49,50),
        (41,42,43,44,51,58,59,60,61),
        (45,46,55,56,57,66,67,68,77),
        (52,53,62,69,70,71,78,79,80),
        (54,63,64,65,72,73,74,75,76),
    )
    REGION_COLORS = (
        (41, 30), (42, 30), (43, 30),
        (44, 30), (45, 30), (46, 30),
        (47, 30), (41, 30), (42, 30),
    )

    def get_region(self, row, col):
        index = self.row_col_to_index(row, col)
        return self.get_region_by_index(index)

    def get_region_by_index(self, index):
        """Returns values used in the region at the specified index"""

        for region in JigsawSudoku.REGIONS:
            if index in region:
                return [self.solution[i] for i in region]

        raise ValueError('Invalid index')

    @requires_solution
    def print_grid(self, grid):
        """Prints a nicely formatted version of the Sudoku grid"""

        fmt = '\033[%s;%sm'
        norm = '\033[0m'
        field_width = len(str(self.side_length)) + 2

        for i, val in enumerate(grid):
            if i % 9 == 0 and i > 0:
                sys.stdout.write('\n')

            for rid, r in enumerate(self.REGIONS):
                if i in r:
                    region_id = rid
                    break

            col = fmt % self.REGION_COLORS[region_id]
            val = str(val).center(field_width)
            sys.stdout.write('%s%s%s' % (col, val, norm))

        sys.stdout.write('\n')

def main():
    s = JigsawSudoku()
    s.print_masked()
    #print '=' * 50
    s.print_solution()

    #s.clear()
    #s.init_grid([3,0,0,0,0,0,0,0,4,0,0,2,0,6,0,1,0,0,0,1,0,9,0,8,0,2,0,0,0,5,0,0,0,6,0,0,0,2,0,0,0,0,0,1,0,0,0,9,0,0,0,8,0,0,0,8,0,3,0,4,0,6,0,0,0,4,0,1,0,9,0,0,5,0,0,0,0,0,0,0,7])
    #s.print_masked()
    #print '=' * 50
    #s.print_solution()

if __name__ == '__main__':
    main()
