# -*- coding: utf-8 -*-
"""
@Author: Faith
@Date: 2026/2/12
@Time: 11:55
@Description:
@FilePath: system_args.py
"""
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    # parser.add_argument("--mul", action="store_true")
    parser.add_argument('--input', type=str, default='', help='input file path')
    parser.add_argument('--output', type=str, default='', help='output file path')
    args = parser.parse_args()
    print(args.input)
    print(args.output)












