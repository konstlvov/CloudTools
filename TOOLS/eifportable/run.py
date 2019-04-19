# -*- coding: utf-8 -*-

import sys
import ProjectEif

if sys.argv[1] == 'commit':
	ProjectEif.ProjectEif(sys.argv[2]).commit()
else:
	ProjectEif.ProjectEif(sys.argv[2]).update()