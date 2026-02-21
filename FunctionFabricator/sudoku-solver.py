from typing import Optional


def solve_sudoku(grid: list[list[int]]) -> Optional[list[list[int]]]:
    """
    Solve a 9x9 Sudoku puzzle using a backtracking algorithm.

    Args:
        grid: A 9x9 list of lists where empty cells are represented by 0
              and filled cells contain integers from 1 to 9.

    Returns:
        The solved 9x9 grid if a solution exists, or None if the puzzle
        is invalid or unsolvable.
    """

    # --- Input Validation ---

    def is_valid_grid(grid: list[list[int]]) -> bool:
        """Validate that the input is a well-formed 9x9 Sudoku grid."""

        # Check that the grid is a list of 9 rows
        if not isinstance(grid, list) or len(grid) != 9:
            return False

        for row in grid:
            # Each row must be a list of exactly 9 elements
            if not isinstance(row, list) or len(row) != 9:
                return False
            for cell in row:
                # Each cell must be an integer between 0 and 9
                if not isinstance(cell, int) or cell < 0 or cell > 9:
                    return False

        return True

    def has_no_duplicates(grid: list[list[int]]) -> bool:
        """
        Check that no row, column, or 3x3 subgrid contains duplicate
        non-zero values. This ensures the initial configuration is a
        legitimate Sudoku starting state.
        """

        # Check each row for duplicates
        for row in range(9):
            seen = set()
            for col in range(9):
                num = grid[row][col]
                if num != 0:
                    if num in seen:
                        return False
                    seen.add(num)

        # Check each column for duplicates
        for col in range(9):
            seen = set()
            for row in range(9):
                num = grid[row][col]
                if num != 0:
                    if num in seen:
                        return False
                    seen.add(num)

        # Check each 3x3 subgrid for duplicates
        for box_row in range(3):
            for box_col in range(3):
                seen = set()
                for row in range(box_row * 3, box_row * 3 + 3):
                    for col in range(box_col * 3, box_col * 3 + 3):
                        num = grid[row][col]
                        if num != 0:
                            if num in seen:
                                return False
                            seen.add(num)

        return True

    # Perform all validation checks before attempting to solve
    if not is_valid_grid(grid):
        return None

    if not has_no_duplicates(grid):
        return None

    # --- Solver Logic ---

    def is_valid_placement(row: int, col: int, num: int) -> bool:
        """
        Determine whether placing `num` at position (row, col) is valid
        according to Sudoku rules (no duplicate in the same row, column,
        or 3x3 subgrid).
        """

        # Check the row for conflicts
        for c in range(9):
            if grid[row][c] == num:
                return False

        # Check the column for conflicts
        for r in range(9):
            if grid[r][col] == num:
                return False

        # Check the 3x3 subgrid for conflicts
        start_row, start_col = (row // 3) * 3, (col // 3) * 3
        for r in range(start_row, start_row + 3):
            for c in range(start_col, start_col + 3):
                if grid[r][c] == num:
                    return False

        return True

    def find_empty_cell() -> Optional[tuple[int, int]]:
        """
        Find the next empty cell (value 0) in the grid, scanning
        left-to-right, top-to-bottom.

        Returns:
            A tuple (row, col) of the empty cell, or None if the grid
            is completely filled.
        """
        for row in range(9):
            for col in range(9):
                if grid[row][col] == 0:
                    return (row, col)
        return None

    def backtrack() -> bool:
        """
        Recursively attempt to fill empty cells using numbers 1-9.
        If a placement leads to a dead end, undo it (backtrack) and
        try the next candidate.

        Returns:
            True if the puzzle is solved, False if no solution exists
            from the current state.
        """

        # Find the next empty cell; if none remain, the puzzle is solved
        empty = find_empty_cell()
        if empty is None:
            return True

        row, col = empty

        # Try each candidate number from 1 to 9
        for num in range(1, 10):
            if is_valid_placement(row, col, num):
                # Place the number tentatively
                grid[row][col] = num

                # Recurse to try filling the rest of the grid
                if backtrack():
                    return True

                # Undo the placement (backtrack) if it didn't lead to a solution
                grid[row][col] = 0

        # No valid number found for this cell — trigger backtracking
        return False

    # --- Execute ---

    if backtrack():
        return grid
    else:
        return None


# --- Demo / Manual Testing ---

if __name__ == "__main__":
    # A sample puzzle (0 represents empty cells)
    puzzle = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9],
    ]

    print("Input puzzle:")
    for row in puzzle:
        print(row)

    solution = solve_sudoku(puzzle)

    if solution is not None:
        print("\nSolved puzzle:")
        for row in solution:
            print(row)
    else:
        print("\nNo solution found (puzzle is invalid or unsolvable).")
