---
title: Quantum logic gate
url: https://en.wikipedia.org/wiki/Quantum_logic_gate
revision: 1376542851 (2026-09-24T20:30:33Z)
fetched: 2026-11-20
license: CC BY-SA 4.0 (Wikipedia contributors)
---

In quantum computing and specifically the quantum circuit model of computation, a quantum logic gate (or simply quantum gate) is a basic quantum circuit operating on a small number of qubits. Quantum logic gates are the building blocks of quantum circuits, like classical logic gates are for conventional digital circuits.
According to quantum mechanics, a quantum system can only either evolve unitarily according to the Schrödinger equation, or be measured (sometimes called "Observed"). Quantum gates describe these unitary transformations, that occur when the system is not being measured. The expression "quantum gate" appears in relation to quantum processors, and in this context they are the logical operations that the quantum computer at the assembly language-level of abstraction (e.g. OpenQASM) can perform on the quantum data (qubits or quantum states) that they process. They can also be whole algorithms (e.g. the Quantum Fourier transform) if such algorithms contain no measurement operations. When the quantum data is measured, it is usually transformed into binary bits, which is then sent to a normal ("classical") computer. The quantum processor behaves like a coprocessor to such classical binary processors.
Unlike many classical logic gates, quantum logic gates are reversible. It is possible to perform classical computing using only reversible gates. For example, the reversible Toffoli gate can implement all Boolean functions, often at the cost of having to use ancilla bits. The Toffoli gate has a direct quantum equivalent, showing that quantum circuits can perform all operations performed by classical circuits.
Quantum gates are unitary operators, and are described as unitary matrices relative to some orthonormal basis. Usually the computational basis is used, which unless comparing it with something, just means that for a d-level quantum system (such as a qubit, a quantum register, or qutrits and qudits) the orthonormal basis vectors are labeled |0⟩,|1⟩,…,|d−1⟩, or use binary notation.


== History ==
The current notation for quantum gates was developed by many of the founders of quantum information science including Adriano Barenco, Charles Bennett, Richard Cleve, David P. DiVincenzo, Norman Margolus, Peter Shor, Tycho Sleator, John A. Smolin, and Harald Weinfurter, building on notation introduced by Richard Feynman in 1986.


== Representation ==

Quantum logic gates are represented by unitary matrices. A gate that acts on n qubits (a register) is represented by a 2n×2n unitary matrix, and the set of all such gates with the group operation of matrix multiplication is the unitary group U(2n). The quantum states that the gates act upon are unit vectors in 2n complex dimensions, with the complex Euclidean norm (the 2-norm). The basis vectors (sometimes called eigenstates) are the possible outcomes if the state of the qubits is measured, and a quantum state is a linear combination of these outcomes. The most common quantum gates operate on vector spaces of one or two qubits, just like the common classical logic gates operate on one or two bits.
Even though the quantum logic gates belong to continuous symmetry groups, real hardware is inexact and thus limited in precision. The application of gates typically introduces errors, and the quantum states' fidelities decrease over time. If error correction is used, the usable gates are further restricted to a finite set. Later in this article, this is ignored as the focus is on the ideal quantum gates' properties.
Quantum states are typically represented by "kets", from a notation known as bra–ket.
The vector representation of a single qubit is

|a⟩=v0|0⟩+v1|1⟩→[v0v1].
Here, v0 and v1 are the complex probability amplitudes of the qubit. These values determine the probability of measuring a 0 or a 1, when measuring the state of the qubit. See measurement below for details.
The value zero is represented by the ket |0⟩=[10], and the value one is represented by the ket |1⟩=[01].
The tensor product (or Kronecker product) is used to combine quantum states. The combined state for a qubit register is the tensor product of the constituent qubits. The tensor product is denoted by the symbol ⊗.
The vector representation of two qubits is:

|ψ⟩=v00|00⟩+v01|01⟩+v10|10⟩+v11|11⟩→[v00v01v10v11].
The action of the gate on a specific quantum state is found by multiplying the vector |ψ1⟩, which represents the state by the matrix U representing the gate. The result is a new quantum state |ψ2⟩:

U|ψ1⟩=|ψ2⟩.


=== Relation to the time evolution operator ===
The Schrödinger equation describes how quantum systems that are not observed evolve over time and is iℏddt|Ψ⟩=Ĥ|Ψ⟩. When the system is in a stable environment, so it has a constant Hamiltonian, the solution to this equation is Ψ(t)=U(t)|Ψ(t=0)⟩, where  U(t)=e−iĤt/ℏ. If the time t is always the same it may be omitted for simplicity, and the way quantum states evolve can be described as U|ψ1⟩=|ψ2⟩, just as in the above section.
That is, a quantum gate is how a quantum system that is not observed evolves over some specific time, or equivalently, a gate is the unitary time evolution operator U acting on a quantum state for a specific duration.


== Notable examples ==

There exists an uncountably infinite number of gates. Some of them have been named by various authors, and below follow some of those most often used in the literature.


=== Identity gate ===
The identity gate is the identity matrix, usually written as I, and is defined for a single qubit as

I=[1001],
where I is basis independent and does not modify the quantum state. The identity gate is most useful when describing mathematically the result of various gate operations or when discussing multi-qubit circuits.


=== Pauli gates (X,Y,Z) ===

The Pauli gates (X,Y,Z) are the three Pauli matrices (σx,σy,σz) and act on a single qubit. The Pauli X, Y and Z equate, respectively, to a rotation around the x, y and z axes of the Bloch sphere by π radians.
The Pauli-X gate is the quantum equivalent of the NOT gate for classical computers with respect to the standard basis |0⟩, |1⟩, which distinguishes the z axis on the Bloch sphere. It is sometimes called a bit-flip as it maps |0⟩ to |1⟩ and |1⟩ to |0⟩. Similarly, the Pauli-Y maps |0⟩ to i|1⟩ and |1⟩ to −i|0⟩. Pauli Z leaves the basis state |0⟩ unchanged and maps |1⟩ to −|1⟩. Due to this nature, Pauli Z is sometimes called phase-flip.
These matrices are usually represented as

X=σx=NOT⁡=[0110],
Y=σy=[0−ii0],
Z=σz=[100−1].
The Pauli matrices are involutory, meaning that the square of a Pauli matrix is the identity matrix.

I2=X2=Y2=Z2=−iXYZ=I
The Pauli matrices also anti-commute, for example ZX=iY=−XZ.
The matrix exponential of a Pauli matrix σj is a rotation operator, often written as e−iσjθ/2.


=== Controlled gates ===

Controlled gates act on 2 or more qubits, where one or more qubits act as a control for some operation. For example, the controlled NOT gate (or CNOT or CX) acts on 2 qubits, and performs the NOT operation on the second qubit only when the first qubit is |1⟩, and otherwise leaves it unchanged. With respect to the basis |00⟩, |01⟩, |10⟩, |11⟩, it is represented by the Hermitian unitary matrix:

CNOT=[1000010000010010].
The CNOT (or controlled Pauli-X) gate can be described as the gate that maps the basis states |a,b⟩↦|a,a⊕b⟩, where ⊕ is XOR.
The CNOT can be expressed in the Pauli basis as:

CNOT=eiπ4(I−Z1)(I−X2)=e−iπ4(I−Z1)(I−X2).
Being a Hermitian unitary operator, CNOT has the property that eiθU=(cos⁡θ)I+(isin⁡θ)U and U=eiπ2(I−U)=e−iπ2(I−U), and is involutory.
More generally if U is a gate that operates on a single qubit with matrix representation

U=[u00u01u10u11],
then the controlled-U gate is a gate that operates on two qubits in such a way that the first qubit serves as a control. It maps the basis states as follows.
|00⟩↦|00⟩
|01⟩↦|01⟩
|10⟩↦|1⟩⊗U|0⟩=|1⟩⊗(u00|0⟩+u10|1⟩)
|11⟩↦|1⟩⊗U|1⟩=|1⟩⊗(u01|0⟩+u11|1⟩)
The matrix representing the controlled U is

CU=[1000010000u00u0100u10u11].
When U is one of the Pauli operators, X,Y, Z, the respective terms "controlled-X", "controlled-Y", or "controlled-Z" are sometimes used. Sometimes this is shortened to just CX, CY and CZ.
In general, any single qubit unitary gate can be expressed as U=eiH, where H is a Hermitian matrix, and then the controlled U is CU=ei12(I−Z1)H2.
Control can be extended to gates with arbitrary number of qubits and functions in programming languages. Functions can be conditioned on superposition states.


==== Classical control ====

 Gates can also be controlled by classical logic. A quantum computer is controlled by a classical computer, and behaves like a coprocessor that receives instructions from the classical computer about what gates to execute on which qubits. Classical control is simply the inclusion, or omission, of gates in the instruction sequence for the quantum computer. Performing measurements in the middle of a quantum circuit, as opposed to the end of it, is difficult and technically challenging because of timing issues and decoherence. Because of this, not all quantum computers support these classical if-statement, where quantum data is converted to bits, which then controls the program flow.


=== Phase shift gates ===
The phase shift is a family of single-qubit gates that map the basis states |0⟩↦|0⟩ and |1⟩↦eiφ|1⟩. The probability of measuring a |0⟩ or |1⟩ is unchanged after applying this gate, however it modifies the phase of the quantum state. This is equivalent to tracing a horizontal circle (a line of constant latitude), or a rotation about the z-axis on the Bloch sphere by φ radians. The phase shift gate is represented by the matrix:

P(φ)=[100eiφ]
where φ is the phase shift with the period 2π. Some common examples are the T gate where φ=π4 (historically known as the π/8 gate), the phase gate (also known as the S gate, written as S, though S is sometimes used for SWAP gates) where φ=π2 and the Pauli-Z gate where φ=π.
The phase shift gates are related to each other as follows:

Z=[100eiπ]=[100−1]=P(π)
S=[100eiπ2]=[100i]=P(π2)=Z
T=[100eiπ4]=P(π4)=S=Z4
Note that the phase gate P(φ) is not Hermitian (except for all φ=nπ,n∈ℤ). These gates are different from their Hermitian conjugates: P†(φ)=P(−φ). The two adjoint (or conjugate transpose) gates S† and T† are sometimes included in instruction sets.


=== Hadamard gate ===
The Hadamard or Walsh-Hadamard gate, named after Jacques Hadamard (French: [adamaʁ]) and Joseph L. Walsh, acts on a single qubit. It maps the basis states |0⟩↦|0⟩+|1⟩2 and |1⟩↦|0⟩−|1⟩2 (it creates an equal superposition state if given a computational basis state). The two states (|0⟩+|1⟩)/2 and (|0⟩−|1⟩)/2 are sometimes written |+⟩ and |−⟩ respectively. The Hadamard gate performs a rotation of π about the axis (x̂+ẑ)/2 at the Bloch sphere, and is therefore involutory. It is represented by the Hadamard matrix: 

H=12[111−1].
If the Hermitian (so H†=H−1=H) Hadamard gate is used to perform a change of basis, it flips x̂ and ẑ. For example, HZH=X and HXH=Z=S.


=== Swap gate ===

The swap gate swaps two qubits. With respect to the basis |00⟩, |01⟩, |10⟩, |11⟩, it is represented by the matrix

SWAP=[1000001001000001].
The swap gate can be decomposed into summation form:

SWAP=I⊗I+X⊗X+Y⊗Y+Z⊗Z2


=== Toffoli (CCNOT) gate ===

The Toffoli gate, named after Tommaso Toffoli and also called the CCNOT gate or Deutsch gate D(π/2), is a 3-bit gate that is universal for classical computation but not for quantum computation. The quantum Toffoli gate is the same gate, defined for 3 qubits. If we limit ourselves to only accepting input qubits that are |0⟩ and |1⟩, then if the first two bits are in the state |1⟩ it applies a Pauli-X (or NOT) on the third bit, else it does nothing. It is an example of a CC-U (controlled-controlled Unitary) gate. Since it is the quantum analog of a classical gate, it is completely specified by its truth table. The Toffoli gate is universal when combined with the single qubit Hadamard gate.

The Toffoli gate is related to the classical AND (∧) and XOR (⊕) operations as it performs the mapping |a,b,c⟩↦|a,b,c⊕(a∧b)⟩ on states in the computational basis.
The Toffoli gate can be expressed using Pauli matrices as

Toff=eiπ8(I−Z1)(I−Z2)(I−X3)=e−iπ8(I−Z1)(I−Z2)(I−X3).


== Universal quantum gates ==

A set of universal quantum gates is any set of gates to which any operation possible on a quantum computer can be reduced, that is, any other unitary operation can be expressed as a finite sequence of gates from the set. Technically, this is impossible with anything less than an uncountable set of gates since the number of possible quantum gates is uncountable, whereas the number of finite sequences from a finite set is countable. To solve this problem, we only require that any quantum operation can be approximated by a sequence of gates from this finite set. Moreover, for unitaries on a constant number of qubits, the Solovay–Kitaev theorem guarantees that this can be done efficiently. Checking if a set of quantum gates is universal can be done using group theory methods and/or relation to (approximate) unitary t-designs. The spectral gap conjecture, if true, would imply that a generically chosen set of quantum gates is efficiently universal.
Some universal quantum gate sets include:

The rotation operators Rx(θ), Ry(θ), Rz(θ), the phase shift gate P(φ) and CNOT are commonly used to form a universal quantum gate set.
The Clifford set {CNOT, H, S} + T gate. The Clifford set alone is not a universal quantum gate set, as it can be efficiently simulated classically according to the Gottesman–Knill theorem.
The Toffoli gate + Hadamard gate. The Toffoli gate alone forms a set of universal gates for reversible Boolean algebraic logic circuits, which encompasses all classical computation.


=== Deutsch gate ===
A single-gate set of universal quantum gates can also be formulated using the parametrized three-qubit Deutsch gate D(θ), named after physicist David Deutsch. It is a general case of CC-U, or controlled-controlled-unitary gate, and is defined as

|a,b,c⟩↦{icos⁡(θ)|a,b,c⟩+sin⁡(θ)|a,b,1−c⟩for a=b=1,|a,b,c⟩otherwise.
Unfortunately, a working Deutsch gate has remained out of reach, due to lack of a protocol. There are some proposals to realize a Deutsch gate with dipole–dipole interaction in neutral atoms.

A universal logic gate for reversible classical computing, the Toffoli gate, is reducible to the Deutsch gate D(π/2), thus showing that all reversible classical logic operations can be performed on a universal quantum computer.
There also exist single two-qubit gates sufficient for universality. In 1996, Adriano Barenco showed that the Deutsch gate can be decomposed using only a single two-qubit gate (Barenco gate), but it is hard to realize experimentally. This feature is exclusive to quantum circuits, as there is no classical two-bit gate that is both reversible and universal. Universal two-qubit gates could be implemented to improve classical reversible circuits in fast low-power microprocessors.


== Circuit composition ==


=== Serially wired gates ===
Assume that we have two gates A and B that both act on n qubits. When B is put after A in a series circuit, then the effect of the two gates can be described as a single gate C.
C=B⋅A
where ⋅ is matrix multiplication. The resulting gate C will have the same dimensions as A and B. The order in which the gates would appear in a circuit diagram is reversed when multiplying them together.
For example, putting the Pauli X gate after the Pauli Y gate, both of which act on a single qubit, can be described as a single combined gate C:

C=X⋅Y=[0110]⋅[0−ii0]=[i00−i]=iZ
The product symbol (⋅) is often omitted.


==== Exponents of quantum gates ====
All real exponents of unitary matrices are also unitary matrices, and all quantum gates are unitary matrices.
Positive integer exponents are equivalent to sequences of serially wired gates (e.g. X3=X⋅X⋅X), and the real exponents is a generalization of the series circuit. For example, Xπ and X=X1/2 are both valid quantum gates.
U0=I for any unitary matrix U. The identity matrix (I) behaves like a NOP and can be represented as bare wire in quantum circuits, or not shown at all.
All gates are unitary matrices, so that U†U=UU†=I and U†=U−1, where † is the conjugate transpose. This means that negative exponents of gates are unitary inverses of their positively exponentiated counterparts: U−n=(Un)†. For example, some negative exponents of the phase shift gates are T−1=T† and T−2=(T2)†=S†.
Note that for a Hermitian matrix H†=H, and because of unitarity, HH†=I, so H2=I for all Hermitian gates. They are involutory. Examples of Hermitian gates are the Pauli gates, Hadamard, CNOT, SWAP and Toffoli. Each Hermitian unitary matrix H has the property that eiθH=(cos⁡θ)I+(isin⁡θ)H where H=eiπ2(I−H)=e−iπ2(I−H).
The exponent of a gate is a multiple of the duration of time that the time evolution operator is applied to a quantum state. E.g., in a spin qubit quantum computer the SWAP gate could be realized via exchange interaction on the spin of two electrons for half the duration of a full exchange interaction.


=== Parallel gates ===

The tensor product (or Kronecker product) of two quantum gates is the gate that is equal to the two gates in parallel.
If we, as in the picture, combine the Pauli-Y gate with the Pauli-X gate in parallel, then this can be written as:

C=Y⊗X=[0−ii0]⊗[0110]=[0[0110]−i[0110]i[0110]0[0110]]=[000−i00−i00i00i000]
Both the Pauli-X and the Pauli-Y gate act on a single qubit. The resulting gate C act on two qubits.
Sometimes the tensor product symbol is omitted, and indexes are used for the operators instead.


==== Hadamard transform ====

The gate H2=H⊗H is the Hadamard gate (H) applied in parallel on 2 qubits. It can be written as:

H2=H⊗H=12[111−1]⊗12[111−1]=12[11111−11−111−1−11−1−11]
This "two-qubit parallel Hadamard gate" will, when applied to, for example, the two-qubit zero-vector (|00⟩), create a quantum state that has equal probability of being observed in any of its four possible outcomes; |00⟩, |01⟩, |10⟩, and |11⟩. We can write this operation as:

H2|00⟩=12[11111−11−111−1−11−1−11][1000]=12[1111]=12|00⟩+12|01⟩+12|10⟩+12|11⟩=|00⟩+|01⟩+|10⟩+|11⟩2

Here the amplitude for each measurable state is 1⁄2. The probability to observe any state is the square of the absolute value of the measurable states amplitude, which in the above example means that there is one in four that we observe any one of the individual four cases. See measurement for details.
H2 performs the Hadamard transform on two qubits. Similarly the gate H⊗H⊗⋯⊗H⏟n times=⨂i=0n−1H=H⊗n=Hn performs a Hadamard transform on a register of n qubits.
When applied to a register of n qubits all initialized to |0⟩, the Hadamard transform puts the quantum register into a superposition with equal probability of being measured in any of its 2n possible states:

⨂i=0n−1(H|0⟩)=12n[11⋮1]=12n(|0⟩+|1⟩+⋯+|2n−1⟩)=12n∑i=02n−1|i⟩
This state is a uniform superposition and it is generated as the first step in some search algorithms, for example in amplitude amplification and phase estimation.
Measuring this state results in a random number between |0⟩ and |2n−1⟩. How random the number is depends on the fidelity of the logic gates. If not measured, it is a quantum state with equal probability amplitude 12n for each of its possible states.
The Hadamard transform acts on a register |ψ⟩ with n qubits such that |ψ⟩=⨂i=0n−1|ψi⟩ as follows:

⨂i=0n−1H|ψ⟩=⨂i=0n−1|0⟩+(−1)ψi|1⟩2=12n⨂i=0n−1(|0⟩+(−1)ψi|1⟩)=H|ψ0⟩⊗H|ψ1⟩⊗⋯⊗H|ψn−1⟩


==== Application on entangled states ====
If two or more qubits are viewed as a single quantum state, this combined state is equal to the tensor product of the constituent qubits. Any state that can be written as a tensor product from the constituent subsystems are called separable states. On the other hand, an entangled state is any state that cannot be tensor-factorized, or in other words: An entangled state can not be written as a tensor product of its constituent qubits states. Special care must be taken when applying gates to constituent qubits that make up entangled states.
If we have a set of N qubits that are entangled and wish to apply a quantum gate on M < N qubits in the set, we will have to extend the gate to take N qubits. This application can be done by combining the gate with an identity matrix such that their tensor product becomes a gate that act on N qubits. The identity matrix (I) is a representation of the gate that maps every state to itself (i.e., does nothing at all). In a circuit diagram the identity gate or matrix will often appear as just a bare wire.

For example, the Hadamard gate (H) acts on a single qubit, but if we feed it the first of the two qubits that constitute the entangled Bell state |00⟩+|11⟩2, we cannot write that operation easily. We need to extend the Hadamard gate H with the identity gate I so that we can act on quantum states that span two qubits:

K=H⊗I=12[111−1]⊗[1001]=12[1010010110−10010−1]
The gate K can now be applied to any two-qubit state, entangled or otherwise. The gate K will leave the second qubit untouched and apply the Hadamard transform to the first qubit. If applied to the Bell state in our example, we may write that as:

K|00⟩+|11⟩2=12[1010010110−10010−1]12[1001]=12[111−1]=|00⟩+|01⟩+|10⟩−|11⟩2


==== Computational complexity and the tensor product ====
The time complexity for multiplying two n×n-matrices is at least Ω(n2log⁡n), if using a classical machine. Because the size of a gate that operates on q qubits is 2q×2q it means that the time for simulating a step in a quantum circuit (by means of multiplying the gates) that operates on generic entangled states is Ω(2q2log⁡(2q)). For this reason it is believed to be intractable to simulate large entangled quantum systems using classical computers. Subsets of the gates, such as the Clifford gates, or the trivial case of circuits that only implement classical Boolean functions (e.g. combinations of X, CNOT, Toffoli), can however be efficiently simulated on classical computers.
The state vector of a quantum register with n qubits is 2n complex entries. Storing the probability amplitudes as a list of floating point values is not tractable for large n.


=== Unitary inversion of gates ===
Because all quantum logical gates are reversible, any composition of multiple gates is also reversible. All products and tensor products (i.e. series and parallel combinations) of unitary matrices are also unitary matrices. This means that it is possible to construct an inverse of all algorithms and functions, as long as they contain only gates.
Initialization, measurement, I/O and spontaneous decoherence are side effects in quantum computers. Gates however are purely functional and bijective.
If U is a unitary matrix, then U†U=UU†=I and U†=U−1. The dagger (†) denotes the conjugate transpose. It is also called the Hermitian adjoint.
If a function F is a product of m gates, F=A1⋅A2⋅⋯⋅Am, the unitary inverse of the function F† can be constructed:
Because (UV)†=V†U† we have, after repeated application on itself

F†=(∏i=1mAi)†=∏i=m1Ai†=Am†⋅⋯⋅A2†⋅A1†
Similarly if the function G consists of two gates A and B in parallel, then G=A⊗B and G†=(A⊗B)†=A†⊗B†.
Gates that are their own unitary inverses are called Hermitian or self-adjoint operators. Some elementary gates such as the Hadamard (H) and the Pauli gates (I, X, Y, Z) are Hermitian operators, while others like the phase shift (S, T, P, CPhase) gates generally are not.
For example, an algorithm for addition can be used for subtraction, if it is being "run in reverse", as its unitary inverse. The inverse quantum Fourier transform is the unitary inverse. Unitary inverses can also be used for uncomputation. Programming languages for quantum computers, such as Microsoft's Q#, Bernhard Ömer's QCL, and IBM's Qiskit, contain function inversion as programming concepts.


== Measurement ==

Measurement (sometimes called observation) is irreversible and therefore not a quantum gate, because it assigns the observed quantum state to a single value. Measurement takes a quantum state and projects it to one of the basis vectors, with a likelihood equal to the square of the vector's length (in the 2-norm) along that basis vector. This is known as the Born rule and appears as a stochastic non-reversible operation as it probabilistically sets the quantum state equal to the basis vector that represents the measured state. At the instant of measurement, the state is said to "collapse" to the definite single value that was measured. Why and how, or even if the quantum state collapses at measurement, is called the measurement problem.
The probability of measuring a value with probability amplitude ϕ is 1≥|ϕ|2≥0, where |⋅| is the modulus.
Measuring a single qubit, whose quantum state is represented by the vector a|0⟩+b|1⟩=[ab], will result in |0⟩ with probability |a|2, and in |1⟩ with probability |b|2.
For example, measuring a qubit with the quantum state |0⟩−i|1⟩2=12[1−i] will yield with equal probability either |0⟩ or |1⟩.

A quantum state |Ψ⟩ that spans n qubits can be written as a vector in 2n complex dimensions: |Ψ⟩∈ℂ2n. This is because the tensor product of n qubits is a vector in 2n dimensions. This way, a register of n qubits can be measured to 2n distinct states, similar to how a register of n classical bits can hold 2n distinct states. Unlike with the bits of classical computers, quantum states can have non-zero probability amplitudes in multiple measurable values simultaneously. This is called superposition.
The sum of all probabilities for all outcomes must always be equal to 1. Another way to say this is that the Pythagorean theorem generalized to ℂ2n has that all quantum states |Ψ⟩ with n qubits must satisfy 1=∑x=02n−1|ax|2, where ax is the probability amplitude for measurable state |x⟩. A geometric interpretation of this is that the possible value-space of a quantum state |Ψ⟩ with n qubits is the surface of the unit sphere in ℂ2n and that the unitary transforms (i.e. quantum logic gates) applied to it are rotations on the sphere. The rotations that the gates perform form the symmetry group U(2n). Measurement is then a probabilistic projection of the points at the surface of this complex sphere onto the basis vectors that span the space (and labels the outcomes).
In many cases the space is represented as a Hilbert space ℋ rather than some specific 2n-dimensional complex space. The number of dimensions (defined by the basis vectors, and thus also the possible outcomes from measurement) is then often implied by the operands, for example as the required state space for solving a problem. In Grover's algorithm, Grover named this generic basis vector set "the database".
The selection of basis vectors against which to measure a quantum state will influence the outcome of the measurement. See change of basis and Von Neumann entropy for details. In this article, we always use the computational basis, which means that we have labeled the 2n basis vectors of an n-qubit register |0⟩,|1⟩,|2⟩,⋯,|2n−1⟩, or use the binary representation |010⟩=|0…002⟩,|110⟩=|0…012⟩,|210⟩=|0…102⟩,⋯,|2n−1⟩=|111…12⟩.
In quantum mechanics, the basis vectors constitute an orthonormal basis.
An example of usage of an alternative measurement basis is in the BB84 cipher.


=== The effect of measurement on entangled states ===

If two quantum states (i.e. qubits, or registers) are entangled (meaning that their combined state cannot be expressed as a tensor product), measurement of one register affects or reveals the state of the other register by partially or entirely collapsing its state too. This effect can be used for computation, and is used in many algorithms.
The Hadamard-CNOT combination acts on the zero-state as follows: 

CNOT⁡(H⊗I)|00⟩=([1000010000010010](12[111−1]⊗[1001]))[1000]=12[1001]=|00⟩+|11⟩2

This resulting state is the Bell state |00⟩+|11⟩2=12[1001]. It cannot be described as a tensor product of two qubits. There is no solution for

[xy]⊗[wz]=[xwxzywyz]=12[1001],
because for example w needs to be both non-zero and zero in the case of xw and yw.
The quantum state spans the two qubits. This is called entanglement. Measuring one of the two qubits that make up this Bell state will result in that the other qubit logically must have the same value, both must be the same: Either it will be found in the state |00⟩, or in the state |11⟩. If we measure one of the qubits to be for example |1⟩, then the other qubit must also be |1⟩, because their combined state became |11⟩. Measurement of one of the qubits collapses the entire quantum state, that span the two qubits.
The GHZ state is a similar entangled quantum state that spans three or more qubits.
This type of value-assignment occurs instantaneously over any distance and this has as of 2018 been experimentally verified by QUESS for distances of up to 1200 kilometers. That the phenomena appears to happen instantaneously as opposed to the time it would take to traverse the distance separating the qubits at the speed of light is called the EPR paradox, and it is an open question in physics how to resolve this. Originally it was solved by giving up the assumption of local realism, but other interpretations have also emerged. For more information see the Bell test experiments. The no-communication theorem proves that this phenomenon cannot be used for faster-than-light communication of classical information.


=== Measurement on registers with pairwise entangled qubits ===

Take a register A with n qubits all initialized to |0⟩, and feed it through a parallel Hadamard gate H⊗n. Register A will then enter the state 12n∑k=02n−1|k⟩ that have equal probability of when measured to be in any of its 2n possible states; |0⟩ to |2n−1⟩. Take a second register B, also with n qubits initialized to |0⟩ and pairwise CNOT its qubits with the qubits in register A, such that for each p the qubits Ap and Bp forms the state |ApBp⟩=|00⟩+|11⟩2.
If we now measure the qubits in register A, then register B will be found to contain the same value as A. If we however instead apply a quantum logic gate F on A and then measure, then |A⟩=F|B⟩⟺F†|A⟩=|B⟩, where F† is the unitary inverse of F.
Because of how unitary inverses of gates act, F†|A⟩=F−1(|A⟩)=|B⟩. For example, say F(x)=x+3(mod2n), then |B⟩=|A−3(mod2n)⟩.
The equality will hold no matter in which order measurement is performed (on the registers A or B), assuming that F has run to completion. Measurement can even be randomly and concurrently interleaved qubit by qubit, since the measurements assignment of one qubit will limit the possible value-space from the other entangled qubits.
Even though the equalities holds, the probabilities for measuring the possible outcomes may change as a result of applying F, as may be the intent in a quantum search algorithm.
This effect of value-sharing via entanglement is used in Shor's algorithm, phase estimation and in quantum counting. Using the Fourier transform to amplify the probability amplitudes of the solution states for some problem is a generic method known as "Fourier fishing".


== Logic function synthesis ==

Functions and routines that only use gates can themselves be described as matrices, just like the smaller gates. The matrix that represents a quantum function acting on q qubits has size 2q×2q. For example, a function that acts on a "qubyte" (a register of 8 qubits) would be represented by a matrix with 28×28=256×256 elements.
Unitary transformations that are not in the set of gates natively available at the quantum computer (the primitive gates) can be synthesised, or approximated, by combining the available primitive gates in a circuit. One way to do this is to factor the matrix that encodes the unitary transformation into a product of tensor products (i.e. series and parallel circuits) of the available primitive gates. The group U(2q) is the symmetry group for the gates that act on q qubits. Factorization is then the problem of finding a path in U(2q) from the generating set of primitive gates. The Solovay–Kitaev theorem shows that given a sufficient set of primitive gates, there exist an efficient approximate for any gate. For the general case with a large number of qubits this direct approach to circuit synthesis is intractable. This puts a limit on how large functions can be brute-force factorized into primitive quantum gates. Typically quantum programs are instead built using relatively small and simple quantum functions, similar to normal classical programming.
Because of the gates unitary nature, all functions must be reversible and always be bijective mappings of input to output. There must always exist a function F−1 such that F−1(F(|ψ⟩))=|ψ⟩. Functions that are not invertible can be made invertible by adding ancilla qubits to the input or the output, or both. After the function has run to completion, the ancilla qubits can then either be uncomputed or left untouched. Measuring or otherwise collapsing the quantum state of an ancilla qubit (e.g. by re-initializing the value of it, or by its spontaneous decoherence) that have not been uncomputed may result in errors, as their state may be entangled with the qubits that are still being used in computations.
Logically irreversible operations, for example addition modulo 2n of two n-qubit registers a and b, F(a,b)=a+b(mod2n), can be made logically reversible by adding information to the output, so that the input can be computed from the output (i.e. there exists a function F−1). In our example, this can be done by passing on one of the input registers to the output: F(|a⟩⊗|b⟩)=|a+b(mod2n)⟩⊗|a⟩. The output can then be used to compute the input (i.e. given the output a+b and a, we can easily find the input; a is given and (a+b)−a=b) and the function is made bijective.
All Boolean algebraic expressions can be encoded as unitary transforms (quantum logic gates), for example by using combinations of the Pauli-X, CNOT and Toffoli gates. These gates are functionally complete in the Boolean logic domain.
There are many unitary transforms available in the libraries of Q#, QCL, Qiskit, and other quantum programming languages. It also appears in the literature.
For example, inc(|x⟩)=|x+1(mod2xlength)⟩, where xlength is the number of qubits that constitutes the register x, is implemented as the following in QCL:

In QCL, decrement is done by "undoing" increment. The prefix ! is used to instead run the unitary inverse of the function. !inc(x) is the inverse of inc(x) and instead performs the operation inc†|x⟩=inc−1(|x⟩)=|x−1(mod2xlength)⟩. The cond keyword means that the function can be conditional.
In the model of computation used in this article (the quantum circuit model), a classic computer generates the gate composition for the quantum computer, and the quantum computer behaves as a coprocessor that receives instructions from the classical computer about which primitive gates to apply to which qubits. Measurement of quantum registers results in binary values that the classical computer can use in its computations. Quantum algorithms often contain both a classical and a quantum part. Unmeasured I/O (sending qubits to remote computers without collapsing their quantum states) can be used to create networks of quantum computers. Entanglement swapping can then be used to realize distributed algorithms with quantum computers that are not directly connected. Examples of distributed algorithms that only require the use of a handful of quantum logic gates are superdense coding, the quantum Byzantine agreement and the BB84 cipherkey exchange protocol.


== See also ==


== Notes ==


== References ==


=== Sources ===
Nielsen, Michael A.; Chuang, Isaac (2000). Quantum Computation and Quantum Information. Cambridge, England: Cambridge University Press. ISBN 0-521-63235-8. OCLC 43641333.
Williams, Colin P. (2011). Explorations in Quantum Computing. Springer. ISBN 978-1-84628-887-6.
Yanofsky, Noson S.; Mannucci, Mirco (2013). Quantum computing for computer scientists. Cambridge University Press. ISBN 978-0-521-87996-5.
