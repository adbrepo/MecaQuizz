print('Bienvenido al MecaQuiz')
answer=input('Estas listo para empezar a jugar ? (si/no) :')
score=0
total_questions=3
 
if answer.lower()=='si':
    answer=input('Pregunta 1: Cual es tu lenguage de programación favorito?')
    if answer.lower()=='python':
        score += 1
        print('Correcto')
    else:
        print('Respuesta incorrecta :(')
 
 
    answer=input('Pregunta 2: Vas a aprender programación en meca? ')
    if answer.lower()=='si':
        score += 1
        print('correct')
    else:
        print('Respuesta incorrecta :(')
 
    answer=input('Pregunta 3: Te sirve  python para realizar proyectos con inteligencia artificial?')
    if answer.lower()=='si':
        score += 1
        print('correct')
    else:
        print('Respuesta incorrecta :(')
 
print('Felicidades hisiste tu primer programa en python, respondiste',score,"preguntas correctamente!")
mark=(score/total_questions)*100
print('Puntos obtenidos:',mark)
print('Adios!!!!')