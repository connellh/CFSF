import glob
content = '<head><meta charset="UTF-8"><link rel="stylesheet" type="text/css" href="main.css"></head>'
def line_prepender(filename):
    with open(filename, 'a+') as f:
        f.write(content)
        f.close()

for file in glob.glob("/home/connell/ArcLogin/CFSF/workouts/*"):
    line_prepender(file)