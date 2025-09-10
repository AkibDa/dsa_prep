class Solution6 {
  public int minimumTeachings(int n, int[][] languages, int[][] friendships) {
    int m = languages.length;
    boolean[][] knows = new boolean[m][n + 1];
    for (int i = 0; i < m; i++) {
      for (int lang : languages[i]) {
        knows[i][lang] = true;
      }
    }
    boolean[] needsHelp = new boolean[m];
    for (int[] friendship : friendships) {
      int u = friendship[0] - 1;
      int v = friendship[1] - 1;
      boolean canCommunicate = false;
      for (int lang = 1; lang <= n; lang++) {
        if (knows[u][lang] && knows[v][lang]) {
          canCommunicate = true;
          break;
        }
      }
      if (!canCommunicate) {
        needsHelp[u] = true;
        needsHelp[v] = true;
      }
    }
    int output = Integer.MAX_VALUE;
    for (int lang = 1; lang <= n; lang++) {
      int count = 0;
      for (int i = 0; i < m; i++) {
        if (needsHelp[i] && !knows[i][lang]) {
          count++;
        }
      }
      output = Math.min(output, count);
    }
    return output;
  }
}