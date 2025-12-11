#comienzo proyecto
#Librerias
import pygame
import sys
import os
import numpy as np

pygame.init()

#-------------Ventana----------------------------------------------
ANCHO, ALTO = 900, 650
VENTANA = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Procesador de Imágenes")

# ------------------ COLORES --------------------------------------
FONDO = (220, 190, 255)     # LILA SUAVE
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
MORADO_BOTON = (170, 0, 200)
MORADO_PRESIONADO = (140, 0, 160)
BORDE_BOTON = (255, 255, 255)

# ------------------ SONIDO ----------------------------------
if not os.path.exists("click.wav"):
    print("⚠ ERROR: No se encontró click.wav")
    sys.exit()
CLICK = pygame.mixer.Sound("click.wav")
# ------------------Fuente------------------------------------
fuente = pygame.font.SysFont("Arial", 24, bold=True)



# BOTONES, INTERFAZ Y EVENTOS --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Rectángulos de botones
btn_90    = pygame.Rect(50, 520, 120, 50)
btn_180   = pygame.Rect(190, 520, 120, 50)
btn_270   = pygame.Rect(330, 520, 120, 50)
btn_gris  = pygame.Rect(470, 520, 150, 50)
btn_reset = pygame.Rect(640, 520, 150, 50)

# Estados para animación
pres90 = pres180 = pres270 = presgris = presreset = False

# Dibujar botón (ovalado + borde + texto)
def boton(superficie, rect, texto, presionado):
    color = MORADO_PRESIONADO if presionado else MORADO_BOTON
    pygame.draw.ellipse(superficie, color, rect)
    pygame.draw.ellipse(superficie, BORDE, rect, 3)

    texto_surf = fuente.render(texto, True, BLANCO)
    superficie.blit(
        texto_surf,
        (
            rect.x + rect.width // 2 - texto_surf.get_width() // 2,
            rect.y + rect.height // 2 - texto_surf.get_height() // 2
        )
    )

if os.path.exists("extrat.jpg"):
    imagen_original = pygame.image.load("extrat.jpg").convert_alpha()
    imagen_original = pygame.transform.smoothscale(imagen_original, (400, 400))
    imagen_actual = imagen_original.copy()
else:
    print("⚠ ERROR: No se encontró extrat.jpg")
    sys.exit()



# LOOP PRINCIPAL ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
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
                CLICK.play(); presgris = True; escala_grises()
            if btn_reset.collidepoint(evento.pos):
                CLICK.play(); presreset = True; reiniciar()

        if evento.type == pygame.MOUSEBUTTONUP:
            pres90 = pres180 = pres270 = presgris = presreset = False

    VENTANA.fill(FONDO)
