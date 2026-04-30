//Introduccion

El proyecto era acerca de una "tienda de fotos" la cual debia guardar un registro en json y que permitira agregar modificar y borrar un paquete de fotos
dicho paquete debia contener un nombre, precio y el tipo o tematica de las fotos

//configurar el sistema

al momento de "usarlo" simplemente para su funcionamiento es necesario clonar el repositorio usando el link de github nada mas.

//estructura de trabajo

El repositorio funciona con 3 ramas add-services, delete-services, edit-services
cada una su creacion fue necesaria para trabajar en cada una de las funciones al tiempo sin tener conflictos y facilitar el trabajo y simplemente a lo ultimo se realizo un merge de cada rama a la main.

//Resolucion de conflictos

Al momento de realizar el primer push debiamos poner "git  push --set-upstream origin Rama" pero no sabiamos y causo un poco de errores,
tambien al momento de realizar el merge de las ramas al main genero un error que dañaban el funcionamiento del sistema todo debido a que andres no actualizo (git pull) el main  tuvo que borrara ese commit y rectificar bien que estaba haciendo y volvier a realizar la fusion.