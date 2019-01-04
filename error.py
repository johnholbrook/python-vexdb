# def foo(p):
# 	if type(p) == type(1):
# 		return p
# 	else:
# 		raise TypeError("Test Error")



# def bar(p):
# 	x = 0
# 	try:
# 		x = foo(p)
# 		# return x
# 	except Exception as e:
# 		print e
# 	return x

# print bar(5)
# # print bar("baz")
# bar("baz")

def foo(a=0, b=1, c=2, d=3):
	return "%s%s%s%s" % (a, b, c, d)

print foo()
print foo(b="Hello, World!")