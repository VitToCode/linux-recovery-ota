# linux-recovery-ota
forked from JaminCheung/X1000 under GPL v2 as is

source https://github.com/YuanhuanLiang/X1000/tree/master/external/recovery/

---

---Linux---

1. Clone 'main' branch of this repo

2. Go to 'server-side' directory. This is a working directory.

The directory 'server-side/otapackage/customer/generated' contains pregenerated config files for M3K fw.

'partition_nand.conf' usually doesn't need to edit (it allready correspond to M3K nand partition scheme)

'customization_nand.conf' you can edit manually or generate it interactively with running 'customize.sh' 

3. Prepare 'customization_nand.conf' in accordance what parts you plain to update with ota update (M3K.fw)

4. Place to directory 'server-side/image/nand/' partition image files which you plain to pack in M3K.fw update

5. Execute 'make' command in a workind directory 'server-side'



---Windows---

Download prebuilded release version


