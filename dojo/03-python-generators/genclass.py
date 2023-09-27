logfile = './OpenSSH_2K.log'


def main():
    for line in open(logfile, 'r'):
        print(line.rstrip())


if __name__ == '__main__':
    main()
