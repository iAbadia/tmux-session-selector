About
=====

`tmux-session-selector` is a small python script that assists the user in starting a new or
continuing an existing [tmux](http://tmux.sourceforge.net/) session. Uses `simple_term_menu`
to offer a selectable list of available sessions.

Workflow
========

Requires installing `simple_term_menu` python package in the user directory or globally.
Combine with a bash function like:

```
function t () {
    python3 ~/my-scripts/bin/t.py
}
```
