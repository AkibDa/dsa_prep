class Solution5 {
  public int[] getNoZeroIntegers(int n) {
      int b;
      for(int a=1;a<=n;a++){
        b=n-a;
        if (!String.valueOf(a).contains("0") && !String.valueOf(b).contains("0")){
            return new int[]{a, b};
        }
    }
    return new int[]{};
  }
}