from pathlib import Path

logfile_dir = Path('C:/Appl/log')
logfile = logfile_dir / 'autotrader_child_0.log.2023-08-30T00_18_56.092811'


def main():
    for line in open(logfile, 'r'):
        l2 = line.rstrip()
        print(l2)


if __name__ == '__main__':
    main()
