# Algogene

Resources:
https://github.com/paulwinex/eel-vuejs-example
https://github.com/SouravJohar/getting-started-with-eel
https://github.com/techformist/simple-vue-html-axios-demo
https://techformist.com/use-vue-from-url-simple-app/
https://github.com/smketterer/vue-eel-starter
https://realpython.com/pyinstaller-python/

The simplest and fastest way to create applications with a Web UI and a Python backend.

## Getting Started
- Clone the repo and cd into the directory
```sh
$ git clone git@github.com:callezenwaka/genesequence.git
$ cd genesequence
```

- Install eel, and pyinstaller

```sh
$ pip install eel pyinstaller
```

- Run the app

```sh
$ python genesequence.py
```

## Packaging the app
You can pass any valid `pyinstaller` flag in the following command to further customize the way your app is built.
For windows OS
```sh
$ python -m eel genesequence.py web --noconsole --onefile --name genesequence --icon=genesequence.ico
```
For macOS
```sh
$ python -m eel genesequence.py web --noconsole --onefile --name genesequence --icon=genesequence.icns
```
