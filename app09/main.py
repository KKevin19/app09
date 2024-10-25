import flet as ft


def main(page: ft.Page):
#establecer tamaño de pantalla

    page.window_width=800
    page.window_height=800
    
    page.bgcolor="pink"
    page.title="mitlan"
    page.fgcolor="red"
    
    
    #funcion para detener audio
    def detener():
            Intro.pause()
            primernivel.pause()
            segundonivel.pause()
            tercernivel.pause()
            cuartonivel.pause()
            quintonivel.pause()
            sextonivel.pause()
            septimonivel.pause()
            octavonivel.pause()
            novenonivel.pause()
            
    #funcion  para producir audios
    def playIntro(e):
        detener()
        Intro.play()
        
    def playnivel1(e):
        detener()
        primernivel.play()
    
    def playnivel2(e):
        detener()
        segundonivel.play()    
            
    def playnivel3(e):
        detener()
        tercernivel.play()    
            
    def playnivel4(e):
        detener()
        cuartonivel.play()    
            
    def playnivel5(e):
        detener()
        quintonivel.play()    
            
    def playnivel6(e):
        detener()
        sextonivel.play()   
        
    def playnivel7(e):
        detener()
        septimonivel.play()   
        
    def playnivel8(e):
        detener()
        octavonivel.play()   
        
    def playnivel9(e):
        detener()
        novenonivel.play()   
            
    Intro=ft.Audio(src="Intro.mp3",volume=1,balance=0)
    page.overlay.append(Intro)
    
    primernivel=ft.Audio(src="Primer_nivel.mp3",volume=1,balance=0)
    page.overlay.append(primernivel)
    
    segundonivel=ft.Audio(src="segundo_nivel.mp3",volume=1,balance=0)
    page.overlay.append(segundonivel)
    
    tercernivel=ft.Audio(src="tercer_nivel.mp3",volume=1,balance=0)
    page.overlay.append(tercernivel)
    
    cuartonivel=ft.Audio(src="cuarto_nivel.mp3",volume=1,balance=0)
    page.overlay.append(cuartonivel)
    
    quintonivel=ft.Audio(src="quinto_nivel.mp3",volume=1,balance=0)
    page.overlay.append(quintonivel)
    
    sextonivel=ft.Audio(src="sexto_nivel.mp3",volume=1,balance=0)
    page.overlay.append(sextonivel)
    
    septimonivel=ft.Audio(src="septimo_nivel.mp3",volume=1,balance=0)
    page.overlay.append(septimonivel)
    
    octavonivel=ft.Audio(src="octavo_nivel.mp3",volume=1,balance=0)
    page.overlay.append(octavonivel)
    
    novenonivel=ft.Audio(src="noveno_nivel.mp3",volume=1,balance=0)
    page.overlay.append(novenonivel)
    
#se crea la interfaz

    btnIntro=ft.FilledButton(text="escucha el Intro", disabled=False,on_click=playIntro)
    
    btnnivel1=ft.ElevatedButton(text="primer nivel",on_click=playnivel1)
    img1=ft.Image(src="primer-nivel.jpeg",width=150,height=150)
    
    btnnivel2=ft.ElevatedButton(text="segundo nivel",on_click=playnivel2)
    img2=ft.Image(src="segundo-nivel.jpeg",width=150,height=150)

    btnnivel3=ft.ElevatedButton(text="tercer nivel",on_click=playnivel3)
    img3=ft.Image(src="tercer-nivel.png",width=150,height=150)

    btnnivel4=ft.ElevatedButton(text="cuarto nivel",on_click=playnivel4)
    img4=ft.Image(src="cuarto-nivel.jpeg",width=150,height=150)

    btnnivel5=ft.ElevatedButton(text="quinto nivel",on_click=playnivel5)
    img5=ft.Image(src="quinto-nivel.jpeg",width=150,height=150)

    btnnivel6=ft.ElevatedButton(text="sexto nivel",on_click=playnivel6)
    img6=ft.Image(src="sexto-nivel.jpeg",width=150,height=150)

    btnnivel7=ft.ElevatedButton(text="septimo nivel",on_click=playnivel7)
    img7=ft.Image(src="septimo-nivel.jpeg",width=150,height=150)

    btnnivel8=ft.ElevatedButton(text="octavo nivel",on_click=playnivel8)
    img8=ft.Image(src="octavo-nivel.png",width=150,height=150)

    btnnivel9=ft.ElevatedButton(text="noveno nivel",on_click=playnivel9)
    img9=ft.Image(src="noveno-nivel.jpeg",width=150,height=150)

    
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
                            controls=[btnnivel1,img1]
                        ),
                        ft.Column(
                            alignment="CENTER",
                            controls=[btnnivel2,img2]
                        ),
                        ft.Column(
                            alignment="CENTER",
                            controls=[btnnivel3,img3]
                    )
                ]
            )
        ]
    ),
    ft.Row(
        alignment="CENTER",
        controls=[
            ft.Column(
                alignment="CENTER",
                spacing=10,
                controls=[btnnivel4,img4]
            ),
                ft.Column(
                alignment="CENTER",
                spacing=10,
                controls=[btnnivel5,img5]  
            ),
            ft.Column(
                alignment="CENTER",
                spacing=10,
                controls=[btnnivel6,img6]
            )
        ]
    ),
    ft.Row(
        alignment="CENTER",
        controls=[
            ft.Column(
                alignment="CENTER",
                spacing=10,
                controls=[btnnivel7,img7]
            ),
            ft.Column(
                alignment="CENTER",
                spacing=10,
                controls=[btnnivel8,img8]  
            ),
            ft.Column(
                alignment="CENTER",                   
                spacing=10,
                controls=[btnnivel9,img9]
            )
        ]
    )
)

    ft.app(main)
