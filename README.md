# Procesador de Imágenes  
Proyecto Final de Álgebra.
Repositorio oficial: **procesador-de-im-genes**

Este proyecto es un procesador de imágenes interactivo desarrollado en **Python con Pygame**.  
Permite manipular una imagen aplicando rotaciones, escala de grises, reinicio y efectos visuales.  
Incluye además animaciones, botones ovalados, sonido al presionar y una interfaz amigable.

---

## Objetivo del Proyecto
Implementar un programa capaz de:
- Cargar una imagen automáticamente.
- Rotarla en 90°, 180° y 270°.
- Convertirla a escala de grises.
- Restablecer la imagen original.
- Operar con botones interactivos diseñados gráficamente.
- Aplicar sonido al presionar cada botón.
- Utilizar conceptos matemáticos (matrices, promedios, coordenadas, centrado).

---

## Autores
Proyecto desarrollado por:
- **Allison Cano Hidalgo** – Sistema de botones, animación, interacción gráfica y posicionamiento.  
- **Jean Carlos Soto Leguizamo** – Diseño visual general, esquema de interfaz.  
- **Leidy Lucero Pantoja** – Lógica de rotación, manejo de matrices e imagen original.

---

## Lógica Matemática del Proyecto

### 1. Centración del texto en los botones
Para ubicar el texto exactamente en el centro del botón se usa la expresión algebraica:

\[
X_{texto} = X + \frac{ancho\_botón}{2} - \frac{ancho\_texto}{2}
\]

Y lo mismo para Y (centro vertical):

\[
Y_{texto} = Y + \frac{alto\_botón}{2} - \frac{alto\_texto}{2}
\]

Esto garantiza que el texto quede en el punto medio exacto.

---

###  2. Imagen representada como matriz tridimensional
Toda imagen se representa así:

\[
Imagen(x, y, c) = \begin{bmatrix} R \\ G \\ B \end{bmatrix}
\]

Es decir, una matriz **3D de píxeles** donde c = canal de color.

---

###  3. Escala de grises
Para convertir cada píxel a blanco y negro se aplica:

\[
Gris = \frac{R + G + B}{3}
\]

Ese promedio reemplaza cada canal, logrando una imagen monocromática.

---

##  Tecnologías utilizadas
- **Python 3**
- **Pygame** (interfaz, sonido, gráficos)
- **Numpy** (manipulación de matrices)

Archivos externos incluidos en el proyecto:
- `extrat.jpg`
- `click.wav`

---

##  Instalación de dependencias

Ejecutar en la terminal:

```bash
pip install pygame
pip install numpy
```
---

## Ejecución del Programa

1. Clonar el repositorio
https://github.com/jeancarlossotoleguizamo-code/procesador-de-im-genes.git

2. Acceder a la carpeta del proyecto
cd procesador-de-im-genes

3. Instalar las dependencias necesarias
pip install pygame
pip install numpy

4. Ejecutar el programa principal
python procesador-de-im-genes.py


5. Verificar que los siguientes archivos estén en la misma carpeta
- procesador-de-im-genes.py  
- extrat.jpg  
- click.wav  

Con estos pasos, el programa iniciará correctamente y mostrará la interfaz interactiva del procesador de imágenes.



