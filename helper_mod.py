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
	
	try: code_compl = [[i.complete, i.name_with_symbols] for i in script.complete(*get_word(code, cursor))]
	except: code_compl = [1]
	try: errors = [(i._parso_error.start_pos, i._parso_error.end_pos) for i in script.get_syntax_errors()]
	except: errors = []
	try: description = script.get_context(*get_word(code, cursor)).description
	except: description = []
	try: refs = [(i.line, i.column) for i in script.get_references(*get_word(code, cursor), scope = 'file')]
	except: refs = []

	ret = {
		"Code Compl": code_compl,
		"Errors": errors,
		"Description": description,
		"Word References": refs
	}

	return ret