import argparse
from logintel.runner import run

def main():
    parser = argparse.ArgumentParser(description="LogIntel CLI - Monitor and Analyze AWS Logs")
    subparsers = parser.add_subparsers(dest='command', required=True)

    config_cmd = subparsers.add_parser('config', help='Run LogIntel with a config YAML file')
    config_cmd.add_argument('--file', required=True, help='Path to config YAML file')

    args = parser.parse_args()

    if args.command == 'config':
        run(args.file)

if __name__ == '__main__':
    main()
