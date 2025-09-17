
import java.util.List;

public class BackTracking {
  public static void printPermutation(String str, String perm, int idx){
    if(str.length() == 0){
      System.out.println(perm);
      return;
    }
    for(int i=0;i<str.length();i++){
      char currChar = str.charAt(i);
      String newStr = str.substring(0,i) + str.substring(i+1);
      printPermutation(newStr, perm + currChar, idx+1);
    }
  }
  public boolean isSafe(char[][] board, int row, int col){
    // vertical up
    for(int i=0;i<board[0].length;i++){
      if(board[i][col] == 'Q'){
        return false;
      }
    }
    // vertical down
    for(int i=0;i<board.length;i++){
      if(board[row][i] == 'Q'){
        return false;
      }
    }
    // diagonal left up
    for(int i=row,j=col;i>=0 && j>=0;i--,j--){
      if(board[i][j] == 'Q'){
        return false;
      }
    }
    // diagonal left down
    for(int i=row,j=col;i<board.length && j>=0;i++,j--){
      if(board[i][j] == 'Q'){
        return false;
      }
    }
    // diagonal right up
    for(int i=row,j=col;i>=0 && j<board.length;i--,j++){
      if(board[i][j] == 'Q'){
        return false;
      }
    }
    // diagonal right down
    for(int i=row,j=col;i<board.length && j<board.length;i++,j++){
      if(board[i][j] == 'Q'){
        return false;
      }
    }
    return true;
  }
  public void saveBoard(char[][] board, List<List<String>> allBoards){
    List<String> newBoard = new java.util.ArrayList<>();
    for (char[] chars : board) {
      String row = "";
      for (char cell : chars) {
        if (cell == 'Q') {
          row += 'Q';
        } else {
          row += '.';
        }
      }
      newBoard.add(row);
    }
    allBoards.add(newBoard);
  }
  public void helper(char[][] board, List<List<String>> allBoards, int col){
    if(col == board.length){
      saveBoard(board, allBoards);
      return;
    }
    for(int row=0;row<board.length;row++){
      if(isSafe(board, row, col)){
        board[row][col] = 'Q';
        helper(board, allBoards, col + 1);
        board[row][col] = '.';
      }
    }
  }
  public List<List<String>> solveNQueens(int n) {
    List<List<String>> allBoards = new java.util.ArrayList<>();
    char[][] board = new char[n][n];
    helper(board, allBoards, n);
    return allBoards;
  }
  public static void main(String[] args) {
    String str = "ABC";
    printPermutation(str, "", 0);
    int n = 4;
    BackTracking bt = new BackTracking();
    List<List<String>> ans = bt.solveNQueens(n);
    System.out.println(ans);
  }
}