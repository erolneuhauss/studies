# chezmoi

```shell
Manage your dotfiles across multiple diverse machines, securely

Usage:
  chezmoi [command]

Available Commands:
  add                  Add an existing file, directory, or symlink to the source state
  age                  Interact with age
  apply                Update the destination directory to match the target state
  archive              Generate a tar archive of the target state
  cat                  Print the target contents of a file, script, or symlink
  cat-config           Print the configuration file
  cd                   Launch a shell in the source directory
  chattr               Change the attributes of a target in the source state
  completion           Generate shell completion code
  data                 Print the template data
  decrypt              Decrypt file or standard input
  destroy              Permanently delete an entry from the source state, the destination directory, and the state
  diff                 Print the diff between the target state and the destination state
  doctor               Check your system for potential problems
  dump                 Generate a dump of the target state
  dump-config          Dump the configuration values
  edit                 Edit the source state of a target
  edit-config          Edit the configuration file
  edit-config-template Edit the configuration file template
  encrypt              Encrypt file or standard input
  execute-template     Execute the given template(s)
  forget               Remove a target from the source state
  generate             Generate a file for use with chezmoi
  git                  Run git in the source directory
  help                 Print help about a command
  ignored              Print ignored targets
  import               Import an archive into the source state
  init                 Setup the source directory and update the destination directory to match the target state
  license              Print license
  managed              List the managed entries in the destination directory
  merge                Perform a three-way merge between the destination state, the source state, and the target state
  merge-all            Perform a three-way merge for each modified file
  purge                Purge chezmoi's configuration and data
  re-add               Re-add modified files
  secret               Interact with a secret manager
  source-path          Print the source path of a target
  state                Manipulate the persistent state
  status               Show the status of targets
  target-path          Print the target path of a source path
  unmanaged            List the unmanaged files in the destination directory
  update               Pull and apply any changes
  upgrade              Upgrade chezmoi to the latest released version
  verify               Exit with success if the destination state matches the target state, fail otherwise

Flags:
      --cache path                                     Set cache directory (default /Users/ENeuhaus/.cache/chezmoi)
      --color bool|auto                                Colorize output (default auto)
  -c, --config path                                    Set config file
      --config-format <none>|json|toml|yaml            Set config file format
      --debug                                          Include debug information in output
  -D, --destination path                               Set destination directory (default /Users/ENeuhaus)
  -n, --dry-run                                        Do not make any modifications to the destination directory
      --force                                          Make all changes without prompting
  -h, --help                                           help for chezmoi
      --interactive                                    Prompt for all changes
  -k, --keep-going                                     Keep going as far as possible after an error
      --mode file|symlink                              Mode (default file)
      --no-pager                                       Do not use the pager
      --no-tty                                         Do not attempt to get a TTY for prompts
  -o, --output path                                    Write output to path instead of stdout
      --persistent-state path                          Set persistent state file
      --progress bool|auto                             Display progress bars (default auto)
  -R, --refresh-externals always|auto|never[=always]   Refresh external cache (default auto)
  -S, --source path                                    Set source directory (default /Users/ENeuhaus/.local/share/chezmoi)
      --source-path                                    Specify targets by source path
      --use-builtin-age bool|auto                      Use builtin age (default auto)
      --use-builtin-diff                               Use builtin diff
      --use-builtin-git bool|auto                      Use builtin git (default auto)
  -v, --verbose                                        Make output more verbose
      --version                                        version for chezmoi
  -W, --working-tree path                              Set working tree directory

```
