---
title: Series de Fourier
---

# Fórmulas

### Serie de Fourier trigonométrica

$$
f(t) = \frac{a_0}{2} + \sum_{n=1}^{\infty} \left[ a_n \cos(n\omega_0 t) + b_n \sin(n\omega_0 t) \right]
$$

#### Coeficientes de la serie de Fourier

$$
a_0 = \frac{2}{T} \int_{0}^{T} f(t) \, dt
$$

$$
a_n = \frac{2}{T} \int_{0}^{T} f(t) \cos(n\omega_0 t) \, dt
$$

$$
b_n = \frac{2}{T} \int_{0}^{T} f(t) \sin(n\omega_0 t) \, dt
$$

#### Serie de Fourier de una función par

$$
f(t) = \frac{a_0}{2} + \sum_{n=1}^{\infty} a_n \cos(n\omega_0 t)
$$

#### Serie de Fourier de una función impar

$$
f(t) = \sum_{n=1}^{\infty} b_n \sin(n\omega_0 t)
$$

### Serie de Fourier exponencial

$$
f(t) = \sum_{n=-\infty}^{\infty} c_n e^{jn\omega_0 t}
$$

#### Coeficientes de la serie de Fourier exponencial

$$
c_{0} = \frac{1}{T} \int_{0}^{T} f(t) \, dt
$$

$$
c_n = \frac{1}{T} \int_{0}^{T} f(t) e^{-jn\omega_0 t} \, dt
$$

$$
c_{-n} = c_{n}^{*}
$$

### Relación entre los coeficientes de la serie de Fourier exponencial y trigonométrica

$$
a_n = c_n + c_{-n}
$$

$$
b_n = j\left[ c_{n} - c_{-n} \right]
$$

$$
c_n = \frac{ a_n - jb_n}{2}
$$

$$
c_{-n} = \frac{a_n + jb_n}{2}
$$
