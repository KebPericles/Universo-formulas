---
title: Series de Fourier
---

# Fórmulas

### Serie de Fourier trigonométrica

$$
f(t) = \frac{a_0}{2} + \sum_{n=1}^{\infty} \left[ a_n \cos(n\omega_0 t) + b_n \sin(n\omega_0 t) \right]
$$

<!----------------------------------------->
<!-- AUTOGENERADO INICIA - NO MODIFICAR --->

```
f(t) = \frac{a_0}{2} + \sum_{n=1}^{\infty} \left[ a_n \cos(n\omega_0 t) + b_n \sin(n\omega_0 t) \right]
```

<!-- AUTOGENERADO TERMINA - NO MODIFICAR -->
<!----------------------------------------->

#### Coeficientes de la serie de Fourier

$$
a_0 = \frac{2}{T} \int_{0}^{T} f(t) \, dt
$$

<!----------------------------------------->
<!-- AUTOGENERADO INICIA - NO MODIFICAR --->

```
a_0 = \frac{2}{T} \int_{0}^{T} f(t) \, dt
```

<!-- AUTOGENERADO TERMINA - NO MODIFICAR -->
<!----------------------------------------->

$$
a_n = \frac{2}{T} \int_{0}^{T} f(t) \cos(n\omega_0 t) \, dt
$$

<!----------------------------------------->
<!-- AUTOGENERADO INICIA - NO MODIFICAR --->

```
a_n = \frac{2}{T} \int_{0}^{T} f(t) \cos(n\omega_0 t) \, dt
```

<!-- AUTOGENERADO TERMINA - NO MODIFICAR -->
<!----------------------------------------->

$$
b_n = \frac{2}{T} \int_{0}^{T} f(t) \sin(n\omega_0 t) \, dt
$$

<!----------------------------------------->
<!-- AUTOGENERADO INICIA - NO MODIFICAR --->

```
b_n = \frac{2}{T} \int_{0}^{T} f(t) \sin(n\omega_0 t) \, dt
```

<!-- AUTOGENERADO TERMINA - NO MODIFICAR -->
<!----------------------------------------->

#### Serie de Fourier de una función par

$$
f(t) = \frac{a_0}{2} + \sum_{n=1}^{\infty} a_n \cos(n\omega_0 t)
$$

<!----------------------------------------->
<!-- AUTOGENERADO INICIA - NO MODIFICAR --->

```
f(t) = \frac{a_0}{2} + \sum_{n=1}^{\infty} a_n \cos(n\omega_0 t)
```

<!-- AUTOGENERADO TERMINA - NO MODIFICAR -->
<!----------------------------------------->

#### Serie de Fourier de una función impar

$$
f(t) = \sum_{n=1}^{\infty} b_n \sin(n\omega_0 t)
$$

<!----------------------------------------->
<!-- AUTOGENERADO INICIA - NO MODIFICAR --->

```
f(t) = \sum_{n=1}^{\infty} b_n \sin(n\omega_0 t)
```

<!-- AUTOGENERADO TERMINA - NO MODIFICAR -->
<!----------------------------------------->

### Serie de Fourier exponencial

$$
f(t) = \sum_{n=-\infty}^{\infty} c_n e^{jn\omega_0 t}
$$

<!----------------------------------------->
<!-- AUTOGENERADO INICIA - NO MODIFICAR --->

```
f(t) = \sum_{n=-\infty}^{\infty} c_n e^{jn\omega_0 t}
```

<!-- AUTOGENERADO TERMINA - NO MODIFICAR -->
<!----------------------------------------->

#### Coeficientes de la serie de Fourier exponencial

$$
c_{0} = \frac{1}{T} \int_{0}^{T} f(t) \, dt
$$

<!----------------------------------------->
<!-- AUTOGENERADO INICIA - NO MODIFICAR --->

```
c_{0} = \frac{1}{T} \int_{0}^{T} f(t) \, dt
```

<!-- AUTOGENERADO TERMINA - NO MODIFICAR -->
<!----------------------------------------->

$$
c_n = \frac{1}{T} \int_{0}^{T} f(t) e^{-jn\omega_0 t} \, dt
$$

<!----------------------------------------->
<!-- AUTOGENERADO INICIA - NO MODIFICAR --->

```
c_n = \frac{1}{T} \int_{0}^{T} f(t) e^{-jn\omega_0 t} \, dt
```

<!-- AUTOGENERADO TERMINA - NO MODIFICAR -->
<!----------------------------------------->

$$
c_{-n} = c_{n}^{*}
$$

<!----------------------------------------->
<!-- AUTOGENERADO INICIA - NO MODIFICAR --->

```
c_{-n} = c_{n}^{*}
```

<!-- AUTOGENERADO TERMINA - NO MODIFICAR -->
<!----------------------------------------->

### Relación entre los coeficientes de la serie de Fourier exponencial y trigonométrica

$$
a_n = c_n + c_{-n}
$$

<!----------------------------------------->
<!-- AUTOGENERADO INICIA - NO MODIFICAR --->

```
a_n = c_n + c_{-n}
```

<!-- AUTOGENERADO TERMINA - NO MODIFICAR -->
<!----------------------------------------->

$$
b_n = j\left[ c_{n} - c_{-n} \right]
$$

<!----------------------------------------->
<!-- AUTOGENERADO INICIA - NO MODIFICAR --->

```
b_n = j\left[ c_{n} - c_{-n} \right]
```

<!-- AUTOGENERADO TERMINA - NO MODIFICAR -->
<!----------------------------------------->

$$
c_n = \frac{ a_n - jb_n}{2}
$$

<!----------------------------------------->
<!-- AUTOGENERADO INICIA - NO MODIFICAR --->

```
c_n = \frac{ a_n - jb_n}{2}
```

<!-- AUTOGENERADO TERMINA - NO MODIFICAR -->
<!----------------------------------------->

$$
c_{-n} = \frac{a_n + jb_n}{2}
$$

<!----------------------------------------->
<!-- AUTOGENERADO INICIA - NO MODIFICAR --->

```
c_{-n} = \frac{a_n + jb_n}{2}
```

<!-- AUTOGENERADO TERMINA - NO MODIFICAR -->
<!----------------------------------------->

