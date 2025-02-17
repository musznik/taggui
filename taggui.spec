# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_data_files, collect_dynamic_libs, copy_metadata

binaries = collect_dynamic_libs('bitsandbytes')
hiddenimports = ['triton._C.libtriton']
datas = [('clip-vit-base-patch32', 'clip-vit-base-patch32'), ('images/icon.ico', 'images')]
datas += collect_data_files('transformers', include_py_files=True, includes=['**/*.py'])
datas += collect_data_files('triton')
datas += collect_data_files('xformers')
datas += copy_metadata('transformers', recursive=True)


block_cipher = None


a = Analysis(
    ['taggui/run_gui.py'],
    pathex=['taggui'],
    binaries=binaries,
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
    module_collection_mode={
        'bitsandbytes': 'pyz+py',
        'triton': 'py',
        'xformers': 'py',
    },
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='taggui',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['images/icon.ico'],
    contents_directory='_taggui',
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='taggui',
)
