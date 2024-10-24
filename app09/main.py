import flet as ft


def main(page: ft.Page):
    
    page.window_width=800
    page.window_height_800

    page.bgcolor="Black"
    page.tilte="Mictlan"
    page.fgcolor="gray"


def detener():
    intro.pause()
    Nivel1.pause()
    Nivel2.pause()
    Nivel3.pause()
    Nivel4.pause()
    Nivel5.pause()
    Nivel6.pause()
    Nivel7.pause()
    Nivel8.pause()
    Nivel9.pause()


def playintro():
    detener()
    intro.play()
    
def playnivel1():    
    detener()
    Nivel1.play()
   
def playnivel1():    
    detener()  
    Nivel2.play()

def playnivel1():    
    detener()
    Nivel3.play()
    
def playnivel1():    
    detener()    
    Nivel4.play()
    
def playnivel1():    
    detener()    
    Nivel5.play()
    
def playnivel1():    
    detener()    
    Nivel6.play()
    
def playnivel1():    
    detener()    
    Nivel7.play()

def playnivel1():    
    detener()
    Nivel8.play()
    
def playnivel1():    
    detener()    
    Nivel9.play()

    intro=ft.Audio(src="Intro.mp3",volume=1,balance=0)
    page.overlay.append(intro)

    Nivel1=ft.Audio(src="Primer_Nivel.mp3",volume=1,balance=0)
    page.overlay.append(Nivel1)

    Nivel2=ft.Audio(src="Segundo_Nivel.mp3",volume=1,balance=0)
    page.overlay.append(Nivel2)

    Nivel3=ft.Audio(src="Tercer_Nivel.mp3",volume=1,balance=0)
    page.overlay.append(Nivel3)

    Nivel4=ft.Audio(src="Cuarto_Nivel.mp3",volume=1,balance=0)
    page.overlay.append(Nivel4)

    Nivel5=ft.Audio(src="Quinto_Nivel.mp3",volume=1,balance=0)
    page.overlay.append(Nivel5)

    Nivel6=ft.Audio(src="Sexto_Nivel.mp3",volume=1,balance=0)
    page.overlay.append(Nivel6)

    Nivel7=ft.Audio(src="Septimo_Nivel.mp3",volume=1,balance=0)
    page.overlay.append(Nivel7)

    Nivel8=ft.Audio(src="Octavo_Nivel.mp3",volume=1,balance=0)
    page.overlay.append(Nivel8)

    Nivel9=ft.Audio(src="Noveno_Nivel.mp3",volume=1,balance=0)
    page.overlay.append(Nivel9)



    btnIntro=ft.FilledButton(text="Escucha el intro",disabled=False)

    
    btnNivel1=ft.ElevatedButton(text="Primer Nivel"),
   
    img1=ft.Image(src="Primer-Nivel.jpeg",width=150,height=150)

    btnNivel2=ft.ElevatedButton(text="Segundo Nivel"),
   
    img2=ft.Image(src="Segundo-Nivel.jpeg",width=150,height=150)

    btnNivel3=ft.ElevatedButton(text="Terser Nivel"),
   
    img3=ft.Image(src="Terser-Nivel.png",width=150,height=150)

    btnNivel4=ft.ElevatedButton(text="Cuarto Nivel"),
   
    img4=ft.Image(src="Cuarto-Nivel.jpeg",width=150,height=150)

    btnNivel5=ft.ElevatedButton(text="Quinto Nivel"),
   
    img5=ft.Image(src="Quinto-Nivel.jpeg",width=150,height=150)

    btnNivel6=ft.ElevatedButton(text="Sexto Nivel"),
   
    img6=ft.Image(src="Sexto-Nivel.jpeg",width=150,height=150)

    btnNivel7=ft.ElevatedButton(text="Septimo Nivel"),
   
    img7=ft.Image(src="Septimo-Nivel.jpeg",width=150,height=150)

    btnNivel8=ft.ElevatedButton(text="Octavo Nivel"),

    img8=ft.Image(src="Octavo-Nivel.png",width=150,height=150)
   
    btnNivel9=ft.ElevatedButton(text="Primer Nivel"),
   
    img9=ft.Image(src="Primer-Nivel.jpeg",width=150,height=150)



    page.add(
        ft.Row(
            alignment="start",
            controls=[btnIntro]
        ),
        ft.Column(
            alignment="CENTER",
            spacing=10,
            scroll=ft.ScrollMode.AUTO,
            controls=[
                ft.Row(
                    alignment="CENTER",
                    controls=[
                        ft.Column(
                            alignment="CENTER",
                            spacing=10,
                            controls=[btnNivel1,img1]
                        ),
                        ft.Column(
                            alignment="CENTER",
                            controls=[btnNivel2,img2]
                        ),
                        ft.Column(
                            alignment="CENTER",
                            controls=[btnNivel3,img3]
                    )
                ]
            )
        ]
    )
    ft.Row(
        alignment="CENTER",
        controls=[
            ft.Column(
                alignment="CENTER",
                spacing=10,
                controls=[btnNivel4,img4]
            ),
                ft.Column(
                alignment="CENTER",
                spacing=10,
                controls=[btnNivel5,img5]  
            ),
            ft.Column(
                alignment="CENTER",
                spacing=10,
                controls=[btnNivel6,img6]
            )
        ]
    ),
    ft.Row(
        alignment="CENTER",
        controls=[
            ft.Column(
                alignment="CENTER",
                spacing=10,
                controls=[btnNivel7,img7]
            ),
            ft.Column(
                alignment="CENTER",
                spacing=10,
                controls=[btnNivel8,img8]  
            ),
            ft.Column(
                alignment="CENTER",                   spacing=10
                controls=[btnNivel9,img9]
            )
        ]
    )
)