# Exact one-use information frontiers

Define (c_r=(dr-1)/(d^2-1)) and (h(t)=((1+t)ln(1+t)+(1-t)ln(1-t))/2). For (1le rle d) and (|	heta|<1), the maxima over all parameter-independent inputs with at most (r)-dimensional reference are

```math
F_r^\star(\theta)=\frac{c_r}{1-\theta^2},\qquad
\sup_\rho D(\mathcal E_\theta(\rho)\Vert\mathcal E_0(\rho))=c_r h(\theta).
```

**Fisher proof.** Convexity reduces the maximum to a pure input of Schmidt rank (qle r), with positive Schmidt weights (lambda_a). Pauli completeness yields (sum_{P
e I}|langle u_a|P|u_bangle|^2=d-delta_{ab}). The SLD quadratic form at zero is

```math
F(0)=\frac{d-1+d\sum_{a\ne b}2\lambda_a\lambda_b/(\lambda_a+\lambda_b)}{M}
\le\frac{dq-1}{M}\le c_r.
```

The first inequality follows from (2xy/(x+y)le(x+y)/2), summing ordered pairs. For nonzero contrast, let (J_A(X)=(AX+XA)/2) on the support, (K=J_sigma^{-1/2}J_BJ_sigma^{-1/2}) and (w=J_sigma^{-1/2}B). The order bound (-sigmale Blesigma) implies (-Ile Kle I). Pairing the two signs gives (langle w,(I-	heta^2K^2)^{-1}wanglelelangle w,wangle/(1-	heta^2)). Sum over (P).

**Relative-entropy proof.** For a pure input write (B_P=sqrt{sigma}Q_Psqrt{sigma}), with (Q_P) the compressed Pauli transpose in the Schmidt support. The Belavkin–Staszewski maximal divergence upper-bounds Umegaki relative entropy, giving

```math
D(\mathcal E_\theta(\rho)\Vert\mathcal E_0(\rho))
\le\frac1M\sum_P\operatorname{Tr}\sigma h(\theta Q_P).
```

The even power series of (h) has positive coefficients, so (h(	heta x)le x^2h(	heta)) for (|x|le1). Pauli twirling gives (sum_P Q_P^2=(dq-1)I_q), hence the bound (c_rh(	heta)). Joint convexity handles mixed inputs. Equality for every integer (r) is proved in [construction](construction.md).

These are exact *one-use* maxima. An arbitrary-(	heta) adaptive Fisher-information equality is not asserted.