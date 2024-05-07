---
title: Transformada de Fourier
---

# Fórmulas

### Transformada de Fourier en tiempo continuo

```math
F(\omega) = \int_{-\infty}^{\infty} f(t) \cdot e^{-j\omega t} \, dt
```

<!----------------------------------------->
<!-- AUTOGENERADO INICIA - NO MODIFICAR --->

```
F(\omega) = \int_{-\infty}^{\infty} f(t) \cdot e^{-j\omega t} \, dt
```

<!-- AUTOGENERADO TERMINA - NO MODIFICAR -->
<!----------------------------------------->

### Transformada inversa de Fourier

```math
f(t) = \frac{1}{2\pi} \int_{-\infty}^{\infty} F(\omega) \cdot e^{j\omega t} \, d\omega
```

<!----------------------------------------->
<!-- AUTOGENERADO INICIA - NO MODIFICAR --->

```
f(t) = \frac{1}{2\pi} \int_{-\infty}^{\infty} F(\omega) \cdot e^{j\omega t} \, d\omega
```

<!-- AUTOGENERADO TERMINA - NO MODIFICAR -->
<!----------------------------------------->

## Propiedades

### Linealidad

```math
\mathcal{F}\{af(t) + bg(t)\} = aF(\omega) + bG(\omega)
```

<!----------------------------------------->
<!-- AUTOGENERADO INICIA - NO MODIFICAR --->

```
\mathcal{F}\{af(t) + bg(t)\} = aF(\omega) + bG(\omega)
```

<!-- AUTOGENERADO TERMINA - NO MODIFICAR -->
<!----------------------------------------->

### Desplazamiento en el dominio del tiempo

```math
\mathcal{F}\{f(t - t_0)\} = F(\omega)e^{-i\omega t_0}
```

<!----------------------------------------->
<!-- AUTOGENERADO INICIA - NO MODIFICAR --->

```
\mathcal{F}\{f(t - t_0)\} = F(\omega)e^{-i\omega t_0}
```

<!-- AUTOGENERADO TERMINA - NO MODIFICAR -->
<!----------------------------------------->

### Desplazamiento en la frecuencia

```math
\mathcal{F}\{e^{i\omega_0 t}f(t)\} = F(\omega - \omega_0)
```

<!----------------------------------------->
<!-- AUTOGENERADO INICIA - NO MODIFICAR --->

```
\mathcal{F}\{e^{i\omega_0 t}f(t)\} = F(\omega - \omega_0)
```

<!-- AUTOGENERADO TERMINA - NO MODIFICAR -->
<!----------------------------------------->

### Simetría

$$F(-\omega) = F^*(\omega)$$

<!----------------------------------------->
<!-- AUTOGENERADO INICIA - NO MODIFICAR --->

```
F(-\omega) = F^*(\omega)
```

<!-- AUTOGENERADO TERMINA - NO MODIFICAR -->
<!----------------------------------------->

## Teorema de convolución

###### Referencias

- Convolución de Tiempo Continuo y el CTFT. (2022, October 30). Rice University. https://espanol.libretexts.org/@go/page/86343

### En tiempo

```math
\mathcal{F}\left\{f * g\right\} =  \mathcal{F}\left\{f\right\} \cdot \mathcal{F}\left\{g\right\}
```

<!----------------------------------------->
<!-- AUTOGENERADO INICIA - NO MODIFICAR --->

```
\mathcal{F}\left\{f * g\right\} =  \mathcal{F}\left\{f\right\} \cdot \mathcal{F}\left\{g\right\}
```

<!-- AUTOGENERADO TERMINA - NO MODIFICAR -->
<!----------------------------------------->

### En frecuencia

```math
\mathcal{F}\left\{f \cdot g\right\} = \frac{1}{2\pi} \mathcal{F}\left\{f\right\} * \mathcal{F}\left\{g\right\}
```

<!----------------------------------------->
<!-- AUTOGENERADO INICIA - NO MODIFICAR --->

```
\mathcal{F}\left\{f \cdot g\right\} = \frac{1}{2\pi} \mathcal{F}\left\{f\right\} * \mathcal{F}\left\{g\right\}
```

<!-- AUTOGENERADO TERMINA - NO MODIFICAR -->
<!----------------------------------------->

# Temas relacionados

- [Series de Fourier](Series%20de%20Fourier.md)
- [Variable compleja](Variable%20compleja.md)

