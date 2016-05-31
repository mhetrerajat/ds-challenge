// https://www.hackerrank.com/challenges/c-tutorial-pointer?h_r=next-challenge&h_v=zen

#include <iostream>
#include <cstdlib>
using namespace std;

void update(int *a,int *b) {
    *a = *a + *b;
    *b = abs((*a) - (*b) -(*b));
}

int main(int argc, char const *argv[]) {
  int a,b;

  cin >> a >> b;
  update(&a, &b);
  cout << a << "\n" << b;

  return 0;
}
