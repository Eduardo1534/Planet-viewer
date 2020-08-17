from tkinter import*

#roi

def root_init_():

    root_init = Tk()
    root_init.geometry('860x592+200+50')
    root_init.title('planet_viewer')
    images = PhotoImage(file='Images/Bg/bg_init.png')
    
    root_init.resizable(0, 0)
    lb_bg = Label(root_init, image=images )
    lb_bg.pack(side=TOP)

    def bt_init_click():

        root_init.destroy()
        root = Tk()
        root.title('planet_viewer')
        #imagens
        
        image = PhotoImage(file='Images/Bg/bg_perm.png')
        imagemz = PhotoImage(file='Images/Planetas/sol.png')
        imagel = PhotoImage(file='Images/Planetas/lua.png')
        imaget = PhotoImage(file='Images/Planetas/terra.png')
        imagem = PhotoImage(file='Images/Planetas/marte.png')
        imagem2 = PhotoImage(file='Images/Planetas/Mercurio.png')
        imagev = PhotoImage(file='Images/Planetas/Venus.png')
        alpha = PhotoImage(file='Images/Planetas/alpha.png')
        imagej = PhotoImage(file='Images/Planetas/jupiter.png')
        imagess = PhotoImage(file='Images/Planetas/Saturno.png')
        imageur = PhotoImage(file='Images/Planetas/urano.png')
        titless = PhotoImage(file='Images/Titulos/titulo ss.png')
        imagenet = PhotoImage(file='Images/Planetas/netuno.png')
        imagep = PhotoImage(file='Images/Planetas/Plutão.png')
        imagec = PhotoImage(file="Images/Planetas/ceres.png")
        imagent = PhotoImage(file='Images/Planetas/Titã.png')

        root.attributes('-fullscreen', True)
        lb_bg_2 = Label(root, image=image)
        lb_bg_2.pack(side=TOP)
        bt_exit = Button(root, width=4, height=1, text='x',font=('arial',12), command=root.destroy)
        bt_exit.place(x=0,y=0)

        lb_titulo = Label(root, image=titless)
        lb_titulo.place(x=475, y=0)

        c_fore = '#00a8f3'
        font = 'Berlin Sans FB',20

        lb_estrela = Label(root, text="Estrelas:",font=font, foreground=c_fore, background='Black')
        lb_estrela.place(x=2, y=50)

        lb_planet = Label(root, text="Planetas: ", font=font, foreground=c_fore, bg='black')
        lb_planet.place(x=0, y=190)

        lb_sate = Label(root, text="Satelites Naturais:", font=font, foregroun=c_fore, bg='black') 
        lb_sate.place(x=0, y=420)

        
        def sol_click():

            lb_sol = Label(root, image=imagemz, bg='black')
            lb_sol.place(x=0,y=0)

            def exit_bt():

                lb_sol.destroy()
                bt_exit.destroy()

            bt_exit = Button(root, text='<<<', font=('arial', 12),width=4,command=exit_bt)
            bt_exit.place(x=0, y=0)
            
        bg = '#F49E12'
        bt_sol = Button(root, text='Sol', font=font,width=15, height=2, bg=bg, command=sol_click)
        bt_sol.place(x=0, y=100)

        def lua_bt():

            lb_lua = Label(root, image=imagel,bg='black')
            lb_lua.place(x=0,y=0)

            def bt_lua_exit():

                lb_lua.destroy()
                bt_lexit.destroy()
            
            bt_lexit = Button(root, text='<<<', font=('arial', 12),width=4,command=bt_lua_exit)
            bt_lexit.place(x=0, y=0)

        bt_lua = Button(root, text='Lua', font=font, width=15, height=2,bg='#D4DEE1',command=lua_bt )
        bt_lua.place(x=0,y=470)

        def terra_bt():

            lb_terra = Label(root, image=imaget, bg='black')
            lb_terra.place(x=0,y=0)

            def bt_terra_exit():

                lb_terra.destroy()
                bt_texit.destroy()

            bt_texit = Button(root, text='<<<', font=('arial',12),width=4,command=bt_terra_exit)
            bt_texit.place(x=0, y=0)

        bt_terra = Button(root,text='Terra', font=font, width=15, height=2,bg='#0E90AD', command=terra_bt)
        bt_terra.place(x=504 , y=240)

        def marte_bt():

            lb_Marte = Label(root, image=imagem, bg='black')
            lb_Marte.place(x=0,y=0)

            def bt_terra_exit():

                lb_Marte.destroy()
                bt_mexit.destroy()

            bt_mexit = Button(root, text='<<<', font=('arial', 12),width=4,command=bt_terra_exit)
            bt_mexit.place(x=0, y=0)

        bt_marte = Button(root,text='Marte', font=font, width=15, height=2,bg='#DA5915', command=marte_bt)
        bt_marte.place(x=756, y=240)
        
        def mercurio_bt():

            lb_merc = Label(root, image=imagem2, bg='black')
            lb_merc.place(x=0, y=0)

            def merc_exit():

                lb_merc.destroy()
                bt_mexit2.destroy()
            bt_mexit2 = Button(root, text='<<<', font=('arial',12), width=4, command=merc_exit)
            bt_mexit2.place(x=0, y=0)

        merc_bt = Button(root, text='Mercurio', font=font, width=15, height=2, bg='#E34234', command=mercurio_bt)
        merc_bt.place(x=0, y=240)

        def bt_venu():

            lb_venu = Label(root, image=imagev,bg='black')
            lb_venu.place(x=0,y=0)

            def vexit():

                lb_venu.destroy()
                bt_vexit.destroy()

            bt_vexit = Button(root, text='<<<', font=('arial',12), width=4, command=vexit)
            bt_vexit.place(x=0, y=0)

        
        venu_bt = Button(root, text='Venus',font=font, width=15, height=2, bg='#F6A430',command=bt_venu)
        venu_bt.place(x=252, y=240)

        def bt_jupy():

            lb_jupy = Label(root, image=imagej, bg='black')
            lb_jupy.place(x=0,y=0)

            def jexit():

                lb_jupy.destroy()
                bt_jexit.destroy()

            bt_jexit = Button(root, text='<<<', font=('arial',12), width=4, command=jexit)
            bt_jexit.place(x=0, y=0)

        
        jupy_bt = Button(root, text='Jupiter',font=font, width=15, height=2, bg='#8A5419',command=bt_jupy)
        jupy_bt.place(x=1008, y=240)

        def bt_sat():

            lb_sat = Label(root, image=imagess, bg='black')
            lb_sat.place(x=0,y=0)

            def sexit():

                lb_sat.destroy()
                bt_sexit.destroy()

            bt_sexit = Button(root, text='<<<', font=('arial',12), width=4, command=sexit)
            bt_sexit.place(x=0, y=0)

        
        sat_bt = Button(root, text='Saturno',font=font, width=15, height=2, bg='#A68608',command=bt_sat)
        sat_bt.place(x=0, y=330)

        def bt_ur():

            lb_ur = Label(root, image=imageur, bg='black')
            lb_ur.place(x=0,y=0)

            def uexit():

                lb_ur.destroy()
                bt_uexit.destroy()

            bt_uexit = Button(root, text='<<<', font=('arial',12), width=4, command=uexit)
            bt_uexit.place(x=0, y=0)

        
        ur_bt = Button(root, text='Urano',font=font, width=15, height=2, bg='#088AA6',command=bt_ur)
        ur_bt.place(x=252, y=330)

        def bt_net():

            lb_ne = Label(root, image=imagenet,bg='black')
            lb_ne.place(x=0,y=0)

            def nexit():

                lb_ne.destroy()
                bt_nexit.destroy()

            bt_nexit = Button(root, text='<<<', font=('arial',12), width=4, command=nexit)
            bt_nexit.place(x=0, y=0)

        
        net_bt = Button(root, text='Netuno',font=font, width=15, height=2, bg='#082B6A',command=bt_net)
        net_bt.place(x=504, y=330)

        def root_2():
            lb_bg_3= Label(root, bg='black', image=image)
            lb_bg_3.place(x=0,y=0)

            lb_anao = Label(root, text='Planetas anões:', font=font, foreground=c_fore, bg='black')
            lb_anao.place(x=50,y=50)

            def bt_plut():
                lb_plut = Label(root, image=imagep, bg='black')
                lb_plut.place(x=0, y=0)

                def pexit():

                    lb_plut.destroy()
                    bt_pexit.destroy()
                    

                bt_pexit = Button(root, text='<<<',font=('arial',12), width=4, command=pexit)
                bt_pexit.place(x=0, y=0)


            plut_bt = Button(root, text='Plutão', font=font, width=15, height=2, bg='#FFFEF3', command=bt_plut)
            plut_bt.place(x=50, y=100)
            
            def bt_cere():

                lb_cere = Label(root, image=imagec, bg='black')
                lb_cere.place(x=0, y=0)

                def pexit():

                    lb_cere.destroy()
                    bt_cexit.destroy()

                bt_cexit = Button(root, text='<<<',font=('arial',12), width=4, command=pexit)
                bt_cexit.place(x=0, y=0)


            cere_bt = Button(root, text='Ceres', font=font, width=15, height=2, bg='#B7B6B1', command=bt_cere)
            cere_bt.place(x=302, y=100)


            def bt_make():

                lb_make = Label(root, image=alpha, bg='black')
                lb_make.place(x=0, y=0)

                def mexit2():

                    lb_make.destroy()
                    bt_mexit2.destroy()

                bt_mexit2 = Button(root, text='<<<',font=('arial',12), width=4, command=mexit2)
                bt_mexit2.place(x=0, y=0)


            make_bt = Button(root, text='Makemake', font=('Berlin Sans FB', 20), width=15, height=2, bg='#B18564', command=bt_make)
            make_bt.place(x=554, y=100)

            def bt_make():

                lb_make = Label(root, image=alpha, bg='black')
                lb_make.place(x=0, y=0)

                def mexit2():

                    lb_make.destroy()
                    bt_mexit2.destroy()

                bt_mexit2 = Button(root, text='<<<',font=('arial',12), width=4, command=mexit2)
                bt_mexit2.place(x=0, y=0)


            make_bt = Button(root, text='Makemake', font=('Berlin Sans FB', 20), width=15, height=2, bg='#B18564', command=bt_make)
            make_bt.place(x=554, y=100)


            

            def btmexit():

                root.destroy()

            btmexit = Button(root, text='x', font=('arial',12), width=4, command=btmexit)
            btmexit.place(x=0, y=0)

            def btmexit2_():

                btmexit.destroy()
                lb_bg_3.destroy()
                btmexit2.destroy()
                lo_bt.destroy()
                cere_bt.destroy()
                plut_bt.destroy()

            btmexit2 = Button(root, text='<', font=('arial',15),  command=btmexit2_)
            btmexit2.place(x=2, y=360)




        btm = Button(root, text='>', font=('arial',15),command=root_2)
        btm.place(x=1330, y=360)


        
        def bt_tita():

            lb_tita = Label(root, image=imagent, bg='black')
            lb_tita.place(x=0, y=0)

            def texit():

                lb_tita.destroy()
                bt_texit.destroy()

            bt_texit = Button(root, text='<<<',font=('arial',12), width=4, command=texit)
            bt_texit.place(x=0, y=0)


        tita_bt = Button(root, text='Titã', font=font, width=15, height=2, bg='#E6D906', command=bt_tita)
        tita_bt.place(x=252, y=470)

        def bt_euro():

            lb_euro = Label(root, image=alpha, bg='black')
            lb_euro.place(x=0, y=0)

            def eexit():

                lb_euro.destroy()
                bt_eexit.destroy()

            bt_eexit = Button(root, text='<<<',font=('arial',12), width=4, command=eexit)
            bt_eexit.place(x=0, y=0)


        euro_bt = Button(root, text='Europa', font=font, width=15, height=2, bg='#E1E0DA', command=bt_euro)
        euro_bt.place(x=504, y=470)

        def bt_lo():

            lb_lo = Label(root, image=alpha, bg='black')
            lb_lo.place(x=0, y=0)

            def lexit2():

                lb_lo.destroy()
                bt_lexit2.destroy()

            bt_lexit2 = Button(root, text='<<<',font=('arial',12), width=4, command=lexit2)
            bt_lexit2.place(x=0, y=0)


        lo_bt = Button(root, text='Lo', font=('Berlin Sans FB', 20), width=15, height=2, bg='#E1E0DA', command=bt_lo)
        lo_bt.place(x=756, y=470)

        root.mainloop()
        
    bt_init = Button(root_init, text='Start',font=('Berlin Sans FB',11), width=17, height=3, command=bt_init_click)
    bt_init.place(x= 369, y=240)
    
        
    root_init.mainloop()
root_init_()