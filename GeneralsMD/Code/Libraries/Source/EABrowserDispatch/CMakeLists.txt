add_library(BrowserDispatch)

set(MIDL_OUTPUT
    ${CMAKE_CURRENT_BINARY_DIR}/BrowserDispatch.h
    ${CMAKE_CURRENT_BINARY_DIR}/GUIDS.c
    ${CMAKE_CURRENT_BINARY_DIR}/BrowserDispatch.c
    ${CMAKE_CURRENT_BINARY_DIR}/BrowserDispatchDll.c
)

set(MIDL_FILE
    ${CMAKE_CURRENT_LIST_DIR}/BrowserDispatch.idl
)

add_custom_command(
    OUTPUT ${MIDL_OUTPUT}
    COMMAND midl /h BrowserDispatch.h /iid GUIDS.c /proxy BrowserDispatch.c /dlldata BrowserDispatchDll.c ${MIDL_FILE}
    WORKING_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}
    DEPENDS ${MIDL_FILE}
    MAIN_DEPENDENCY ${MIDL_FILE}
    VERBATIM
)

target_sources(BrowserDispatch PRIVATE ${MIDL_FILE} ${MIDL_OUTPUT})