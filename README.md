# Quantum Portfolio

The origin of this project was extension on a project in a senior physics course *PHYS 4315: Introduction to Quantum Computing*, which is crosslisted as a masters course in electrical engineering *ECE 5332: Special Topics in Electrical Engineering*. The majority of the background and coursework was from the text ***Introduction to Classical and Quantum Computing*** by Thomas G. Wong. The text explores creation of 

$$
\begin{aligned}
|q_0\rangle &\ \xrightarrow{\ H\ }\ \frac{|0\rangle + |1\rangle}{\sqrt{2}} \\
|q_1\rangle &\ \xrightarrow{\text{CNOT}}\ \frac{|00\rangle + |11\rangle}{\sqrt{2}}
\end{aligned}
$$

$$
\Qcircuit @C=1em @R=1em {
    \lstick{|q_0\rangle} & \gate{H} & \ctrl{1} & \qw \\
    \lstick{|q_1\rangle} & \qw      & \targ    & \qw
}
$$
