**Equations and variables**

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
    * **Footnote: there might be some inconsistencies between distance parameters in the explanation in the article and on the figure 1 in the article!**

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
    
* (16) $` p_i^d(k) = p_i(k) - p_d `$ ... distance between $` i `$th sheep and sheepfold

* (17) $` d(q(0),\mathbb{P}_s(0)) \gt 0 `$ ... initial condition
  * (18) $` \lim\limits_{k \to \infty} d(p_i(k),\mathbb{P}_d) = 0 `$ ... for all $` i \in N `$


**Algorithm**

* (19) $` \underline{ D^{cd}(k) = o(p_d - p_c(k)) } `$ ... direction of the sheep herd (center) based on center of sheepfold
* (19) $` \underline{ D^{qd}(k) = o(p_d - q(k))  } `$ ... direction of the sheepdog based on center of sheepfold 

* (20) $` \underline{ D_r(k) = \{ p_i(k)|i \in \mathbb{V}(k), \forall j \in \mathbb{V}(k), j \neq i, p_j^q(k) \in \mathbb{P}_l(p_i^q(k)) \} } `$ ... the $` i `$th sheep is the rightmost sheep from the view of the sheepdog
  * position of the $` i `$th sheep ($` p_i(k) `$), where the sheep is among visible sheep ($` i \in \mathbb{V}(k) `$) and for every other sheep ($` j `$) among visible sheep ($` \forall j \in \mathbb{V}(k), j \neq i `$), it holds that distances between every other sheep and sheepdog are on the left-hand side area of the distance between $` i `$th sheep and sheepdog ($` p_j^q(k) \in \mathbb{P}_l(p_i^q(k)) `$)

* (21) $` \underline{ D_l(k) = \{ p_i(k)|i \in \mathbb{V}(k), \forall j \in \mathbb{V}(k), j \neq i, p_j^q(k) \in \mathbb{P}_r(p_i^q(k)) \} } `$ ... the $` i `$th sheep is the leftmost sheep from the view of the sheepdog
  * position of the $` i `$th sheep ($` p_i(k) `$), where the sheep is among visible sheep ($` i \in \mathbb{V}(k) `$) and for every other sheep ($` j `$) among visible sheep ($` \forall j \in \mathbb{V}(k), j \neq i `$), it holds that distances between every other sheep and sheepdog are on the right-hand side area of the distance between $` i `$th sheep and sheepdog ($` p_j^q(k) \in \mathbb{P}_r(p_i^q(k)) `$)

* (22) $` \underline{ C_r(k) = \{ p_i(k)|i \in \mathbb{V}(k), \text{ such that, } \forall j \in \mathbb{V}(k), j\neq i, \text{ it follows } p_j^d(k) \in \mathbb{P}_l(p_i^d(k)), ||p_i^d(k)|| \gt ||p_j^d(k)|| \} } `$ ... the $` i `$th sheep is the rightmost sheep from the view of the sheepfold
  * position of the $` i `$th sheep ($` p_i(k) `$), where the sheep is among visible sheep ($` i \in \mathbb{V}(k) `$), such that for every other sheep ($` j `$) among visible sheep ($` \forall j \in \mathbb{V}(k), j \neq i `$), it follows that distances between every other sheep and sheepfold are on the left-hand side area of the distance between $` i `$th sheep and sheepfold ($` p_j^q(k) \in \mathbb{P}_l(p_i^q(k)) `$) and that length of the distance between $` i `$th sheep and sheepfold is greater than lengths of the distances between every other sheep and sheepfold ($` ||p_i^d(k)|| \gt ||p_j^d(k)|| `$)

* (23) $` \underline{ C_l(k) = \{ p_i(k)|i \in \mathbb{V}(k), \text{ such that, } \forall j \in \mathbb{V}(k), j\neq i, \text{ it follows } p_j^d(k) \in \mathbb{P}_r(p_i^d(k)), ||p_i^d(k)|| \gt ||p_j^d(k)|| \} } `$ ... the $` i `$th sheep is the leftmost sheep from the view of the sheepfold
  * position of the $` i `$th sheep ($` p_i(k) `$), where the sheep is among visible sheep ($` i \in \mathbb{V}(k) `$), such that for every other sheep ($` j `$) among visible sheep ($` \forall j \in \mathbb{V}(k), j \neq i `$), it follows that distances between every other sheep and sheepfold are on the right-hand side area of the distance between $` i `$th sheep and sheepfold ($` p_j^q(k) \in \mathbb{P}_r(p_i^q(k)) `$) and that length of the distance between $` i `$th sheep and sheepfold is greater than lengths of the distances between every other sheep and sheepfold ($` ||p_i^d(k)|| \gt ||p_j^d(k)|| `$)
 
* (24) $` \underline{ \mathbb{Q}_l(k) = \{ x \in \mathbb{R}^{2}|p_i(k) \in \mathbb{S}_r(p_d - x) \} } `$
* (24) $` \underline{ \mathbb{Q}_r(k) = \{ x \in \mathbb{R}^{2}|p_i(k) \in \mathbb{S}_l(p_d - x) \} } `$
  * if $` q(k) \in \mathbb{Q}_l(k) `$ then all the sheep are on the right-hand side of $` D^{qd}(k) `$
  * if $` q(k) \in \mathbb{Q}_r(k) `$ then all the sheep are on the left-hand side of $` D^{qd}(k) `$

* (25) $` \underline{ R_c(k) = \frac{\langle D^{cd}(k), q(k) - C_r(k) \rangle}{||D^{cd}(k)||*||q(k) - C_r(k)||} } `$
  * $` \langle D^{cd}(k), q(k) - C_r(k) \rangle `$ ... inner product or dot product of vectors $` D^{cd}(k) `$ and $` q(k) - C_r(k) `$
  * $` \theta_t `$ positive threshold for $` R_c(k) `$
  
* (26) $` \underline{ L_c(k) = \frac{\langle D^{cd}(k), q(k) - C_l(k) \rangle}{||D^{cd}(k)||*||q(k) - C_l(k)||} } `$
  * $` \langle D^{cd}(k), q(k) - C_l(k) \rangle `$ ... inner product or dot product of vectors $` D^{cd}(k) `$ and $` q(k) - C_l(k) `$
  * $` \theta_t `$ positive threshold for $` L_c(k) `$

* $` \underline{ \lambda(k) } `$ ... flag function indication the current state of the sheepdog

* $` \underline{\textit{K}} `$ ... upper time limit


**Algorithm parameters defined by user**

* $` p_d `$ -> position of sheepfold
* $` \rho_o `$ -> radius of sheepfold
* $` q(0) `$ -> starting position of sheepdog
* $` \rho_n `$ -> radius of sheepdog
* $` N `$ -> number of sheep
* $` p_1(0)\text{, ..., }p_N(0) `$ -> starting positions of sheep
* $` \rho_s `$ -> radius of sheep
* $` a_i `$ -> parameter used in equation (8)
* $` \omega_i `$ -> parameter used in equation (8)
* $` \alpha `$ -> gain parameter used in equation (10a)
* $` \beta `$ -> gain parameter used in equation (10b)
* $` \gamma `$ -> gain parameter used in equation (10b)
* $` \rho_r `$ -> distance parameter used in equation (10b)
* $` \rho_g `$ -> distance parameter used in equation (10b)
* $` \rho_d `$ -> distance parameter used in equation (10b)
* $` \theta_t `$ -> threshold parameter used for equations (25) and (26) (design parameter in initialization)
* $` \theta_l `$ -> parameter in algorithm (design parameter in initialization)
* $` \theta_r `$ -> parameter in algorithm (design parameter in initialization)
* $` r_a `$ -> parameter in algorithm (design parameter in initialization)
* $` \gamma_a `$ -> parameter in algorithm (design parameter in initialization)
* $` \gamma_b `$ -> parameter in algorithm (design parameter in initialization)
