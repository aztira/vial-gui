### vial-gui

# Docs and getting started

### Please visit [get.vial.today](https://get.vial.today/) to get started with Vial

Vial is an open-source cross-platform (Windows, Linux and Mac) GUI and a QMK fork for configuring your keyboard in real time.


![](https://get.vial.today/img/vial-win-1.png)


---


#### Releases

Visit https://get.vial.today/ to download a binary release of Vial.

#### Development

Python 3.12 is recommended.

Install dependencies:

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

To launch the application afterwards:

```
source venv/bin/activate
pyinstaller misc/Vial.spec
./dist/Vial/Vial
```

## macOS (Apple Silicon)

Native arm64 build, no Rosetta required. Python 3.12 recommended.

```bash
# one-time setup
make venv

# run from source
make run

# build, sign and launch Vial.app
make app
```

The Makefile creates the virtualenv, installs dependencies, builds with PyInstaller and ad-hoc signs the app so Gatekeeper allows it to open.

Useful targets:

- `make run` — start from source
- `make app` — build, sign and launch
- `make open` — open the built app
- `make clean` — remove build artifacts
