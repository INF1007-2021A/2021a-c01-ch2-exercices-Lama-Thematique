#!/usr/bin/env python
# -*- coding: utf-8 -*-
def majuscule(mot):
    if(len(mot) == 0):
        return mot
    i = ord(mot[0])
    if (i >= 97 and i <= 122):
        return chr(i-32) + majuscule(mot[1:])
    return mot[0] + majuscule(mot[1:])


if __name__ == '__main__':
    mots = [
        'riz',
        'cours',
        'voiture',
        'oiseau',
        'bonjour',
        'églantier',
        'arbre'
    ]
    for i in range(len(mots)):
        mots[i] = majuscule(mots[i])

    print(mots)

