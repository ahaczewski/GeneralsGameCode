set(ZLIB_PARENT_DIR ${CMAKE_SOURCE_DIR}/Dependencies/.zlib-1.1.4)
set(ZLIB_DIR ${ZLIB_PARENT_DIR}/ZLib)

FetchContent_Populate(zlib DOWNLOAD_EXTRACT_TIMESTAMP
    GIT_REPOSITORY https://github.com/xezon/zlib-1.1.4
    GIT_TAG        main
    SOURCE_DIR     ${ZLIB_DIR})

set(ZLIB_SOURCES
    "${ZLIB_DIR}/adler32.c"
    "${ZLIB_DIR}/compress.c"
    "${ZLIB_DIR}/crc32.c"
    "${ZLIB_DIR}/gzio.c"
    "${ZLIB_DIR}/uncompr.c"
    "${ZLIB_DIR}/deflate.c"
    "${ZLIB_DIR}/trees.c"
    "${ZLIB_DIR}/zutil.c"
    "${ZLIB_DIR}/inflate.c"
    "${ZLIB_DIR}/infblock.c"
    "${ZLIB_DIR}/inftrees.c"
    "${ZLIB_DIR}/infcodes.c"
    "${ZLIB_DIR}/infutil.c"
    "${ZLIB_DIR}/inffast.c")

add_library(libzlib STATIC)
target_sources(libzlib PRIVATE ${ZLIB_SOURCES})
target_include_directories(libzlib PUBLIC ${ZLIB_PARENT_DIR})
target_compile_definitions(libzlib PUBLIC Z_PREFIX)
