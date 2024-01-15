secret_number = 777

print(
"""
+================================+
| ¡Bienvenido a mi juego, muggle!|
| Introduce un número entero     |
| y adivina qué número he        |
| elegido para ti.               |
|¿Cuál es el número secreto?     |
+================================+
""")

while True:
    user_number = int(input("+======" +  "Adivina el numero"  + "======+\n"))
    
    if user_number == secret_number:
        print(
            """
            +=======================================+
            
            ¡Bien hecho muggle!, Eres libre Ahora.
            
            +=======================================+
            """)
    else:
        print(
        """
        +============================================+
        
        ¡Ja, ja! ¡Estás atrapado en mi bucle!. 
        
        +=============================================+
        """)

