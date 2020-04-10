from string import Template

t = Template('${nama} adalah seorang $profesi.')
print (t.substitute(nama='Judith', profesi='Programmer'))