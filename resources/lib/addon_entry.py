# -*- coding: utf-8 -*-
# GNU General Public License v3.0 (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""This is the actual FOSDEM video plugin entry point"""

if __name__ == '__main__':
    from sys import argv
    from addon import run
    run(argv)
