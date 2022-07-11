from mar import Mar, Suporte_mar



#cadastrando

#Serie
stranger_things = Mar('Serie', 45, 25)
stranger_things_4 = Mar('Serie', 70, 6)
outer_banks = Mar('Serie', 43, 18)
the_umbrella_academy = Mar('Serie', 45, 23)
riverdale = Mar('Serie', 41, 92)


#Podcasts
kanye_west_joe_rogan = Mar('Podcast', 177)
miley_cyrus_joe_rogan = Mar('Podcast', 126)
post_malone_joe_rogan = Mar('Podcast', 229)
neil_deGrasse_joe_rogan = Mar('Podcast', 72)
elon_musk_joe_rogan = Mar('Podcast', 81)
wiz_khalifa_joe_rogan = Mar('Podcast', 123)
alex_Jones_e_Tim_Dillon_joe_rogan = Mar('Podcast', 36)
elon_musk_joe_rogan_dois = Mar('Podcast', 28)

#adicionando na lista
suporte_mar = Suporte_mar()
suporte_mar.adicionar_programa(stranger_things)
suporte_mar.adicionar_programa(outer_banks)
suporte_mar.adicionar_programa(stranger_things_4)
suporte_mar.adicionar_programa(the_umbrella_academy)
suporte_mar.adicionar_programa(riverdale)
suporte_mar.adicionar_programa(wiz_khalifa_joe_rogan)

suporte_mar.adicionar_programa(post_malone_joe_rogan)
suporte_mar.adicionar_programa(miley_cyrus_joe_rogan)
suporte_mar.adicionar_programa(neil_deGrasse_joe_rogan)
suporte_mar.adicionar_programa(kanye_west_joe_rogan)
suporte_mar.adicionar_programa(elon_musk_joe_rogan)

#imprimindo horas de mar
horas_de_mar = suporte_mar.imprimi_horas_de_mar()
print(horas_de_mar)