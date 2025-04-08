# -*- mode: python ; coding: utf-8 -*-
# add ('env/lib/python3.11/site-packages/ffprobe', './ffprobe') to datas

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    #datas=[('env/lib/python3.11/site-packages/whisper/assets/mel_filters.npz', 'env/lib/python3.11/site-packages/whisper/assets'), 
    #('env/lib/python3.11/site-packages/whisper/assets', './whisper/assets'),
    #('env/lib/python3.11/site-packages/ffprobe', './ffprobe'),
    #('env/lib/python3.11/site-packages/ffmpeg', './ffmpeg')],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='autonote',
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
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='autonote',
)
app = BUNDLE(
    coll,
    name='autonote.app',
    icon=None,
    bundle_identifier=None,
)
