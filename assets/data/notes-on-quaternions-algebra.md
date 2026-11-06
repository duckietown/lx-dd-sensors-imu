### Quaternion multiplication and the rotation of a vector

Using scalar-last notation, let $a=(\mathbf{a},a_w)$ and $b=(\mathbf{b},b_w)$ be two quaternions. Their product, called the Hamilton product, is defined as

$$
ab=
\left(
a_w\mathbf{b}+b_w\mathbf{a}+\mathbf{a}\times\mathbf{b},
\;
a_wb_w-\mathbf{a}\cdot\mathbf{b}
\right),
$$

where $\cdot$ and $\times$ denote the usual vector dot and cross products. Quaternion multiplication is associative, although it is generally not commutative: reversing the factors reverses the cross-product term.

To see how this multiplication produces a rotation, consider a unit axis $\mathbf{u}$ and a rotation angle $\psi$. Write

$$
q=(s\mathbf{u},c),
\qquad
s=\sin\left(\frac{\psi}{2}\right),
\qquad
c=\cos\left(\frac{\psi}{2}\right).
$$

Since $q$ is a unit quaternion, its inverse is

$$
q^{-1}=(-s\mathbf{u},c).
$$

Represent the vector to be rotated as the quaternion $p=(\mathbf{v},0)$. Applying the multiplication rule first gives

$$
qp=
\left(
c\mathbf{v}+s\,\mathbf{u}\times\mathbf{v},
\;
-s\,\mathbf{u}\cdot\mathbf{v}
\right).
$$

Multiplying this result by $q^{-1}$ and using
$(\mathbf{u}\times\mathbf{v})\times\mathbf{u}
=\mathbf{v}-\mathbf{u}(\mathbf{u}\cdot\mathbf{v})$
gives

$$
qpq^{-1}
=
\left(
(c^2-s^2)\mathbf{v}
+2s^2\mathbf{u}(\mathbf{u}\cdot\mathbf{v})
+2cs\,\mathbf{u}\times\mathbf{v},
\;
0
\right).
$$

The double-angle identities turn the vector part into

$$
\mathbf{v}'
=
\mathbf{v}\cos\psi
+\mathbf{u}(\mathbf{u}\cdot\mathbf{v})(1-\cos\psi)
+(\mathbf{u}\times\mathbf{v})\sin\psi.
$$

This is Rodrigues' rotation formula. Its geometry becomes clearer by separating the vector into components parallel and perpendicular to the axis:

$$
\mathbf{v}_{\parallel}
=\mathbf{u}(\mathbf{u}\cdot\mathbf{v}),
\qquad
\mathbf{v}_{\perp}
=\mathbf{v}-\mathbf{v}_{\parallel}.
$$

The result can then be written as

$$
\mathbf{v}'
=
\mathbf{v}_{\parallel}
+\mathbf{v}_{\perp}\cos\psi
+(\mathbf{u}\times\mathbf{v}_{\perp})\sin\psi.
$$

The parallel component stays unchanged, while the perpendicular component rotates through $\psi$ in the plane normal to $\mathbf{u}$, following the right-hand rule. Thus,

$$
\boxed{(\mathbf{v}',0)=q\,(\mathbf{v},0)\,q^{-1}}
$$

represents an active rotation of the vector in a fixed coordinate basis. The calculation also explains the half-angle in $q$: multiplying on both sides produces the double-angle terms corresponding to the full rotation angle $\psi$.

### Why quaternion multiplication composes rotations

A vector $\mathbf{v}$ can be written as a quaternion with zero scalar part:

$$
p=(\mathbf{v},0).
$$

For a unit quaternion $q$, the corresponding rotation acts on this vector through

$$
p'=q\,p\,q^{-1},
$$

where multiplication is quaternion multiplication. The result again has zero scalar part, and its vector part is the rotated vector. For a unit quaternion, the inverse is its conjugate:

$$
q^{-1}=(-\mathbf{q}_v,q_w).
$$

Now consider two successive rotations, represented by $q_1$ and $q_2$, with both rotation operators expressed in the same fixed coordinate basis. Applying $q_1$ first and $q_2$ second gives

$$
p''
=q_2\left(q_1 p q_1^{-1}\right)q_2^{-1}.
$$

Quaternion multiplication is associative, so the factors can be regrouped:

$$
p''
=(q_2q_1)\,p\,(q_1^{-1}q_2^{-1}).
$$

Using the inverse-of-a-product identity,

$$
(q_2q_1)^{-1}=q_1^{-1}q_2^{-1},
$$

the result becomes

$$
p''=(q_2q_1)\,p\,(q_2q_1)^{-1}.
$$

This has exactly the form of a single quaternion rotation. Therefore, the combined rotation is represented by

$$
\boxed{q_{\mathrm{combined}}=q_2q_1}.
$$

The product remains a unit quaternion because quaternion norms multiply:

$$
\|q_2q_1\|=\|q_2\|\,\|q_1\|=1.
$$

With this convention, the rightmost factor acts first. Reversing the factors generally changes the result, just as reversing the order of rotation matrices generally changes the final orientation.

The same quaternion algebra maps body components into world components when $q$ represents $\mathbf{R}_{\mathrm{WB}}$. In that use the vector stays fixed and its components change basis; the active-rotation derivation above establishes the matrix action. 
