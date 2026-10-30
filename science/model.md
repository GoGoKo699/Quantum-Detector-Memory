# Model and exact resource contract

Let (d=2^n), (M=d^2-1), and let (mathcal P_n^circ) be the (M) nonidentity Hermitian Pauli representatives. The destructive detector has classical output ((P,s)), with (sin{-1,+1}), and effects

```math
E_{P,s}(	heta)=\frac{I+s\theta P}{2M},\qquad |\theta|<1.
```

The detector selects (P) independently on every call and reports its identity **after** the input has been supplied. The input is consumed. The only unknown is the common scalar (	heta). Arbitrary parameter-independent adaptive controls and unlimited classical history are allowed. At every invocation all coherent registers outside the queried (n)-qubit input have combined dimension at most (r), (1le rle d); future prepared probes and retained purifications are not free. Independent device calls, ideal probe preparation and reference readout are assumed. Query complexity is not hardware gate cost.

For input (ho_{SR}), write (sigma=operatorname{Tr}_Sho) and (B_P=operatorname{Tr}_S[(Potimes I)ho]). The post-measurement classical-quantum blocks are ((sigma+s	heta B_P)/(2M)). Positivity gives (-sigmale B_Plesigma).

The central results are the exact one-use Fisher-information frontier, an exact relative-entropy frontier against (	heta=0), and a global adaptive minimax scaling law. Read [information bounds](information.md), [adaptive converse](adaptive.md), [construction](construction.md), and [interpretation](interpretation.md).