#!/usr/bin/env python3

import asyncssh
import sys
import asyncio
import argparse
import shlex
import subprocess
from initialization import *



async def run_client(port, host, user, passw, debug):
    if debug == None:
       debug = False
    session_options = await asyncssh.SSHClientConnectionOptions(known_hosts=None, username=user, password=passw) 
    async with asyncssh.connect(host, port=port, options=session_options) as conn:
        mainchan, mainsession = await conn.open_session()
        while True:
            initialize(mainchan, mainsession, debug)


def main(args):
    try:
        asyncio.get_event_loop().run_until_complete(run_client(args.port, args.host, args.user, args.passw, args.debug))
    except (OSError, asyncssh.Error) as exc:
        sys.exit('SSH connection failed: ' + str(exc))

if __name__ == "__main__":
    args = argparse.ArgumentParser(prog='connect.py', add_help=True)
    args.add_argument('-p', '--port', dest='port', help='remote port to connect', default=22, type=int)
    args.add_argument('-n', '--hostname', dest='host', help='hostname or IP Address', type=str)
    args.add_argument('--pass', dest='passw', help='password to authenticate', type=str)
    args.add_argument('--user', dest='user', help='username to authenticate', type=str)
    args.add_argument('--debug', dest='debug', help='Turns debug mode on', action='store_const', const=True)
    parsedargs = args.parse_args()
    print(parsedargs)
    main(parsedargs)
	#### TO DO: ARGPARSER #####
