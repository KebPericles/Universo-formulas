# Repositorio de fórmulas en LaTeX

Este repositorio pretende ser un compendio de fórmulas en LaTeX que puedan ser reutilizadas, sin necesidad de buscar en todo internet o de reescribir las fórmulas cada que se necesiten.

No se tiene como objetivo ser un apunte en el que se profundize sobre las fórmulas.

## Estructura del repositorio

Usaremos el término formulario para referirnos a cualquier archivo markdown (`.md`) que contenga fórmulas en LaTeX.

Actualmente los formularios se encuentran en la carpeta base del repositorio, lo cual nos lleva al tema de la organización para lo cual deberemos explicar primero como se organizará un formulario.

### Organización de un formulario

TL;DR: En la siguiente sección se explica a detalle y con ejemplos cómo se organiza un formulario. Si prefieres omitir la explicación y ver directamente un ejemplo, el formulario ["Transformada de Fourier"](formularios/Transformada%20de%20Fourier.md) es excelente para ver toda la estructura de un formulario.

Un formulario se compone de tres secciones:

1. [Frontmatter](#frontmatter)

2. [Fórmulas](#fórmulas)
3. [Temas relacionados (todo)](#temas-relacionados)

##### Ejemplo de un formulario

```markdown
---
title: Series de Fourier
---

# Fórmulas

### Serie de Fourier trigonométrica

\[ f(t) = \frac{a*0}{2} + \sum*{n=1}^{\infty} \left( a_n \cos \left( \frac{2\pi n t}{T} \right) + b_n \sin \left( \frac{2\pi n t}{T} \right) \right) \]

# Temas relacionados

- [Transformada de Fourier](Transformada%20de%20Fourier.md)
```

#### Frontmatter

El Frontmatter, que es la sección entre dos `---` en la que se pueden poner metadatos en un archivo Markdown, se incluirán metadatos del formulario.

Hasta ahora se tiene planeado incluir los siguientes campos:

- `title`: Título del formulario. De momento no tiene ninguna función, pero se planea usarlo para generar los índices de áreas (ver [Generación de índices](#generación-de-índices)).

#### Fórmulas

Esta sección contendrá las fórmulas en LaTeX. Se iniciará con un título de nivel 1 (`# Fórmulas`) y se organizarán las fórmulas por subtema de nivel 2 (`## Subtema 1`, `## Subtema 2`, etc.).

Dentro de cada subtema se pondrán las fórmulas, empezando con un título de nivel 3 (`### Fórmula 1`, `### Fórmula 2`, etc.) y la fórmula en LaTeX (para aquellas fórmulas que no necesiten subtema se podrán incluir inmediatamente después del título `# Fórmulas`).

Opcionalmente se pueden incluir referencias, para lo cual se pondrá un título de nivel 6 al final de la fórmula (`###### Referencias`) y dentro las referencias (se recomienda citar en APA para mantener un estilo, pero no es estrictamente necesario). Para aquellas referencias que sirvan para todas o la mayoría de las fórmulas de un subtema se podrá poner el título de nivel 6 antes de las fórmulas.

##### Ejemplo de fórmulas

El formulario de [Transformada de Fourier](formularios/Transformada%20de%20Fourier.md) es un muy buen ejemplo de la organización de fórmulas y, en general, de la estructura para un formulario.

```markdown
# Fórmulas

## Subtema 1

###### Referencias ------- (Referencias para todas las fórmulas de este subtema)

- [Wikipedia](https://es.wikipedia.org/wiki/Serie_de_Fourier)

### Fórmula con referencias únicas

$$
f(t) = \frac{a*0}{2} + \sum*{n=1}^{\infty} \left( a_n \cos \left( \frac{2\pi n t}{T} \right) + b_n \sin \left( \frac{2\pi n t}{T} \right) \right)
$$

###### Referencias ------- (Referencias para esta fórmula)

- [Wikipedia](https://es.wikipedia.org/wiki/Serie_de_Fourier)

### Fórmula sin referencias únicas

$$
a_n = \frac{2}{T} \int_{0}^{T} f(t) \cos \left( \frac{2\pi n t}{T} \right) \, dt
$$
```

Nota: este formato puede cambiar en el futuro si es necesario.

> [!IMPORTANT]  
> Para las fórmulas se podrá usar el formato estándar de LaTeX `$$ $$`, aunque se recomienda usar el bloque de código `math`.  
> En caso de que existan problemas de renderizado con la sintaxis de LaTeX, será obligatorio usar el bloque de código `math` con el objetivo de mantener la compatibilidad, ya que es la implementación más estable y compatible del [GitHub Flavored Markdown](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions#writing-expressions-as-blocks) con la sintáxis de LaTeX.  
> En [esta discusión](https://github.com/orgs/community/discussions/36984#discussioncomment-3981018) se da una breve razón (no oficial) del porque la incompatibilidad y en [esta otra](https://github.com/orgs/community/discussions/87461) se pide que lo arreglen.

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

### Cambio de variables

Opción para cambiar las variables de las fórmulas, por ejemplo, cambiar `t` por `x` en todas las fórmulas de un formulario o de forma más compleja un conjunto a otro. Por ejemplo en el formulario de las [Series de Fourier](formularios/Series%20de%20Fourier.md) poder escoger entre usar la frecuencia angular, la frecuencia o el periodo:

$$
n\omega_0=\frac{2\pi n}{T} = 2\pi nf
$$

### Mostrar bloque de código LatTeX

Compilar los formularios para mostrar el código LaTeX de las fórmulas, esto con el fin de que se puedan copiar y pegar fácilmente.

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
