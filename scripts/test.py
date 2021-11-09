#!/usr/bin/env python3
import pandas

def main():
  datasets = [('brazil children', './data/BRA_children_under_five_2019-06-01.csv'),
              ('sweden general', './data/swe_general_2020.csv')]
  for name, curr_path in datasets:
    print(f'\n\nName: {name}')
    df = pandas.read_csv(curr_path)
    print(df.head())
    print(df.columns)
    print(df.describe())

if __name__ == '__main__':
    main()
