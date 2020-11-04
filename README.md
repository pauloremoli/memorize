# memorize
Tool to help in the memorization of any content

Example of content:

Jak ci się spało? / How did you sleep?

Dobrze spałeś? / Did you sleep well?


usage: memorize.py [-h] [-a] [-r] [-s SEPARATOR] [-f FILTER] [-d DIR]
                   [-c {LEFT,RIGHT,RANDOM}]

optional arguments:
  -h, --help            show this help message and exit
  -a, --append          Append mistakes to existing file
  -r, --readonly        Read only mode
  -s SEPARATOR, --separator SEPARATOR
                        Separator for content file (Default: '/')
  -f FILTER, --filter FILTER
                        Filter for filename (Default: '*.txt')
  -d DIR, --dir DIR     Directory to search for files (Default: '.')
  -c {LEFT,RIGHT,RANDOM}, --column {LEFT,RIGHT,RANDOM}
                        Show value from which column (Default: RANDOM)
