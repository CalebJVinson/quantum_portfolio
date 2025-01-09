# Quantum Portfolio

The origin of this project was extension on a project in a senior physics course *PHYS 4315: Introduction to Quantum Computing*, which is crosslisted as a masters course in electrical engineering *ECE 5332: Special Topics in Electrical Engineering*. The majority of the background and coursework was from the text ***Introduction to Classical and Quantum Computing*** by Thomas G. Wong. The text explores creation of 

\begin{tikzpicture}[thick]
    % `operator' will only be used by Hadamard (H) gates here.
    % `phase' is used for controlled phase gates (dots).
    % `surround' is used for the background box.
    \tikzstyle{operator} = [draw,fill=white,minimum size=1.5em] 
    \tikzstyle{phase} = [draw,fill,shape=circle,minimum size=5pt,inner sep=0pt]
    \tikzstyle{surround} = [fill=blue!10,thick,draw=black,rounded corners=2mm]
    %
    \matrix[row sep=0.4cm, column sep=0.8cm] (circuit) {
    % First row.
    \node (q1) {\ket{0}}; &[-0.5cm] 
    \node[operator] (H11) {H}; &
    \node[phase] (P12) {}; &
    \node[phase] (P13) {}; &
    &[-0.3cm]
    \coordinate (end1); \\
    % Second row.
    \node (q2) {\ket{0}}; &
    \node[operator] (H21) {H}; &
    \node[phase] (P22) {}; &
    &
    \node[operator] (H24) {H}; &
    \coordinate (end2);\\
    % Third row.
    \node (q3) {\ket{0}}; &
    \node[operator] (H31) {H}; &
    &
    \node[phase] (P33) {}; &
    \node[operator] (H34) {H}; &
    \coordinate (end3); \\
    };
    % Draw bracket on right with resultant state.
    \draw[decorate,decoration={brace},thick]
        ($(circuit.north east)-(0cm,0.3cm)$)
        to node[midway,right] (bracket) {$\displaystyle\frac{\ket{000}+\ket{111}}{\sqrt{2}}$}
        ($(circuit.south east)+(0cm,0.3cm)$);
    \begin{pgfonlayer}{background}
        % Draw background box.
        \node[surround] (background) [fit = (q1) (H31) (bracket)] {};
        % Draw lines.
        \draw[thick] (q1) -- (end1)  (q2) -- (end2) (q3) -- (end3) (P12) -- (P22) (P13) -- (P33);
    \end{pgfonlayer}
    %
    \end{tikzpicture}
