#include <fstream>
#include <iostream>
#include <iomanip>
#include <nlohmann/json.hpp>

using json = nlohmann::json;
using Point = std::array<float, 3>;

const float zAtCalo = 20000;

Point extrapolate(Point& p1, Point& p2) {
  auto dx = p2[0] - p1[0];
  auto dy = p2[1] - p1[1];
  auto dz = p2[2] - p1[2];
  auto xslope = dx / dz;
  auto yslope = dy / dz;
  auto newDz = zAtCalo - p2[2];
  auto newDx = xslope*newDz;
  auto newDy = yslope*newDz;
  return { p2[0] + newDx, p2[1] + newDy, zAtCalo};
}

int main(int argc, char** argv) {

  if (argc != 2) {
    std::cout << "Wrong number of arguments\n"
              << "Syntax:\n"
              << argv[0] << "<filename>" << std::endl;
    return 1;
  }

  std::ifstream input("../data/LHCbEventDataV2.json");
  json j;
  input >> j;

  for (auto& [name, event] : j.items()) {
    auto& longTracks = event["Tracks"]["LongTracks"];
    for (auto& track : longTracks) {
      auto& positions = track["pos"];
      auto& p1 = positions[positions.size()-2];
      Point lastBut1Point {p1[0], p1[1], p1[2]};
      auto& p2 = positions[positions.size()-1];
      Point lastPoint {p2[0], p2[1], p2[2]};
      auto newPoint = extrapolate(lastBut1Point, lastPoint);
      positions.push_back(newPoint);
    }
  }

  std::ofstream output("toto");
  output << std::setw(2) << j << std::endl;
}
