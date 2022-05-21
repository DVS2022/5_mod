import json


class Model(object):
	
	a = 'Какое-то значение 1'
	b = 'Какое-то значение 2'
	c = 'Какое-то значение 3'

	def save(self):
		d = {}
		attr = list(filter(lambda x: not x.startswith('_'), dir(Model)))
		attr.remove('save')
		for i in attr:
			d[i] = eval('self.' + i)
		with open('file.json', 'w') as f:
			json.dump(d, f)
		return print(d)

test = Model()
test.a = '123'
test.b = '456'

test.save()

