import argparse
import sys

from pylint.lint import Run

sys.excepthook = lambda exctype, exc, traceback: print("{}: {}".format(exctype.__name__, exc))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run pylint and raise only if the score is below a threshold.')
    parser.add_argument('--target', type=str, default='.', help='Target for pylint.')
    parser.add_argument('--score', type=float, default=8., help='Minimum score (default=8).')
    parser.add_argument('--rcfile', type=str, default='.pylintrc', help='pylintrc file to use.')
    args = parser.parse_args()
    print(args)

    results = Run([f'--rcfile={args.rcfile}', f'{args.target}'], do_exit=False)
    if results.linter.stats['global_note'] < args.score:
        raise Exception(f'Score to low: {results.linter.stats["global_note"]}')
