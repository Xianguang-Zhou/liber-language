# -*- coding: utf-8 -*-

import re


class LazyPattern:
    def __init__(self, string: str):
        self._string = string
        self.pattern = self.compile

    def compile(self):
        pattern = re.compile(self._string)
        self.pattern = lambda: pattern
        return pattern

    def __hash__(self):
        return hash(self._string)

    def __eq__(self, other):
        return self._string == other._string

    def __ne__(self, other):
        return not (self == other)


def toPatternDict(expressionDict: dict):
    patternDict = {}
    for expression, value in expressionDict.items():
        pattern = LazyPattern(expression)
        patternDict[pattern] = value
    return patternDict


def toPatternSet(expressionSet: set):
    patternSet = set()
    for expression in expressionSet:
        pattern = LazyPattern(expression)
        patternSet.add(pattern)
    return patternSet


def finditer(pattern: LazyPattern, string):
    return pattern.pattern().finditer(string)


def search(pattern: LazyPattern, string):
    return pattern.pattern().search(string)


def match(pattern: LazyPattern, string):
    return pattern.pattern().match(string)
