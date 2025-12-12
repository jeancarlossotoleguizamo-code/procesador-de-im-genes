#comienzo proyecto
#Librerias
import pygame
import sys
import os
import numpy as np

pygame.init()

# ------------------ VENTANA ------------------
ANCHO, ALTO = 900, 650
VENTANA = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Procesador de Imágenes")

# ------------------ COLORES ------------------
FONDO = (220, 190, 255)     # LILA SUAVE
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
MORADO_BOTON = (170, 0, 200)
MORADO_PRESIONADO = (140, 0, 160)
BORDE_BOTON = (255, 255, 255)

# ------------------ SONIDO ------------------
if not os.path.exists("click.wav"):
    print("⚠ ERROR: No se encontró click.wav")
    sys.exit()
CLICK = pygame.mixer.Sound("click.wav")

# ------------------ CARGA DE IMAGEN ------------------
if os.path.exists("extrat.jpg"):
    imagen_original = pygame.image.load("extrat.jpg").convert_alpha()
    # ajustar tamaño si es muy grande (opcional)
    imagen_original = pygame.transform.smoothscale(imagen_original, (400, 400))
    imagen_actual = imagen_original.copy()
else:
    print("⚠ ERROR: No se encontró el archivo extrat.jpg")
    sys.exit()

# ------------------ FUNCIONES ------------------
def rotar_90():
    global imagen_actual
    imagen_actual = pygame.transform.rotate(imagen_actual, -90)

def rotar_180():
    global imagen_actual
    imagen_actual = pygame.transform.rotate(imagen_actual, 180)

def rotar_270():
    global imagen_actual
    imagen_actual = pygame.transform.rotate(imagen_actual, 90)

def escala_grises():
    global imagen_actual
    # reproducir sonido
    CLICK.play()
    # Obtener array (width x height x 3)
    arr = pygame.surfarray.array3d(imagen_actual).astype(float)
    # promedio por canal -> escala de grises
    gris = arr.mean(axis=2)
    # reconstruir array 3 canales
    arr2 = np.zeros_like(arr)
    arr2[:, :, 0] = gris
    arr2[:, :, 1] = gris
    arr2[:, :, 2] = gris
    # convertir a uint8 y crear surface (pygame usa arrays con shape (w,h,3))
    arr2 = arr2.astype('uint8')
    imagen_actual = pygame.surfarray.make_surface(arr2)

def reiniciar():
    global imagen_actual
    CLICK.play()
    imagen_actual = imagen_original.copy()

# ------------------ BOTONES (definición) ------------------
# posiciones centradas / ajustadas
btn_90    = pygame.Rect(50, 520, 120, 50)
btn_180   = pygame.Rect(190, 520, 120, 50)
btn_270   = pygame.Rect(330, 520, 120, 50)
btn_gris  = pygame.Rect(470, 520, 150, 50)
btn_reset = pygame.Rect(640, 520, 150, 50)

# flags para efecto presionado
pres90 = pres180 = pres270 = presgris = presreset = False

# fuente
fuente = pygame.font.SysFont("Arial", 24, bold=True)

# función para dibujar botón ovalado con borde y texto
def boton(superficie, rect, texto, presionado):
    color = MORADO_PRESIONADO if presionado else MORADO_BOTON
    # dibuja el óvalo relleno
    pygame.draw.ellipse(superficie, color, rect)
    # borde (segunda elipse con width)
    pygame.draw.ellipse(superficie, BORDE_BOTON, rect, 3)
    # texto centrado
    text_surf = fuente.render(texto, True, BLANCO)
    tx = rect.x + rect.width // 2 - text_surf.get_width() // 2
    ty = rect.y + rect.height // 2 - text_surf.get_height() // 2
    superficie.blit(text_surf, (tx, ty))

# ------------------ LOOP PRINCIPAL ------------------
clock = pygame.time.Clock()
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if evento.type == pygame.MOUSEBUTTONDOWN:
            if btn_90.collidepoint(evento.pos):
                CLICK.play(); pres90 = True; rotar_90()
            if btn_180.collidepoint(evento.pos):
                CLICK.play(); pres180 = True; rotar_180()
            if btn_270.collidepoint(evento.pos):
                CLICK.play(); pres270 = True; rotar_270()
            if btn_gris.collidepoint(evento.pos):
                presgris = True; escala_grises()
            if btn_reset.collidepoint(evento.pos):
                CLICK.play(); presreset = True; reiniciar()

        if evento.type == pygame.MOUSEBUTTONUP:
            pres90 = pres180 = pres270 = presgris = presreset = False

    # dibujar fondo
    VENTANA.fill(FONDO)

    # dibujar imagen (centrada horizontalmente, un poco arriba)
    img_rect = imagen_actual.get_rect(center=(ANCHO // 2, ALTO // 2 - 40))
    VENTANA.blit(imagen_actual, img_rect)

    # dibujar botones (con borde)
    boton(VENTANA, btn_90, "90°", pres90)
    boton(VENTANA, btn_180, "180°", pres180)
    boton(VENTANA, btn_270, "270°", pres270)
    boton(VENTANA, btn_gris, "Grises", presgris)
    boton(VENTANA, btn_reset, "Reiniciar", presreset)

    pygame.display.update()
    clock.tick(60)
