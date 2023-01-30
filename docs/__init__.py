#! /usr/bin/env python
# -*- coding: utf-8 -*-

def allSame(s):
    return not filter(lambda x: x != s[0], s)


def hasDigit(s):
    return any(map(lambda x: x.isdigit(), s))


def getVersion(data):
    data = data.splitlines()
    return list(filter(
        lambda x: hasDigit(x) and "." in x, data
    ))[0]
