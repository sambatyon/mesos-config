#!/usr/bin/env python3
import argparse
import sys
import yaml
import master_config



def process_arguments(args):
    parser = argparse.ArgumentParser(description='''
    Reads a yaml formatted file which imitates the TeamCity build.
    ''')
    parser.add_argument('yaml_file', help='The Mesos configuration file',\
        metavar='YAML_FILE')
    return parser.parse_args(args[1:])

def main(args):
    with open(process_arguments(args).yaml_file) as yaml_file:
        raw_yaml = yaml.load(yaml_file)
        master_configuration = master_config.MasterConfig(raw_yaml)

if __name__ == '__main__':
    main(sys.argv)
