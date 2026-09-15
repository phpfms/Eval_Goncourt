#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Application de gestion de votes
"""

from Application import Application


def main() -> None:
    """Programme principal."""
    print("""\
--------------------------
Bienvenue dans notre école
--------------------------""")

    app = Application()
    app.run()


if __name__ == "__main__":
    main()
