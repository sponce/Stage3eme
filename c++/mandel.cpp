#include <chrono>
#include <iostream>

extern "C" {

  int kernel(float ax, float ay, float zx, float zy) {
    float x = zx;
    float y = zy;
    for (int n = 1; n <= 1000; n++) {
      auto newx = x*x - y*y + ax;
      auto newy = 2*x*y + ay;
      if (4 < newx*newx + newy*newy) {
        return n;
      }
      x = newx;
      y = newy;
    }
    return -1;
  }
  
  void mandel(int* buffer,
              const float minx,
              const float dx,
              const unsigned int nx,
              const float miny,
              const float dy,
              const unsigned int ny) {
    auto start = std::chrono::steady_clock::now();
    float ay = miny;
    for (unsigned int any = 0; any < ny; ay += dy, any++) {
      float ax = minx;
      for (unsigned int anx = 0; anx < nx; ax += dx, anx++) {
        buffer[any*nx+anx] = kernel(ax, ay, 0, 0);
      }
    }
    auto end = std::chrono::steady_clock::now();
    std::cout << "Elapsed time in microseconds : " 
              << std::chrono::duration_cast<std::chrono::microseconds>(end - start).count()
              << " us" << std::endl;
  }
  
  void julia(int* buffer,
             const float minx,
             const float dx,
             const unsigned int nx,
             const float miny,
             const float dy,
             const unsigned int ny,
             const float cx,
             const float cy) {
    auto start = std::chrono::steady_clock::now();
    float ay = miny;
    for (unsigned int any = 0; any < ny; ay += dy, any++) {
      float ax = minx;
      for (unsigned int anx = 0; anx < nx; ax += dx, anx++) {
        buffer[any*nx+anx] = kernel(cx, cy, ax, ay);
      }
    }
    auto end = std::chrono::steady_clock::now();
    std::cout << "Elapsed time in microseconds : " 
              << std::chrono::duration_cast<std::chrono::microseconds>(end - start).count()
              << " us" << std::endl;
  }
}
