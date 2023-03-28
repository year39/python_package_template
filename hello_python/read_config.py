
import yaml
import os

def print_config():
    config_file = os.path.join(os.path.dirname(__file__), "config","system_config.yaml")

    with open(config_file, "r") as fd:
        config = yaml.load(fd, Loader=yaml.FullLoader)
        output = yaml.dump(config, Dumper=yaml.Dumper)

    print (output)

if __name__ == '__main__':
    print_config()
