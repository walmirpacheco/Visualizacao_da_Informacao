import matplotlib.pyplot as plt


labels = 'Sem instrução e menos de 1 ano de estudo','Ensino fundamental incompleto ou equivalente','Ensino fundamental completo ou equivalente','Ensino médio incompleto ou equivalente','Ensino médio completo ou equivalente','Ensino superior incompleto ou equivalente','Ensino superior completo ou equivalente','Não determinado'
sizes = [15394, 70634, 15258, 13267, 48376, 8973, 25286, 0]
colors = ['gold', 'yellowgreen', 'coral', 'lightskyblue', 'red', 'grey', 'cyan', 'blue']
patches, texts, autotexts = plt.pie(sizes, colors=colors, autopct='%1.0f%%', startangle=90)
plt.legend(patches, labels, loc='lower right')
plt.axis('equal')

plt.show()