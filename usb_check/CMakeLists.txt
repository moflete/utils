cmake_minimum_required(VERSION 3.24)

if(WIN32)
    set(VCPKG_TARGET_TRIPLET "x64-windows-static" CACHE STRING "Vcpkg triplet")
    set(CMAKE_TOOLCHAIN_FILE "C:/dev/vcpkg/scripts/buildsystems/vcpkg.cmake" CACHE STRING "Vcpkg toolchain file")
endif()
if(APPLE)
    set(VCPKG_TARGET_TRIPLET "x64-osx" CACHE STRING "Vcpkg triplet")
    set(CMAKE_TOOLCHAIN_FILE "/opt/vcpkg/scripts/buildsystems/vcpkg.cmake" CACHE STRING "Vcpkg toolchain file")
endif(APPLE)

# Vcpkg settings
# set vcpkg toolchain 

set(VCPKG_MANIFEST_MODE OFF CACHE BOOL "Enable manifest mode")
set(VCPKG_PREFER_SYSTEM_LIBS ON CACHE BOOL "Do not prefer system libraries")
set(VCPKG_APPLOCAL_DEPS OFF CACHE BOOL "Install dependencies locally")
set(VCPKG_VERBOSE ON CACHE BOOL "Do not be verbose")
set(VCPKG_PREFER_STATIC ON CACHE BOOL "Prefer vcpkg static libraries")

######################################################################################
#____________________________________________________________________________________
project(usb_dev_connected)
set(APP usb_dev_connected)
set(SRCS usb_dev_connected.c)

find_package(PkgConfig REQUIRED)
pkg_check_modules(libusb REQUIRED IMPORTED_TARGET libusb-1.0)

add_executable(${APP} ${SRCS})
target_link_libraries(${APP} PRIVATE PkgConfig::libusb)

