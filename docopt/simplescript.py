#!/usr/bin/env python
"""\
Summary:
    runtests -- generalized test runner of some sort -- put together as an
                example lighting talk for the Minneapolis pymntos python
                user's group.

Usage:
    runtests [--help|-h] [--quiet] [--coverage=<pkg>...]
             [--scratch-path=<path>] [--leave-pyc]
             [--collect-only] [--list] [<test-name-regex>...]

Examples:
    runtests -q '.*'
    runtests -q --leavepyc 'regression_test|branch_push_tests'
    runtests -c webtools -c django-extensions -c 'release/.*'

Options:
    --help, -h                 Show this help message.
    --quiet, -q                No need to make a big fuss about everything ...
    --coverage=<pkg>, -c=<pkg> Run nose coverage tools, create html on listed
                               packages.
    --scratch-path=<path>      Temp area to run in [default: /tmp/tests].
    --leavepyc                 Don't cleanup pyc file before running tests.
    --collect-only             Run nose collect-only.
    --list                     List all tests.
"""

def test_runner(args):
    quiet = args['--quiet']
    coverage = args['--coverage']

    for key, value in args.iteritems():
        print key, value



if __name__ == '__main__':

    import docopt

    args = docopt.docopt(
        __doc__, version='runtests version 0.0')

    test_runner(args)

