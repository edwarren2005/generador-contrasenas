import random
import string

print("🔐 Generador de contraseñas seguras 🔐")

# Pedimos la longitud deseada
longitud = int(input("¿Qué longitud quieres para tu contraseña?: "))

# Definimos los caracteres disponibles
letras = string.ascii_letters  # abc...XYZ
digitos = string.digits        # 0123456789
simbolos = string.punctuation  # !@#$%^&*()...

# Combinamos todos
caracteres = letras + digitos + simbolos

# Generamos la contraseña
contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))

# Mostramos la contraseña generada
print(f"Tu contraseña segura es: {contrasena}")
