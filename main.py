#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Application de gestion de votes
"""

from application import Application


def main() -> None:
    """Programme principal."""
    print("""\
--------------------------
Bienvenue dans notre prix Goncourt
--------------------------""")

    app = Application()
    app.run()


if __name__ == "__main__":
    main()
