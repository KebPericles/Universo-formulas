# Repositorio de fórmulas en LaTeX

Este repositorio pretende ser un compendio de fórmulas en LaTeX que puedan ser reutilizadas, sin necesidad de pasar horas buscando en internet o de reescribir las fórmulas cada que se necesiten.

No se tiene como objetivo ser un formulario o apunte completo en el que se profundize.

## Estructura del repositorio

Usaremos el término formulario para referirnos a cualquier archivo markdown (`.md`) que contenga fórmulas en LaTeX.

Actualmente los formularios se encuentran en la carpeta base del repositorio, lo cual nos lleva al tema de la organización para lo cual deberemos explicar primero como se organizará un formulario.

### Organización de un formulario

Un formulario se compone de tres secciones:

1. [Frontmatter](#frontmatter)

2. [Fórmulas (todo)](#fórmulas)
3. [Temas relacionados (todo)](#temas-relacionados)

##### Ejemplo de un formulario

```markdown
---
title: Series de Fourier
---

# Fórmulas

#### Serie de Fourier trigonométrica

\[ f(t) = \frac{a*0}{2} + \sum*{n=1}^{\infty} \left( a_n \cos \left( \frac{2\pi n t}{T} \right) + b_n \sin \left( \frac{2\pi n t}{T} \right) \right) \]

# Temas relacionados

- [Transformada de Fourier](Transformada%20de%20Fourier.md)
```

#### Frontmatter

El Frontmatter, que es la sección entre dos `---` en la que se pueden poner metadatos en un archivo Markdown, se incluirán metadatos del formulario.

Hasta ahora se tiene planeado incluir los siguientes campos:

- `title`: Título del formulario. De momento no tiene ninguna función, pero se planea usarlo para generar los índices de áreas (ver [Generación de índices](#generación-de-índices)).

#### Fórmulas

TODO Aquí se pondrá una explicación de cómo se estructuran las fórmulas en un formulario.

#### Temas relacionados

TODO Aquí se pondrá una explicación de cómo se estructuran los temas relacionados en un formulario y su objetivo.

## Planes futuros

### Generación de índices

Se planea compilar los formularios para generar índices de cada área. En el índice se enlazarán los formularios del área, mostrando el título del formulario (en caso de no estar definido se usará el nombre del archivo enlazado).

Las áreas a las que pertenece un formulario se definiran en la sección `# Áreas`, la cual contendrá una lista como se muestra:

```markdown
# Áreas

- [Área 1]
- [Área 2]
```

##### Explicación de los enlaces

La notación anterior `[Área 1]` es para un enlace con estilo de referencia ([más información aquí](https://www.markdownguide.org/basic-syntax/#reference-style-links)), en principio no es necesario agregar el estilo de referencia, ya que al compilar los formularios se añadirá y si ya se encuentra se quitará y se reemplazará por el enlace correcto.

## Contribución

### Nomenclatura de commits

Se usará la siguiente nomenclatura para los commits:

```plaintext
<tipo>: <mensaje>
```

Donde `<tipo>` puede ser:

- `formulario`: Para cambios en los formularios.
- `docs`: Para cambios en la documentación (README's, etc.)
- `workflow`: Para cambios en los flujos de trabajo (CI/CD, etc.)
- `estilo`: Para cambios que no afectan el significado del código (espacios en blanco, formato, etc.)

Y `<mensaje>` es una descripción corta del cambio realizado.

### Formateo markdown

Se usa Prettier para formatear los archivos markdown. Se recomienda instalar la extensión de Prettier en el editor de texto que se use.

La configuración de Prettier se encuentra en el archivo `.prettierrc`.
