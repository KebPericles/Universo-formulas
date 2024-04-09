---
title: Transformada de Fourier
---

# Fórmulas

### Transformada de Fourier en tiempo continuo

$$
F(\omega) = \int_{-\infty}^{\infty} f(t) \cdot e^{-j\omega t} \, dt
$$

### Transformada inversa de Fourier

$$
f(t) = \frac{1}{2\pi} \int_{-\infty}^{\infty} F(\omega) \cdot e^{j\omega t} \, d\omega
$$

## Propiedades

### Linealidad

$$\mathcal{F}\{af(t) + bg(t)\} = aF(\omega) + bG(\omega)$$

### Desplazamiento en el dominio del tiempo

$$\mathcal{F}\{f(t - t_0)\} = F(\omega)e^{-i\omega t_0}$$

### Desplazamiento en la frecuencia

$$\mathcal{F}\{e^{i\omega_0 t}f(t)\} = F(\omega - \omega_0)$$

### Simetría

$$F(-\omega) = F^*(\omega)$$

# Temas relacionados

- [Series de Fourier](Series%20de%20Fourier.md)
- [Variable compleja](Variable%20compleja.md)
