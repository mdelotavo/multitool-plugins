# multitool-plugins

## Install the `multitool` package
```
pip3 install -U multitool
```

## Check available commands before installing plugins
```
$ multitool -h
Usage: multitool [OPTIONS] COMMAND [ARGS]...

  Welcome to the Multitool command-line interface!

  PyPI:   https://pypi.org/project/multitool/
  GitHub: https://github.com/mdelotavo/multitool

Options:
  -V, --version  Show the version and exit.
  -h, --help     Show this message and exit.

Commands:
  plugins   Simple plugins manager for distributing commands.
```

## Install the plugins in this repository
```
multitool plugins configure -a
echo -e '[sources]\npublic = https://github.com/mdelotavo/multitool-plugins.git' > ~/.multitool/plugins/config
multitool plugins update
multitool plugins show
multitool plugins show -n public
multitool plugins show -n public --show-commit-only
# OUT: 1a1f847 - (HEAD -> main, origin/main, origin/HEAD) Add code examples (31 minutes ago) <Matthew Delotavo>
multitool plugins show -n public --show-dependencies-only
# OUT: click
```

## Check installed plugin commands
```
$ multitool examples -h
Usage: multitool examples [OPTIONS] COMMAND [ARGS]...

  First paragraph.

  This is a very long second paragraph and as you can see wrapped very early
  in the source text but will be rewrapped to the terminal width in the final
  output.

  This is
  a paragraph
  without rewrapping.

  And this is a paragraph that will be rewrapped again.

Options:
  -V, --version         Show the version and exit.
  --repo-home TEXT
  --debug / --no-debug
  -h, --help            Show this message and exit.

Commands:
  ansi-colors
  callbacks-eager
  cat
  chmod
  clear
  clone
  commit
  convert
  copy                Move file SRC to DST.
  cp
  delete              delete the repo
  digest
  dropdb
  echo                Print value of SRC environment variable.
  edit                Edit FILENAME if the file exists.
  encrypt
  feature-switches
  get-commit-message
  get-streams
  getchar
  greet
  hello               Simple program that greets NAME for a total of...
  info
  init                init the repo
  initdb
  inout               Copy contents of INPUT to OUTPUT.
  launch              This can be used to open the default application...
  less
  log
  login
  parse-bool
  parse-datetime
  parse-float
  parse-int
  parse-str
  parse-uuid
  pause
  perform
  print-stdout
  progress-bar
  prompt
  prompt2
  putitem
  read-config         Print APP_NAME config file.
  read-user
  repeat
  repeat-float
  roll
  runserver
  sync
  touch               Print FILENAME if the file exists.
  write-file          Write 'Hello World!' to FILENAME.
```
