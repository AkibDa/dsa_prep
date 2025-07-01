#include <iostream>

using namespace std;

int main() {

  float sales = 95000;

  cout << "Sales: $" << sales << endl;
  cout << "State Tax: $" << sales * 0.04 << endl;
  cout << "County Tax: $" << sales * 0.02 << endl;
  cout << "Total Tax: $" << (sales * 0.04) + (sales * 0.02) << endl;
  cout << "Total Sales: $" << sales + ((sales * 0.04) + (sales * 0.02)) << endl;

  return 0;
}