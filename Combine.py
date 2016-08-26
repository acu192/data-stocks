import os
import sys


def read_file(symbol, path, outfile):

    with open(path) as f:
        for line in f:
            parts = line.strip().split(',')
            if len(parts) != 7:
                continue
            if parts[0] == 'Date':
                continue
            line = ','.join([symbol] + parts) + '\n'
            outfile.write(line)


def main():

    dir_path = sys.argv[1]

    with open('all.csv', 'w') as outfile:

        for filename in os.listdir(dir_path):
            symbol = filename.split('_')[0]
            path = os.path.join(dir_path, filename)
            read_file(symbol, path, outfile)



if __name__ == '__main__':
    main()
