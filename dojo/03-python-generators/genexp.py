logfile = './OpenSSH_2K.log'


def main():
    log = open(logfile, 'r')

    for line in log:
        print(line.rstrip())


if __name__ == '__main__':
    main()
