# Adaptive converse and global risk

For arbitrary two input states (ho,eta), let (mathcal E_	heta) denote the detector acting on the queried system while retaining the bounded reference. At the null parameter, (mathcal E_0(eta)=u_Xotimeseta_R), where (u_X) is uniform on all (2M) detector outcomes. The product-reference chain rule gives

```math
D(\mathcal E_\theta(\rho)\Vert\mathcal E_0(\eta))
=D(\mathcal E_\theta(\rho)\Vert\mathcal E_0(\rho))
+D(\rho_R\Vert\eta_R)
\le c_rh(\theta)+D(\rho\Vert\eta).
```

The last step uses the one-use bound and partial-trace data processing. For classical adaptive histories, the classical-quantum chain rule averages the same bound branchwise. Intermediate parameter-independent instruments cannot increase divergence. Telescoping therefore proves, for any at-most-(N)-call adaptive protocol,

```math
D(\omega_\theta^{(N)}\Vert\omega_0^{(N)})\le Nc_rh(\theta).
```

The statement allows coherent reuse and feedback; every coherent side system present at each call is counted. At (	heta=0), the SLD quadratic form also splits into the inherited memory derivative and the sign-odd detector derivative; the cross terms cancel between (s=pm1). Hence (F_{m out}(0)le F_{m in}(0)+c_r) and (F_{m final}(0)le Nc_r), with equality for the independent construction.

Fix (0<a<1). Since (h(	heta)=Theta_a(	heta^2)) on ([-a,a]), testing zero against (delta=min(a,gamma/sqrt{Nc_r})), with sufficiently small absolute (gamma), and applying Pinsker plus Le Cam yields the lower bound

```math
\inf_{\widehat\theta}\sup_{|\theta|\le a}
\mathbb E_\theta(\widehat\theta-\theta)^2
=\Omega_a\bigl(\min\{1,(Nc_r)^{-1}\}\bigr).
```

The flagged-coin estimator from [construction](construction.md) has variance at most (1/(Nc_r)), and the constant estimator zero handles (Nc_rll1). This matches the lower bound up to constants. For (r=2^k), (c_r=(2^{n+k}-1)/(2^{2n}-1)=Theta(2^{k-n})), giving RMS accuracy query complexity (Theta(2^{n-k}epsilon^{-2})) in the small-error regime.

This is a minimax *order*, not an exact finite-sample risk or an arbitrary-contrast adaptive Fisher optimum.