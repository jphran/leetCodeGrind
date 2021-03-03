//
// Created by jfrancis on 3/2/21.
//

#ifndef LEETCODEGRIND_CANPLACEFLOWERS_H
#define LEETCODEGRIND_CANPLACEFLOWERS_H

#include <vector>

class CanPlaceFlowers {
public:
  bool canPlaceFlowers(std::vector<int>& flowerbed, int n) {
    uint8_t count = 0;
    std::vector<int> fb = flowerbed;
    if(fb.size() == 1) {
      if(fb.at(0) == 0)
        return ++count >= n;
      else {
        return count >= n;
      }
    }


    // check the first and last placements
    if(fb.at(0) == 0 && fb.at(1) == 0)
      addFlower(fb, count, 0);
    if(fb.at(fb.size()-1) == 0 && fb.at(fb.size()-2) == 0)
      addFlower(fb, count, fb.size() - 1);


    for(int i = 1; i < fb.size() - 1; ++i) {
      if(fb.at(i-1) == 0
          && fb.at(i) == 0
                 && fb.at(i+1) == 0) {
        addFlower(fb, count, i);
      }
    }
    return count >= n;
  }

private:
  void addFlower(std::vector<int>& flowerbed, uint8_t& count, int idx) {
    flowerbed.at(idx) = 1;
    ++count;
  }
};

#endif // LEETCODEGRIND_CANPLACEFLOWERS_H
