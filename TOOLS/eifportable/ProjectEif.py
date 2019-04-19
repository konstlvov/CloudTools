# -*- coding: utf-8 -*-

import os, os.path
import shutil
import fnmatch
from ProjectXML import ProjectXML
from ProjectFile import ProjectFile
from PathResolver import PathResolver
###############################################################################
class ProjectEif:

	def __init__(self, file_name):
		"В file_name указываем путь к любому файлу внутри проекта"
		path_r   = PathResolver(file_name)
		peif     = path_r.GetBankEifDir()
		putils   = path_r.GetUtilsDir()
		puser    = path_r.GetUserDir()

		self.path_to_bank_eif = peif
		self.path_to_tmp_eif  = os.path.join(putils, "LoadEif")		
		self.path_to_user     = puser

	def get_all_eif(self, dir_path):
		ief_dict = {}
		for root, dirs, filenames in os.walk(dir_path):
			for filename in fnmatch.filter(filenames, '*.eif'):
				full_path  = os.path.join(root, filename).decode('cp1251')
				eif = ProjectFile(full_path)
				data = eif.get_data()
				eif.update_md5(data)
				ief_dict[eif.get_name()] = eif
		return ief_dict

	def get_xml_data(self):
		return ProjectXML(self.path_to_user).get_eif_files()

	def commit(self):
		ief_dict = self.get_all_eif(self.path_to_bank_eif)
		xml_dict = self.get_xml_data()
		for name in ief_dict:
			eif = ief_dict[name]			
			if xml_dict.get(name):
				xml_dict[name]["eif_md5"] = eif.get_md5()
			else:
				xml_dict[name] = {"eif_md5" : eif.get_md5()}
		ProjectXML(self.path_to_user).save_eif_files(xml_dict)

	def update(self):
		ief_dict = self.get_all_eif(self.path_to_bank_eif)
		xml_dict = self.get_xml_data()
		for name in ief_dict:
			eif = ief_dict[name]
			is_copy = True
			if xml_dict.get(name):
				if eif.get_md5() == xml_dict[name]["eif_md5"]:
					is_copy = False
			if is_copy:
				src = eif.get_path()
				dst = os.path.join(self.path_to_tmp_eif, os.path.basename(src))
				shutil.copyfile(src, dst)
###############################################################################