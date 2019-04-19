# -*- coding: utf-8 -*-

import re
import os.path
###############################################################################
def parse_bls(txt, header):
	""" В тексте txt удалить комментарии, найти слово header,
		разобрать список слов после него, удалить дубликаты, привести к нижнему регистру
		и вернуть получившийся список
	"""
	str_cmnt     = "//.*?(\n|\r)"
	block_cmnt1  = "\{.*?\}"
	block_cmnt2  = "\(\*.*?\*\)"
	pattern_cmnt = '(' + str_cmnt + ')|(' + block_cmnt1 + ')|(' + block_cmnt2 + ')'
	pattern_uses = r'\b'+header+r'\b(.*?);'
	reg_cmnt     = re.compile(pattern_cmnt, re.DOTALL)
	reg_header   = re.compile(pattern_uses, re.DOTALL | re.IGNORECASE)

	txt = reg_cmnt.sub('', txt)
	p = reg_header.search(txt)
	if p == None:
		return []
	res_list = map(lambda a: a.strip().lower(), p.group(1).split(','))
	# удаляем дубликаты
	return list(set(res_list))
###############################################################################
def file_name_by_basename(basename):
	"По имени файла с расширением получить имя файла и привести его к нижнему регистру (FiLe.exe -> file)"
	return os.path.splitext(basename)[0].strip().lower()
###############################################################################
def file_name_by_fullname(fullname):
	"По полному пути к файлу получить имя файла и привести его к нижнему регистру (c:\FiLe.exe -> file)"
	basename = os.path.basename(fullname)
	return file_name_by_basename(basename)
###############################################################################