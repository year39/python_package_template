
import yaml

def main():
    print ("hello from simple.py")

    with open("system_config.yaml", "r") as fd:
        config = yaml.load(fd, Loader=yaml.FullLoader)
        output = yaml.dump(config, Dumper=yaml.Dumper)
        print (output)

if __name__ == '__main__':
    main()
