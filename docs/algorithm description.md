**Input:** $` p_1(t),...,p_n(t), q(t), \lambda(k) `$.

**Output:** $` u(k) `$. // velocity of the sheepdog

1. **Set $` \varpi = 0 `$.**
// set *the number of sheep in sheepfold area variable*
2. **for $` (i = 1, i \leq \underline{N}, i = i + 1) `$ do**
// for *every sheep* do
3. **&ensp; if $` \mathbf{d}(p_i(t), \mathbb{P}_d) = 0 `$ then**
// if *distance between position of $` i `$th sheep at $` t `$th step and the sheepfold area is 0 (sheep is inside the area of sheepfold)* then
4. **&ensp; &ensp; $` \varpi = \varpi + 1 `$**
// *increment $` \varpi `$ variable*
5. **if $` \varpi \lt \underline{N} `$ then**
// if *the number of sheep in sheepfold is less than the number of all sheep* then
6. **&ensp; if $` q(k) \in \mathbb{Q}_l(k) \text{ \& } L_c(k) \gt \theta_t `$ then**
// if *the position of the sheepdog is in $` \mathbb{Q}_l `$ (left) set (all the sheep are on the righthand side) and the variable $` L_c `$ (left) is greater than threshold $` \theta_t `$ angle* then
7. **&ensp; &ensp; $` \lambda(k) = 0 `$**
// *set the flag function indicating the current state of the dog $` \lambda `$ to 0*
8. **&ensp; &ensp; if $` ||q(k) - D_r(k)|| \geq r_a `$ then**
// if *the length of subtraction of the rightmost sheep from the position of the sheepdog (distance between sheepdog and rightmost sheep) is greater or equal to parameter $` r_a `$,* then
9. **&ensp; &ensp; &ensp; $` u(k) = \gamma_a \mathbf{o}(q(k) - D_r(k)) `$**
// *set the velocity of the sheepdog $` u(k) `$ to unit vector of subtraction of the rightmost sheep from the position of the sheepdog, multiplied by parameter $` \gamma_a `$.*
10. **&ensp; &ensp; else**

11. **&ensp; &ensp; &ensp; $` u(k) = \gamma_b \mathbf{R}(\theta_r) \mathbf{o}(q(k) - D_r(k)) `$**
// *set the velocity of the sheepdog $` u(k) `$ to unit vector of subtraction of the rightmost sheep from the position of the sheepdog, multiplied by parameter $` \gamma_b `$ and by rotation matrix using the parameter $` \theta_r `$.*
12. **&ensp; else if $` q(k) \in \mathbb{Q}_r(k) \text{ \& } R_c(k) \gt \theta_t `$ then**
// else if *the position of the sheepdog is in $` \mathbb{Q}_r `$ (right) set (all the sheep are on the lefthand side) and the variable $` R_c `$ (right) is greater than threshold $` \theta_t `$ angle* then
13. **&ensp; &ensp; $` \lambda(k) = 1 `$**
// *set the flag function indicating the current state of the dog $` \lambda `$ to 1*
14. **&ensp; &ensp; if $` ||q(k) - D_l(k)|| \geq r_a `$ then**
// if *the length of subtraction of the leftmost sheep from the position of the sheepdog (distance between sheepdog and leftmost sheep) is greater or equal to parameter $` r_a `$,* then
15. **&ensp; &ensp; &ensp; $` u(k) = \gamma_a \mathbf{o}(q(k) - D_l(k)) `$**
// *set the velocity of the sheepdog $` u(k) `$ to unit vector of subtraction of the leftmost sheep from the position of the sheepdog, multiplied by parameter $` \gamma_a `$.*
16. **&ensp; &ensp; else**

17. **&ensp; &ensp; &ensp; $` u(k) = \gamma_b \mathbf{R}(\theta_l) \mathbf{o}(q(k) - D_l(k)) `$**
// *set the velocity of the sheepdog $` u(k) `$ to unit vector of subtraction of the leftmost sheep from the position of the sheepdog, multiplied by parameter $` \gamma_b `$ and by rotation matrix using the parameter $` \theta_l `$.*
18. **&ensp; else if $` \lambda(k) = 1 `$ then**
// else if *the flag function indicating the current state of the dog $` \lambda `$ is equal to 1* then
19. **&ensp; &ensp; if $` ||q(k) - D_l(k)|| \geq r_a `$ then**
// same as line 14
20. **&ensp; &ensp; &ensp; $` u(k) = \gamma_a \mathbf{o}(q(k) - D_l(k)) `$**
// same as line 15
21. **&ensp; &ensp; else**

22. **&ensp; &ensp; &ensp; $` u(k) = \gamma_b \mathbf{R}(\theta_l) \mathbf{o}(q(k) - D_l(k)) `$**
// same as line 17
23. **&ensp; else**

24. **&ensp; &ensp; if $` ||q(k) - D_r(k)|| \geq r_a `$ then**
// same as line 8
25. **&ensp; &ensp; &ensp; $` u(k) = \gamma_a \mathbf{o}(q(k) - D_r(k)) `$**
// same as line 9
26. **&ensp; &ensp; else**

27. **&ensp; &ensp; &ensp; $` u(k) = \gamma_b \mathbf{R}(\theta_r) \mathbf{o}(q(k) - D_r(k)) `$**
// same as line 11
28. **else**

29. **&ensp; $` u(k) = 0 `$**
// *set the velocity of the dog to 0*
30. **return result**
