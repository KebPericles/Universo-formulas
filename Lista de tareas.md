# Lista de tareas

## Formularios

- [ ] Probabilidad
- [ ] Lógica difusa
- [ ] Transformada de Laplace

Además agregar referencias a los ya existentes, el de integrales y derivadas creo que sería sencillo por la gran cantidad de videos que existen en YouTube, solo es cuestión de validar el video.

- [x] Separar Integrales y Derivadas en dos formularios.
- [ ] Etiquetar fórmulas de integrales

## Workflow

- [ ] Limpiar espacios en blanco antes y después del bloque de matemáticas antes de pasarlo al bloque de código. (se me ocurre incluirlo en la regex)

## API de fórmulas

Se pretende realizar una API que compile los formularios a JSON.

La estructura actual para un formulario compilado sería la siguiente:

```
{
  uuid: 'uuid',
  nombre: 'Nombre del formulario',
  aliases: ['alias 1', 'alias 2', 'alias 3'],
  temas_relacionados: ['uuid-tema-relacionado-1', 'uuid-tema-relacionado-2', 'uuid-tema-relacionado-3'],
  metadatos: {
    metadato_1: 'OwO',
    metadato_2: [1, 2, 3]
  },
  referencias: ['referencia 1', 'referencia 2'],
  subtemas: [
    {
      nombre: 'Default',
      aliases: [],
      referencias: ['referencia 1', 'referencia 2'],
      formulas: [
        {
          nombre: 'Nombre de la formula',
          aliases: ['alias 1', 'alias 2', 'alias 3'],
          referencias: [
            'referencia 1',
            'referencia 2'
          ],
          codigo: 'codigo de la formula',
          contenido_bruto: '',
          otras_formulas: [
            'codigo de otra formula'
          ]
        }
      ]
    },
    {
      nombre: 'Subtema 1',
      aliases: ['alias 1', 'alias 2', 'alias 3'],
      referencias: ['referencia 1', 'referencia 2'],
      formulas: [
        {
          nombre: 'Nombre de la formula',
          aliases: ['alias 1', 'alias 2', 'alias 3'],
          referencias: [
            'referencia 1',
            'referencia 2'
          ],
          codigo: 'codigo de la formula',
          contenido_bruto: '',
          otras_formulas: [
            'codigo de otra formula'
          ]
        }
      ]
    }
  ]
}
```

Será necesario incluir un UUID (probablemente con 32 bits sea suficiente) en cada formulario para esto, ya que será más fácil detectar los cambios de nombre de un formulario y tal vez otras cosas. Probablemente sea también necesario incluir un índice de nombre de formulario a UUID o viceversa.

### MVP

- Compilado de formularios a JSON.

### Otras tareas

- [ ] Indice Nombre de formulario a UUID
