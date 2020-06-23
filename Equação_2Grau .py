#!/usr/bin/env python
# coding: utf-8

# # Função para Calcular Equações do 2º Grau (quadrática)

# In[ ]:


# Solução
import math

a=float(input('digite o coeficiente a:'))
while a == 0:
    a=float(input('digite o coeficiente a diferente de zero:'))
           
b=float(input('digite o coeficiente b:'))
c=float(input('digite o coeficiente c:'))

delta= b**2-(4*a*c)

if delta < 0:
    print('Sem solução em ℝ')
elif delta == 0:
    
    print('A equação tem apenas uma solução em ℝ', b*2*a)
    
elif delta > 0:
    x1 = ((-b + math.sqrt(delta))/(2*a))
    x2 = ((-b - math.sqrt(delta))/(2*a))
    print('A equação tem duas soluções', x1 ,"e", x2)

