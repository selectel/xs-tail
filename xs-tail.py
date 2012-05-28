#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function

import time

from xen.lowlevel import xs as libxs


def tail():
    h = libxs.xs()
    h.watch("/", None)  # Watch *all* events.

    while True:
        path, _ = h.read_watch()
        print("[{0}] {1} := {2}".format(time.time(), path, h.read("", path))


if __name__ == "__main__":
    tail()
