import re
import datetime
import pygal

regex = r"([0-9]{2})(:{1})([0-9]{2})(:{1})([0-9]{2})(.{1})([0-9]{3})"

def chunks(l, n):
    value=list()
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        value.append(l[i:i + n])
    return value

def changeTime(s):
    hr, min, sec = map(float, s.split(':'))
    return datetime.timedelta(hours=hr, minutes=min, seconds=sec)

def differnceTime(newline):
    starttime = re.search(regex, newline[0]).group(0)
    endtime = re.search(regex, newline[4]).group(0)
    differnce = changeTime(endtime) - changeTime(starttime)
    return newline[0],differnce

file=open("/home/soumya/Documents/sakibthesis/IMS_Custom.log",'r')

instantiating=list()
modify=list()
start=list()
release=list()

for line in file:
    if "Received NFVO Message: Instantiating" in line:
        instantiating.append(line)
    elif "Received NFVO Message: MODIFY" in line:
        modify.append(line)
    elif "Received NFVO Message: START" in line:
        start.append(line)
    else:
        release.append(line)
new_lines_instantiating=chunks(instantiating, 5)
new_lines_modify=chunks(modify, 5)
new_lines_start=chunks(start, 5)

print "length instantiating",len(new_lines_instantiating)
print "length modify",len(new_lines_modify)
print "length start",len(new_lines_start)

instantiating_time=list()
modify_time=list()
start_time=list()
release_time=list()

for newline in new_lines_instantiating:
    line,differnce=differnceTime(newline)
    instantiating_time.append(differnce.total_seconds())

for newline in new_lines_modify:
    line,differnce=differnceTime(newline)
    modify_time.append(differnce.total_seconds())

for newline in new_lines_start:
    line,differnce=differnceTime(newline)
    start_time.append(differnce.total_seconds())

print instantiating_time
print modify_time
print start_time

line_chart = pygal.StackedBar()
line_chart.title = 'Time for different life cycles of OpenIMS deployment'
line_chart.x_title='deployment number -->'
line_chart.y_title='in seconds -->'
line_chart.x_labels = map(str, range(1, 6))
line_chart.add('instantiating', instantiating_time)
line_chart.add('modify',  modify_time)
line_chart.add('start', start_time)
line_chart.render()
line_chart.render_to_png('/home/soumya/Documents/sakibthesis/chart.png')