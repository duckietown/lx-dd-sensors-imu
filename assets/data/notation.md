# Notation used in the IMU LX

The tables below collect the mathematical conventions, the spaces and structures, and the symbols used throughout this learning experience (LX). Each notebook also defines its symbols where they first appear.

## Mathematical conventions

| Notation | Meaning |
| --- | --- |
| $\mathbf{u}$ or $\boldsymbol{\omega}$ | Bold lower-case Latin or Greek letter: a vector |
| $\mathbf{A}$ or $\mathbf{R}$ | Bold upper-case Latin letter: a matrix; $\mathbf{R}_{\mathrm{WB}}$ and $\mathbf{R}_{\mathrm{BS}}$ are rotation matrices |
| $(\cdot)_{\mathrm{S}}$, $(\cdot)_{\mathrm{B}}$, $(\cdot)_{\mathrm{W}}$ | Components expressed in the sensor, body, or world frame |
| $(\cdot)_i$, $(\cdot)_k$, $(\cdot)_{i,k}$ | Cartesian-component, sample-time, and combined component/sample subscripts |
| $\{\cdots\}$ | Set containing the listed elements |
| $\tilde{(\cdot)}$ | Measured quantity |
| $\Delta(\cdot)$ | Difference between two values of the enclosed quantity |
| $\hat{(\cdot)}$ | Estimate |
| $\dot{(\cdot)}$, $\ddot{(\cdot)}$ | First and second time derivatives |
| $(\cdot)(t)$ | Continuous-time value at time $t$ |
| $\int$, $\sum$ | Continuous accumulation and discrete summation |
| $\frac{a}{b}$ | Quotient of $a$ and nonzero $b$ |
| $\sin$, $\cos$, $\arcsin$, $\operatorname{atan2}(y, x)$ | Sine, cosine, inverse sine, and two-argument inverse tangent; the signs of $y$ and $x$ select the quadrant |
| $\det(\mathbf{A})$ | Determinant of the square matrix $\mathbf{A}$ |
| $\begin{bmatrix}\cdots\end{bmatrix}$, $\mathsf{T}$ | Column vector and transpose |
| $\lvert\cdot\rvert$, $\lVert\cdot\rVert$ | Scalar magnitude and Euclidean vector length |
| $\pm$ | Plus or minus |
| $=$, $\approx$, $\in$ | Equality, approximate equality, and set membership |
| $<$, $\leq$, $>$, $\geq$ | Strict and non-strict order relations |

## Spaces and structures

| Space or structure | Meaning |
| --- | --- |
| $\mathbb{Z}_{\geq 0}$ | Non-negative integers, $\{0, 1, 2, \ldots\}$ |
| $\mathbb{Z}_{>0}$ | Positive integers, $\{1, 2, \ldots\}$ |
| $\mathbb{R}$ | Real numbers |
| $\mathbb{R}_{\geq 0}$ | Non-negative real numbers |
| $\mathbb{R}_{>0}$ | Positive real numbers |
| $\mathbb{R}^3$ | Three-dimensional real vector space |
| $\mathbb{H}$ | Quaternion algebra |
| $\mathrm{SO}(3)$ | Set of right-handed three-dimensional rotation matrices |

## Symbols

| Symbol | Meaning | Type | Units |
| --- | --- | --- | --- |
| $\mathrm{S}$, $\mathrm{B}$, $\mathrm{W}$ | Sensor, Duckiedrone body, and stationary world frame labels | Frame labels | - |
| $i$ | Cartesian component index | $i \in \{x, y, z\}$ | - |
| $\mathbf{R}_{\mathrm{WB}}$, $\mathbf{R}_{\mathrm{BS}}$, $\mathbf{R}_i(\theta)$ | Body-to-world rotation, sensor-to-body rotation, and right-handed elementary rotation about axis $i$ through angle $\theta$ | $\mathbf{R}_{\mathrm{WB}}, \mathbf{R}_{\mathrm{BS}}, \mathbf{R}_i(\theta) \in \mathrm{SO}(3)$ | - |
| $\mathbf{I}$ | Three-by-three identity matrix | Dimensionless matrix | - |
| $\mathbf{p}$, $p_i$ | Coordinates of a point and its component on the chosen axes | $\mathbf{p} \in \mathbb{R}^3$, $p_i \in \mathbb{R}$ | $\mathrm{m}$ |
| $\mathbf{e}_i$ | Unit basis vector along Cartesian axis $i$ | $\mathbf{e}_i \in \mathbb{R}^3$, $\lVert\mathbf{e}_i\rVert = 1$ | - |
| $\mathbf{0}$ | Additive identity vector | $\mathbf{0} \in \mathbb{R}^3$ | Units of the surrounding vector |
| $\mathbf{a}$, $a_i$ | Linear acceleration and the component with index $i$ on the chosen axes | $\mathbf{a} \in \mathbb{R}^3$, $a_i \in \mathbb{R}$ | $\mathrm{m/s^2}$ |
| $\mathbf{v}$, $v_i$ | Linear velocity and the component with index $i$ on the chosen axes | $\mathbf{v} \in \mathbb{R}^3$, $v_i \in \mathbb{R}$ | $\mathrm{m/s}$ |
| $\mathbf{x}$, $x_i$ | Position and the component with index $i$ on the chosen axes | $\mathbf{x} \in \mathbb{R}^3$, $x_i \in \mathbb{R}$ | $\mathrm{m}$ |
| $v_k$ | Dead-reckoned vertical velocity at sample $k$ | $v_k \in \mathbb{R}$ | $\mathrm{m/s}$ |
| $x_k$ | Dead-reckoned altitude at sample $k$ | $x_k \in \mathbb{R}$ | $\mathrm{m}$ |
| $\mathbf{f}$, $f_i$ | Proper acceleration and the component with index $i$ on the chosen axes | $\mathbf{f} \in \mathbb{R}^3$, $f_i \in \mathbb{R}$ | $\mathrm{m/s^2}$ |
| $\tilde{\mathbf{f}}$, $\tilde{f}_i$ | Measured proper acceleration and the component with index $i$ on the chosen axes | $\tilde{\mathbf{f}} \in \mathbb{R}^3$, $\tilde{f}_i \in \mathbb{R}$ | $\mathrm{m/s^2}$ |
| $\mathbf{b}_{a}$, $b_{a,i}$, $b$ | Accelerometer bias, its component, and the constant one-axis alias used in the drift example | $\mathbf{b}_{a} \in \mathbb{R}^3$, $b_{a,i}, b \in \mathbb{R}$ | $\mathrm{m/s^2}$ |
| $\mathbf{n}_{a}$, $n_{a,i}$ | Random proper-acceleration measurement noise and the component with index $i$ on the chosen axes | $\mathbf{n}_{a} \in \mathbb{R}^3$, $n_{a,i} \in \mathbb{R}$ | $\mathrm{m/s^2}$ |
| $\boldsymbol{\omega}$, $\omega_i$ | Angular velocity and the component with index $i$ on the chosen axes | $\boldsymbol{\omega} \in \mathbb{R}^3$, $\omega_i \in \mathbb{R}$ | $\mathrm{rad/s}$ |
| $\tilde{\boldsymbol{\omega}}$, $\tilde{\omega}_i$ | Measured angular velocity and the component with index $i$ on the chosen axes | $\tilde{\boldsymbol{\omega}} \in \mathbb{R}^3$, $\tilde{\omega}_i \in \mathbb{R}$ | $\mathrm{rad/s}$ |
| $\theta$, $\theta_i$ | Generic rotation angle and angle of rotation about axis $i$ | $\theta, \theta_i \in \mathbb{R}$ | $\mathrm{rad}$ |
| $\alpha$, $\beta$, $\gamma$ | Roll, pitch, and yaw in the ZYX Euler-angle convention | $\alpha, \beta, \gamma \in \mathbb{R}$ | $\mathrm{rad}$ |
| $\psi$ | Axis-angle rotation angle | $\psi \in \mathbb{R}$ | $\mathrm{rad}$ |
| $\mathbf{u}$, $u_x$, $u_y$, $u_z$ | Unit axis of an axis-angle rotation and its Cartesian components | $\mathbf{u} = (u_x, u_y, u_z)^{\mathsf{T}} \in \mathbb{R}^3$, $\lVert\mathbf{u}\rVert = 1$ | - |
| $q$, $\mathbf{q}_{\mathrm{v}}$, $q_x$, $q_y$, $q_z$, $q_w$ | Unit quaternion, its vector and scalar parts, and scalar-last ROS components | $q = (\mathbf{q}_{\mathrm{v}}, q_w) \in \mathbb{H}$, $\lVert q\rVert = 1$; $\mathbf{q}_{\mathrm{v}} \in \mathbb{R}^3$; $q = (q_x, q_y, q_z, q_w)$ | - |
| $\mathbf{b}_{\omega}$, $b_{\omega,i}$ | Gyroscope bias and the component with index $i$ on the chosen axes | $\mathbf{b}_{\omega} \in \mathbb{R}^3$, $b_{\omega,i} \in \mathbb{R}$ | $\mathrm{rad/s}$ |
| $\mathbf{n}_{\omega}$, $n_{\omega,i}$ | Random angular-velocity measurement noise and the component with index $i$ on the chosen axes | $\mathbf{n}_{\omega} \in \mathbb{R}^3$, $n_{\omega,i} \in \mathbb{R}$ | $\mathrm{rad/s}$ |
| $\mathbf{g}$, $g_i$ | Gravitational acceleration and the component with index $i$ on the chosen axes | $\mathbf{g} \in \mathbb{R}^3$, $g_i \in \mathbb{R}$ | $\mathrm{m/s^2}$ |
| $g_0$, $\mathrm{m}g_0$ | Standard-gravity magnitude and its milligravity unit | $g_0 \in \mathbb{R}_{>0}$ | $\mathrm{m/s^2}$ |
| $\varepsilon$ | One-axis position error due to a constant accelerometer bias | $\varepsilon \in \mathbb{R}$ | $\mathrm{m}$ |
| $t$ | Continuous time | $t \in \mathbb{R}_{\geq 0}$ | $\mathrm{s}$ |
| $s$, $\tau$ | Dummy continuous-time integration variables | $s, \tau \in \mathbb{R}_{\geq 0}$ | $\mathrm{s}$ |
| $k$ | Sample index | $k \in \mathbb{Z}_{\geq 0}$ | - |
| $j$ | Local post-reference sample index | $j \in \mathbb{Z}_{\geq 0}$ | - |
| $t_k$ | Time of sample $k$ | $t_k \in \mathbb{R}_{\geq 0}$ | $\mathrm{s}$ |
| $\tau_j$ | Elapsed time from the start of integration to local sample $j$ | $\tau_j \in \mathbb{R}_{\geq 0}$ | $\mathrm{s}$ |
| $\Delta t_k$ | Elapsed time from sample $k - 1$ to sample $k$ | $\Delta t_k \in \mathbb{R}_{>0}$ | $\mathrm{s}$ |
| $\Delta t$ | Fixed sample interval, when $\Delta t_k = \Delta t$ | $\Delta t \in \mathbb{R}_{>0}$ | $\mathrm{s}$ |
| $N$ | Number of stationary-reference samples | $N \in \mathbb{Z}_{>0}$ | - |
| $T_{\mathrm{ref}}$ | Stationary-reference duration | $T_{\mathrm{ref}} \in \mathbb{R}_{>0}$ | $\mathrm{s}$ |
| $\hat{r}$ | Stationary reference for the measured vertical proper acceleration | $\hat{r} \in \mathbb{R}$ | $\mathrm{m/s^2}$ |
