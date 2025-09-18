public class Sudoku {

  public boolean isSafe(char[][] board, int row, int col, int val) {
    for(int i=0; i<board.length; i++){
      if(board[row][i] == (char)(val + '0')){
        return false;
      }
      if(board[i][col] == (char)(val + '0')){
        return false;
      }
      if(board[3 * (row / 3) + i / 3][3 * (col / 3) + i % 3] == (char)(val + '0')){
        return false;
      }
    }
    return true;
  }

  public boolean helper(char[][] board, int row, int col) {
    if(row == board.length){
      return true;
    }
    int newRow;
    int newCol;
    if(col != board.length - 1){
      newRow = row;
      newCol = col + 1;
    } else {
      newRow = row + 1;
      newCol = 0;
    }
    if(board[row][col] != '.'){
      if(helper(board, newRow, newCol)){
        return true;
      }
    } else {
      for(int i=0; i<board.length; i++){
        if(isSafe(board, row, col, i)){
          board[row][col] = (char)(i + '0');
          if(helper(board, newRow, newCol)){
            return true;
          } else {
            board[row][col] = '.';
          }
        }
      }
    }
    return false;
  }

  public void solveSudoku(char[][] board) {
    helper(board, 0, 0);
  }
  public static void main(String[] args) {
    Sudoku sudoku = new Sudoku();
    char[][] board = {
      {'5','3','.','.','7','.','.','.','.'},
      {'6','.','.','1','9','5','.','.','.'},
      {'.','9','8','.','.','.','.','6','.'},
      {'8','.','.','.','6','.','.','.','3'},
      {'4','.','.','8','.','3','.','.','1'},
      {'7','.','.','.','2','.','.','.','6'},
      {'.','6','.','.','.','.','2','8','.'},
      {'.','.','.','4','1','9','.','.','5'},
      {'.','.','.','.','8','.','.','7','9'}
    };
    sudoku.solveSudoku(board);
    for(int i=0; i<board.length; i++){
      for(int j=0; j<board[0].length; j++){
        System.out.print(board[i][j] + " ");
      }
      System.out.println();
    }
  }
}
