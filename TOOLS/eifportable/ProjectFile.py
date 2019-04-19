# -*- coding: utf-8 -*-

import utils
import hashlib
import os.path
###############################################################################
class ProjectFile(object):
	"Базовый класс для хранение информации о каком-либо файле проекта"
	def __init__(self, full_path):	
		self.full_path = full_path
		self.name      = utils.file_name_by_fullname(full_path)
		self.md5       = ''

	def is_exists(self):
		return os.path.exists(self.full_path)

	def get_data(self):
		data = None
		if self.is_exists():
			data = open(self.full_path, "rb").read()
		return data

	def update_md5(self, data):
		if data == None:
			self.md5 = ''
		else:
			self.md5 = hashlib.md5(data).hexdigest()

	def get_path(self):
		return self.full_path

	def get_name(self):
		return self.name

	def get_md5(self):
		return self.md5
###############################################################################