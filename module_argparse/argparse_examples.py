#-*- coding: utf-8 -*-
"""Работа с модулем argparse"""
import argparse

parser = argparse.ArgumentParser(description="Работа с модулем argparse")

# Если аргумент является необязательным, перед ним ставится --
# Например --equipment
# Краткое имя для необязательного аргумента можно задать с помощью -
# Например '-eq' '--equipment'
parser.add_argument('-eq','--equipment', help="Select a brand of equipment")
args = parser.parse_args()
if args.equipment == 'ARIS':
    print("You've chosen ARIS!")
