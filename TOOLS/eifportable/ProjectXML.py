# -*- coding: utf-8 -*-

import sys
import etree
import os.path
###############################################################################
class ProjectXMLException(Exception):
	def __init__(self, value):
		self.value = value

class ErrFileNotFound(ProjectXMLException):
	def __str__(self):
		return repr("Can'not find file for path: " + self.value)

class ErrTagNotFound(ProjectXMLException):
	def __str__(self):
		return repr("Can'not find tag: " + self.value)
###############################################################################
class ProjectXMLImpl:
	def __init__(self, user_path):
		self.path = os.path.join(user_path, 'sublime_prj.xml')

	def get_root(self, is_create):
		"is_create - создавать ли xml файл, если он не найден"
		if os.path.exists(self.path):
			txt = open(self.path).read()
			root = etree.XML(txt)
		else:
			if is_create:
				root = etree.Element("Project")
			else:
				raise ErrFileNotFound(self.path)
		return root

	def save(self, root):
		txt = etree.tostring(root, xml_declaration=True, encoding='utf-8')
		open(self.path, "wb").write(txt)

	def get_tag(self, root, tag_name, is_create):
		"is_create - создавать ли tag, если он не найден"
		for it in root.iter(tag=tag_name):
			return it
		if is_create:
			return etree.SubElement(root, tag_name)
		else:
			ErrTagNotFound(tag_name)

	def get_bls_files(self):
		bls_dict = {}
		try:
			root = self.get_root(False)
			for it in self.get_tag(root, "BLS", False):
				name = it.get("name")
				bls_md5 = it.get("bls_md5")
				bll_md5 = it.get("bll_md5")
				bls_dict[name] = {"bls_md5" : bls_md5, "bll_md5" : bll_md5}
		except Exception, e:
			pass
		return bls_dict

	def get_eif_files(self):
		eif_dict = {}
		try:
			root = self.get_root(False)
			for it in self.get_tag(root, "EIF", False):			
				name = it.get("name")
				eif_md5 = it.get("eif_md5")
				eif_dict[name] = {"eif_md5" : eif_md5}
		except Exception, e:
			pass
		return eif_dict

	def save_bls_files(self, bls_dict):
		root = self.get_root(True)
		bls_root = self.get_tag(root, "BLS", True)
		bls_root.clear()
		for it in bls_dict:
			obj = bls_dict[it]
			el = etree.Element("t", name = it, bls_md5=obj["bls_md5"], bll_md5=obj["bll_md5"])
			bls_root.append(el)
		self.save(root)

	def save_eif_files(self, eif_dict):
		root = self.get_root(True)
		eif_root = self.get_tag(root, "EIF", True)
		eif_root.clear()
		for it in eif_dict:
			# print sys.getfilesystemencoding()
			# file_name  = it.encode(sys.getfilesystemencoding())
			# file_name  = it.decode('cp1251')
			obj = eif_dict[it]
			el = etree.Element("t", name = it, eif_md5=obj["eif_md5"])
			eif_root.append(el)
		self.save(root)
###############################################################################
class ProjectXML(ProjectXMLImpl):
	def __init__(self, user_path):
		"user_path - путь к папке user"
		ProjectXMLImpl.__init__(self, user_path)

	def get_bls_files(self):
		"Получить словарь с bls файлами проиндексированный по имени и содержащий элементы вида {bll_md5, bls_md5}"
		return ProjectXMLImpl.get_bls_files(self)

	def get_eif_files(self):
		"Получить словарь с bls файлами проиндексированный по имени и содержащий элементы вида {eif_md5}"
		return ProjectXMLImpl.get_eif_files(self)

	def save_bls_files(self, bls_dict):
		"На вход нужно подать словарь такой же структуры, как возвращает get_bls_files"
		return ProjectXMLImpl.save_bls_files(self, bls_dict)

	def save_eif_files(self, eif_dict):
		"На вход нужно подать словарь такой же структуры, как возвращает get_eif_files"
		return ProjectXMLImpl.save_eif_files(self, eif_dict)
###############################################################################