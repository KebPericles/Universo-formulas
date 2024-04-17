---
title: Transformada de Fourier
---

# Fórmulas

### Transformada de Fourier en tiempo continuo

```math
F(\omega) = \int_{-\infty}^{\infty} f(t) \cdot e^{-j\omega t} \, dt
```

### Transformada inversa de Fourier

```math
f(t) = \frac{1}{2\pi} \int_{-\infty}^{\infty} F(\omega) \cdot e^{j\omega t} \, d\omega
```

## Propiedades

### Linealidad

```math
\mathcal{F}\{af(t) + bg(t)\} = aF(\omega) + bG(\omega)
```

### Desplazamiento en el dominio del tiempo

```math
\mathcal{F}\{f(t - t_0)\} = F(\omega)e^{-i\omega t_0}
```

### Desplazamiento en la frecuencia

```math
\mathcal{F}\{e^{i\omega_0 t}f(t)\} = F(\omega - \omega_0)
```

### Simetría

$$F(-\omega) = F^*(\omega)$$

## Teorema de convolución

###### Referencias

- Convolución de Tiempo Continuo y el CTFT. (2022, October 30). Rice University. https://espanol.libretexts.org/@go/page/86343

### En tiempo

```math
\mathcal{F}\left\{f * g\right\} =  \mathcal{F}\left\{f\right\} \cdot \mathcal{F}\left\{g\right\}
```

### En frecuencia

```math
\mathcal{F}\left\{f \cdot g\right\} = \frac{1}{2\pi} \mathcal{F}\left\{f\right\} * \mathcal{F}\left\{g\right\}
```

# Temas relacionados

- [Series de Fourier](Series%20de%20Fourier.md)
- [Variable compleja](Variable%20compleja.md)
