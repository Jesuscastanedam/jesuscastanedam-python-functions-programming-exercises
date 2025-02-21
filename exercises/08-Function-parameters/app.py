# Your code goes here:
def render_person(*param):
    nombre = param[0]
    age = param[3] 
    genero = param[-1]
    born = param[1]
    color = param[2]
    mensaje = f"{nombre} is a {age} years old {genero} born in {born} with {color} eyes"
    return mensaje


# Do not edit below this line
print(render_person('Bob', '05/22/1983', 'green', 23, 'male'))