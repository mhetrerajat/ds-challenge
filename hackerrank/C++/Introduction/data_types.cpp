//Basic Data Types
#include <iostream>
using namespace std;

int main(){
  int a;
  long int b;
  long long int c;
  char d;
  float e;
  double f;

  //cin >> a >> b >> c >> d >> e >> f;
  //cout << a << "\n" << b << "\n" << c << "\n" << d << "\n" << e << "\n" << f << endl;

  scanf("%d %ld %lld %c %f %lf", &a, &b, &c, &d, &e, &f);
  printf("%d \n%ld \n%lld \n%c \n%f \n%lf",a,b,c,d,e,f);

  return 0;
}
