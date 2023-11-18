Input: p1(t),...,pn(t), q(t), λ(k).

Output: u(k). // velocity of the sheepdog

1. Set $` \varpi = 0 `$.
//
2. for $` (i = 1, i \leq \underline{N}, i = i + 1) `$ do
// for *every sheep* do
3. &ensp; if $` \mathbf{d}(p_i(t), \mathbb{P}_d) = 0 `$ then
//
4. &ensp; &ensp; $` \varpi = \varpi + 1 `$
//
5. if $` \varpi \lt \underline{N} `$ then
//
6. &ensp; if $` q(k) \in \mathbb{Q}_l(k) \text{ \& } L_c(k) \gt \theta_t `$ then
//
7. &ensp; &ensp; $` \lambda(k) = 0 `$
//
8. &ensp; &ensp; if $` ||q(k) - D_r(k)|| \geq r_a `$ then
//
9. &ensp; &ensp; &ensp; $` u(k) = \gamma_a \mathbf{o}(q(k) - D_r(k)) `$
//
10. &ensp; &ensp; else
//
11. &ensp; &ensp; &ensp; $` u(k) = \gamma_b \mathbf{R}(\theta_r) \mathbf{o}(q(k) - D_r(k)) `$
//
12. &ensp; else if $` q(k) \in \mathbb{Q}_r(k) \text{ \& } R_c(k) \gt \theta_t `$
//
13. &ensp; &ensp; $` \lambda(k) = 1 `$
//
14. &ensp; &ensp; if $` ||q(k) - D_l(k)|| \geq r_a `$ then
//
15. &ensp; &ensp; &ensp; $` u(k) = \gamma_a \mathbf{o}(q(k) - D_l(k)) `$
//
16. &ensp; &ensp; else
//
17. &ensp; &ensp; &ensp; $` u(k) = \gamma_b \mathbf{R}(\theta_l) \mathbf{o}(q(k) - D_l(k)) `$
//
18. &ensp; else if $` \lambda(k) = 1 `$ then
//
19. &ensp; &ensp; if $` ||q(k) - D_l(k)|| \geq r_a `$ then
//
20. &ensp; &ensp; &ensp; $` u(k) = \gamma_a \mathbf{o}(q(k) - D_l(k)) `$
//
21. &ensp; &ensp; else
//
22. &ensp; &ensp; &ensp; $` u(k) = \gamma_b \mathbf{R}(\theta_l) \mathbf{o}(q(k) - D_l(k)) `$
//
23. &ensp; else
//
24. &ensp; &ensp; if $` ||q(k) - D_r(k)|| \geq r_a `$ then
//
25. &ensp; &ensp; &ensp; $` u(k) = \gamma_a \mathbf{o}(q(k) - D_r(k)) `$
//
26. &ensp; &ensp; else
//
27. &ensp; &ensp; &ensp; $` u(k) = \gamma_b \mathbf{R}(\theta_r) \mathbf{o}(q(k) - D_r(k)) `$
//
28. else
//
29. &ensp; $` u(k) = 0 `$
//
30. return result
