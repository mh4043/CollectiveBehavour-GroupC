* \$` x \in \mathbb{R}^{2} `$ ... nonzero vector

* $` o(x) = \frac{x}{||x||} `$ ... unit vector with same orientation as $` x `$

* $` R(\theta) = \begin{bmatrix} cos(\theta) & -sin(\theta) \\ sin(\theta) & cos(\theta) \end{bmatrix} `$ ... rotation matrix for the angle $` \theta `$

* (2) $` \mathbb{P}_l(x) = \{y \in \mathbb{R}^{2}|\theta \in (0,\pi) \text{, so that, } o(y) = R(\theta)*o(x)\} `$ ... left-hand side area of $` x `$ (vectors $y$ for which there exists a $\theta$, so that $` o(y) = R(\theta)*o(x) `$)

* (3) $` \mathbb{P}_r(x) = \{y \in \mathbb{R}^{2}|\theta \in (-\pi,0) \text{, so that, } o(y) = R(\theta)*o(x)\} `$ ... right-hand side area of $` x `$ (vectors $y$ for which there exists a $\theta$, so that $` o(y) = R(\theta)*o(x) `$)

* $` C(\mathbb{P}) `$ ... cardinality of set $\mathbb{P}$ (number of elements)

* $` N `$ ... number of sheep

* $` i \in N `$ ... $` i `$th sheep

* (4) $` p_i(k + 1) = p_i(k) + T*v_i(k) `$ ... motion of the $` i `$th sheep (next position) at next step
  * $` k `$ ... step
  * $` T `$ ... sampling period
  * $` p_i(k) \in \mathbb{R}^{2} `$ ... position of the $` i `$th sheep at $` k `$th step
  * $` v_i(k) \in \mathbb{R}^{2} `$ ... velocity of the $` i `$th sheep at $` k `$th step

* (5) $` q(k + 1) = q(k) + T*u(k) `$ ... motion of the sheepdog (next position) at next step
  * $` k `$ ... step
  * $` T `$ ... sampling period
  * $` q(k) \in \mathbb{R}^{2} `$ ... position of the sheepdog at $` k `$th step
  * $` u(k) \in \mathbb{R}^{2} `$ ... velocity of the sheepdog at $` k `$th step

* (6) $` p_i^q(k) = p_i(k) - q(k) `$ ... distance between $` i `$th sheep and sheepdog

*  
