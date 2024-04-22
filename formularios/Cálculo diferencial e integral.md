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

### Derivadas triviales

$$\frac{d}{dx} x = 1$$

$$\frac{d}{dx} c = 0 $$

$$\frac{d}{dx} c \cdot f(x) = c \cdot \frac{d}{dx} f(x)$$

$$\frac{d}{dx} (f(x) + g(x) - h(x)) = \frac{d}{dx} f(x) + \frac{d}{dx} g(x) - \frac{d}{dx} h(x)$$

### Composición de funciones (regla de la cadena)

$$\frac{d}{dx} f(g(x)) = \frac{df}{dg} \cdot \frac{dg}{dx}$$

$$\frac{d}{dx} f(g(h(x))) = \frac{df}{dg} \cdot \frac{dg}{dh} \cdot \frac{dh}{dx}$$

### Producto y división de funciones

$$\frac{d}{dx} (u \cdot v) = u\cdot\frac{dv}{dx} + v\cdot\frac{du}{dx}$$

$$\frac{d}{dx} (u \cdot v \cdot w) = \frac{du}{dx}\cdot v \cdot w +  u\cdot\frac{dv}{dx}\cdot w + u \cdot v \cdot \frac{dw}{dx}$$

$$\frac{d}{dx} \frac{u}{v} = \frac{\displaystyle v\cdot\frac{du}{dx} - u \cdot \frac{dv}{dx}}{\displaystyle v^2}$$

### Potencias y logaritmos

$$\frac{d}{dx} u^n = n\cdot u^{n-1} \cdot \frac{du}{dx}$$

$$\frac{d}{dx} log_c(u) = \frac{1}{u\cdot ln(c)}\cdot \frac{du}{dx}$$

$$\frac{d}{dx} ln(u) = \frac{1}{u}\cdot \frac{du}{dx}$$

$$\frac{d}{dx} e^u = e^u \cdot \frac{du}{dx}$$

$$\frac{d}{dx} c^u = c^u\cdot ln(a) \cdot \frac{du}{dx}$$

$$\frac{d}{dx} u^v = v \cdot u^{v-1} \cdot \frac{du}{dx} + u^v \cdot ln(u) \cdot \frac{dv}{dx}$$

### Valor absoluto

$$\frac{d}{dx} |x| = \frac{x}{ |x| }$$

### Trigonométricas

$$\frac{d}{dx} sin(u) = cos(u)\cdot\frac{du}{dx}$$

$$\frac{d}{dx} cos(u) = -sin(u) \cdot\frac{du}{dx}$$

$$\frac{d}{dx} tan(u) = sec^2(u) \cdot\frac{du}{dx}$$

$$\frac{d}{dx} cot(u) = -csc^2(u) \cdot\frac{du}{dx}$$

$$\frac{d}{dx} sec(u) = sec(u)\cdot tan(u) \cdot\frac{du}{dx}$$

$$\frac{d}{dx} csc(u) = -csc(u)\cdot cot(u) \cdot\frac{du}{dx}$$

$$\frac{d}{dx} arcsin(u) = \frac{1}{\sqrt{1-u^2}}\cdot\frac{du}{dx}$$

$$\frac{d}{dx} arccos(u) = -\frac{1}{\sqrt{1-u^2}} \cdot\frac{du}{dx}$$

$$\frac{d}{dx} arctan(u) = \frac{1}{{1+u^2}} \cdot\frac{du}{dx}$$

$$\frac{d}{dx} arccot(u) = -\frac{1}{{1+u^2}}  \cdot\frac{du}{dx}$$

$$\frac{d}{dx} arcsec(u) = \frac{1}{u\cdot\sqrt{u^2-1}} \cdot\frac{du}{dx}$$

$$\frac{d}{dx} arccsc(u) = -\frac{1}{u\cdot\sqrt{u^2-1}} \cdot\frac{du}{dx}$$

### Funciones hiperbólicas

$$\frac{d}{dx} sinh(u) = cosh(u)\cdot\frac{du}{dx}$$

$$\frac{d}{dx} cosh(u) = sinh(u) \cdot\frac{du}{dx}$$

$$\frac{d}{dx} tanh(u) = sec^2(u) \cdot\frac{du}{dx}$$

$$\frac{d}{dx} coth(u) = -csc^2(u) \cdot\frac{du}{dx}$$

$$\frac{d}{dx} sech(u) = -sech(u)\cdot tanh(u) \cdot\frac{du}{dx}$$

$$\frac{d}{dx} csch(u) = -csch(u)\cdot coth(u) \cdot\frac{du}{dx}$$

$$\frac{d}{dx} arcsinh(u) = \frac{1}{\sqrt{1+u^2}}\cdot\frac{du}{dx}$$

$$\frac{d}{dx} arccosh(u) = \frac{1}{\sqrt{u^2-1}} \cdot\frac{du}{dx}$$

$$\frac{d}{dx} arctanh(u) = \frac{1}{{1-u^2}} \cdot\frac{du}{dx}$$

$$\frac{d}{dx} arccoth(u) = -\frac{1}{{1-u^2}}  \cdot\frac{du}{dx}$$

$$\frac{d}{dx} arcsech(u) = -\frac{1}{u\cdot\sqrt{1-u^2}} \cdot\frac{du}{dx}$$

$$\frac{d}{dx} arccsch(u) = -\frac{1}{ |u|\cdot\sqrt{1+u^2}} \cdot\frac{du}{dx}$$

## Integrales

### Integrales triviales

$$\int dx = x + \mathfrak{C}$$

$$\int c\cdot du = c \int du$$

$$\int(du + dv + dw) = \int du + \int dv - \int dw$$

### Exponentes y logaritmos

$$\int u^n du = \frac{u^{n+1}}{n+1} + \mathfrak{C}, (n\neq -1)$$

$$\int u^{-1}du = ln(u) + \mathfrak{C}$$

$$\int e^udu = e^u + \mathfrak{C}$$

$$\int a^udu = \frac{a^u}{ln(a)} + \mathfrak{C}$$

### Trigonométricas

$$\int sin(u)du = -cos(u) + \mathfrak{C}$$ $$\int cos(u)du = sin(u) + \mathfrak{C}$$ $$\int tan(u)du = -ln(cos(u)) + \mathfrak{C} = ln(sec(u)) + \mathfrak{C}$$ $$\int cot(u)du = ln(sin(u)) + \mathfrak{C}$$ $$\int sec(u)du = ln(sec(u) + tan(u)) + \mathfrak{C}$$ $$\int csc(u)du = ln(csc(u) - cot(u)) + \mathfrak{C}$$

$$\int sec^2(u)du = tan(u) + \mathfrak{C}$$ $$\int csc^2(u)du = -cot(u) + \mathfrak{C}$$ $$\int sec(u)tan(u)du = sec(u) + \mathfrak{C}$$ $$\int csc(u)cot(u)du = -csc(u) + \mathfrak{C}$$

### Raíces comunes por inversas trigonométricas

$$\int \frac{du}{u^2 + c^2} = \frac{1}{c}arctan\left(\frac{u}{a}\right) + \mathfrak{C}$$

$$\int \frac{du}{u^2 - c^2} = \frac{1}{2c}ln \left(\frac{u-c}{u+c}\right) + \mathfrak{C}$$

$$\int \frac{du}{c^2 - u^2} = \frac{1}{2c}ln \left(\frac{c+u}{c-u}\right) + \mathfrak{C}$$

$$\int \frac{du}{\sqrt{c^2-u^2}} = arcsin \left( \frac{u}{a} \right) + \mathfrak{C}$$

$$\int \frac{du}{u\sqrt{u^2-c^2}} = \frac{1}{c} arcsec \left( \frac{u}{a} \right) + \mathfrak{C}$$

$$\int \frac{du}{\sqrt{u^2 \pm c^2}} = ln\left( u + \sqrt{u^2 \pm c^2} \right) + \mathfrak{C}$$

$$\int \sqrt{c^2-u^2}du = \frac{u}{2}\sqrt{c^2-u^2} + \frac{c^2}{2}arcsin\left( \frac{u}{a} \right) + \mathfrak{C}$$

$$\int \sqrt{u^2\pm c^2}du = \frac{u}{2}\sqrt{u^2 \pm c^2} \pm \frac{c^2}{2}ln\left( u + \sqrt{u^2 + c^2} \right) + \mathfrak{C}$$
