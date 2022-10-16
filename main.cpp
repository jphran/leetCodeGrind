#include <array/PostNimble/EncodeAndDecodeStrings.h>
#include <iostream>


int main() {
    Codec s;

    std::vector<std::string> input{"hello", "world"};
    auto ans = s.encode(input);

    auto decode = s.decode(ans);

    for (auto& s : decode) {
        std::cout << s << std::endl;
    }

    return 0;
}
