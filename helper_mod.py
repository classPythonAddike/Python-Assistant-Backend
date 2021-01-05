import jedi

def get_word(cd, n):
	line = cd[:n].count("\n")

	i = 0
	cnt = 0
	for a in cd:
		cnt += 1
		if a == "\n":
			i += 1
		if i == line:
			break
	return (line + 1, n + 1 - cnt)

def get_code_compl(code, cursor):

	script = jedi.Script(code)
	return [i.complete for i in script.complete(*get_word(code, cursor))]

if __name__ == "__main__":
	with open("app.py", "r") as f:
		g = f.read()
	u = 200
	print(g[u])
	print("------------")
	print(g[u:u + 5])
	print("------------")
	print(g[u - 10:u + 10])
	print("------------")
	print(get_code_compl(g, u))