#!/usr/bin/env python3
import os
import csv
import re
from pathlib import Path
import argparse

def sanitize_flag(flag):
    # Remove quotes and escape backslashes
    return flag.replace('"', '\\"').replace('\\', '\\\\')

def parse_include_paths(cpp_flags):
    # Extract include paths from CPP flags
    includes = []
    for flag in cpp_flags.split():
        if flag.startswith('/I'):
            # Remove /I and any surrounding quotes
            path = flag[2:].strip('"')
            includes.append(path)
    return includes

def parse_defines(cpp_flags):
    # Extract preprocessor definitions from CPP flags
    defines = []
    for flag in cpp_flags.split():
        if flag.startswith('/D'):
            # Remove /D and any surrounding quotes
            define = flag[2:].strip('"')
            defines.append(define)
    return defines

def parse_libs(link_flags):
    # Extract libraries from LINK flags
    libs = []
    for part in link_flags.split():
        if part.endswith('.lib'):
            # Remove .lib extension
            lib = part[:-4]
            if lib not in libs:
                libs.append(lib)
    return libs

def convert_vs_to_cmake_flags(cpp_flags):
    # Convert Visual Studio flags to CMake format
    cmake_flags = []

    # Handle common VS flags
    flag_mapping = {
        '/O2': '-O2',
        '/Od': '-O0',
        '/W3': '-Wall',
        '/WX': '-Werror',
        '/Zi': '-g',
        '/ZI': '-g',
        '/GX': '-fexceptions',
        '/EHsc': '-fexceptions',
        '/MD': '-MD',
        '/MDd': '-MDd',
        '/MT': '-MT',
        '/MTd': '-MTd',
        '/Gm': '',  # Minimal rebuild
        '/GZ': '',  # Debug runtime checks
        '/GS': '',  # Buffer security check
        '/G6': '-march=pentium2',
        '/GL': '-flto',
        '/Ob2': '-finline-functions',
    }

    for flag in cpp_flags.split():
        if flag in flag_mapping:
            cmake_flag = flag_mapping[flag]
            if cmake_flag and cmake_flag not in cmake_flags:
                cmake_flags.append(cmake_flag)

    return cmake_flags

def generate_cmake_file(project_name, configs, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    cmake_path = os.path.join(output_dir, "CMakeLists.txt")

    with open(cmake_path, 'w') as cmake_file:
        cmake_file.write(f'cmake_minimum_required(VERSION 3.10)\n')
        cmake_file.write(f'project({project_name} LANGUAGES CXX)\n\n')

        # Define configurations
        config_names = [config['name'] for config in configs]
        cmake_file.write(f'set(CMAKE_CONFIGURATION_TYPES "{";".join(config_names)}" CACHE STRING "" FORCE)\n\n')

        # Add source files placeholder
        cmake_file.write('# Add source files\n')
        cmake_file.write('file(GLOB_RECURSE SOURCES "src/*.cpp" "src/*.h")\n\n')

        # Create target
        cmake_file.write(f'add_executable({project_name} ${{SOURCES}})\n\n')

        # Common include directories from all configs
        all_includes = set()
        for config in configs:
            all_includes.update(config['includes'])

        if all_includes:
            cmake_file.write('# Common include directories\n')
            cmake_file.write(f'target_include_directories({project_name} PRIVATE\n')
            for include in sorted(all_includes):
                cmake_file.write(f'    "{include}"\n')
            cmake_file.write(')\n\n')

        # Common compile definitions from all configs
        all_defines = set()
        for config in configs:
            all_defines.update(config['defines'])

        if all_defines:
            cmake_file.write('# Common compile definitions\n')
            cmake_file.write(f'target_compile_definitions({project_name} PRIVATE\n')
            for define in sorted(all_defines):
                cmake_file.write(f'    {define}\n')
            cmake_file.write(')\n\n')

        # Config specific settings
        for config in configs:
            config_name = config['name']
            cmake_flags = config['cmake_flags']

            cmake_file.write(f'# {config_name} configuration\n')

            if cmake_flags:
                cmake_file.write(f'target_compile_options({project_name} PRIVATE\n')
                cmake_file.write(f'    $<$<CONFIG:{config_name}>:')
                cmake_file.write(' '.join(cmake_flags))
                cmake_file.write('>\n')
                cmake_file.write(')\n')

            # Config-specific defines (those not in common)
            config_defines = set(config['defines']) - all_defines
            if config_defines:
                cmake_file.write(f'target_compile_definitions({project_name} PRIVATE\n')
                cmake_file.write(f'    $<$<CONFIG:{config_name}>:')
                cmake_file.write(';'.join(sorted(config_defines)))
                cmake_file.write('>\n')
                cmake_file.write(')\n')

            # Link libraries
            if config['libs']:
                cmake_file.write(f'target_link_libraries({project_name} PRIVATE\n')
                cmake_file.write(f'    $<$<CONFIG:{config_name}>:')
                cmake_file.write(' '.join(sorted(config['libs'])))
                cmake_file.write('>\n')
                cmake_file.write(')\n')

            cmake_file.write('\n')

    print(f"Generated {cmake_path}")

def process_csv_file(csv_file):
    project_name = os.path.basename(csv_file).replace("_flags.csv", "")
    output_dir = f"cmake_{project_name}"

    configs = []

    with open(csv_file, 'r') as f:
        reader = csv.DictReader(f, delimiter=';')
        for row in reader:
            config_name = row['Config'].split(' - ')[1].strip()

            # Combine BASE CPP and CPP flags
            cpp_flags = f"{row['BASE CPP']} {row['CPP']}".strip()

            # Combine BASE LINK32 and LINK32 flags if they exist
            link_flags = ""
            if 'BASE LINK32' in row and 'LINK32' in row:
                link_flags = f"{row['BASE LINK32']} {row['LINK32']}".strip()

            includes = parse_include_paths(cpp_flags)
            defines = parse_defines(cpp_flags)
            libs = parse_libs(link_flags)
            cmake_flags = convert_vs_to_cmake_flags(cpp_flags)

            configs.append({
                'name': config_name,
                'cpp_flags': cpp_flags,
                'link_flags': link_flags,
                'includes': includes,
                'defines': defines,
                'libs': libs,
                'cmake_flags': cmake_flags
            })

    generate_cmake_file(project_name, configs, output_dir)

def find_csv_files(start_dir):
    return list(Path(start_dir).glob('**/*_flags.csv'))

def main():
    parser = argparse.ArgumentParser(description="Generate CMakeLists.txt from Visual Studio flag CSV files")
    parser.add_argument("-d", "--dir", help="Directory to search for CSV files", default=".")
    args = parser.parse_args()

    csv_files = find_csv_files(args.dir)
    if not csv_files:
        print(f"No *_flags.csv files found in {args.dir}")
        return

    print(f"Found {len(csv_files)} CSV files")

    for csv_file in csv_files:
        process_csv_file(csv_file)

    print(f"Successfully processed {len(csv_files)} CSV files")

if __name__ == "__main__":
    main()