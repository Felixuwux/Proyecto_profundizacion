import matplotlib.pyplot as plt 

x = ["5 am","6 am","7 am","8 am","9.5 am","10 am"]
y = [0,156252, 98561, 120587,587516, 856656 ]

plt.plot(x, y , color="blue", linewidth =3, label="Busqueda de videos de gatos")
plt.ylabel("Resultados")
plt.xlabel("Hora")
plt.legend()
plt.grid()
plt.show()