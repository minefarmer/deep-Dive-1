# 3b - module1_source.py

module1 = importer.import_('module_source.py', '.')

print('sys says:', sys.modules.get('module1', ''))
