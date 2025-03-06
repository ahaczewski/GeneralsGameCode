# Given the following fragment of a .dsp file, extract all the CPP and BASE CPP flags from each configuration, and output it as following:
#
# RTS - Win32 Release;<BASE CPP FLAGS>;<CPP FLAGS>
# RTS - Win32 Debug;<BASE CPP FLAGS>;<CPP FLAGS>
#
# The .dsp file has the following format:
#
# !IF  "$(CFG)" == "RTS - Win32 Release"
#
# # PROP BASE Use_MFC 0
# # PROP BASE Use_Debug_Libraries 0
# # PROP BASE Output_Dir "Release"
# # PROP BASE Intermediate_Dir "Release"
# # PROP BASE Target_Dir ""
# # PROP Use_MFC 0
# # PROP Use_Debug_Libraries 0
# # PROP Output_Dir "Main\Release"
# # PROP Intermediate_Dir "Main\Release"
# # PROP Ignore_Export_Lib 0
# # PROP Target_Dir ""
# # ADD BASE CPP /nologo /W3 /GX /O2 /D "WIN32" /D "NDEBUG" /D "_WINDOWS" /D "_MBCS" /YX /FD /c
# # ADD CPP /nologo /G6 /MD /W3 /WX /GX /Zi /O2 /Ob2 /I "Libraries\Include" /I "GameEngine\Include" /I "gameenginedevice\Include" /I "Libraries\Source\WWVegas" /I "Libraries\Source\WWVegas\WWLib" /I "Libraries\Source\WWVegas\WWMath" /I "Libraries\Source\WWVegas\WWDebug" /I "Libraries\Source\WWVegas\WWSaveLoad" /I "Libraries\Source\WWVegas\WW3D2" /I "Libraries\Include\Granny" /D "IG_DEBUG_STACKTRACE" /D "NDEBUG" /D "_RELEASE" /D "WIN32" /D "_WINDOWS" /D "_MBCS" /YX /FD /c
# # SUBTRACT CPP /Fr
# # ADD BASE MTL /nologo /D "NDEBUG" /mktyplib203 /win32
# # ADD MTL /nologo /D "NDEBUG" /mktyplib203 /win32
# # ADD BASE RSC /l 0x409 /d "NDEBUG"
# # ADD RSC /l 0x409 /d "NDEBUG"
# BSC32=bscmake.exe
# # ADD BASE BSC32 /nologo
# # ADD BSC32 /nologo
# LINK32=link.exe
# # ADD BASE LINK32 kernel32.lib user32.lib gdi32.lib winspool.lib comdlg32.lib advapi32.lib shell32.lib ole32.lib oleaut32.lib uuid.lib odbc32.lib odbccp32.lib /nologo /subsystem:windows /machine:I386
# # ADD LINK32 Benchmark.lib WW3D2.lib WWDebug.lib WWLib.lib WWUtil.lib WWMath.lib GameEngine.lib GameEngineDevice.lib binkw32.lib dxguid.lib dinput8.lib kernel32.lib user32.lib gdi32.lib winspool.lib comdlg32.lib advapi32.lib shell32.lib ole32.lib oleaut32.lib uuid.lib odbc32.lib odbccp32.lib d3dx8.lib mss32.lib d3d8.lib winmm.lib vfw32.lib dsound.lib wsock32.lib imm32.lib wininet.lib /nologo /subsystem:windows /pdb:"..\Run\RTS.pdb" /map:"..\Run\RTS.map" /debug /machine:I386 /nodefaultlib:"libc.lib" /nodefaultlib:"debug.lib" /out:"..\Run\RTS.exe" /libpath:"..\..\GameEngine" /libpath:"GameEngine\Lib" /libpath:"GameEngineDevice\Lib" /libpath:"Libraries\Lib" /libpath:"GameEngine" /OPT:REF /OPT:ICF
# # SUBTRACT LINK32 /pdb:none
#
# !ELSEIF  "$(CFG)" == "RTS - Win32 Debug"
#
# # PROP BASE Use_MFC 0
# # PROP BASE Use_Debug_Libraries 1
# # PROP BASE Output_Dir "Debug"
# # PROP BASE Intermediate_Dir "Debug"
# # PROP BASE Target_Dir ""
# # PROP Use_MFC 0
# # PROP Use_Debug_Libraries 1
# # PROP Output_Dir "Main\Debug"
# # PROP Intermediate_Dir "Main\Debug"
# # PROP Ignore_Export_Lib 0
# # PROP Target_Dir ""
# # ADD BASE CPP /nologo /W3 /Gm /GX /ZI /Od /D "WIN32" /D "_DEBUG" /D "_WINDOWS" /D "_MBCS" /YX /FD /GZ /c
# # ADD CPP /nologo /G6 /MDd /W3 /WX /Gm /GX /ZI /Od /I "Libraries\Include" /I "GameEngine\Include" /I "gameenginedevice\Include" /I "Libraries\Source\WWVegas" /I "Libraries\Source\WWVegas\WWLib" /I "Libraries\Source\WWVegas\WWMath" /I "Libraries\Source\WWVegas\WWDebug" /I "Libraries\Source\WWVegas\WWSaveLoad" /I "Libraries\Source\WWVegas\WW3D2" /I "Libraries\Include\Granny" /D "_DEBUG" /D "WIN32" /D "_WINDOWS" /D "_MBCS" /D "BROWSER_DEBUG" /YX /FD /GZ /c
# # SUBTRACT CPP /Fr
# # ADD BASE MTL /nologo /D "_DEBUG" /mktyplib203 /win32
# # ADD MTL /nologo /D "_DEBUG" /mktyplib203 /win32
# # ADD BASE RSC /l 0x409 /d "_DEBUG"
# # ADD RSC /l 0x409 /d "_DEBUG"
# BSC32=bscmake.exe
# # ADD BASE BSC32 /nologo
# LINK32=link.exe
# # ADD BASE LINK32 kernel32.lib user32.lib gdi32.lib winspool.lib comdlg32.lib advapi32.lib shell32.lib ole32.lib oleaut32.lib uuid.lib odbc32.lib odbccp32.lib /nologo /subsystem:windows /debug /machine:I386
# # ADD LINK32 BenchmarkD.lib WW3D2Debug.lib WWDebugDebug.lib WWUtilDebug.lib WWLibDebug.lib WWMathDebug.lib GameEngineDebug.lib GameEngineDeviceDebug.lib binkw32.lib dxguid.lib dinput8.lib kernel32.lib user32.lib gdi32.lib winspool.lib comdlg32.lib advapi32.lib shell32.lib ole32.lib oleaut32.lib uuid.lib odbc32.lib odbccp32.lib d3dx8.lib mss32.lib d3d8.lib winmm.lib vfw32.lib dsound.lib wsock32.lib imm32.lib wininet.lib /nologo /subsystem:windows /pdb:"..\Run\RTSD.pdb" /map:"..\Run\RTSD.map" /debug /machine:I386 /nodefaultlib:"libcd.lib" /out:"..\Run\RTSD.exe" /libpath:"GameEngine" /libpath:"GameEngine\Lib" /libpath:"GameEngineDevice\Lib" /libpath:"Libraries\Lib"
# # SUBTRACT LINK32 /pdb:none
#
# !ELSEIF  "$(CFG)" == "RTS - Win32 Internal"
#
# # PROP BASE Use_MFC 0
# # PROP BASE Use_Debug_Libraries 0
# # PROP BASE Output_Dir "Internal"
# # PROP BASE Intermediate_Dir "Internal"
# # PROP BASE Target_Dir ""
# # PROP Use_MFC 0
# # PROP Use_Debug_Libraries 0
# # PROP Output_Dir "Main\Internal"
# # PROP Intermediate_Dir "Main\Internal"
# # PROP Ignore_Export_Lib 0
# # PROP Target_Dir ""
# # ADD BASE CPP /nologo /W3 /GX /O2 /D "WIN32" /D "NDEBUG" /D "_WINDOWS" /D "_MBCS" /YX /FD /c
# # ADD CPP /nologo /G6 /MD /W3 /WX /GX /Zi /O2 /I "Libraries\Include" /I "GameEngine\Include" /I "gameenginedevice\Include" /I "Libraries\Source\WWVegas" /I "Libraries\Source\WWVegas\WWLib" /I "Libraries\Source\WWVegas\WWMath" /I "Libraries\Source\WWVegas\WWDebug" /I "Libraries\Source\WWVegas\WWSaveLoad" /I "Libraries\Source\WWVegas\WW3D2" /I "Libraries\Include\Granny" /D "NDEBUG" /D "_INTERNAL" /D "WIN32" /D "_WINDOWS" /D "_MBCS" /YX /FD /c
# # SUBTRACT CPP /Fr
# # ADD BASE MTL /nologo /D "NDEBUG" /mktyplib203 /win32
# # ADD MTL /nologo /D "NDEBUG" /mktyplib203 /win32
# # ADD BASE RSC /l 0x409 /d "NDEBUG"
# # ADD RSC /l 0x409 /d "NDEBUG"
# BSC32=bscmake.exe
# # ADD BASE BSC32 /nologo
# # ADD BSC32 /nologo
# LINK32=link.exe
# # ADD BASE LINK32 kernel32.lib user32.lib gdi32.lib winspool.lib comdlg32.lib advapi32.lib shell32.lib ole32.lib oleaut32.lib uuid.lib odbc32.lib odbccp32.lib wsock32.lib /nologo /subsystem:windows /machine:I386
# # ADD LINK32 Benchmark.lib WW3D2Internal.lib WWDebugInternal.lib WWLibInternal.lib WWUtilInternal.lib WWMathInternal.lib GameEngineInternal.lib GameEngineDeviceInternal.lib binkw32.lib dxguid.lib dinput8.lib kernel32.lib user32.lib gdi32.lib winspool.lib comdlg32.lib advapi32.lib shell32.lib ole32.lib oleaut32.lib uuid.lib odbc32.lib odbccp32.lib d3dx8.lib mss32.lib d3d8.lib winmm.lib vfw32.lib dsound.lib wsock32.lib imm32.lib wininet.lib /nologo /subsystem:windows /pdb:"..\Run\RTSI.pdb" /map:"..\Run\RTSI.map" /debug /machine:I386 /nodefaultlib:"libc.lib" /out:"..\Run\RTSI.exe" /libpath:"GameEngine\Lib" /libpath:"GameEngineDevice\Lib" /libpath:"Libraries\Lib" /libpath:"GameEngine" /fixed:no
# # SUBTRACT LINK32 /pdb:none
#
# !ELSEIF  "$(CFG)" == "RTS - Win32 DebugW3D"
#
# # PROP BASE Use_MFC 0
# # PROP BASE Use_Debug_Libraries 1
# # PROP BASE Output_Dir "DebugW3D"
# # PROP BASE Intermediate_Dir "DebugW3D"
# # PROP BASE Target_Dir ""
# # PROP Use_MFC 0
# # PROP Use_Debug_Libraries 1
# # PROP Output_Dir "Main\DebugW3D"
# # PROP Intermediate_Dir "Main\DebugW3D"
# # PROP Ignore_Export_Lib 0
# # PROP Target_Dir ""
# # ADD BASE CPP /nologo /W3 /Gm /GX /ZI /Od /D "WIN32" /D "_DEBUG" /D "_WINDOWS" /D "_MBCS" /YX /FD /GZ /c
# # ADD CPP /nologo /G6 /MDd /W3 /WX /Gm /GX /ZI /Od /I "Libraries\Include" /I "GameEngine\Include" /I "gameenginedevice\Include" /I "Libraries\Source\WWVegas" /I "Libraries\Source\WWVegas\WWLib" /I "Libraries\Source\WWVegas\WWMath" /I "Libraries\Source\WWVegas\WWDebug" /I "Libraries\Source\WWVegas\WWSaveLoad" /I "Libraries\Source\WWVegas\WW3D2" /I "Libraries\Include\Granny" /D "_DEBUG" /D "WIN32" /D "_WINDOWS" /D "_MBCS" /YX /FD /GZ /c
# # SUBTRACT CPP /Fr
# # ADD BASE MTL /nologo /D "_DEBUG" /mktyplib203 /win32
# # ADD MTL /nologo /D "_DEBUG" /mktyplib203 /win32
# # ADD BASE RSC /l 0x409 /d "_DEBUG"
# # ADD RSC /l 0x409 /d "_DEBUG"
# BSC32=bscmake.exe
# # ADD BASE BSC32 /nologo
# # ADD BSC32 /nologo
# LINK32=link.exe
# # ADD BASE LINK32 kernel32.lib user32.lib gdi32.lib winspool.lib comdlg32.lib advapi32.lib shell32.lib ole32.lib oleaut32.lib uuid.lib odbc32.lib odbccp32.lib /nologo /subsystem:windows /debug /machine:I386
# # ADD LINK32 BenchmarkD.lib WWDownloadDebug.lib GameSpyHTTPDebug.lib GameSpyPresenceDebug.lib GameSpyStatsDebug.lib GameSpyPeerDebug.lib GameSpyPatchingDebug.lib WW3D2DebugW3D.lib WWDebugDebugW3D.lib WWUtilDebugW3D.lib WWLibDebugW3D.lib WWMathDebugW3D.lib GameEngineDebug.lib GameEngineDeviceDebug.lib binkw32.lib dxguid.lib dinput8.lib kernel32.lib user32.lib gdi32.lib winspool.lib comdlg32.lib advapi32.lib shell32.lib ole32.lib oleaut32.lib uuid.lib odbc32.lib odbccp32.lib d3dx8.lib mss32.lib d3d8.lib winmm.lib vfw32.lib dsound.lib wsock32.lib imm32.lib wininet.lib /nologo /subsystem:windows /pdb:"..\Run\RTSDW3D.pdb" /map:"..\Run\RTSDW3D.map" /debug /machine:I386 /nodefaultlib:"libcd.lib" /out:"..\Run\RTSDW3D.exe" /libpath:"GameEngine" /libpath:"GameEngine\Lib" /libpath:"GameEngineDevice\Lib" /libpath:"Libraries\Lib"
# # SUBTRACT LINK32 /pdb:none
#
# !ELSEIF  "$(CFG)" == "RTS - Win32 Profile"
#
# # PROP BASE Use_MFC 0
# # PROP BASE Use_Debug_Libraries 0
# # PROP BASE Output_Dir "Profile"
# # PROP BASE Intermediate_Dir "Profile"
# # PROP BASE Ignore_Export_Lib 0
# # PROP BASE Target_Dir ""
# # PROP Use_MFC 0
# # PROP Use_Debug_Libraries 0
# # PROP Output_Dir "Main\Profile"
# # PROP Intermediate_Dir "Main\Profile"
# # PROP Ignore_Export_Lib 0
# # PROP Target_Dir ""
# # ADD BASE CPP /nologo /G6 /MD /W3 /WX /GX /O2 /Ob2 /I "Libraries\Include" /I "GameEngine\Include" /I "gameenginedevice\Include" /I "Libraries\Source\WWVegas" /I "Libraries\Source\WWVegas\WWLib" /I "Libraries\Source\WWVegas\WWMath" /I "Libraries\Source\WWVegas\WWDebug" /I "Libraries\Source\WWVegas\WWSaveLoad" /I "Libraries\Source\WWVegas\WW3D2" /I "Libraries\Include\Granny" /D "IG_DEBUG_STACKTRACE" /D "NDEBUG" /D "_RELEASE" /D "WIN32" /D "_WINDOWS" /D "_MBCS" /YX /FD /c
# # SUBTRACT BASE CPP /Fr
# # ADD CPP /nologo /G6 /MD /W3 /WX /GX /Zi /O2 /Ob2 /I "Libraries\Include" /I "GameEngine\Include" /I "gameenginedevice\Include" /I "Libraries\Source\WWVegas" /I "Libraries\Source\WWVegas\WWLib" /I "Libraries\Source\WWVegas\WWMath" /I "Libraries\Source\WWVegas\WWDebug" /I "Libraries\Source\WWVegas\WWSaveLoad" /I "Libraries\Source\WWVegas\WW3D2" /I "Libraries\Include\Granny" /D "IG_DEBUG_STACKTRACE" /D "NDEBUG" /D "_RELEASE" /D "WIN32" /D "_WINDOWS" /D "_MBCS" /D "_PROFILE" /YX /FD /Gh /c
# # ADD BASE MTL /nologo /D "NDEBUG" /mktyplib203 /win32
# # ADD MTL /nologo /D "NDEBUG" /mktyplib203 /win32
# # ADD BASE RSC /l 0x409 /d "NDEBUG"
# # ADD RSC /l 0x409 /d "NDEBUG"
# BSC32=bscmake.exe
# # ADD BASE BSC32 /nologo
# # ADD BSC32 /nologo
# LINK32=link.exe
# # ADD BASE LINK32 Benchmark.lib WW3D2.lib WWDebug.lib WWLib.lib WWUtil.lib WWMath.lib GameEngine.lib GameEngineDevice.lib binkw32.lib dxguid.lib dinput8.lib kernel32.lib user32.lib gdi32.lib winspool.lib comdlg32.lib advapi32.lib shell32.lib ole32.lib oleaut32.lib uuid.lib odbc32.lib odbccp32.lib d3dx8.lib mss32.lib d3d8.lib winmm.lib vfw32.lib dsound.lib wsock32.lib imm32.lib wininet.lib /nologo /subsystem:windows /machine:I386 /nodefaultlib:"libc.lib" /out:"..\Run\RTS.exe" /libpath:"..\..\GameEngine" /libpath:"GameEngine\Lib" /libpath:"GameEngineDevice\Lib" /libpath:"Libraries\Lib" /libpath:"GameEngine"
# # SUBTRACT BASE LINK32 /pdb:none /debug
# # ADD LINK32 Benchmark.lib WW3D2Profile.lib WWDebugProfile.lib WWLibProfile.lib WWUtilProfile.lib WWMathProfile.lib GameEngineProfile.lib GameEngineDeviceProfile.lib binkw32.lib dxguid.lib dinput8.lib kernel32.lib user32.lib gdi32.lib winspool.lib comdlg32.lib advapi32.lib shell32.lib ole32.lib oleaut32.lib uuid.lib odbc32.lib odbccp32.lib d3dx8.lib mss32.lib d3d8.lib winmm.lib vfw32.lib dsound.lib wsock32.lib imm32.lib wininet.lib gamespyhttp.lib /nologo /subsystem:windows /pdb:"..\Run\RTSP.pdb" /map:"..\Run\RTSP.map" /debug /machine:I386 /nodefaultlib:"libc.lib" /nodefaultlib:"gameengine.lib" /out:"..\Run\RTSP.exe" /libpath:"GameEngine\Lib" /libpath:"GameEngineDevice\Lib" /libpath:"Libraries\Lib" /libpath:"GameEngine"
# # SUBTRACT LINK32 /pdb:none
#
# !ENDIF
import re
import sys
import os
import argparse
from pathlib import Path

def extract_cpp_flags(file_content):
    # Define patterns for matching configurations and flags
    config_pattern = re.compile(r'!IF\s+"(\$\(CFG\))"\s*==\s*"([^"]+)"')
    elseif_pattern = re.compile(r'!ELSEIF\s+"(\$\(CFG\))"\s*==\s*"([^"]+)"')
    base_cpp_pattern = re.compile(r'#\s*ADD\s+BASE\s+CPP\s+(.+)')
    cpp_pattern = re.compile(r'#\s*ADD\s+CPP\s+(.+)')
    subtract_cpp_pattern = re.compile(r'#\s*SUBTRACT\s+CPP\s+(.+)')
    base_link_pattern = re.compile(r'#\s*ADD\s+BASE\s+LINK32\s+(.+)')
    link_pattern = re.compile(r'#\s*ADD\s+LINK32\s+(.+)')
    subtract_link_pattern = re.compile(r'#\s*SUBTRACT\s+LINK32\s+(.+)')

    # Variables to store current state
    current_config = None
    configs = {}

    config_counter = 0

    # Process the file line by line
    lines = file_content.split('\n')
    for i, line in enumerate(lines):
        line = line.strip()

        # Match configuration in !IF blocks
        config_match = config_pattern.search(line)
        if config_match:
            current_config = config_match.group(2).strip()
            if current_config not in configs:
                configs[current_config] = {'BASE_CPP': '', 'CPP': '', 'SUBTRACT_CPP': '', 'BASE_LINK32': '', 'LINK32': '', 'SUBTRACT_LINK32': ''}
            config_counter += 1
            continue

        # Match configuration in !ELSEIF blocks
        elseif_match = elseif_pattern.search(line)
        if elseif_match:
            current_config = elseif_match.group(2).strip()
            if current_config not in configs:
                configs[current_config] = {'BASE_CPP': '', 'CPP': '', 'SUBTRACT_CPP': '', 'BASE_LINK32': '', 'LINK32': '', 'SUBTRACT_LINK32': ''}
            config_counter += 1
            continue

        # Match BASE CPP flags
        base_cpp_match = base_cpp_pattern.search(line)
        if base_cpp_match and current_config:
            configs[current_config]['BASE_CPP'] = base_cpp_match.group(1).strip()
            continue

        # Match CPP flags
        cpp_match = cpp_pattern.search(line)
        if cpp_match and current_config:
            configs[current_config]['CPP'] = cpp_match.group(1).strip()
            continue

        # Match SUBTRACT CPP flags
        subtract_cpp_match = subtract_cpp_pattern.search(line)
        if subtract_cpp_match and current_config:
            configs[current_config]['SUBTRACT_CPP'] = subtract_cpp_match.group(1).strip()
            continue

        # Match BASE LINK32 flags
        base_link_match = base_link_pattern.search(line)
        if base_link_match and current_config:
            configs[current_config]['BASE_LINK32'] = base_link_match.group(1).strip()
            continue

        # Match LINK32 flags
        link_match = link_pattern.search(line)
        if link_match and current_config:
            configs[current_config]['LINK32'] = link_match.group(1).strip()
            continue

        # Match SUBTRACT LINK32 flags
        subtract_link_match = subtract_link_pattern.search(line)
        if subtract_link_match and current_config:
            configs[current_config]['SUBTRACT_LINK32'] = subtract_link_match.group(1).strip()
            continue

    print(f"Found {config_counter} configs")
    return configs

def process_dsp_file(dsp_path, output_dir, verbose=False):
    try:
        # Try different encodings if needed
        encodings = ['latin-1', 'utf-8', 'windows-1252']
        file_content = None

        for encoding in encodings:
            try:
                with open(dsp_path, 'r', encoding=encoding) as file:
                    file_content = file.read()
                break
            except UnicodeDecodeError:
                continue

        if file_content is None:
            # Last resort - use binary mode and decode as best as possible
            with open(dsp_path, 'rb') as file:
                file_content = file.read().decode('ascii', errors='replace')

    except Exception as e:
        print(f"Error reading file {dsp_path}: {e}")
        return False

    if verbose:
        print(f"Processing file: {dsp_path}")
        # Print a sample of the file to verify content
        sample_lines = file_content.split('\n')[:20]
        print("Sample of the file content (first 20 lines):")
        for line in sample_lines:
            print(line)

    configs = extract_cpp_flags(file_content)
    if not configs:
        if verbose:
            print(f"No configuration flags found in {dsp_path}")
        return False

    # Create output filename based on the dsp filename
    output_filename = os.path.basename(dsp_path).replace('.dsp', '_flags.csv')
    output_path = os.path.join(output_dir, output_filename)

    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    try:
        with open(output_path, 'w', encoding='utf-8') as outfile:
            outfile.write("Config;BASE CPP;CPP;SUBTRACT CPP;BASE LINK32;LINK32;SUBTRACT LINK32\n")
            for config, flags in configs.items():
                outfile.write(f"{config};{flags['BASE_CPP']};{flags['CPP']};{flags['SUBTRACT_CPP']};{flags['BASE_LINK32']};{flags['LINK32']};{flags['SUBTRACT_LINK32']}\n")
        print(f"Extracted flags from {dsp_path} to {output_path}")
        return True
    except Exception as e:
        print(f"Error writing to {output_path}: {e}")
        return False

def find_dsp_files(start_dir):
    return list(Path(start_dir).rglob('*.dsp'))

def main():
    parser = argparse.ArgumentParser(description="Extract compiler flags from Visual Studio .dsp files")
    parser.add_argument("-d", "--dir", help="Directory to search for .dsp files", default=".")
    parser.add_argument("-o", "--output", help="Directory to save output files", default="./flags_output")
    parser.add_argument("-f", "--file", help="Process a single .dsp file instead of searching")
    parser.add_argument("-v", "--verbose", help="Enable verbose output for debugging", action="store_true")
    args = parser.parse_args()

    if args.file:
        # Process a single file
        if not os.path.isfile(args.file):
            print(f"Error: File '{args.file}' not found.")
            return
        process_dsp_file(args.file, args.output, args.verbose)
    else:
        # Search for .dsp files and process them
        if not os.path.isdir(args.dir):
            print(f"Error: Directory '{args.dir}' not found.")
            return

        dsp_files = find_dsp_files(args.dir)
        if not dsp_files:
            print(f"No .dsp files found in {args.dir}")
            return

        print(f"Found {len(dsp_files)} .dsp files")

        success_count = 0
        for dsp_file in dsp_files:
            if process_dsp_file(dsp_file, args.output, args.verbose):
                success_count += 1

        print(f"Successfully processed {success_count} out of {len(dsp_files)} .dsp files")

if __name__ == "__main__":
    main()
