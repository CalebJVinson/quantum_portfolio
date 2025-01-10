# Quantum Portfolio

The origin of this project was extension on a project in a senior physics course *PHYS 4315: Introduction to Quantum Computing*, which is crosslisted as a masters course in electrical engineering *ECE 5332: Special Topics in Electrical Engineering*. The majority of the background and coursework was from the text ***Introduction to Classical and Quantum Computing*** by Thomas G. Wong. The text explores classical computing and its quantum counterparts. This leads into the eventual work of Nielsen and Chuang's ***Quantum Computation and Quantum Information***, which we covered sections of along with some of Schrödinger's equation for algorithmic preparation.

This is a brief overview of differences in the classical and quantum, listed from Wong's text.

| Concept                  | Classical               | Quantum                |
|--------------------------|-------------------------|------------------------|
| Fundamental Unit         | Bit                    | Qubit                 |
| Gates                   | Logic Gates            | Unitary Gates          |
| Gates Reversible         | Sometimes              | Always                 |
| Universal Gate Set       | NAND                 | H, T, CNOT           |
| Programming Language     | Verilog                | OpenQASM               |
| Algebra                  | Boolean                | Linear                 |
| Error Correcting Code    | Repetition Code        | Shor Code              |
| Complexity Class         | P                      | BQP                    |
| Strong Church-Turing Thesis | Supports           | Possibly Violates       |

# Quantum Approximate Optimization Algorithm

## Solving a Network

The way I understood this to work was to consider nodes as representing each asset in a set, where the edges could represent items from covariance to high-correlation or other ways assets may be connected. The QAOA is best in this case as we can then consider a MaxCut problem, which I primarily referenced from [here](https://www.mustythoughts.com/quantum-approximate-optimization-algorithm-explained).

The interesting start to QAOA is with a utility or cost function represented by a Hamiltonian matrix. From this we initiate a second Hamiltonian that can operate as the "exploration" figure on the cost function.
In the standard version of these, we have two angles which we are trying to determine to produce the eventual solution. We can call the former an $H_0$ and the latter $H_E$.

For this set up we use Dirac notation starting with an initial state, usually $|0...0 \rangle$ which we define for the initial state $|s \rangle$. Considering the angles, $\beta, \text{ and } \gamma$, we form the state:

$$|\beta_p, \gamma_p \rangle = U(H_E, \beta_p) U(H_0, \gamma_p) ... U(H_E, \beta_1) U(H_0, \gamma_1) | s \rangle $$

where p is the number of steps taken in revaluating the maesured solution and performing
# Future Interests: Quantum Coins & Quantum Walks
