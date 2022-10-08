import os

def disk_usage(path):
	total=os.path.getsize(path)
	if os.path.isdir(path):
		for file in os.listdir(path):
			childname=os.path.join(path,file)
			total+=disk_usage(childname)
	print ('%d\t%s' % (total,path))
	return total
