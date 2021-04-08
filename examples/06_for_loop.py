blog_posts = ["Os 10 livros acadêmicos mais influentes de todos os tempos", "Sonda da Nasa envia foto de dunas de areia contendo água congelada em Marte", "Em testes, droga contra câncer diminui efeitos de proteínas do Sars-CoV-2"]

for post in blog_posts:
    if post == "":
        continue
    else:
        print(post)

print ("---------------------")

myString = "This is a string"

for char in myString:
    print(char)

print ("---------------------")

for x in range(0,10):
    print(x)

print ("---------------------")

person = {'Name':'Livia', 'Age':25, 'Gender':'Female'}

for key in person:
    print(key, ':', person[key])

print ("---------------------")

exemplo = {"Categoria 1": [1, 2, 3], "Categoria 2":[1, 2, 3]}

for categoria in exemplo:
    print(categoria)
    for key in exemplo[categoria]:
        print(key)


