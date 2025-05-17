import requests

def capturar_ultimos_resultados(qtd=10):
    url = "https://loteriascaixa-api.lucasmedeiros.dev/api/lotofacil/"
    concursos = []

    try:
        for i in range(qtd):
            resp = requests.get(url + str(-i))
            if resp.status_code == 200:
                data = resp.json()
                numero = data.get("concurso")
                dezenas = [int(d) for d in data.get("dezenas")]
                concursos.append((numero, dezenas))
    except Exception as e:
        print("Erro ao acessar nova API:", e)

    return concursos
