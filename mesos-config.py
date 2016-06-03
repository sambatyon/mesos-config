#!/usr/bin/env python3
import argparse
import sys
import yaml

def process_arguments(args):
    parser = argparse.ArgumentParser(description='''
    Reads a yaml formatted file which imitates the TeamCity build.
    ''')
    parser.add_argument('yaml_file', help='The Mesos configuration file',\
        metavar='YAML_FILE')
    return parser.parse_args(args[1:])

def main(args):
    with open(process_arguments(args).yaml_file) as yaml_file:
        print(yaml.load(yaml_file))

if __name__ == '__main__':
    main(sys.argv)
