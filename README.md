# Elige tu Propia Aventura 🎮

¡Bienvenido a "Elige tu Propia Aventura"! Un juego de texto interactivo donde tus decisiones moldean el destino de tu personaje en un mundo lleno de monstruos y tesoros escondidos.
## Características 🌟 
- **Narrativa Inmersiva** : Sumérgete en un mundo de fantasía donde cada elección cuenta. 
- **Sistema de Progresión** : Gana experiencia y aumenta tus habilidades enfrentándote a desafíos. 
- **Elemento de Azar** : Encuentra pociones y otros ítems de forma aleatoria después de enfrentarte a monstruos. 
- **Interfaz Colorida** : Gracias al uso de `consolemenu` y `ansicolors`, disfruta de una experiencia visualmente atractiva.
## Instalación 🚀
1. Clona este repositorio:

```bash

git clone https://github.com/BlueberryMalaga/aventura.git
```


2. Instala las dependencias necesarias:

```bash

pip install console-menu
pip install ansicolors
```


3. Ejecuta el archivo principal para comenzar tu aventura:

```bash

python main.py
```


4. ¡Haz tus elecciones y ve a dónde te llevan!


## Formateo del Código 📏

Para asegurar la consistencia y legibilidad del código, será obligatorio formatear cualquier contribución usando [black](https://black.readthedocs.io/) :

```bash

pip install black
black main.py
```

## Contribuciones 🤝

¡Las contribuciones son bienvenidas! Si tienes ideas para mejorar el juego, añadir más narrativa o solucionar errores, no dudes en hacer un fork y enviar un pull request.
## Licencia ⚖️

Este proyecto está licenciado bajo MIT. Consulta el archivo `LICENSE` para más detalles.

# Guía de Contribución para Principiantes en "Elige tu Propia Aventura" 📘

Si eres nuevo en Git, programación o ambos, ¡no te preocupes! Esta guía te llevará paso a paso a través del proceso de contribución a este proyecto.
## Instalación de Git en Windows 10 🛠️ 
1. **Descarga el Instalador** : Ve al sitio web oficial de Git [git-scm.com](https://git-scm.com/) y descarga la versión para su sistema operativo. 
2. **Ejecuta el Instalador** : Una vez descargado, abre el archivo `.exe` para comenzar la instalación. 
3. **Sigue las Instrucciones** : Durante la instalación, puedes mantener la mayoría de las opciones predeterminadas. Sin embargo, cuando llegues a la pantalla que te pregunta qué editor de texto prefieres, si no estás familiarizado con Vim, te sugiero que elijas un editor diferente, como Nano o, si tienes otro preferido, selecciónalo. 
4. **Finaliza la Instalación** : Haz clic en "Finish" una vez que la instalación esté completa.

Para comprobar que Git se ha instalado correctamente, abre la terminal (puedes buscar "cmd" en la barra de búsqueda de Windows) y escribe:

```bash

git --version
```

Deberías ver la versión de Git que acabas de instalar.
## Contribuir al Proyecto: Pasos Detallados 🚀 
1. **Fork del Repositorio** : Ve al repositorio principal en GitHub y haz clic en el botón "Fork" en la esquina superior derecha. Esto creará una copia del repositorio en tu cuenta de GitHub. 
2. **Clonar el Repositorio** : Ahora, clona el fork que acabas de hacer a tu máquina local. Abre la terminal y escribe:

```bash

git clone https://github.com/<TU_NOMBRE_DE_USUARIO>/nombre-del-repositorio.git
```

3. **Configurar el Upstream** : Esto te permitirá sincronizar los cambios del repositorio original.

```bash

cd nombre-del-repositorio
git remote add upstream https://github.com/nombre-del-autor-original/nombre-del-repositorio.git
```

4. **Crear una Nueva Rama** : Antes de hacer cambios, crea una nueva rama:

```bash

git checkout -b nombre-de-tu-rama
```

 
5. **Haz tus Cambios** : Ahora puedes empezar a hacer cambios en el código o añadir contenido. Asegúrate de probar cualquier cambio para asegurarte de que no introduces errores. 
6. **Commit y Push** :

```bash

git add .
git commit -m "Descripción breve de tus cambios"
git push origin nombre-de-tu-rama
```

 
7. **Pull Request** : Ve a la página de tu fork en GitHub. Haz clic en "Pull Requests" y luego en "New Pull Request". Asegúrate de seleccionar tu rama en el desplegable y revisa tus cambios. Si todo se ve bien, haz clic en "Create Pull Request". 
8. **Espera la Revisión** : Los mantenedores del proyecto revisarán tu Pull Request y, si todo está bien, lo fusionarán en el proyecto. ¡Felicidades! Has contribuido al proyecto.

Espero que esta guía te ayude a entender el proceso de contribución y te anime a hacer tu primera contribución. ¡Buena suerte!

