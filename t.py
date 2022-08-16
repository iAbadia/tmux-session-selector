#!/usr/bin/env python

import subprocess
import readline
import sys
import os

from simple_term_menu import TerminalMenu


class TmuxSessions(object):

    def __init__(self):
        self._sessions = self._fetch_sessions()


    def complete(self, prefix, iteration):
        matches = [session for session in self._sessions if session.startswith(prefix)]
        match = None
        if iteration < len(matches):
            match = matches[iteration]
        return match


    def connect(self, session):
        if session in self._sessions:
            self._attach(session)
        else:
            self._create(session)


    def _fetch_sessions(self):
        names = []

        try:
            raw_sessions = subprocess.getoutput("tmux ls | cut -d':' -f 1")
        except subprocess.CalledProcessError:
            # tmux returns 1 if there are no sessions
            pass
        else:
            sessions = str(raw_sessions).split('\n')
            sessions = filter(bool, sessions)

            for session in sessions:
                name = session.split(':')[0]
                names.append(name)

        return names


    def _attach(self, session):
        print("Attaching to existing tmux session '{}'".format(session))
        os.execlp('tmux', 'tmux', 'attach-session', '-t', session)


    def _create(self, session):
        print("Creating new tmux session '{}'".format(session))
        args = ['tmux', 'new-session']
        if session:
            args.extend(['-s', session])
        os.execvp('tmux', args)


    def __nonzero__(self):
        return len(self._sessions)


    def __iter__(self):
        return self._sessions.__iter__()

    def list(self):
        return self._sessions;


if __name__ == '__main__':

    sessions = TmuxSessions()

    readline.parse_and_bind('tab: complete')
    readline.set_completer(sessions.complete)

    session=""
    if sessions:
        list_sessions = sessions.list()
        terminal_menu = TerminalMenu(list_sessions)
        menu_entry_index = terminal_menu.show()
        session=list_sessions[menu_entry_index]
        sessions.connect(session)
    else:
        print("No sessions available.")
