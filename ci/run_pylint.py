from pylint.lint import Run
from pylint.reporters.collecting_reporter import CollectingReporter

if __name__ == '__main__':
    this = Run(['--rcfile=.pylintrc', '--output-format=colorized', 'adventure/'], reporter=CollectingReporter)
