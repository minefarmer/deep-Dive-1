
import sys
import importer

module1 = importer.import_('module1', 'module1_source.py', '.')

print('ys says:', sys.modules.get('module1'))
