from googletrans import Translator



# Instanciando o objeto Translator
translator = Translator()

# Texto para traduzir
texto = "Hello, how are you?"

# Traduzindo para Hebraico
traducao_hebraico = translator.translate(texto, src='en', dest='he').text
print(f'Tradução para Hebraico: {traducao_hebraico}')

# Traduzindo para Chinês Tradicional
traducao_chines_tradicional = translator.translate(texto, src='en', dest='zh-tw').text
print(f'Tradução para Chinês Tradicional: {traducao_chines_tradicional}')