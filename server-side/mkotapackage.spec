# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['otapackage\\mkotapackage.py'],
             pathex=['C:\\ota_update_fiio_M3K\\server-side'],
             binaries=[],
             datas=[(".\\otapackage\\res\\keys\\testkey.pk8", "."),
             (".\\otapackage\\res\\keys\\testkey.x509.pem", ".")],
             hiddenimports=[],
             hookspath=[],
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
          name='mkotapackage',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
