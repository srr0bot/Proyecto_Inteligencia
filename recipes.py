import requests

# Definir tu clave de API y la lista de ingredientes
api_key = '08325894061646be8f25b2125df5283a'
categoria = 'dessert'
ingredientes = ['vanilla', 'milk']

# Convertir la lista de ingredientes a una cadena separada por comas
ingredientes_str = ','.join(ingredientes)

# Construir la URL de la solicitud con el parámetro number=1
url = f'https://api.spoonacular.com/recipes/search?apiKey={api_key}&type={categoria}&query={ingredientes_str}&number=3'

# Hacer la solicitud GET para buscar recetas
response_busqueda = requests.get(url)

# Verificar si la solicitud de búsqueda fue exitosa (código de estado 200)
if response_busqueda.status_code == 200:
    # Obtener los datos en formato JSON
    data_busqueda = response_busqueda.json()

    # Iterar sobre los primeros 3 resultados
    for result in data_busqueda['results']:
        # Obtener el ID de la receta
        recipe_id = result['id']

        # Construir la URL de la solicitud para obtener información detallada de la receta
        url_info_receta = f'https://api.spoonacular.com/recipes/{recipe_id}/information?apiKey={api_key}'

        # Hacer la solicitud GET para obtener información detallada de la receta
        response_info_receta = requests.get(url_info_receta)

        # Verificar si la solicitud de información de la receta fue exitosa (código de estado 200)
        if response_info_receta.status_code == 200:
            # Obtener los datos en formato JSON
            data_info_receta = response_info_receta.json()

            # Imprimir detalles de la receta
            print(f"A recipe called: {data_info_receta['title']}")
            print("Made with:")
            for ingrediente in data_info_receta['extendedIngredients']:
                print(f"- {ingrediente['name']}")
            print("="*50 + "\n")  # Separador
        else:
            print(f"Error en la solicitud de información de la receta. Código de estado: {response_info_receta.status_code}")
            print(response_info_receta.text)  # Imprimir el contenido de la respuesta en caso de error
else:
    print(f"Error en la solicitud de búsqueda. Código de estado: {response_busqueda.status_code}")
    print(response_busqueda.text)  # Imprimir el contenido de la respuesta en caso de error
