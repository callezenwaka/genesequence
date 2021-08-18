# getting-started-with-eel

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
$ git clone git@github.com:callezenwaka/algogene.git
$ cd algogene
```

- Install eel, and pyinstaller

```sh
$ pip install eel pyinstaller
```

- Run the app

```sh
$ python algogene.py
```

## Packaging the app
You can pass any valid `pyinstaller` flag in the following command to further customize the way your app is built.
```sh
$ python -m eel algogene.py web --noconsole --onefile --name algogene --icon=algogene.icns
```
