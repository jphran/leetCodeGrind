# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.17

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Disable VCS-based implicit rules.
% : %,v


# Disable VCS-based implicit rules.
% : RCS/%


# Disable VCS-based implicit rules.
% : RCS/%,v


# Disable VCS-based implicit rules.
% : SCCS/s.%


# Disable VCS-based implicit rules.
% : s.%


.SUFFIXES: .hpux_make_needs_suffix_list


# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /home/jfrancis/.local/share/JetBrains/Toolbox/apps/CLion/ch-0/203.6682.181/bin/cmake/linux/bin/cmake

# The command to remove a file.
RM = /home/jfrancis/.local/share/JetBrains/Toolbox/apps/CLion/ch-0/203.6682.181/bin/cmake/linux/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/jfrancis/Documents/leetCodeGrind

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/jfrancis/Documents/leetCodeGrind/cmake-build-debug

# Include any dependencies generated for this target.
include CMakeFiles/leetCodeGrind.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/leetCodeGrind.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/leetCodeGrind.dir/flags.make

CMakeFiles/leetCodeGrind.dir/main.cpp.o: CMakeFiles/leetCodeGrind.dir/flags.make
CMakeFiles/leetCodeGrind.dir/main.cpp.o: ../main.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/jfrancis/Documents/leetCodeGrind/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/leetCodeGrind.dir/main.cpp.o"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/leetCodeGrind.dir/main.cpp.o -c /home/jfrancis/Documents/leetCodeGrind/main.cpp

CMakeFiles/leetCodeGrind.dir/main.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/leetCodeGrind.dir/main.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/jfrancis/Documents/leetCodeGrind/main.cpp > CMakeFiles/leetCodeGrind.dir/main.cpp.i

CMakeFiles/leetCodeGrind.dir/main.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/leetCodeGrind.dir/main.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/jfrancis/Documents/leetCodeGrind/main.cpp -o CMakeFiles/leetCodeGrind.dir/main.cpp.s

CMakeFiles/leetCodeGrind.dir/src/TwoSum.cpp.o: CMakeFiles/leetCodeGrind.dir/flags.make
CMakeFiles/leetCodeGrind.dir/src/TwoSum.cpp.o: ../src/TwoSum.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/jfrancis/Documents/leetCodeGrind/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object CMakeFiles/leetCodeGrind.dir/src/TwoSum.cpp.o"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/leetCodeGrind.dir/src/TwoSum.cpp.o -c /home/jfrancis/Documents/leetCodeGrind/src/TwoSum.cpp

CMakeFiles/leetCodeGrind.dir/src/TwoSum.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/leetCodeGrind.dir/src/TwoSum.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/jfrancis/Documents/leetCodeGrind/src/TwoSum.cpp > CMakeFiles/leetCodeGrind.dir/src/TwoSum.cpp.i

CMakeFiles/leetCodeGrind.dir/src/TwoSum.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/leetCodeGrind.dir/src/TwoSum.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/jfrancis/Documents/leetCodeGrind/src/TwoSum.cpp -o CMakeFiles/leetCodeGrind.dir/src/TwoSum.cpp.s

# Object files for target leetCodeGrind
leetCodeGrind_OBJECTS = \
"CMakeFiles/leetCodeGrind.dir/main.cpp.o" \
"CMakeFiles/leetCodeGrind.dir/src/TwoSum.cpp.o"

# External object files for target leetCodeGrind
leetCodeGrind_EXTERNAL_OBJECTS =

leetCodeGrind: CMakeFiles/leetCodeGrind.dir/main.cpp.o
leetCodeGrind: CMakeFiles/leetCodeGrind.dir/src/TwoSum.cpp.o
leetCodeGrind: CMakeFiles/leetCodeGrind.dir/build.make
leetCodeGrind: CMakeFiles/leetCodeGrind.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/jfrancis/Documents/leetCodeGrind/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Linking CXX executable leetCodeGrind"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/leetCodeGrind.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/leetCodeGrind.dir/build: leetCodeGrind

.PHONY : CMakeFiles/leetCodeGrind.dir/build

CMakeFiles/leetCodeGrind.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/leetCodeGrind.dir/cmake_clean.cmake
.PHONY : CMakeFiles/leetCodeGrind.dir/clean

CMakeFiles/leetCodeGrind.dir/depend:
	cd /home/jfrancis/Documents/leetCodeGrind/cmake-build-debug && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/jfrancis/Documents/leetCodeGrind /home/jfrancis/Documents/leetCodeGrind /home/jfrancis/Documents/leetCodeGrind/cmake-build-debug /home/jfrancis/Documents/leetCodeGrind/cmake-build-debug /home/jfrancis/Documents/leetCodeGrind/cmake-build-debug/CMakeFiles/leetCodeGrind.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/leetCodeGrind.dir/depend

