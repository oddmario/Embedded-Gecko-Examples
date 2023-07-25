# GeckoEmbed

An attempt to embed Gecko in a Qt application using Python

## How to run
1. Install Firefox Portable (https://portableapps.com/apps/internet/firefox_portable) into the `src/firefox/base/FirefoxPortable` directory of this project. (The Firefox Portable version doesn't matter, this project at its current stage should be compatibile with all the Firefox versions ever introduced)

2. Make sure you have both the `PyQt5` and `pywin32` packages installed using pip.

3. Run `src/GeckoEmbed.py`

## Important notes
- This project is currently highly experimental and isn't suited for any production applications. This repository mostly introduces one idea for embedding Gecko into a native window using the Qt bindings of Python. If I ever get this whole thing to work properly without any annoyances, inconveniences and user-unfriendly experiences, I will be happy to introduce the first Electron-like alternative for the Gecko engine :)

- This project currently works for the Windows operating system only. Support for Mac OSX and Linux is definitely planned.

## References used (thanks to)
- https://gist.github.com/chipolux/acf28d367822e20cc62672f49eb1aab7
- https://superuser.com/a/1269912/936854