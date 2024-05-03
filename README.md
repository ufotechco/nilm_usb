# NILM: Clasificador de Imágenes Utilizando Redes Neuronales Convolucionales

Este proyecto consiste en una clase de Python llamada NILM (Neural Network Image Classifier) diseñada para realizar clasificaciones sobre imágenes utilizando un modelo de red neuronal convolucional pre-entrenado. El propósito principal de esta clase es predecir y clasificar imágenes en una de las cuatro clases distintas.

## Uso

Para utilizar la clase NILM, sigue estos pasos:

1. **Instalación:** Para la instalación de esta librería utiliza el comando `pip`:
   `pip install nilm-usb`

2. **Importa la clase NILM:** En tu script de Python, importa la clase NILM desde el archivo que contiene su definición.

   `from nilm_usb.NILM import NILM`

3. **Inicializa la clase NILM:** Carga el modelo de red neuronal convolucional pre-entrenado proporcionando la ruta al archivo del modelo como argumento.

    `classifier = NILM("ruta/al/modelo.h5")`

4. **Realiza predicciones:** Utiliza el método predict() para realizar predicciones sobre imágenes. Este método toma la ruta de la imagen como argumento y devuelve la clase predicha y la probabilidad asociada.

    `clase_predicha, probabilidad = classifier.predict("ruta/a/la/imagen.jpg")`
    `print("Clase predicha:", clase_predicha)`
    `print("Probabilidad:", probabilidad)`

**Clases para clasificación**
    
El modelo de red neuronal convolucional pre-entrenado está configurado para clasificar las imágenes en las siguientes cuatro clases:

* DISH
* FRIDGE
* HTPC
* KETTLE
* WASHER

**Atributos y Métodos**

La clase NILM tiene los siguientes atributos y métodos:

* **model**: El modelo de red neuronal cargado.
* **actual_classes**: Lista de las clases actuales utilizadas para la predicción.

**Métodos:**


| **Método** | **Descripción**                        | **Uso**             |
|------------|----------------------------------------|---------------------|
| predict    | Realiza la predicción sobre la imagen en la ruta especificada y devuelve la clase predicha y la probabilidad asociada. | `predict(image_path)` |


**Licencia:**

Este proyecto está bajo la licencia MIT.
