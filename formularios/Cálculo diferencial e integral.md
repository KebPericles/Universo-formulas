---
title: Cálculo diferencial e integral
---

# Fórmulas

### Notación:

La siguiente notación será usada para este formulario:

| Símbolo | Significado |
| --- | --- |
| $x$ | Variable independiente |
| $f(x)$, $g(x)$, $h(x)$ | Funciones sobre x |
| $\displaystyle \frac{d}{dx}f(x)$, $\displaystyle \frac{df}{dx}$ | Derivada sobre x de una función |
| $u$, $v$, $w$ | Variables dependientes |
| $c$, $n$ | Un valor constante |
| $dx$, $du$, $dv$, $dw$ | Diferencial de una variable |
| $\displaystyle \int dx$ | Integral |
| $\mathfrak{C}$ | Constante de integración |

## Derivadas

### Función identidad

$$\frac{d}{dx} x = 1$$

<!----------------------------------------->
<!-- AUTOGENERADO INICIA - NO MODIFICAR --->

```
\frac{d}{dx} x = 1
```

<!-- AUTOGENERADO TERMINA - NO MODIFICAR -->
<!----------------------------------------->

### Constante

$$\frac{d}{dx} c = 0 $$

<!----------------------------------------->
<!-- AUTOGENERADO INICIA - NO MODIFICAR --->

```
\frac{d}{dx} c = 0
```

<!-- AUTOGENERADO TERMINA - NO MODIFICAR -->
<!----------------------------------------->

### Producto por una constante

$$\frac{d}{dx} c \cdot f(x) = c \cdot \frac{d}{dx} f(x)$$

<!----------------------------------------->
<!-- AUTOGENERADO INICIA - NO MODIFICAR --->

```
\frac{d}{dx} c \cdot f(x) = c \cdot \frac{d}{dx} f(x)
```

<!-- AUTOGENERADO TERMINA - NO MODIFICAR -->
<!----------------------------------------->

###### Alias
- Linealidad de la derivada

### Regla de la suma

$$\frac{d}{dx} (f(x) + g(x) - h(x)) = \frac{d}{dx} f(x) + \frac{d}{dx} g(x) - \frac{d}{dx} h(x)$$

<!----------------------------------------->
<!-- AUTOGENERADO INICIA - NO MODIFICAR --->

```
\frac{d}{dx} (f(x) + g(x) - h(x)) = \frac{d}{dx} f(x) + \frac{d}{dx} g(x) - \frac{d}{dx} h(x)
```

<!-- AUTOGENERADO TERMINA - NO MODIFICAR -->
<!----------------------------------------->

###### Alias

- Linealidad de la derivada
- Derivada de una suma de funciones

### Composición de funciones

$$\frac{d}{dx} f(g(x)) = \frac{df}{dg} \cdot \frac{dg}{dx}$$

<!----------------------------------------->
<!-- AUTOGENERADO INICIA - NO MODIFICAR --->

```
\frac{d}{dx} f(g(x)) = \frac{df}{dg} \cdot \frac{dg}{dx}
```

<!-- AUTOGENERADO TERMINA - NO MODIFICAR -->
<!----------------------------------------->

$$\frac{d}{dx} f(g(h(x))) = \frac{df}{dg} \cdot \frac{dg}{dh} \cdot \frac{dh}{dx}$$

<!----------------------------------------->
<!-- AUTOGENERADO INICIA - NO MODIFICAR --->

```
\frac{d}{dx} f(g(h(x))) = \frac{df}{dg} \cdot \frac{dg}{dh} \cdot \frac{dh}{dx}
```

<!-- AUTOGENERADO TERMINA - NO MODIFICAR -->
<!----------------------------------------->

###### Alias

- Regla de la cadena

### Producto de funciones

$$\frac{d}{dx} (u \cdot v) = u\cdot\frac{dv}{dx} + v\cdot\frac{du}{dx}$$

<!----------------------------------------->
<!-- AUTOGENERADO INICIA - NO MODIFICAR --->

```
\frac{d}{dx} (u \cdot v) = u\cdot\frac{dv}{dx} + v\cdot\frac{du}{dx}
```

<!-- AUTOGENERADO TERMINA - NO MODIFICAR -->
<!----------------------------------------->

$$\frac{d}{dx} (u \cdot v \cdot w) = \frac{du}{dx}\cdot v \cdot w +  u\cdot\frac{dv}{dx}\cdot w + u \cdot v \cdot \frac{dw}{dx}$$

<!----------------------------------------->
<!-- AUTOGENERADO INICIA - NO MODIFICAR --->

```
\frac{d}{dx} (u \cdot v \cdot w) = \frac{du}{dx}\cdot v \cdot w +  u\cdot\frac{dv}{dx}\cdot w + u \cdot v \cdot \frac{dw}{dx}
```

<!-- AUTOGENERADO TERMINA - NO MODIFICAR -->
<!----------------------------------------->

### Divisón de funciones

$$\frac{d}{dx} \frac{u}{v} = \frac{\displaystyle v\cdot\frac{du}{dx} - u \cdot \frac{dv}{dx}}{\displaystyle v^2}$$

<!----------------------------------------->
<!-- AUTOGENERADO INICIA - NO MODIFICAR --->

```
\frac{d}{dx} \frac{u}{v} = \frac{\displaystyle v\cdot\frac{du}{dx} - u \cdot \frac{dv}{dx}}{\displaystyle v^2}
```

<!-- AUTOGENERADO TERMINA - NO MODIFICAR -->
<!----------------------------------------->

### Potencia de una función

$$\frac{d}{dx} u^n = n\cdot u^{n-1} \cdot \frac{du}{dx}$$

<!----------------------------------------->
<!-- AUTOGENERADO INICIA - NO MODIFICAR --->

```
\frac{d}{dx} u^n = n\cdot u^{n-1} \cdot \frac{du}{dx}
```

<!-- AUTOGENERADO TERMINA - NO MODIFICAR -->
<!----------------------------------------->

### Logaritmo de una función

$$\frac{d}{dx} log_c(u) = \frac{1}{u\cdot ln(c)}\cdot \frac{du}{dx}$$

<!----------------------------------------->
<!-- AUTOGENERADO INICIA - NO MODIFICAR --->

```
\frac{d}{dx} log_c(u) = \frac{1}{u\cdot ln(c)}\cdot \frac{du}{dx}
```

<!-- AUTOGENERADO TERMINA - NO MODIFICAR -->
<!----------------------------------------->

$$\frac{d}{dx} ln(u) = \frac{1}{u}\cdot \frac{du}{dx}$$

<!----------------------------------------->
<!-- AUTOGENERADO INICIA - NO MODIFICAR --->

```
\frac{d}{dx} ln(u) = \frac{1}{u}\cdot \frac{du}{dx}
```

<!-- AUTOGENERADO TERMINA - NO MODIFICAR -->
<!----------------------------------------->

### Exponencial de una función

$$\frac{d}{dx} e^u = e^u \cdot \frac{du}{dx}$$

<!----------------------------------------->
<!-- AUTOGENERADO INICIA - NO MODIFICAR --->

```
\frac{d}{dx} e^u = e^u \cdot \frac{du}{dx}
```

<!-- AUTOGENERADO TERMINA - NO MODIFICAR -->
<!----------------------------------------->

$$\frac{d}{dx} c^u = c^u\cdot ln(a) \cdot \frac{du}{dx}$$

<!----------------------------------------->
<!-- AUTOGENERADO INICIA - NO MODIFICAR --->

```
\frac{d}{dx} c^u = c^u\cdot ln(a) \cdot \frac{du}{dx}
```

<!-- AUTOGENERADO TERMINA - NO MODIFICAR -->
<!----------------------------------------->

### Función elevada a otra función

$$\frac{d}{dx} u^v = v \cdot u^{v-1} \cdot \frac{du}{dx} + u^v \cdot ln(u) \cdot \frac{dv}{dx}$$

<!----------------------------------------->
<!-- AUTOGENERADO INICIA - NO MODIFICAR --->

```
\frac{d}{dx} u^v = v \cdot u^{v-1} \cdot \frac{du}{dx} + u^v \cdot ln(u) \cdot \frac{dv}{dx}
```

<!-- AUTOGENERADO TERMINA - NO MODIFICAR -->
<!----------------------------------------->

### Valor absoluto

$$\frac{d}{dx} |x| = \frac{x}{ |x| }$$

<!----------------------------------------->
<!-- AUTOGENERADO INICIA - NO MODIFICAR --->

```
\frac{d}{dx} |x| = \frac{x}{ |x| }
```

<!-- AUTOGENERADO TERMINA - NO MODIFICAR -->
<!----------------------------------------->

### Seno

$$\frac{d}{dx} sin(u) = cos(u)\cdot\frac{du}{dx}$$

<!----------------------------------------->
<!-- AUTOGENERADO INICIA - NO MODIFICAR --->

```
\frac{d}{dx} sin(u) = cos(u)\cdot\frac{du}{dx}
```

<!-- AUTOGENERADO TERMINA - NO MODIFICAR -->
<!----------------------------------------->

### Coseno

$$\frac{d}{dx} cos(u) = -sin(u) \cdot\frac{du}{dx}$$

<!----------------------------------------->
<!-- AUTOGENERADO INICIA - NO MODIFICAR --->

```
\frac{d}{dx} cos(u) = -sin(u) \cdot\frac{du}{dx}
```

<!-- AUTOGENERADO TERMINA - NO MODIFICAR -->
<!----------------------------------------->

### Tangente

$$\frac{d}{dx} tan(u) = sec^2(u) \cdot\frac{du}{dx}$$

<!----------------------------------------->
<!-- AUTOGENERADO INICIA - NO MODIFICAR --->

```
\frac{d}{dx} tan(u) = sec^2(u) \cdot\frac{du}{dx}
```

<!-- AUTOGENERADO TERMINA - NO MODIFICAR -->
<!----------------------------------------->

### Cotangente

$$\frac{d}{dx} cot(u) = -csc^2(u) \cdot\frac{du}{dx}$$

<!----------------------------------------->
<!-- AUTOGENERADO INICIA - NO MODIFICAR --->

```
\frac{d}{dx} cot(u) = -csc^2(u) \cdot\frac{du}{dx}
```

<!-- AUTOGENERADO TERMINA - NO MODIFICAR -->
<!----------------------------------------->

### Secante

$$\frac{d}{dx} sec(u) = sec(u)\cdot tan(u) \cdot\frac{du}{dx}$$

<!----------------------------------------->
<!-- AUTOGENERADO INICIA - NO MODIFICAR --->

```
\frac{d}{dx} sec(u) = sec(u)\cdot tan(u) \cdot\frac{du}{dx}
```

<!-- AUTOGENERADO TERMINA - NO MODIFICAR -->
<!----------------------------------------->

### Cosecante

$$\frac{d}{dx} csc(u) = -csc(u)\cdot cot(u) \cdot\frac{du}{dx}$$

<!----------------------------------------->
<!-- AUTOGENERADO INICIA - NO MODIFICAR --->

```
\frac{d}{dx} csc(u) = -csc(u)\cdot cot(u) \cdot\frac{du}{dx}
```

<!-- AUTOGENERADO TERMINA - NO MODIFICAR -->
<!----------------------------------------->

### Arco seno

$$\frac{d}{dx} arcsin(u) = \frac{1}{\sqrt{1-u^2}}\cdot\frac{du}{dx}$$

<!----------------------------------------->
<!-- AUTOGENERADO INICIA - NO MODIFICAR --->

```
\frac{d}{dx} arcsin(u) = \frac{1}{\sqrt{1-u^2}}\cdot\frac{du}{dx}
```

<!-- AUTOGENERADO TERMINA - NO MODIFICAR -->
<!----------------------------------------->

###### Alias
- Seno inverso

### Arco coseno

$$\frac{d}{dx} arccos(u) = -\frac{1}{\sqrt{1-u^2}} \cdot\frac{du}{dx}$$

<!----------------------------------------->
<!-- AUTOGENERADO INICIA - NO MODIFICAR --->

```
\frac{d}{dx} arccos(u) = -\frac{1}{\sqrt{1-u^2}} \cdot\frac{du}{dx}
```

<!-- AUTOGENERADO TERMINA - NO MODIFICAR -->
<!----------------------------------------->

###### Alias
- Coseno inverso

### Arco tangente

$$\frac{d}{dx} arctan(u) = \frac{1}{{1+u^2}} \cdot\frac{du}{dx}$$

<!----------------------------------------->
<!-- AUTOGENERADO INICIA - NO MODIFICAR --->

```
\frac{d}{dx} arctan(u) = \frac{1}{{1+u^2}} \cdot\frac{du}{dx}
```

<!-- AUTOGENERADO TERMINA - NO MODIFICAR -->
<!----------------------------------------->

###### Alias
- Tangente inversa

### Arco cotangente

$$\frac{d}{dx} arccot(u) = -\frac{1}{{1+u^2}}  \cdot\frac{du}{dx}$$

<!----------------------------------------->
<!-- AUTOGENERADO INICIA - NO MODIFICAR --->

```
\frac{d}{dx} arccot(u) = -\frac{1}{{1+u^2}}  \cdot\frac{du}{dx}
```

<!-- AUTOGENERADO TERMINA - NO MODIFICAR -->
<!----------------------------------------->

###### Alias
- Cotangente inversa

### Arco secante

$$\frac{d}{dx} arcsec(u) = \frac{1}{u\cdot\sqrt{u^2-1}} \cdot\frac{du}{dx}$$

<!----------------------------------------->
<!-- AUTOGENERADO INICIA - NO MODIFICAR --->

```
\frac{d}{dx} arcsec(u) = \frac{1}{u\cdot\sqrt{u^2-1}} \cdot\frac{du}{dx}
```

<!-- AUTOGENERADO TERMINA - NO MODIFICAR -->
<!----------------------------------------->

###### Alias
- Secante inversa

### Arco cosecante

$$\frac{d}{dx} arccsc(u) = -\frac{1}{u\cdot\sqrt{u^2-1}} \cdot\frac{du}{dx}$$

<!----------------------------------------->
<!-- AUTOGENERADO INICIA - NO MODIFICAR --->

```
\frac{d}{dx} arccsc(u) = -\frac{1}{u\cdot\sqrt{u^2-1}} \cdot\frac{du}{dx}
```

<!-- AUTOGENERADO TERMINA - NO MODIFICAR -->
<!----------------------------------------->

###### Alias
- Cosecante inversa

### Seno hiperbólico

$$\frac{d}{dx} sinh(u) = cosh(u)\cdot\frac{du}{dx}$$

<!----------------------------------------->
<!-- AUTOGENERADO INICIA - NO MODIFICAR --->

```
\frac{d}{dx} sinh(u) = cosh(u)\cdot\frac{du}{dx}
```

<!-- AUTOGENERADO TERMINA - NO MODIFICAR -->
<!----------------------------------------->

### Coseno hiperbólico

$$\frac{d}{dx} cosh(u) = sinh(u) \cdot\frac{du}{dx}$$

<!----------------------------------------->
<!-- AUTOGENERADO INICIA - NO MODIFICAR --->

```
\frac{d}{dx} cosh(u) = sinh(u) \cdot\frac{du}{dx}
```

<!-- AUTOGENERADO TERMINA - NO MODIFICAR -->
<!----------------------------------------->

### Tangente hiperbólica

$$\frac{d}{dx} tanh(u) = sec^2(u) \cdot\frac{du}{dx}$$

<!----------------------------------------->
<!-- AUTOGENERADO INICIA - NO MODIFICAR --->

```
\frac{d}{dx} tanh(u) = sec^2(u) \cdot\frac{du}{dx}
```

<!-- AUTOGENERADO TERMINA - NO MODIFICAR -->
<!----------------------------------------->

### Cotangente hiperbólica

$$\frac{d}{dx} coth(u) = -csc^2(u) \cdot\frac{du}{dx}$$

<!----------------------------------------->
<!-- AUTOGENERADO INICIA - NO MODIFICAR --->

```
\frac{d}{dx} coth(u) = -csc^2(u) \cdot\frac{du}{dx}
```

<!-- AUTOGENERADO TERMINA - NO MODIFICAR -->
<!----------------------------------------->

### Secante hiperbólica

$$\frac{d}{dx} sech(u) = -sech(u)\cdot tanh(u) \cdot\frac{du}{dx}$$

<!----------------------------------------->
<!-- AUTOGENERADO INICIA - NO MODIFICAR --->

```
\frac{d}{dx} sech(u) = -sech(u)\cdot tanh(u) \cdot\frac{du}{dx}
```

<!-- AUTOGENERADO TERMINA - NO MODIFICAR -->
<!----------------------------------------->

### Cosecante hiperbólica

$$\frac{d}{dx} csch(u) = -csch(u)\cdot coth(u) \cdot\frac{du}{dx}$$

<!----------------------------------------->
<!-- AUTOGENERADO INICIA - NO MODIFICAR --->

```
\frac{d}{dx} csch(u) = -csch(u)\cdot coth(u) \cdot\frac{du}{dx}
```

<!-- AUTOGENERADO TERMINA - NO MODIFICAR -->
<!----------------------------------------->
### Arco seno hiperbólico
$$\frac{d}{dx} arcsinh(u) = \frac{1}{\sqrt{1+u^2}}\cdot\frac{du}{dx}$$

<!----------------------------------------->
<!-- AUTOGENERADO INICIA - NO MODIFICAR --->

```
\frac{d}{dx} arcsinh(u) = \frac{1}{\sqrt{1+u^2}}\cdot\frac{du}{dx}
```

<!-- AUTOGENERADO TERMINA - NO MODIFICAR -->
<!----------------------------------------->

### Arco coseno hiperbólico

$$\frac{d}{dx} arccosh(u) = \frac{1}{\sqrt{u^2-1}} \cdot\frac{du}{dx}$$

<!----------------------------------------->
<!-- AUTOGENERADO INICIA - NO MODIFICAR --->

```
\frac{d}{dx} arccosh(u) = \frac{1}{\sqrt{u^2-1}} \cdot\frac{du}{dx}
```

<!-- AUTOGENERADO TERMINA - NO MODIFICAR -->
<!----------------------------------------->

### Arco tangente hiperbólica

$$\frac{d}{dx} arctanh(u) = \frac{1}{{1-u^2}} \cdot\frac{du}{dx}$$

<!----------------------------------------->
<!-- AUTOGENERADO INICIA - NO MODIFICAR --->

```
\frac{d}{dx} arctanh(u) = \frac{1}{{1-u^2}} \cdot\frac{du}{dx}
```

<!-- AUTOGENERADO TERMINA - NO MODIFICAR -->
<!----------------------------------------->

### Arco cotangente hiperbólica

$$\frac{d}{dx} arccoth(u) = -\frac{1}{{1-u^2}}  \cdot\frac{du}{dx}$$

<!----------------------------------------->
<!-- AUTOGENERADO INICIA - NO MODIFICAR --->

```
\frac{d}{dx} arccoth(u) = -\frac{1}{{1-u^2}}  \cdot\frac{du}{dx}
```

<!-- AUTOGENERADO TERMINA - NO MODIFICAR -->
<!----------------------------------------->

### Arco secante hiperbólica

$$\frac{d}{dx} arcsech(u) = -\frac{1}{u\cdot\sqrt{1-u^2}} \cdot\frac{du}{dx}$$

<!----------------------------------------->
<!-- AUTOGENERADO INICIA - NO MODIFICAR --->

```
\frac{d}{dx} arcsech(u) = -\frac{1}{u\cdot\sqrt{1-u^2}} \cdot\frac{du}{dx}
```

<!-- AUTOGENERADO TERMINA - NO MODIFICAR -->
<!----------------------------------------->

### Arco cosecante hiperbólica

$$\frac{d}{dx} arccsch(u) = -\frac{1}{ |u|\cdot\sqrt{1+u^2}} \cdot\frac{du}{dx}$$

<!----------------------------------------->
<!-- AUTOGENERADO INICIA - NO MODIFICAR --->

```
\frac{d}{dx} arccsch(u) = -\frac{1}{ |u|\cdot\sqrt{1+u^2}} \cdot\frac{du}{dx}
```

<!-- AUTOGENERADO TERMINA - NO MODIFICAR -->
<!----------------------------------------->

## Integrales

### Integrales triviales

$$\int dx = x + \mathfrak{C}$$

<!----------------------------------------->
<!-- AUTOGENERADO INICIA - NO MODIFICAR --->

```
\int dx = x + \mathfrak{C}
```

<!-- AUTOGENERADO TERMINA - NO MODIFICAR -->
<!----------------------------------------->

$$\int c\cdot du = c \int du$$

<!----------------------------------------->
<!-- AUTOGENERADO INICIA - NO MODIFICAR --->

```
\int c\cdot du = c \int du
```

<!-- AUTOGENERADO TERMINA - NO MODIFICAR -->
<!----------------------------------------->

$$\int(du + dv + dw) = \int du + \int dv - \int dw$$

<!----------------------------------------->
<!-- AUTOGENERADO INICIA - NO MODIFICAR --->

```
\int(du + dv + dw) = \int du + \int dv - \int dw
```

<!-- AUTOGENERADO TERMINA - NO MODIFICAR -->
<!----------------------------------------->

### Exponentes y logaritmos

$$\int u^n du = \frac{u^{n+1}}{n+1} + \mathfrak{C}, (n\neq -1)$$

<!----------------------------------------->
<!-- AUTOGENERADO INICIA - NO MODIFICAR --->

```
\int u^n du = \frac{u^{n+1}}{n+1} + \mathfrak{C}, (n\neq -1)
```

<!-- AUTOGENERADO TERMINA - NO MODIFICAR -->
<!----------------------------------------->

$$\int u^{-1}du = ln(u) + \mathfrak{C}$$

<!----------------------------------------->
<!-- AUTOGENERADO INICIA - NO MODIFICAR --->

```
\int u^{-1}du = ln(u) + \mathfrak{C}
```

<!-- AUTOGENERADO TERMINA - NO MODIFICAR -->
<!----------------------------------------->

$$\int e^udu = e^u + \mathfrak{C}$$

<!----------------------------------------->
<!-- AUTOGENERADO INICIA - NO MODIFICAR --->

```
\int e^udu = e^u + \mathfrak{C}
```

<!-- AUTOGENERADO TERMINA - NO MODIFICAR -->
<!----------------------------------------->

$$\int a^udu = \frac{a^u}{ln(a)} + \mathfrak{C}$$

<!----------------------------------------->
<!-- AUTOGENERADO INICIA - NO MODIFICAR --->

```
\int a^udu = \frac{a^u}{ln(a)} + \mathfrak{C}
```

<!-- AUTOGENERADO TERMINA - NO MODIFICAR -->
<!----------------------------------------->

### Trigonométricas

$$\int sin(u)du = -cos(u) + \mathfrak{C}$$

<!----------------------------------------->
<!-- AUTOGENERADO INICIA - NO MODIFICAR --->

```
\int sin(u)du = -cos(u) + \mathfrak{C}
```

<!-- AUTOGENERADO TERMINA - NO MODIFICAR -->
<!----------------------------------------->

$$\int cos(u)du = sin(u) + \mathfrak{C}$$

<!----------------------------------------->
<!-- AUTOGENERADO INICIA - NO MODIFICAR --->

```
\int cos(u)du = sin(u) + \mathfrak{C}
```

<!-- AUTOGENERADO TERMINA - NO MODIFICAR -->
<!----------------------------------------->

$$\int tan(u)du = -ln(cos(u)) + \mathfrak{C} = ln(sec(u)) + \mathfrak{C}$$

<!----------------------------------------->
<!-- AUTOGENERADO INICIA - NO MODIFICAR --->

```
\int tan(u)du = -ln(cos(u)) + \mathfrak{C} = ln(sec(u)) + \mathfrak{C}
```

<!-- AUTOGENERADO TERMINA - NO MODIFICAR -->
<!----------------------------------------->

$$\int cot(u)du = ln(sin(u)) + \mathfrak{C}$$

<!----------------------------------------->
<!-- AUTOGENERADO INICIA - NO MODIFICAR --->

```
\int cot(u)du = ln(sin(u)) + \mathfrak{C}
```

<!-- AUTOGENERADO TERMINA - NO MODIFICAR -->
<!----------------------------------------->

$$\int sec(u)du = ln(sec(u) + tan(u)) + \mathfrak{C}$$

<!----------------------------------------->
<!-- AUTOGENERADO INICIA - NO MODIFICAR --->

```
\int sec(u)du = ln(sec(u) + tan(u)) + \mathfrak{C}
```

<!-- AUTOGENERADO TERMINA - NO MODIFICAR -->
<!----------------------------------------->

$$\int csc(u)du = ln(csc(u) - cot(u)) + \mathfrak{C}$$

<!----------------------------------------->
<!-- AUTOGENERADO INICIA - NO MODIFICAR --->

```
\int csc(u)du = ln(csc(u) - cot(u)) + \mathfrak{C}
```

<!-- AUTOGENERADO TERMINA - NO MODIFICAR -->
<!----------------------------------------->

$$\int sec^2(u)du = tan(u) + \mathfrak{C}$$

<!----------------------------------------->
<!-- AUTOGENERADO INICIA - NO MODIFICAR --->

```
\int sec^2(u)du = tan(u) + \mathfrak{C}
```

<!-- AUTOGENERADO TERMINA - NO MODIFICAR -->
<!----------------------------------------->

$$\int csc^2(u)du = -cot(u) + \mathfrak{C}$$

<!----------------------------------------->
<!-- AUTOGENERADO INICIA - NO MODIFICAR --->

```
\int csc^2(u)du = -cot(u) + \mathfrak{C}
```

<!-- AUTOGENERADO TERMINA - NO MODIFICAR -->
<!----------------------------------------->

$$\int sec(u)tan(u)du = sec(u) + \mathfrak{C}$$

<!----------------------------------------->
<!-- AUTOGENERADO INICIA - NO MODIFICAR --->

```
\int sec(u)tan(u)du = sec(u) + \mathfrak{C}
```

<!-- AUTOGENERADO TERMINA - NO MODIFICAR -->
<!----------------------------------------->

$$\int csc(u)cot(u)du = -csc(u) + \mathfrak{C}$$

<!----------------------------------------->
<!-- AUTOGENERADO INICIA - NO MODIFICAR --->

```
\int csc(u)cot(u)du = -csc(u) + \mathfrak{C}
```

<!-- AUTOGENERADO TERMINA - NO MODIFICAR -->
<!----------------------------------------->

### Raíces comunes por inversas trigonométricas

$$\int \frac{du}{u^2 + c^2} = \frac{1}{c}arctan\left(\frac{u}{a}\right) + \mathfrak{C}$$

<!----------------------------------------->
<!-- AUTOGENERADO INICIA - NO MODIFICAR --->

```
\int \frac{du}{u^2 + c^2} = \frac{1}{c}arctan\left(\frac{u}{a}\right) + \mathfrak{C}
```

<!-- AUTOGENERADO TERMINA - NO MODIFICAR -->
<!----------------------------------------->

$$\int \frac{du}{u^2 - c^2} = \frac{1}{2c}ln \left(\frac{u-c}{u+c}\right) + \mathfrak{C}$$

<!----------------------------------------->
<!-- AUTOGENERADO INICIA - NO MODIFICAR --->

```
\int \frac{du}{u^2 - c^2} = \frac{1}{2c}ln \left(\frac{u-c}{u+c}\right) + \mathfrak{C}
```

<!-- AUTOGENERADO TERMINA - NO MODIFICAR -->
<!----------------------------------------->

$$\int \frac{du}{c^2 - u^2} = \frac{1}{2c}ln \left(\frac{c+u}{c-u}\right) + \mathfrak{C}$$

<!----------------------------------------->
<!-- AUTOGENERADO INICIA - NO MODIFICAR --->

```
\int \frac{du}{c^2 - u^2} = \frac{1}{2c}ln \left(\frac{c+u}{c-u}\right) + \mathfrak{C}
```

<!-- AUTOGENERADO TERMINA - NO MODIFICAR -->
<!----------------------------------------->

$$\int \frac{du}{\sqrt{c^2-u^2}} = arcsin \left( \frac{u}{a} \right) + \mathfrak{C}$$

<!----------------------------------------->
<!-- AUTOGENERADO INICIA - NO MODIFICAR --->

```
\int \frac{du}{\sqrt{c^2-u^2}} = arcsin \left( \frac{u}{a} \right) + \mathfrak{C}
```

<!-- AUTOGENERADO TERMINA - NO MODIFICAR -->
<!----------------------------------------->

$$\int \frac{du}{u\sqrt{u^2-c^2}} = \frac{1}{c} arcsec \left( \frac{u}{a} \right) + \mathfrak{C}$$

<!----------------------------------------->
<!-- AUTOGENERADO INICIA - NO MODIFICAR --->

```
\int \frac{du}{u\sqrt{u^2-c^2}} = \frac{1}{c} arcsec \left( \frac{u}{a} \right) + \mathfrak{C}
```

<!-- AUTOGENERADO TERMINA - NO MODIFICAR -->
<!----------------------------------------->

$$\int \frac{du}{\sqrt{u^2 \pm c^2}} = ln\left( u + \sqrt{u^2 \pm c^2} \right) + \mathfrak{C}$$

<!----------------------------------------->
<!-- AUTOGENERADO INICIA - NO MODIFICAR --->

```
\int \frac{du}{\sqrt{u^2 \pm c^2}} = ln\left( u + \sqrt{u^2 \pm c^2} \right) + \mathfrak{C}
```

<!-- AUTOGENERADO TERMINA - NO MODIFICAR -->
<!----------------------------------------->

$$\int \sqrt{c^2-u^2}du = \frac{u}{2}\sqrt{c^2-u^2} + \frac{c^2}{2}arcsin\left( \frac{u}{a} \right) + \mathfrak{C}$$

<!----------------------------------------->
<!-- AUTOGENERADO INICIA - NO MODIFICAR --->

```
\int \sqrt{c^2-u^2}du = \frac{u}{2}\sqrt{c^2-u^2} + \frac{c^2}{2}arcsin\left( \frac{u}{a} \right) + \mathfrak{C}
```

<!-- AUTOGENERADO TERMINA - NO MODIFICAR -->
<!----------------------------------------->

$$\int \sqrt{u^2\pm c^2}du = \frac{u}{2}\sqrt{u^2 \pm c^2} \pm \frac{c^2}{2}ln\left( u + \sqrt{u^2 + c^2} \right) + \mathfrak{C}$$

<!----------------------------------------->
<!-- AUTOGENERADO INICIA - NO MODIFICAR --->

```
\int \sqrt{u^2\pm c^2}du = \frac{u}{2}\sqrt{u^2 \pm c^2} \pm \frac{c^2}{2}ln\left( u + \sqrt{u^2 + c^2} \right) + \mathfrak{C}
```

<!-- AUTOGENERADO TERMINA - NO MODIFICAR -->
<!----------------------------------------->
