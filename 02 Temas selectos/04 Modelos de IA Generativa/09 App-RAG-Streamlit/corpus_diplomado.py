"""Base de conocimiento del Módulo V del Diplomado de Ciencia de Datos.

Cada entrada es un fragmento corto y autocontenido: es la unidad que el
recuperador devuelve y que el modelo de lenguaje recibe como contexto.

Para agregar contenido propio basta con añadir diccionarios a esta lista; no hay
que tocar ninguna otra parte del código.
"""

CORPUS = [
    {"sesion": 1, "titulo": "Esperanza condicional",
     "texto": "La esperanza condicional E[Y|X] es el valor promedio de Y dado que conocemos X. "
              "Es el objeto que en el fondo estiman casi todos los modelos del módulo: la regresión "
              "lineal la aproxima con una función lineal de X, y los modelos de respuesta binaria "
              "con una función no lineal acotada entre cero y uno."},

    {"sesion": 1, "titulo": "DAG, confusores y colisionadores",
     "texto": "Un grafo acíclico dirigido, o DAG, representa los supuestos causales de un problema "
              "mediante flechas entre variables. Sirve para decidir por qué variables hay que "
              "controlar. Un confusor abre una ruta trasera que sesga el efecto estimado y hay que "
              "controlarlo; en cambio, controlar por un colisionador introduce sesgo de selección "
              "donde antes no había, así que hay que dejarlo fuera."},

    {"sesion": 2, "titulo": "Mínimos cuadrados ordinarios",
     "texto": "El estimador de mínimos cuadrados ordinarios, MCO, elige los coeficientes que "
              "minimizan la suma de los residuos al cuadrado. Bajo los supuestos clásicos es "
              "insesgado y tiene la varianza mínima entre los estimadores lineales insesgados."},

    {"sesion": 2, "titulo": "Bondad de ajuste y R cuadrada",
     "texto": "El coeficiente de determinación R cuadrada mide la proporción de la varianza de la "
              "variable dependiente que el modelo explica. Nunca baja al agregar variables, así que "
              "dentro de muestra no sirve para comparar modelos con distinto número de regresores: "
              "para eso hay que mirar el desempeño fuera de muestra."},

    {"sesion": 2, "titulo": "Sobreajuste y separación de la muestra",
     "texto": "Separar los datos en un conjunto de entrenamiento y uno de prueba permite estimar el "
              "error fuera de muestra. Un modelo puede memorizar el ruido del entrenamiento y lucir "
              "excelente ahí, pero fallar con datos nuevos: eso es sobreajuste, y solo se detecta "
              "evaluando en datos que el modelo no vio al ajustarse."},

    {"sesion": 2, "titulo": "Regresión Ridge",
     "texto": "La regresión Ridge agrega a la función objetivo una penalización proporcional a la "
              "suma de los coeficientes al cuadrado. Encoge los coeficientes hacia cero y reduce la "
              "varianza del estimador cuando hay colinealidad entre los regresores, pero nunca los "
              "deja exactamente en cero, así que conserva todas las variables."},

    {"sesion": 2, "titulo": "Regresión Lasso y selección de variables",
     "texto": "La regresión Lasso agrega una penalización proporcional a la suma de los valores "
              "absolutos de los coeficientes. A diferencia de Ridge, sí puede dejar coeficientes "
              "exactamente en cero, por lo que descarta variables y hace selección automática de "
              "predictores. Es el método a usar cuando se quiere un modelo más simple e "
              "interpretable a partir de muchas variables candidatas."},

    {"sesion": 3, "titulo": "Análisis de componentes principales",
     "texto": "El análisis de componentes principales, PCA, encuentra ejes ortogonales nuevos que "
              "capturan la mayor varianza posible de los datos. Se usa para reducir el número de "
              "dimensiones y para poder graficar en un plano de dos ejes conjuntos de datos con "
              "muchas columnas. Es una técnica no supervisada: no usa la variable a predecir."},

    {"sesion": 3, "titulo": "K-medias",
     "texto": "El algoritmo de K-medias parte las observaciones en k grupos minimizando la distancia "
              "entre cada observación y el centroide del grupo al que fue asignada. Es un método no "
              "supervisado: agrupa clientes, municipios u observaciones parecidas sin necesidad de "
              "ninguna etiqueta previa."},

    {"sesion": 4, "titulo": "Coeficiente de silueta y número de grupos",
     "texto": "El coeficiente de silueta compara qué tan cerca está una observación de su propio "
              "grupo frente al grupo vecino más cercano. Es el criterio que se usa para elegir "
              "cuántos grupos conviene formar: se prueban varios valores de k y se toma el que da "
              "mejor silueta. Se degrada en espacios de muchas dimensiones, así que sirve más para "
              "comparar alternativas que como calificación absoluta."},

    {"sesion": 4, "titulo": "Agrupamiento jerárquico",
     "texto": "El agrupamiento jerárquico construye un árbol de grupos, ya sea uniendo las "
              "observaciones más parecidas o dividiendo el conjunto completo. A diferencia de "
              "K-medias no exige fijar de antemano el número de grupos, que se decide después "
              "cortando el árbol a cierta altura."},

    {"sesion": 4, "titulo": "Deformación dinámica del tiempo (DTW)",
     "texto": "La deformación dinámica del tiempo, o DTW, compara dos series de tiempo permitiendo "
              "estirarlas o desplazarlas temporalmente, algo que la distancia euclidiana no puede "
              "hacer: dos series con la misma forma pero desfasadas se ven muy distintas para la "
              "distancia euclidiana y muy parecidas para DTW. Su costo crece con el cuadrado de la "
              "longitud de la serie, por lo que conviene reducir la frecuencia de los datos."},

    {"sesion": 5, "titulo": "Modelo logit",
     "texto": "El modelo logit supone que la probabilidad de un resultado binario sigue una función "
              "logística de un índice lineal de las covariables. Se estima por máxima verosimilitud. "
              "Sus coeficientes no se interpretan directamente como efectos marginales: hay que "
              "calcular el efecto marginal o razones de momios."},

    {"sesion": 6, "titulo": "Logit ordinal",
     "texto": "El logit ordinal se usa cuando la variable dependiente tiene categorías con un orden "
              "natural: una calificación del uno al cinco, un nivel de satisfacción, una escala de "
              "acuerdo o desacuerdo. Supone odds proporcionales, es decir, que el efecto de cada "
              "variable es el mismo entre cualquier par de categorías adyacentes."},

    {"sesion": 6, "titulo": "Matriz de confusión",
     "texto": "La matriz de confusión cruza las clases predichas contra las clases verdaderas. De "
              "ella se calculan la precisión, la sensibilidad y la exactitud, y permite ver si el "
              "modelo se equivoca más en una clase que en otra, algo que una sola cifra de exactitud "
              "esconde cuando las clases están desbalanceadas."},

    {"sesion": 7, "titulo": "Expresiones regulares y tokenización",
     "texto": "Las expresiones regulares son patrones para buscar y extraer texto. Son el primer "
              "paso del análisis de texto: sirven para limpiar, extraer campos y separar el texto en "
              "unidades (tokenizar) antes de aplicar cualquier modelo."},

    {"sesion": 7, "titulo": "Modelos de lenguaje de n-gramas",
     "texto": "Un modelo de lenguaje de n-gramas estima la probabilidad de una palabra dadas las n "
              "menos una palabras anteriores. Su limitación de fondo es que solo ve una ventana "
              "corta: no puede relacionar palabras separadas por mucha distancia dentro del texto, "
              "que es justo el problema que resolvió la arquitectura Transformer."},

    {"sesion": 8, "titulo": "Clasificador de Bayes ingenuo",
     "texto": "El clasificador de Bayes ingenuo aplica el teorema de Bayes suponiendo que los "
              "atributos son condicionalmente independientes dada la clase. Ese supuesto casi nunca "
              "se cumple en texto real, y aun así el método funciona sorprendentemente bien para "
              "clasificar documentos y detectar spam."},

    {"sesion": 9, "titulo": "Árboles de decisión y bosques aleatorios",
     "texto": "Un bosque aleatorio ajusta muchos árboles de decisión sobre muestras bootstrap y "
              "promedia sus predicciones. En cada partición considera solo un subconjunto aleatorio "
              "de predictores, y ese muestreo de variables decorrelaciona los árboles entre sí, que "
              "es lo que hace bajar la varianza frente a un solo árbol."},

    {"sesion": 9, "titulo": "Redes neuronales",
     "texto": "Una red neuronal encadena capas de transformaciones lineales seguidas de funciones de "
              "activación no lineales, como ReLU. La capa de salida usa softmax cuando el problema "
              "es de clasificación multiclase. Las capas ocultas aprenden representaciones "
              "intermedias de la entrada que sirven como embeddings."},

    {"sesion": 10, "titulo": "Qué es un word embedding",
     "texto": "Un word embedding convierte un texto en un vector denso de números reales, de modo "
              "que textos con significado parecido queden cerca entre sí. A diferencia de la bolsa "
              "de palabras, reconoce que dos palabras distintas pueden significar lo mismo, aunque "
              "no comparta ninguna letra con la otra."},

    {"sesion": 10, "titulo": "Similitud coseno",
     "texto": "La similitud coseno mide la diferencia de dirección entre dos vectores, ignorando su "
              "magnitud. Es la métrica más usada para comparar embeddings de oraciones. Cuando los "
              "vectores están normalizados coincide exactamente con el producto punto, y por eso las "
              "bases de datos vectoriales normalizan al guardar."},

    {"sesion": 10, "titulo": "Embeddings de token frente a embeddings de oración",
     "texto": "BERT produce un vector por cada token y ese vector depende del contexto, por lo que "
              "una misma palabra escrita igual, como banco, recibe representaciones distintas según "
              "el sentido en que se use. Los modelos tipo SBERT producen en cambio un solo vector "
              "por oración completa, entrenado para que la distancia entre dos oraciones refleje qué "
              "tan parecidas son en significado."},

    {"sesion": 10, "titulo": "Arquitectura Transformer y atención",
     "texto": "La arquitectura Transformer calcula pesos de atención entre todos los pares de tokens "
              "de la secuencia, lo que le permite relacionar palabras distantes entre sí. Es la base "
              "de los modelos de lenguaje grandes actuales y lo que superó la limitación de ventana "
              "corta de los modelos de n-gramas."},

    {"sesion": 10, "titulo": "Generación aumentada con recuperación (RAG)",
     "texto": "La generación aumentada con recuperación, o RAG, recupera de una base propia los "
              "documentos relevantes para una pregunta y se los entrega al modelo de lenguaje como "
              "contexto, en lugar de esperar que el modelo lo recuerde todo de su entrenamiento. "
              "Sirve para que el modelo no invente datos, para citar la fuente de cada afirmación y "
              "para usar información privada o más reciente que el modelo."},

    {"sesion": 10, "titulo": "Prompt de sistema",
     "texto": "El prompt de sistema son las instrucciones que fijan el comportamiento del modelo "
              "antes de que el usuario escriba nada: qué papel tomar, en qué idioma responder, qué "
              "tono usar y qué límites respetar. En un sistema RAG es donde se le ordena responder "
              "únicamente con el contexto recuperado, citar el fragmento y admitir cuando no tiene "
              "la información."},

    {"sesion": 10, "titulo": "Agentes y uso de herramientas",
     "texto": "Un agente es un modelo de lenguaje al que se le dan herramientas y que decide por sí "
              "mismo cuándo usarlas, siguiendo un ciclo de pensar, actuar y observar. Darle "
              "herramientas amplía lo que puede hacer, pero agrega latencia, dependencia de "
              "servicios externos, variabilidad en las respuestas y riesgos de seguridad."},

    {"sesion": 10, "titulo": "Parámetros de un modelo de lenguaje",
     "texto": "La temperatura controla qué tan variadas son las respuestas: con temperatura cero el "
              "modelo es casi determinista y con valores altos se vuelve más creativo y menos "
              "predecible. La ventana de contexto es el número máximo de tokens que el modelo puede "
              "leer de una vez, y es la razón por la que en RAG se recuperan solo unos pocos "
              "fragmentos en lugar de mandar el corpus completo."},

    {"sesion": 0, "titulo": "Evaluación del módulo",
     "texto": "La evaluación del Módulo V se reparte en partes iguales entre la Tarea 01, de "
              "regresión lineal y agrupamiento, y la Tarea 02, de análisis de texto. Cada una vale "
              "el cincuenta por ciento de la calificación del módulo. El Reporte Final pertenece al "
              "Módulo VI y se evalúa por separado."},
]
