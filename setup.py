from setuptools import setup

APP = ['app.py']
DATA_FILES = ['icon.png']
OPTIONS = {
    'argv_emulation': True,
    'iconfile': 'icon.icns',
    'plist': {
        'CFBundleShortVersionString': '1.0.2',
        'LSUIElement': True,
    },
    'packages': ['rumps','requests', 'commands']
}

setup(
    app=APP,
    name='MenubarPing',
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'], install_requires=['rumps','requests']
)
