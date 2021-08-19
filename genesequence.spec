# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['genesequence.py'],
             pathex=['/Users/mac/Documents/Projects/genesequence'],
             binaries=[],
             datas=[('/Users/mac/anaconda3/envs/algogene/lib/python3.9/site-packages/eel/eel.js', 'eel'), ('web', 'web')],
             hiddenimports=['bottle_websocket'],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,  
          [],
          name='genesequence',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None , icon='genesequence.icns')
app = BUNDLE(exe,
             name='genesequence.app',
             icon='genesequence.icns',
             bundle_identifier=None)
