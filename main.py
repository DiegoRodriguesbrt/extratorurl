url = "https://bytebank.com/cambio?moedaDestino=dolar&quantidade=100&moedaOrigem=real"

#Sanitização da URL
url = url.strip()


#Validação da URL
if url == "":
    raise ValueError("A URL está vazia")

indice_interrogacao= url.find("?")
url_base = url[:indice_interrogacao]

#Separa base e os parametros
url_parametros = url[indice_interrogacao+1:]
print(url_parametros)

#Busca valor de um parametro
parametro_busca = "moedaOrigem"
indice_parametro = url_parametros.find(parametro_busca)
indice_valor = indice_parametro + len(parametro_busca) + 1
indice_e_comercial = url_parametros.find("&", indice_valor)

if indice_e_comercial == -1:

    valor = url_parametros [indice_valor:]
else:
    valor = url_parametros [indice_valor:indice_e_comercial]

print(valor)
