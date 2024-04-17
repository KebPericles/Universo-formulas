# Contribuciones

¡Gracias por tu interés en contribuir a este proyecto! Queremos que cualquiera pueda colaborar y mejorar la calidad de los formularios, y pensando en ello hemos creado esta guía para que puedas ayudar de la forma que más te agrade.

## Formas de contribuir

> [!NOTE]  
> Cualquier ayuda es bienvenida y aquí solo presentamos las formas más comunes de colaborar, pero si tienes alguna otra idea, ¡no dudes en proponerla!

- [Reportando errores, problemas o sugerencias.](#reportando-errores-problemas-o-sugerencias)
- [Pull requests con correcciones o mejoras en los formularios.](#pull-requests-con-correcciones-o-mejoras-en-los-formularios)

### Reportando errores, problemas o sugerencias

, i encuentras algún error, tienes problema o tienes alguna sugerencia, por favor abre un issue en el repositorio.

¡Gracias por tu colaboración!

### Pull requests con correcciones o mejoras en los formularios

Esta sección aún está en construcción, aún así si quieres ayudar de esta forma puedes hacerlo e incluso nos ayudará a mejorar el proceso.

A grandes rasgos los pasos para contribuir con un formulario son los siguientes:

1. Haz un fork del repositorio.
2. Clona el repositorio en tu computadora.
3. Crea una rama con un nombre descriptivo.
4. Haz los cambios necesarios.
5. Haz un commit con los cambios siguiendo la [guía de estilo de commits](#commits).
6. Haz un push de la rama a tu fork.
7. Crea un pull request en el repositorio principal explicando los cambios. Si el pull request está relacionado con un issue, por favor menciona el número del issue en la descripción del pull request.

> [!TIP] Mantén el pull request pequeño y enfocado en un solo cambio. Esto facilitará la revisión y la aceptación de los cambios.

¡Gracias por tu colaboración!

## Guía de estilo

### Commits

Mantener un historial de commits limpio y ordenado es importante para facilitar la revisión de los cambios. Se recomienda hacer commits pequeños y siguiendo la guía de estilo que se presenta a continuación.

Se usará la siguiente estructura para los mensajes de los commits:

```plaintext
<tipo>: <mensaje>
```

Donde `<tipo>` puede ser:

- `formulario`: Para cambios en los formularios.
- `docs`: Para cambios en la documentación (README's, etc.)
- `workflow`: Para cambios en los flujos de trabajo (CI/CD, etc.)
- `estilo`: Para cambios que no afectan el significado del código (espacios en blanco, formato, etc.)

Y `<mensaje>` es una descripción corta del cambio realizado.

### Prettier

No es necesario tener Prettier instalado, ya que se tiene automatizado el formateo, esto se hace para mantener un estilo consistente en los archivos Markdown. En caso de formatear el código localmente, se recomienda usar Prettier con la configuración del proyecto o no formatear. Esto para facilitar la revisión de los cambios.
