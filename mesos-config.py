#!/usr/bin/env python3
import argparse
import csv
import sys
import yaml
import master_config



def process_arguments(args):
    parser = argparse.ArgumentParser(description='''
    Mesos launcher script generator
    ''')
    parser.add_argument(\
        'config_file', \
        help='The Mesos configuration file',\
        metavar='CONFIG_FILE')

    parser.add_argument(\
        '--csv', \
        type=bool, \
        default=False, \
        help='The configuration file is given as a CSV file instead of a YAML')

    return parser.parse_args(args[1:])

def main(args):
    arguments = process_arguments(args)
    with open(arguments.config_file) as config_file:
        if not arguments.csv:
            yaml_contents = yaml.load(config_file)
        else:
            csv_contents = cvs.reader(config_file)
            print(csv_contents)
            exit(0)
        master_configuration = master_config.MasterConfig(yaml_contents)
        print(master_configuration)

if __name__ == '__main__':
    main(sys.argv)
