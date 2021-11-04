#!/usr/bin/python37all
import cgi
data = cgi.FieldStorage()
s1 = data.getvalue('slider1')
s2 = data.getvalue('change')
s3 = data.getvalue('zero')

with open('stepper_control.txt', 'w') as f:  
  f.write(str(s1) + "\t" + str(s2) + "\t" + str(s3))

print('Content-type: text/html\n\n')
print('<html>')
print('<form action="/cgi-bin/stepper_control.py" method="POST">')
print('<input type="range" name="slider1" min="0" max="360" value="%s"><br>' % s1)
print('<input type="submit" name="change" value="Change motor angle">')
print('<input type="submit" name="zero" value="Zero">')
print('</form>')
print('Angle = %s' % s1)
print('</html>')