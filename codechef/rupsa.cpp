// Rupsa and the Game : https://www.codechef.com/problems/RGAME

#include <cstdio>
using namespace std;
typedef unsigned long long ulong;
#define gc getchar_unlocked
const ulong MOD = 1000000007;

// Fast I/O Operations
ulong scanint() {
  int n = 0;
  int c = gc();

  while (c < '0' || c > '9')
    c = gc();

  while ('0' <= c && c <= '9') {
    n *= 10;
    n += c - '0';
    c = gc();
  }
  return n;
}


int main(int argc, char const *argv[]) {
  ulong T = scanint();

  while(T){
    ulong N = scanint();

    ulong f = scanint();
    f = (f*2) % MOD;

    ulong sum = 0;
    for (ulong i = 0, coeff=2; i < N; i++) {
      ulong a = scanint();
      sum = (sum*2 + a*f) % MOD;
      f = (f + coeff*a) % MOD;
      coeff = (coeff*2) % MOD;
    }
    printf("%llu\n", sum);
    T--;
  }
  return 0;
}
