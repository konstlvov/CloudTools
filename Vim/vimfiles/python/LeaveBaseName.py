#coding:utf8
import vim
import os
for i in range(vim.current.buffer.mark('<')[0] - 1, vim.current.buffer.mark('>')[0]):
  line = vim.current.buffer[i]
  vim.current.buffer[i] = os.path.basename(line)
