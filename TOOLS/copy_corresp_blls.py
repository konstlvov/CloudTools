#coding=cp1251

import sys
import os
import fnmatch
import shutil

print sys.argv
if len(sys.argv) != 4:
  print 'Copies corresponding BLLs to dst_bll_dir'
  print 'Usage:  copy_corresp_blls.py <src_bls_dir> <src_bll_dir> <dst_bll_dir>'
  print 'e.g.:   copy_corresp_blls.py C:\\models\\SanPit\\SOURCE C:\\models\\SanPit\\USER C:\\UPGRADES\\SanPit\\00000001\\USER'
  print 'May be used from .cmd file with content like this:'
  print 'C:\\Python27\\python.exe .\\copy_corresp_blls.py C:\\tmp\\SanPit\\SOURCE C:\\tmp\\SanPit\\USER C:\\tmp\\SanPitUpgrades\\00000001\\USER'
  exit()

src_bls_dir = sys.argv[1]
src_bll_dir = sys.argv[2]
dst_bll_dir = sys.argv[3]

def GetFilesInDir(rootDir, fileMask):
  matches = []
  for root, dirnames, filenames in os.walk(rootDir):
    for filename in fnmatch.filter(filenames, fileMask):
      matches.append(os.path.join(root, filename))
  return matches

def ForceCopyFile(absSrcPath, absDstPath):
  dirname = os.path.dirname(absDstPath)
  if os.path.exists(dirname):
    if not os.path.isdir(dirname):
      raise Exception(dirname + ' already exists and is not directory. Stopping.')
  else:
    print 'about to make dirs: ' + dirname
    os.makedirs(dirname)
  print 'about to copy ' + absSrcPath + ' to ' + absDstPath
  shutil.copyfile(absSrcPath, absDstPath)


for fp in GetFilesInDir(src_bls_dir, '*.bls'):
  dirname = os.path.dirname(fp) # строка вида C:\tmp\SanPit\SOURCE\Admin\Common
  basename = os.path.splitext(os.path.basename(fp)) # tuple вида ('laBank', '.bls')
  bllname = basename[0] + '.bll'
  ForceCopyFile(src_bll_dir + '\\' + bllname, dst_bll_dir + '\\' + bllname)

