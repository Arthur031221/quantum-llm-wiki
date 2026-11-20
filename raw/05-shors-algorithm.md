---
title: Shor's algorithm
url: https://en.wikipedia.org/wiki/Shor%27s_algorithm
revision: 1384103273 (2026-11-06T16:24:40Z)
fetched: 2026-11-20
license: CC BY-SA 4.0 (Wikipedia contributors)
---

Shor's algorithm is a quantum algorithm for finding the prime factors of an integer. It was developed in 1994 by the American mathematician Peter Shor. It is one of the few known quantum algorithms with compelling potential applications and strong evidence of superpolynomial speedup compared to best known classical (non-quantum) algorithms. However, beating classical computers may require quantum computers with millions of qubits due to the overhead caused by quantum error correction.
Shor proposed multiple similar algorithms for solving the factoring problem, the discrete logarithm problem, and the period-finding problem. "Shor's algorithm" usually refers to the factoring algorithm, but may refer to any of the three algorithms. The discrete logarithm algorithm and the factoring algorithm are instances of the period-finding algorithm, and all three are instances of the hidden subgroup problem.
On a quantum computer, to factor an integer n, Shor's algorithm runs in polynomial time, meaning the time taken is polynomial in log⁡n. It takes quantum gates of order O((log⁡n)2(log⁡log⁡n)(log⁡log⁡log⁡n)) using fast multiplication, or even O((log⁡n)2(log⁡log⁡n)) using the asymptotically fastest multiplication algorithm currently known due to Harvey and van der Hoeven, thus demonstrating that the integer factorization problem is in complexity class BQP. Shor's algorithm is asymptotically faster than the most scalable classical factoring algorithm, the general number field sieve, which works in sub-exponential time.


== Feasibility and implications ==

Assuming a quantum computer with a sufficient number of qubits could operate without succumbing to quantum noise and other quantum-decoherence phenomena, then Shor's algorithm could be used to break public-key cryptography schemes, such as

The RSA scheme
The finite-field Diffie–Hellman key exchange
The elliptic-curve Diffie–Hellman key exchange
RSA can be broken if factoring large integers is computationally feasible. As far as is known, this is not possible using classical (non-quantum) computers; no classical algorithm is known that can factor integers in polynomial time. However, Shor's algorithm shows that factoring integers can be done with a polynomial complexity circuit on an ideal quantum computer. Thus, it might be feasible to defeat RSA by constructing a large enough quantum computer. This was a powerful motivator for the design and construction of quantum computers, and for the study of new quantum-computer algorithms. It has also facilitated research on new cryptosystems that are secure from quantum computers, collectively called post-quantum cryptography (PQC).


=== Physical implementation ===
As of 2026, the high error rates of quantum computers and limited number of physical qubits available for quantum error correction, laboratory demonstrations of Shor's algorithm obtain correct results in only a fraction of attempts, and have only succeeded with small semiprimes.
In 2001, Shor's algorithm was demonstrated by a group at IBM, who factored 15 into 3×5, using an NMR implementation of a quantum computer with seven qubits. After IBM's implementation, two independent groups implemented Shor's algorithm using photonic qubits. In 2012, the factorization of 15 was performed with solid-state qubits. Later, in 2012, the factorization of 21 was achieved. In 2016, the factorization of 15 was performed again using trapped-ion qubits. However, none of these demonstrations fulfill the requirements of Shor’s algorithm: they compile the circuit using prior knowledge of the solution, and some have even oversimplified the algorithm in a way that makes it equivalent to coin flipping.


== Algorithm ==
The problem that we are trying to solve is: given an odd composite number N, find its integer factors.
To achieve this, Shor's algorithm consists of two parts:

A classical reduction of the factoring problem to the problem of order-finding. This reduction is similar to that used for other factoring algorithms, such as the quadratic sieve.
A quantum algorithm to solve the order-finding problem.


=== Classical reduction ===
A complete factoring algorithm is possible if we're able to efficiently factor arbitrary N into just two integers p and q greater than 1, since if either p or q are not prime, then the factoring algorithm can in turn be run on those until only primes remain.
A basic observation is that, using Euclid's algorithm, we can always compute the GCD between two integers efficiently. In particular, this means we can check efficiently whether N is even, in which case 2 is trivially a factor. Let us thus assume that N is odd for the remainder of this discussion. Afterwards, we can use efficient classical algorithms to check whether N is a prime power. For prime powers, efficient classical factorization algorithms exist, hence the rest of the quantum algorithm may assume that N is not a prime power.
If those easy cases do not produce a nontrivial factor of N, the algorithm proceeds to handle the remaining case. We pick a random integer 2≤a<N. A possible nontrivial divisor of N can be found by computing gcd⁡(a,N), which can be done classically and efficiently using the Euclidean algorithm. If this produces a nontrivial factor (meaning gcd⁡(a,N)≠1), the algorithm is finished, and the other nontrivial factor is N/gcd⁡(a,N). If a nontrivial factor was not identified, then this means that N and the choice of a are coprime, so a is contained in the multiplicative group of integers modulo N, having a multiplicative inverse modulo N. Thus, a has a multiplicative order r modulo N, meaning

ar≡1modN,
and r is the smallest positive integer satisfying this congruence.
The quantum subroutine finds r. It can be seen from the congruence that N divides ar−1, written N∣ar−1. This can be factored using difference of squares:N∣(ar/2−1)(ar/2+1).Since we have factored the expression in this way, the algorithm doesn't work for odd r (because ar/2 must be an integer), meaning that the algorithm would have to restart with a new a. Hereafter we can therefore assume that r is even. It cannot be the case that N∣ar/2−1, since this would imply ar/2≡1modN, which would contradictorily imply that r/2 would be the order of a, which was already r. At this point, it may or may not be the case that N∣ar/2+1. If N does not divide ar/2+1, then this means that we are able to find a nontrivial factor of N. We computed=gcd⁡(N,ar/2−1).If d=1, then N∣ar/2+1 was true, and a nontrivial factor of N cannot be achieved from a, and the algorithm must restart with a new a. Otherwise, we have found a nontrivial factor of N, with the other being N/d, and the algorithm is finished. For this step, it is also equivalent to compute gcd⁡(N,ar/2+1); it will produce a nontrivial factor if gcd⁡(N,ar/2−1) is nontrivial, and will not if it's trivial (where N∣ar/2+1).
The algorithm restated shortly follows: let N be odd, and not a prime power. We want to output two nontrivial factors of N.

Pick a random number 1<a<N.
Compute K=gcd⁡(a,N), the greatest common divisor of a and N.
If K≠1, then K is a nontrivial factor of N, with the other factor being N/K, and we are done.
Otherwise, use the quantum subroutine to find the order r of a.
If r is odd, then go back to step 1.
Compute g=gcd⁡(N,ar/2+1). If g is nontrivial, the other factor is N/g, and we're done. Otherwise, go back to step 1.
It has been shown that this will be likely to succeed after a few runs. In practice, a single call to the quantum order-finding subroutine is enough to completely factor N with very high probability of success if one uses a more advanced reduction.


=== Quantum order-finding subroutine ===
The goal of the quantum subroutine of Shor's algorithm is, given coprime integers N and 1<a<N, to find the order r of a modulo N, the smallest positive integer r such that ar≡1(modN). To achieve this, Shor's algorithm uses a quantum circuit involving two registers. The second register uses n qubits, where n is the smallest integer such that N≤2n, i.e., n=⌈log2N⌉. The size of the first register determines how accurate an approximation the circuit produces. It can be shown that using 2n qubits gives sufficient accuracy to find r. The exact quantum circuit depends on the parameters a and N, which define the problem. The following description of the algorithm uses bra–ket notation to denote quantum states, and ⊗ to denote the tensor product.
The algorithm consists of two main steps:

Use quantum phase estimation with unitary matrix U representing the operation of multiplying by a (modulo N), and input state |0⟩⊗2n⊗|1⟩ (where the second register is |1⟩ made from n qubits). The eigenvalues of this U encode information about the period, and |1⟩ can be seen to be writable as a sum of its eigenvectors. Thanks to these properties, the quantum phase estimation stage gives as output a random integer of the form jr22n for random j=0,1,...,r−1.
Use the continued fractions algorithm to extract the period r from the measurement outcomes obtained in the previous stage. This is a procedure to post-process (with a classical computer) the measurement data obtained from measuring the output quantum states, and retrieve the period.
The connection with quantum phase estimation was not discussed in the original formulation of Shor's algorithm, but was later proposed by Alexei Kitaev.


==== Quantum phase estimation ====

In general the quantum phase estimation algorithm, for any unitary U and eigenstate |ψ⟩ such that U|ψ⟩=e2πiθ|ψ⟩, sends input states |0⟩|ψ⟩ to output states close to |ϕ⟩|ψ⟩, where ϕ is a superposition of integers close to 22nθ. In other words, it sends each eigenstate |ψj⟩ of U to a state containing information close to the associated eigenvalue. For the purposes of quantum order-finding, we employ this strategy using the unitary defined by the action
U|k⟩={|ak(modN)⟩0≤k<N,|k⟩N≤k<2n.
The action of U on states |k⟩ with N≤k<2n is not crucial to the functioning of the algorithm, but needs to be included to ensure that the overall transformation is a well-defined quantum gate. Implementing the circuit for quantum phase estimation with U requires being able to efficiently implement the gates U2j. This can be accomplished via modular exponentiation, which is the slowest part of the algorithm.
The gate thus defined satisfies Ur=I, which immediately implies that its eigenvalues are the r-th roots of unity ωrk=e2πik/r. Furthermore, each eigenvalue ωrj has an eigenvector of the form |ψj⟩=r−1/2∑k=0r−1ωr−kj|ak⟩, and these eigenvectors are such that
1r∑j=0r−1|ψj⟩=1r∑j=0r−1∑k=0r−1ωrjk|ak⟩=|1⟩+1r∑k=1r−1(∑j=0r−1ωrjk)|ak⟩=|1⟩,
where the last identity follows from the geometric series formula, which implies ∑j=0r−1ωrjk=0.
Using quantum phase estimation on an input state |0⟩⊗2n|ψj⟩ would then return the integer 22nj/r with high probability. More precisely, the quantum phase estimation circuit sends |0⟩⊗2n|ψj⟩ to |ϕj⟩|ψj⟩ such that the resulting probability distribution pk≡|⟨k|ϕj⟩|2 is peaked around k=22nj/r, with p22nj/r≥4/π2≈0.4053. This probability can be made arbitrarily close to 1 using extra qubits.
Applying the above reasoning to the input |0⟩⊗2n|1⟩, quantum phase estimation thus results in the evolution|0⟩⊗2n|1⟩=1r∑j=0r−1|0⟩⊗2n|ψj⟩→1r∑j=0r−1|ϕj⟩|ψj⟩.Measuring the first register, we now have a balanced probability 1/r to find each |ϕj⟩, each one giving an integer approximation to 22nj/r, which can be divided by 22n to get a decimal approximation for j/r.


==== Continued-fraction algorithm to retrieve the period ====
Then, we apply the continued-fraction algorithm to find integers b and c, where b/c gives the best fraction approximation for the approximation measured from the circuit, for b,c<N and coprime b and c. The number of qubits in the first register, 2n, which determines the accuracy of the approximation, guarantees thatbc=jr,
given the best approximation from the superposition of |ϕj⟩ was measured (which can be made arbitrarily likely by using extra bits and truncating the output). However, while b and c are coprime, it may be the case that j and r are not coprime. Because of that, b and c may have lost some factors that were in j and r. This can be remedied by rerunning the quantum order-finding subroutine an arbitrary number of times, to produce a list of fraction approximationsb1c1,b2c2,…,bscs,where s is the number of times the subroutine was run. Each ck will have different factors taken out of it because the circuit will (likely) have measured multiple different possible values of j. To recover the actual r value, we can take the least common multiple of each ck:lcm⁡(c1,c2,…,cs).The least common multiple will be the order r of the original integer a with high probability. In practice, a single run of the quantum order-finding subroutine is in general enough if more advanced post-processing is used.


==== Choosing the size of the first register ====
Phase estimation requires choosing the size of the first register to determine the accuracy of the algorithm, and for the quantum subroutine of Shor's algorithm, 2n qubits is sufficient to guarantee that the optimal bitstring measured from phase estimation (meaning the |k⟩ where k/22n is the most accurate approximation of the phase from phase estimation) will allow the actual value of r to be recovered.
Each |ϕj⟩ before measurement in Shor's algorithm represents a superposition of integers approximating 22nj/r. Let |k⟩ represent the most optimal integer in |ϕj⟩. The following theorem guarantees that the continued fractions algorithm will recover j/r from k/22n:

 As k is the optimal bitstring from phase estimation, k/22n is accurate to j/r by 2n bits. Thus,|jr−k22n|≤122n+1≤12N2≤12r2which implies that the continued fractions algorithm will recover j and r (or with their greatest common divisor taken out).


=== The bottleneck ===
The runtime bottleneck of Shor's algorithm is quantum modular exponentiation, which is by far slower than the quantum Fourier transform and classical pre-/post-processing. There are several approaches to constructing and optimizing circuits for modular exponentiation. The simplest and (currently) most practical approach is to mimic conventional arithmetic circuits with reversible gates, starting with ripple-carry adders. Knowing the base and the modulus of exponentiation facilitates further optimizations. Reversible circuits typically use on the order of n3 gates for n qubits. Alternative techniques asymptotically improve gate counts by using quantum Fourier transforms, but are not competitive with fewer than 600 qubits owing to high constants.


== Period finding and discrete logarithms ==
Shor's algorithms for the discrete log and the order finding problems are instances of an algorithm solving the period finding problem. All three are instances of the hidden subgroup problem.


=== Shor's algorithm for discrete logarithms ===
Given a group G with order p and generator g∈G, suppose we know that x=gr∈G, for some r∈ℤp, and we wish to compute r, which is the discrete logarithm: r=logg(x). Consider the abelian group ℤp×ℤp, where each factor corresponds to modular addition of values. Now, consider the function

f:ℤp×ℤp→G;f(a,b)=gax−b.
This gives us an abelian hidden subgroup problem, where f corresponds to a group homomorphism. The kernel corresponds to the multiples of (r,1). So, if we can find the kernel, we can find r. A quantum algorithm for solving this problem exists. This algorithm is, like the factor-finding algorithm, due to Peter Shor and both are implemented by creating a superposition through using Hadamard gates, followed by implementing f as a quantum transform, followed finally by a quantum Fourier transform. Due to this, the quantum algorithm for computing the discrete logarithm is also occasionally referred to as "Shor's Algorithm."
The order-finding problem can also be viewed as a hidden subgroup problem. To see this, consider the group of integers under addition, and for a given a∈ℤ such that: ar=1, the function

f:ℤ→ℤ;f(x)=ax,f(x+r)=f(x).
For any finite abelian group G, a quantum algorithm exists for solving the hidden subgroup for G in polynomial time.


== See also ==
GEECM, a factorization algorithm said to be "often much faster than Shor's"
Grover's algorithm


== References ==


== Further reading ==
Nielsen, Michael A.; Chuang, Isaac L. (2010). Quantum Computation and Quantum Information: 10th Anniversary Edition. Cambridge University Press. ISBN 978-1-107-00217-3.
Kaye, Phillip; Laflamme, Raymond; Mosca, Michele (2006). An Introduction to Quantum Computing. doi:10.1093/oso/9780198570004.001.0001. ISBN 978-0-19-857000-4.
"Explanation for the man in the street" by Scott Aaronson, "approved" by Peter Shor. (Shor wrote "Great article, Scott! That's the best job of explaining quantum computing to the man on the street that I've seen."). An alternate metaphor for the QFT was presented in one of the comments. Scott Aaronson suggests the following 12 references as further reading (out of "the 10105000 quantum algorithm tutorials that are already on the web."):
Shor, Peter W. (1997), "Polynomial-Time Algorithms for Prime Factorization and Discrete Logarithms on a Quantum Computer", SIAM J. Comput., 26 (5): 1484–1509, arXiv:quant-ph/9508027v2, Bibcode:1999SIAMR..41..303S, doi:10.1137/S0036144598347011. Revised version of the original paper by Peter Shor ("28 pages, LaTeX. This is an expanded version of a paper that appeared in the Proceedings of the 35th Annual Symposium on Foundations of Computer Science, Santa Fe, New Mexico, November 20--22, 1994. Minor revisions made January, 1996").
Quantum Computing and Shor's Algorithm, Matthew Hayward's Quantum Algorithms Page, 2005-02-17, imsa.edu, LaTeX2HTML version of the original LaTeX document, also available as PDF or postscript document.
Quantum Computation and Shor's Factoring Algorithm, Ronald de Wolf, CWI and University of Amsterdam, January 12, 1999, 9 page postscript document.
Shor's Factoring Algorithm, Notes from Lecture 9 of Berkeley CS 294–2, dated 4 Oct 2004, 7 page postscript document.
Chapter 6 Quantum Computation Archived 2020-04-30 at the Wayback Machine, 91 page postscript document, Caltech, Preskill, PH229.
Quantum computation: a tutorial by Samuel L. Braunstein.
The Quantum States of Shor's Algorithm, by Neal Young, Last modified: Tue May 21 11:47:38 1996.
III. Breaking RSA Encryption with a Quantum Computer: Shor's Factoring Algorithm, Lecture notes on Quantum computation, Cornell University, Physics 481–681, CS 483; Spring, 2006 by N. David Mermin. Last revised 2006-03-28, 30 page PDF document.
Lavor, C.; Manssur, L. R. U.; Portugal, R. (2003). "Shor's Algorithm for Factoring Large Integers". arXiv:quant-ph/0303175.
Lomonaco, Jr (2000). "Shor's Quantum Factoring Algorithm". arXiv:quant-ph/0010034. This paper is a written version of a one-hour lecture given on Peter Shor's quantum factoring algorithm. 22 pages.
Chapter 20 Quantum Computation, from Computational Complexity: A Modern Approach, Draft of a book: Dated January 2007, Sanjeev Arora and Boaz Barak, Princeton University. Published as Chapter 10 Quantum Computation of Sanjeev Arora, Boaz Barak, "Computational Complexity: A Modern Approach", Cambridge University Press, 2009, ISBN 978-0-521-42426-4
A Step Toward Quantum Computing: Entangling 10 Billion Particles. Archived 2011-01-20 at the Wayback Machine, from "Discover Magazine", Dated January 19, 2011.
Josef Gruska - Quantum Computing Challenges also in Mathematics unlimited: 2001 and beyond, Editors Björn Engquist, Wilfried Schmid, Springer, 2001, ISBN 978-3-540-66913-5


== External links ==
Version 1.0.0 of libquantum: contains a C language implementation of Shor's algorithm with their simulated quantum computer library, but the width variable in shor.c should be set to 1 to improve the runtime complexity.
PBS Infinite Series created two videos explaining the math behind Shor's algorithm, "How to Break Cryptography" and "Hacking at Quantum Speed with Shor's Algorithm".
Complete implementation of Shor's algorithm with Classiq
