// https://www.hackerrank.com/challenges/c-tutorial-strings

#include <iostream>
#include <string>
using namespace std;

int main(int argc, char const *argv[]) {
  string a,b;
  cin >> a >> b;

  cout << a.size() << " " << b.size() << endl;
  cout << a + b << endl;

  char A=a[0], B=b[0];
  a[0] = B;
  b[0] = A;

  cout << a << " " << b << endl;
  return 0;
}
