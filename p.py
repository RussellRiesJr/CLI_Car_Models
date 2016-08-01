

class cars:
	# Method to open 'car-makes.txt'
	def read_makes():
		with open('car-makes.txt', 'r') as makes:
			make_set = {make for make in makes}
		return make_set

	# Method to open 'car-models.txt'
	def read_models():
		with open('car-models.txt', 'r') as models:
			model_set = {model for model in models}
		return model_set

	# Creating empty dictionary
	make_mod = {}

	makes = read_makes()
	models = read_models()

	for make in makes:
		make_mod[make[:-1]] = None
		# print("Make:", make)
		for model in models:
			# print("Model:", models)
			# print("make = {0}, model = {1}".format(make, model))
			if make[0] == model[0]:
				# print(model)
				new_model = model[:-1]
				make_mod[make[:-1]] = new_model[2:]
	print(make_mod)
			

