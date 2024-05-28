---
title: Integrales
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
