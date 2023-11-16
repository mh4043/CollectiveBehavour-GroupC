* $` \underline{ x \in \mathbb{R}^{2} } `$ ... nonzero vector

* $` \underline{ o(x) = \frac{x}{||x||} } `$ ... unit vector with same orientation as $` x `$

* $` \underline{ R(\theta) = \begin{bmatrix} cos(\theta) & -sin(\theta) \\ sin(\theta) & cos(\theta) \end{bmatrix} } `$ ... rotation matrix for the angle $` \theta `$

* (2) $` \underline{ \mathbb{P}_l(x) = \{y \in \mathbb{R}^{2}|\theta \in (0,\pi) \text{, so that, } o(y) = R(\theta)*o(x)\} } `$ ... left-hand side area of $` x `$ (vectors $y$ for which there exists a $\theta$, so that $` o(y) = R(\theta)*o(x) `$)

* (3) $` \underline{ \mathbb{P}_r(x) = \{y \in \mathbb{R}^{2}|\theta \in (-\pi,0) \text{, so that, } o(y) = R(\theta)*o(x)\} } `$ ... right-hand side area of $` x `$ (vectors $y$ for which there exists a $\theta$, so that $` o(y) = R(\theta)*o(x) `$)

* $` \underline{ C(\mathbb{P}) } `$ ... cardinality of set $\mathbb{P}$ (number of elements)

* $` \underline{ N } `$ ... number of sheep

* $` \underline{ i \in N } `$ ... $` i `$th sheep

* (4) $` \underline{ p_i(k + 1) = p_i(k) + T*v_i(k) } `$ ... motion of the $` i `$th sheep (next position) at next step
  * $` k `$ ... step
  * $` T `$ ... sampling period
  * $` p_i(k) \in \mathbb{R}^{2} `$ ... position of the $` i `$th sheep at $` k `$th step
  * $` v_i(k) \in \mathbb{R}^{2} `$ ... velocity of the $` i `$th sheep at $` k `$th step

* (5) $` \underline{ q(k + 1) = q(k) + T*u(k) } `$ ... motion of the sheepdog (next position) at next step
  * $` k `$ ... step
  * $` T `$ ... sampling period
  * $` q(k) \in \mathbb{R}^{2} `$ ... position of the sheepdog at $` k `$th step
  * $` u(k) \in \mathbb{R}^{2} `$ ... velocity of the sheepdog at $` k `$th step

* (6) $` \underline{ p_i^q(k) = p_i(k) - q(k) } `$ ... distance between $` i `$th sheep and sheepdog

* (7) $` \underline{ v_i(k) = v_{di}(k) + R(\theta_i(k))*v_{si}(k) } `$ ... velocity of $` i `$th sheep divided into two parts
  * (8) $` \underline{ \theta_i(k) = a_i * \frac{\pi}{180} * sin(\omega_i*k*T) } `$
    * $`a_i`$ ... parameter
    * $` w_i `$ ... parameter
  * (9a) $` \underline{ v_{di} = \varphi(||p_i^q(k)||)*o(p_i^q(k)) } `$ ... reaction to the dog ($` ||p_i^q(k)|| `$ is the length of vector $` p_i^q(k) `$)
  * (9b) $` \underline{ v_{si} = \sum\limits_{\substack{j = 1 \\ j \neq i}}^N \psi(||p_i(k) - p_j(k)||) * o(p_i(k) - p_j(k)) } `$
  * (10a) $` \varphi(x) =
               \begin{cases}
                 \alpha(\frac{1}{x} - \frac{1}{\rho_n}), & 0 \lt x \leq \rho_n \\
                 0, & x \gt \rho_n
               \end{cases} `$
  * (10b) $` \psi(x) =
               \begin{cases}
                 \beta(\frac{1}{x-\rho_s} - \frac{1}{\rho_r-\rho_s}), & \rho_s \lt x \leq \rho_r \\
                 0, & \rho_r \lt x \leq \rho_g \\
                 \gamma(x - \rho_g), & \rho_g \lt x \leq \rho_d \\
                 0, & x \gt \rho_d
               \end{cases} `$
    * $` \alpha, \beta \gt 0, \gamma \lt 0 `$ ... gains
    * $` \rho_n, \rho_r, \rho_g, \rho_d \gt 0 `$ ... distance parameters (radius from center of an entity, user defined)
    * **Footnote: there are some inconsistencies between distance parameters in the explanation in the article and on the figure 1 in the article!**

* if $` \underline{ o(p_i^q(k)) = o(p_j^q(k)) } `$ and $` \underline{ ||p_j^q(k)|| \lt ||p_i^q(k)|| } `$ ... then $` i `$th sheep is *vision-blocked* by $` j `$th sheep from viewpoint of sheepdog. Otherwise it is *non vision-blocked*
  * $` i, j \in N, i \neq j `$

* if sheep *non vision-blocked* and $` \underline{ ||p_i^q(k)|| \leq \rho_v } `$ ... then it is *visible* to the sheepdog. Otherwise it is *in-visible*
  * $` \rho_v `$ .. vision radius of sheepdog

* (11) $` \underline{ \Lambda_i(t) =
           \begin{cases}
             1, & \text{the }i\text{th sheep is }\textit{visible}\text{ to the sheepdog} \\
             0, & \text{the }i\text{th sheep is }\textit{invisible}\text{ to the sheepdog}
           \end{cases} } `$

* (12) $` \underline{ \mathbb{V}(k) = \{i|i \in N, \Lambda_i(k) = 1\} } `$ ... set of visible sheep for the sheepdog

* (13) $` \underline{ p_c(k) = \frac{\sum\limits_{\substack{i \in \mathbb{V}(k)}} p_i(k)}{C(\mathbb{V}(k))} } `$ ... estimated center of sheep herd (sum of positions of sheep from the set of visible sheep $` \mathbb{V}(k) `$ divided by the number of all sheep in the set of visible sheep $` C(\mathbb{V}(k)) `$)
  * $` C(\mathbb{V}(k)) \gt 0 `$
 
* (14) $` \underline{ \mathbb{P}_s(k) = \{ p(k)|p(k) \in \mathbb{R}^{2}, p(k) = \sum\limits_{\substack{i = 1}}^N \gamma_ip_i(k), 0 \leq \gamma_i \leq 1, \sum\limits_{\substack{i = 1}}^N \gamma_i = 1 \} } `$ ... the sheep herd polygon
  * $` \gamma_i `$ ... parameter, user defined

* (15) $` \underline{ \mathbb{P}_d = \{ p|p \in \mathbb{R}^{2}, ||p-p_d|| \leq \rho_o \} } `$ ... definition of sheepfold
  * $` p_d \in \mathbb{R}^{2} `$
  * $` \rho_o \gt 0 `$ ... parameter, user defined
