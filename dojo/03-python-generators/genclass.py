from pathlib import Path

logfile_dir = Path('C:/Appl/log')
logfile = logfile_dir / 'autotrader_child_0.log.2023-08-30T00_18_56.092811'
logfile = logfile_dir / 'thousand.log'


def main():
    for line in open(logfile, 'r'):
        print(line.rstrip())


if __name__ == '__main__':
    main()
