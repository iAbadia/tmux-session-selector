#!/usr/bin/env python

import subprocess
import readline
import sys
import os


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
            #use explicit path to force use of v1.7
            raw_sessions = subprocess.check_output(['tmux', 'list-sessions'],
                                                   stderr=subprocess.PIPE)
        except subprocess.CalledProcessError:
            # tmux returns 1 if there are no sessions
            pass
        else:
            sessions = raw_sessions.split('\n')
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


if __name__ == '__main__':

    sessions = TmuxSessions()

    readline.parse_and_bind('tab: complete')
    readline.set_completer(sessions.complete)

    if sessions:
        print("Please select one of the existing sessions to attach to\n" \
              "or enter a name for a new session:")
        for session in sessions:
            print("\t{}".format(session))
    else:
        print("Currently, there are no sessions.\n" \
              "Please enter a name for a new session")

    try:
        session = raw_input('session: ')
    except (KeyboardInterrupt, EOFError):
        sys.exit()

    sessions.connect(session)

