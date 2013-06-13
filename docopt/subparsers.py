#!/usr/bin/env python
"""\
expect -- example copy and compare script that uses docopt subparsers. Put 
          together as an example lighting talk for the Minneapolis pymntos 
          python user's group. 

Usage:
    expect [--version] [-h|--help] <command> [options] [<args>...]

Currently supported expect commands are:

   cp        Copy expect data for later use.
   compare   Compare previously copied data to a live data set.

See 'expect help <command>' for more information on a specific command.
"""

from textwrap import dedent as _dedent


def dedentfn(fn):
    fn.__doc__ = _dedent(fn.__doc__)
    return fn


@dedentfn
def cp(args, subargs):
    """\
    Summary:
        expect cp -- copy files to be used as basis expect data when doing a
        'expect compare' operation.

    Usage:
        expect cp [--help|-h] [--quiet|-q] [--force|-f]
                  [--remove|-r] [--levels=<number>]
                  [--include=<regex>...] [--exclude=<regex>...]
                  [--include-hidden] [--include-links]
                  <src> <dst>

    Options:
        --help, -h           Show this help message.
        --quiet, -q          Be quiet.
        --force, -f          Do not prompt for copy if file already exists.
        --remove, -r         Remove dst directory before copy.
        --levels <number>    Levels to descend [default: None].
        --include <regex>    Regex pattern to filter files to copy.
                             Only applies to files (not dirs) [default: .*].
        --exclude <regex>    Regex pattern to filter files/dirs to skip
                             [default: None].
        --include-hidden     Include dirs/files that start with '.'.
        --include-links      Do descend into/copy symlinks.

    Examples:
        expect cp -qrf golden expect
        expect cp --include '\.yml(\.gz)$' --exclude 'userlogs' golden expect

    """


@dedentfn
def compare(args, subargs):
    """\
    Summary:
        expect compare -- compare a src and dst directory using a diff tool of
        choice.

    Usage:
        expect compare [--help|-h] [--quiet|-q] [--stop|-s]
                       [--rc-path=<path>] [--diff-tool=<tool>] 
                       [--view-tool=<tool>] [--include=<regex>...] 
                       [--exclude=<regex>...] <src> <dst>

    Examples:
        expect compare expect golden
        expect compare --viewtool 'vimdiff -c 'set diffopt+=iwhite' expect golden
        expect compare --include '\.spf(\.gz)$' expect golden

    Options:
        --help, -h           Show this help message.
        --quiet, -q          Be quiet.
        --stop, -s           Stop on first error. 
        --difftool=<tool>    Diff tool to use.  On no difference, tool should
                             output nothing to stdout/stderr
                             [default: None].
        --viewtool=<tool>    If output of difftool shows difference, use this
                             tool to view. If none given, use difftool.  
                             If 'None' or 'False' is provided, viewing is 
                             suppressed. [default: diff -dwB].
        --include=<regex>    Regex pattern to filter files to copy.
                             Only applies to files (not dirs) [default: .*].
        --exclude=<regex>    Regex pattern to filter files/dirs to skip
                             [default: None].
    """



if __name__ == '__main__':

    import sys
    import docopt

    args = docopt.docopt(__doc__, version='expect ver 0.0', options_first=True)

    cmd = args['<command>']

    argv = [cmd] + args['<args>']

    try:
        fn = getattr(sys.modules[__name__], cmd)
    except (AttributeError, TypeError,):
        exit("%r is not a valid sub command. See 'expect help'." % cmd)

    sub_args = docopt.docopt(fn.__doc__, argv=sub_argv)
    fn(args, sub_args)
