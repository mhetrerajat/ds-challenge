// https://www.hackerrank.com/challenges/arrays-introduction?h_r=next-challenge&h_v=zen

#include <iostream>
#include <algorithm>
#include <iterator>
using namespace std;

int main(int argc, char const *argv[]) {
  int N, A[1000];
  cin >> N;

  for (int i = 0; i < N; i++) {
    cin >> A[i];
  }

  for (int i = N-1; i >= 0; i--) {
    cout << A[i] << " ";
  }
  return 0;
}
