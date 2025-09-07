class Solution2 {
  public boolean isPalindrome(int x) {
      int m = x;
      int ld = 0;
      while(m>0){
          ld = ld * 10 + m%10;
          m = m/10;
      }
      return (ld == x);
  }
}