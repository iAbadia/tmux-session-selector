About
=====

`Sessel` is a small python script that assists the user in starting a new or
continuing an existing [tmux](http://tmux.sourceforge.net/) session.

Use Case
========

You may use it upon launch of a
[terminal](http://software.schmorp.de/pkg/rxvt-unicode.html) to always work
inside a named, structured (through buffers) session that you may reattach to
and continue.

Workflow
========

When executed, it presents you with the names of the existing sessions and
prompts you to either select one or start a new one.

`Sessel` supports you in selecting a session by offering tab
completion for existing session names.

Selecting an existing session attaches you to the same. Entering a new name will
start an appropriately named session for you. Cutting a corner by just pressing
enter will start a new session with tmux choosing a default name (which is an
incrementing integer).

If you instructed your terminal to execute `sessel` upon launch, it will exit
when you close your last buffer.
