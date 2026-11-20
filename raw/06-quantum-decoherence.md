---
title: Quantum decoherence
url: https://en.wikipedia.org/wiki/Quantum_decoherence
revision: 1384689551 (2026-11-09T16:18:45Z)
fetched: 2026-11-20
license: CC BY-SA 4.0 (Wikipedia contributors)
---

Quantum decoherence is the loss of quantum coherence.  It involves generally a loss of information of a system to its environment. Quantum decoherence has been studied to understand how quantum systems convert to systems that can be explained by classical mechanics.  Beginning out of attempts to extend the understanding of quantum mechanics, the theory has developed in several  directions and experimental studies have confirmed some of the key issues. Quantum computing relies on quantum coherence and is one of the primary practical applications of the concept.


== Concept ==
In quantum mechanics, a physical system is described by a mathematical representation called a quantum state. Probabilities for the outcomes of experiments upon a system are calculated by applying the Born rule to the quantum state describing that system. Quantum states are either pure or mixed; pure states are also known as wavefunctions. Assigning a pure state to a quantum system implies certainty about the outcome of some measurement on that system, i.e., that there exists a measurement for which one of the possible outcomes will occur with probability 1. In the absence of outside forces or interactions, the quantum system is "closed", which implies that its quantum state evolves unitarily over time. Consequently, a pure quantum state remains pure. However, if the system is "open", that is, not perfectly isolated, for example during a measurement, coherence is shared with the environment and appears to be lost with time — a process called quantum decoherence or environmental decoherence. The quantum coherence is not lost but rather mixed with many more degrees of freedom in the environment, analogous to the way energy appears to be lost during friction in classical mechanics when it actually has produced heat in the environment.
Decoherence can be viewed as the loss of information from a system into the environment (often modelled as a heat bath), since every system is loosely coupled with the energetic state of its surroundings. Viewed in isolation, the system's dynamics are non-unitary (although the combined system plus environment evolves in a unitary fashion). Thus the dynamics of the system alone are irreversible. As with any coupling, entanglements are generated between the system and environment. These have the effect of sharing quantum information with—or transferring it to—the surroundings.


== History and interpretation ==


=== Relation to interpretation of quantum mechanics ===
An interpretation of quantum mechanics is an attempt to explain how the mathematical theory of quantum physics might correspond to experienced reality. Decoherence calculations can be done in any interpretation of quantum mechanics, since those calculations are an application of the standard mathematical tools of quantum theory. However, the subject of decoherence has been closely related to the problem of interpretation throughout its history.
Decoherence has been used to understand the possibility of the collapse of the wave function in quantum mechanics. Decoherence does not generate actual wave-function collapse. It only provides a framework for apparent wave-function collapse, as the components of a quantum system entangle with other quantum systems within the same environment. That is, components of the wave function are decoupled from a coherent system and acquire phases from their immediate surroundings. A total superposition of the global or universal wavefunction still exists (and remains coherent at the global level), but its ultimate fate remains an interpretational issue.
With respect to the measurement problem, decoherence provides an explanation for the transition of the system to a mixture of states that seem to correspond to those states observers perceive. Moreover, observation indicates that this mixture looks like a proper quantum ensemble in a measurement situation, as the measurements lead to the "realization" of precisely one state in the "ensemble".
The philosophical views of Werner Heisenberg and Niels Bohr have often been grouped together as the "Copenhagen interpretation", despite significant divergences between them on important points. In 1955, Heisenberg suggested that the interaction of a system with its surrounding environment would eliminate quantum interference effects. However, Heisenberg did not provide a detailed account of how this might transpire, nor did he make explicit the importance of entanglement in the process.


=== Origin of the concepts ===
Nevill Mott's solution to the iconic Mott problem in 1929 is considered in retrospect to be the first quantum decoherence work. It was cited by the first modern theoretical treatment.
Although he did not use the term, the concept of quantum decoherence was first introduced in 1951 by the American physicist David Bohm, who called it the "destruction of interference in the process of measurement". Bohm later used decoherence to handle the measurement process in the de Broglie-Bohm interpretation of quantum theory.
The significance of decoherence was further highlighted in 1970 by the German physicist H. Dieter Zeh, and it has been a subject of active research since the 1980s. Decoherence has been developed into a complete framework, but there is controversy as to whether it solves the measurement problem, as the founders of decoherence theory admit in their seminal papers.
The study of decoherence as a proper subject began in 1970, with H. Dieter Zeh's paper "On the Interpretation of Measurement in Quantum Theory". Zeh regarded the wavefunction as a physical entity, rather than a calculational device or a compendium of statistical information (as is typical for Copenhagen-type interpretations), and he proposed that it should evolve unitarily, in accord with the Schrödinger equation, at all times. Zeh was initially unaware of Hugh Everett III's earlier work, which also proposed a universal wavefunction evolving unitarily; he revised his paper to reference Everett after learning of Everett's "relative-state interpretation" through an article by Bryce DeWitt. (DeWitt was the one who termed Everett's proposal the many-worlds interpretation, by which name it is commonly known.) For Zeh, the question of how to interpret quantum mechanics was of key importance, and an interpretation along the lines of Everett's was the most natural. Partly because of a general disinterest among physicists for interpretational questions, Zeh's work remained comparatively neglected until the early 1980s, when two papers by Wojciech Zurek invigorated the subject. Unlike Zeh's publications, Zurek's articles were fairly agnostic about interpretation, focusing instead on specific problems of density-matrix dynamics. Zurek's interest in decoherence stemmed from furthering Bohr's analysis of the double-slit experiment in his reply to the Einstein–Podolsky–Rosen paradox, work he had undertaken with Bill Wootters, and he has since argued that decoherence brings a kind of rapprochement between Everettian and Copenhagen-type views.
Decoherence does not claim to provide a mechanism for some actual wave-function collapse; rather it puts forth a reasonable framework for the appearance of wave-function collapse. The quantum nature of the system is simply entangled into the environment so that a total superposition of the wave function still exists, but exists—at least for all practical purposes—beyond the realm of measurement. By definition, the claim that a merged but unmeasurable wave function still exists cannot be proven experimentally. Decoherence is needed to understand why a quantum system begins to obey classical probability rules after interacting with its environment (due to the suppression of the interference terms when applying Born's probability rules to the system).
Criticism of the adequacy of decoherence theory to solve the measurement problem has been expressed by Anthony Leggett.


== Mechanisms ==
To examine how decoherence operates, an "intuitive" model is presented below. The model requires some familiarity with quantum theory basics. Analogies are made between visualizable classical phase spaces and Hilbert spaces. A more rigorous derivation in Dirac notation shows how decoherence destroys interference effects and the "quantum nature" of systems. Next, the density matrix approach is presented for perspective.


=== Phase-space picture ===
An N-particle system can be represented in non-relativistic quantum mechanics by a wave function ψ(x1,x2,…,xN), where each xi is a point in 3-dimensional space. This has analogies with the classical phase space. A classical phase space contains a real-valued function in 6N dimensions (each particle contributes 3 spatial coordinates and 3 momenta). In this case a "quantum" phase space, on the other hand, involves a complex-valued function on a 3N-dimensional space. The position and momenta are represented by operators that do not commute, and ψ lives in the mathematical structure of a Hilbert space. Aside from these differences, however, the rough analogy holds.
Different previously isolated, non-interacting systems occupy different phase spaces. Alternatively we can say that they occupy different lower-dimensional subspaces in the phase space of the joint system. The effective dimensionality of a system's phase space is the number of degrees of freedom present, which—in non-relativistic models—is 6 times the number of a system's free particles. For a macroscopic system this will be a very large dimensionality. When two systems (the environment being one system) start to interact, though, their associated state vectors are no longer constrained to the subspaces. Instead the combined state vector time-evolves a path through the "larger volume", whose dimensionality is the product of the dimensions of the two subspaces. The extent to which two vectors interfere with each other is a measure of how "close" they are to each other (formally, their overlap or Hilbert space multiplies together) in the phase space. When a system couples to an external environment, the dimensionality of, and hence "volume" available to, the joint state vector increases enormously. Each environmental degree of freedom contributes an extra dimension.
The original system's wave function can be expanded in many different ways as a sum of elements in a quantum superposition. Each expansion corresponds to a projection of the wave vector onto a basis. The basis can be chosen at will. Choosing an expansion where the resulting basis elements interact with the environment in an element-specific way, such elements will—with overwhelming probability—be rapidly separated from each other by their natural unitary time evolution along their own independent paths. After a very short interaction, there is almost no chance of further interference. The process is effectively irreversible. The different elements effectively become "lost" from each other in the expanded phase space created by coupling with the environment. In phase space, this decoupling is monitored through the Wigner quasi-probability distribution. The original elements are said to have decohered. The environment has effectively selected out those expansions or decompositions of the original state vector that decohere (or lose phase coherence) with each other. This is called "environmentally-induced superselection", or einselection. The decohered elements of the system no longer exhibit quantum interference between each other, as in a double-slit experiment. Any elements that decohere from each other via environmental interactions are said to be quantum-entangled with the environment. The converse is not true: not all entangled states are decohered from each other.
Any measuring device or apparatus acts as an environment, since at some stage along the measuring chain, it has to be large enough to be read by humans. It must possess a very large number of hidden degrees of freedom. In effect, the interactions may be considered to be quantum measurements. As a result of an interaction, the wave functions of the system and the measuring device become entangled with each other. Decoherence happens when different portions of the system's wave function become entangled in different ways with the measuring device. For two einselected elements of the entangled system's state to interfere, both the original system and the measuring in both elements device must significantly overlap, in the scalar product sense. If the measuring device has many degrees of freedom, it is very unlikely for this to happen.
As a consequence, the system behaves as a classical statistical ensemble of the different elements rather than as a single coherent quantum superposition of them. From the perspective of each ensemble member's measuring device, the system appears to have irreversibly collapsed onto a state with a precise value for the measured attributes, relative to that element. This provides one explanation of how the Born rule coefficients effectively act as probabilities as per the measurement postulate constituting a solution to the quantum measurement problem.


=== Dirac notation ===
Using Dirac notation, let the system initially be in the state

|ψ⟩=∑i|i⟩⟨i|ψ⟩,
where the |i⟩s form an einselected basis (environmentally induced selected eigenbasis), and let the environment initially be in the state |ϵ⟩. The vector basis of the combination of the system and the environment consists of the tensor products of the basis vectors of the two subsystems. Thus, before any interaction between the two subsystems, the joint state can be written as

|before⟩=∑i|i⟩|ϵ⟩⟨i|ψ⟩,
where |i⟩|ϵ⟩ is shorthand for the tensor product |i⟩⊗|ϵ⟩. There are two extremes in the way the system can interact with its environment: either (1) the system loses its distinct identity and merges with the environment (e.g. photons in a cold, dark cavity get converted into molecular excitations within the cavity walls), or (2) the system is not disturbed at all, even though the environment is disturbed (e.g. the idealized non-disturbing measurement). In general, an interaction is a mixture of these two extremes that we examine.


==== System absorbed by environment ====
If the environment absorbs the system, each element of the total system's basis interacts with the environment such that

|i⟩|ϵ⟩ evolves into |ϵi⟩,
and so

|before⟩ evolves into |after⟩=∑i|ϵi⟩⟨i|ψ⟩.
The unitarity of time evolution demands that the total state basis remains orthonormal, i.e. the scalar or inner products of the basis vectors must vanish, since ⟨i|j⟩=δij:

⟨ϵi|ϵj⟩=δij.
This orthonormality of the environment states is the defining characteristic required for einselection.


==== System not disturbed by environment ====
In an idealized measurement, the system disturbs the environment, but is itself undisturbed by the environment. In this case, each element of the basis interacts with the environment such that

|i⟩|ϵ⟩ evolves into the product |i,ϵi⟩=|i⟩|ϵi⟩,
and so

|before⟩ evolves into |after⟩=∑i|i,ϵi⟩⟨i|ψ⟩.
In this case, unitarity demands that

⟨i,ϵi|j,ϵj⟩=⟨i|j⟩⟨ϵi|ϵj⟩=δij⟨ϵi|ϵj⟩=δij⟨ϵi|ϵi⟩=δij,
where ⟨ϵi|ϵi⟩=1 was used. Additionally, decoherence requires, by virtue of the large number of hidden degrees of freedom in the environment, that

⟨ϵi|ϵj⟩≈δij.
As before, this is the defining characteristic for decoherence to become einselection. The approximation becomes more exact as the number of environmental degrees of freedom affected increases.
Note that if the system basis |i⟩ were not an einselected basis, then the last condition is trivial, since the disturbed environment is not a function of i, and we have the trivial disturbed environment basis |ϵj⟩=|ϵ′⟩. This would correspond to the system basis being degenerate with respect to the environmentally defined measurement observable. For a complex environmental interaction (which would be expected for a typical macroscale interaction) a non-einselected basis would be hard to define.


=== Loss of interference and the transition from quantum to classical probabilities ===
The utility of decoherence lies in its application to the analysis of probabilities, before and after environmental interaction, and in particular to the vanishing of quantum interference terms after decoherence has occurred. If we ask what is the probability of observing the system making a transition from ψ to ϕ before ψ has interacted with its environment, then application of the Born probability rule states that the transition probability is the squared modulus of the scalar product of the two states:

probbefore(ψ→ϕ)=|⟨ψ|ϕ⟩|2=|∑iψi∗ϕi|2=∑i|ψi∗ϕi|2+∑ij;i≠jψi∗ψjϕj∗ϕi,
where ψi=⟨i|ψ⟩, ψi∗=⟨ψ|i⟩, and ϕi=⟨i|ϕ⟩ etc.
The above expansion of the transition probability has terms that involve i≠j; these can be thought of as representing interference between the different basis elements or quantum alternatives. This is a purely quantum effect and represents the non-additivity of the probabilities of quantum alternatives.
To calculate the probability of observing the system making a quantum leap from ψ to ϕ after ψ has interacted with its environment, then application of the Born probability rule states that we must sum over all the relevant possible states |ϵi⟩ of the environment before squaring the modulus:

probafter(ψ→ϕ)=∑j|⟨after|ϕ,ϵj⟩|2=∑j|∑iψi∗⟨i,ϵi|ϕ,ϵj⟩|2=∑j|∑iψi∗ϕi⟨ϵi|ϵj⟩|2.
The internal summation vanishes when we apply the decoherence/einselection condition ⟨ϵi|ϵj⟩≈δij, and the formula simplifies to

probafter(ψ→ϕ)≈∑j|ψj∗ϕj|2=∑i|ψi∗ϕi|2.
If we compare this with the formula we derived before the environment introduced decoherence, we can see that the effect of decoherence has been to move the summation sign ∑i from inside of the modulus sign to outside. As a result, all the cross- or quantum interference-terms

∑ij;i≠jψi∗ψjϕj∗ϕi
have vanished from the transition-probability calculation. The decoherence has irreversibly converted quantum behaviour (additive probability amplitudes) to classical behaviour (additive probabilities). 
However, Ballentine shows that the significant impact of decoherence to reduce interference need not have significance for the transition of quantum systems to classical limits.
In terms of density matrices, the loss of interference effects corresponds to the diagonalization of the "environmentally traced-over" density matrix.


=== Density-matrix approach ===
The effect of decoherence on density matrices is essentially the decay or rapid vanishing of the off-diagonal elements of the partial trace of the joint system's density matrix, i.e. the trace, with respect to any environmental basis, of the density matrix of the combined system and its environment. The decoherence irreversibly converts the "averaged" or "environmentally traced-over" density matrix from a pure state to a reduced mixture; it is this that gives the appearance of wave-function collapse. Again, this is called "environmentally induced superselection", or einselection. The advantage of taking the partial trace is that this procedure is indifferent to the environmental basis chosen.
Initially, the density matrix of the combined system can be denoted as

ρ=|before⟩⟨before|=|ψ⟩⟨ψ|⊗|ϵ⟩⟨ϵ|,
where |ϵ⟩ is the state of the environment.
Then if the transition happens before any interaction takes place between the system and the environment, the environment subsystem has no part and can be traced out, leaving the reduced density matrix for the system:

ρsys=Trenv(ρ)=|ψ⟩⟨ψ|⟨ϵ|ϵ⟩=|ψ⟩⟨ψ|.
Now the probability of finding the system described by a density matrix ρ in a particular state |ϕ⟩, i.e. the transition probability mentioned above, is given as

probbefore(ψ→ϕ)=⟨ϕ|ρsys|ϕ⟩=⟨ϕ|ψ⟩⟨ψ|ϕ⟩=|⟨ψ|ϕ⟩|2=∑i|ψi∗ϕi|2+∑ij;i≠jψi∗ψjϕj∗ϕi,
where ψi=⟨i|ψ⟩, ψi∗=⟨ψ|i⟩, and ϕi=⟨i|ϕ⟩ etc.
Now the case when transition takes place after the interaction of the system with the environment. The combined density matrix will be

ρ=|after⟩⟨after|=∑i,jψiψj∗|i,ϵi⟩⟨j,ϵj|=∑i,jψiψj∗|i⟩⟨j|⊗|ϵi⟩⟨ϵj|.
To get the reduced density matrix of the system, we trace out the environment and employ the decoherence/einselection condition and see that the off-diagonal terms vanish (a result obtained by Erich Joos and H. D. Zeh in 1985):

ρsys=Trenv(∑i,jψiψj∗|i⟩⟨j|⊗|ϵi⟩⟨ϵj|)=∑i,jψiψj∗|i⟩⟨j|⟨ϵj|ϵi⟩=∑i,jψiψj∗|i⟩⟨j|δij=∑i|ψi|2|i⟩⟨i|.
The transition probability to |ϕ⟩ will then, using the same equation as before the interaction, be given as

probafter(ψ→ϕ)=∑i|ψi|2|ϕi|2=∑i|ψi∗ϕi|2,
which has no contribution from the interference terms

∑ij;i≠jψi∗ψjϕj∗ϕi.
The density-matrix approach has been combined with the Bohmian approach to yield a reduced-trajectory approach, taking into account the system reduced density matrix and the influence of the environment.


=== Operator-sum representation ===
Consider a system S and environment (bath) B, which are closed and can be treated quantum-mechanically. Let ℋS and ℋB be the system's and bath's Hilbert spaces respectively. Then the Hamiltonian for the combined system is

Ĥ=ĤS⊗ÎB+ÎS⊗ĤB+ĤI,
where ĤS,ĤB are the system and bath Hamiltonians respectively, ĤI is the interaction Hamiltonian between the system and bath, and ÎS,ÎB are the identity operators on the system and bath Hilbert spaces respectively. The time-evolution of the density operator of this closed system is unitary and, as such, is given by

ρSB(t)=Û(t)ρSB(0)Û†(t),
where the unitary operator is Û=e−iĤt/ℏ. If the system and bath are not entangled initially, then we can write ρSB=ρS⊗ρB. Therefore, the evolution of the system becomes

ρSB(t)=Û(t)[ρS(0)⊗ρB(0)]Û†(t).
The system–bath interaction Hamiltonian can be written in a general form as

ĤI=∑iŜi⊗B̂i,
where Ŝi⊗B̂i is the operator acting on the combined system–bath Hilbert space, and Ŝi,B̂i are the operators that act on the system and bath respectively. This coupling of the system and bath is the cause of decoherence in the system alone. To see this, a partial trace is performed over the bath to give a description of the system alone:

ρS(t)=TrB[Û(t)[ρS(0)⊗ρB(0)]Û†(t)].
ρS(t) is called the reduced density matrix and gives information about the system only. If the bath is written in terms of its set of orthogonal basis kets, that is, if it has been initially diagonalized, then ρB(0)=∑jaj|j⟩⟨j|. Computing the partial trace with respect to this (computational) basis gives

ρS(t)=∑lÂlρS(0)Âl†,
where Âl,Âl† are defined as the Kraus operators and are represented as (the index l combines indices k and j):

Âl=aj⟨k|Û|j⟩.
This is known as the operator-sum representation (OSR). A condition on the Kraus operators can be obtained by using the fact that Tr⁡[ρS(t)]=1; this then gives

∑lÂl†Âl=ÎS.
This restriction determines whether decoherence will occur or not in the OSR. In particular, when there is more than one term present in the sum for ρS(t), then the dynamics of the system will be non-unitary, and hence decoherence will take place.


=== Semigroup approach ===
A more general consideration for the existence of decoherence in a quantum system is given by the master equation, which determines how the density matrix of the system alone evolves in time (see also the Belavkin equation for the evolution under continuous measurement). This uses the Schrödinger picture, where evolution of the state (represented by its density matrix) is considered. The master equation is

ρ'S(t)=−iℏ[H~S,ρS(t)]+LD[ρS(t)],
where H~S=HS+Δ is the system Hamiltonian HS along with a (possible) unitary contribution Δ from the bath, and LD is the Lindblad decohering term. The Lindblad decohering term is represented as

LD[ρS(t)]=12∑α,β=1Mbαβ([𝐅α,ρS(t)𝐅β†]+[𝐅αρS(t),𝐅β†]).
The {𝐅α}α=1M are basis operators for the M-dimensional space of bounded operators that act on the system Hilbert space ℋS and are the error generators. The matrix elements bαβ represent the elements of a positive semi-definite Hermitian matrix; they characterize the decohering processes and, as such, are called the noise parameters. The semigroup approach is particularly nice, because it distinguishes between the unitary and decohering (non-unitary) processes, which is not the case with the OSR. In particular, the non-unitary dynamics are represented by LD, whereas the unitary dynamics of the state are represented by the usual Heisenberg commutator. Note that when LD[ρS(t)]=0, the dynamical evolution of the system is unitary. The conditions for the evolution of the system density matrix to be described by the master equation are:

the evolution of the system density matrix is determined by a one-parameter semigroup
the evolution is "completely positive" (i.e. probabilities are preserved)
the system and bath density matrices are initially decoupled


== Non-unitary modelling examples ==
Decoherence can be modelled as a non-unitary process by which a system couples with its environment (although the combined system plus environment evolves in a unitary fashion). Thus the dynamics of the system alone, treated in isolation, are non-unitary and, as such, are represented by irreversible transformations acting on the system's Hilbert space ℋ. Since the system's dynamics are represented by irreversible representations, then any information present in the quantum system can be lost to the environment or heat bath. Alternatively, the decay of quantum information caused by the coupling of the system to the environment is referred to as decoherence. Thus decoherence is the process by which information of a quantum system is altered by the system's interaction with its environment (which form a closed system), hence creating an entanglement between the system and heat bath (environment). As such, since the system is entangled with its environment in some unknown way, a description of the system by itself cannot be made without also referring to the environment (i.e. without also describing the state of the environment).


=== Rotational decoherence ===
Consider a system of N qubits that is coupled to a bath symmetrically. Suppose this system of N qubits undergoes a rotation around the |↑⟩⟨↑|,|↓⟩⟨↓| (|0⟩⟨0|,|1⟩⟨1|) eigenstates of Jẑ. Then under such a rotation, a random phase ϕ will be created between the eigenstates |0⟩, |1⟩ of Jẑ. Thus these basis qubits |0⟩ and |1⟩ will transform in the following way:

|0⟩→|0⟩,|1⟩→eiϕ|1⟩.
This transformation is performed by the rotation operator

Rz(ϕ)=(100eiϕ).
Since any qubit in this space can be expressed in terms of the basis qubits, then all such qubits will be transformed under this rotation. Consider the jth qubit in a pure state |ψj⟩⟨ψj| where |ψj⟩=a|0⟩+b|1⟩. Before application of the rotation this state is:

ρj,init=(|a|2ab∗a∗b|b|2).
This state will decohere, since it is not 'encoded' with (dependent upon) the dephasing factor eiϕ. This can be seen by examining the density matrix averaged over the random phase ϕ:

ρj=𝔼[Rz(ϕ)|ψj⟩⟨ψj|Rz†(ϕ)]=∫−∞∞Rz(ϕ)|ψj⟩⟨ψj|Rz†(ϕ)P(dϕ),
where P(⋅) is a probability measure of the random phase, ϕ. Although not entirely necessary, let us assume for simplicity that this is given by the Gaussian distribution, i.e. P(dϕ)=12πσe−12(ϕσ)2dϕ, where σ represents the spread of the random phase. Then the density matrix computed as above is

ρj=(|a|2ab∗e−12σ2a∗be−12σ2|b|2).
Observe that the off-diagonal elements—the coherence terms—decay as the spread of the random phase, σ, increases over time (which is a realistic expectation). Thus the density matrices for each qubit of the system become indistinguishable over time. This means that no measurement can distinguish between the qubits, thus creating decoherence between the various qubit states. In particular, this dephasing process causes the qubits to collapse to one of the pure states in {|0⟩⟨0|,|1⟩⟨1|}. This is why this type of decoherence process is called collective dephasing, because the mutual phases between all qubits of the N-qubit system are destroyed.


=== Depolarizing ===
Depolarizing is a non-unitary transformation on a quantum system which maps pure states to mixed states. This is a non-unitary process because any transformation that reverses this process will map states out of their respective Hilbert space thus not preserving positivity (i.e. the original probabilities are mapped to negative probabilities, which is not allowed). The 2-dimensional case of such a transformation would consist of mapping pure states on the surface of the Bloch sphere to mixed states within the Bloch sphere. This would contract the Bloch sphere by some finite amount and the reverse process would expand the Bloch sphere, which cannot happen.


=== Dissipation ===

Dissipation is a decohering process by which the populations of quantum states are changed due to entanglement with a bath. An example of this would be a quantum system that can exchange its energy with a bath through the interaction Hamiltonian. If the system is not in its ground state and the bath is at a temperature lower than that of the system's, then the system will give off energy to the bath, and thus higher-energy eigenstates of the system Hamiltonian will decohere to the ground state after cooling and, as such, will all be non-degenerate. Since the states are no longer degenerate, they are not distinguishable, and thus this process is irreversible (non-unitary).


== Timescales ==
Decoherence represents an extremely fast process for macroscopic objects, since these are interacting with many microscopic objects, with an enormous number of degrees of freedom in their natural environment. The process is needed if we are to understand why we tend not to observe quantum behavior in everyday macroscopic objects and why we do see classical fields emerge from the properties of the interaction between matter and radiation for large amounts of matter. The time taken for off-diagonal components of the density matrix to effectively vanish is called the decoherence time. It is typically extremely short for everyday, macroscale processes. A modern basis-independent definition of the decoherence time relies on the short-time behavior of the fidelity between the initial and the time-dependent state or, equivalently, the decay of the purity.


== Mathematical details ==
Assume for the moment that the system in question consists of a subsystem A being studied and the "environment" ϵ, and the total Hilbert space is the tensor product of a Hilbert space ℋA describing A and a Hilbert space ℋϵ describing ϵ, that is,

ℋ=ℋA⊗ℋϵ.
This is a reasonably good approximation in the case where A and ϵ are relatively independent (e.g. there is nothing like parts of A mixing with parts of ϵ or conversely). The point is, the interaction with the environment is for all practical purposes unavoidable (e.g. even a single excited atom in a vacuum would emit a photon, which would then go off). Let's say this interaction is described by a unitary transformation U acting upon ℋ. Assume that the initial state of the environment is |in⟩, and the initial state of A is the superposition state

c1|ψ1⟩+c2|ψ2⟩,
where |ψ1⟩ and |ψ2⟩ are orthogonal, and there is no entanglement initially. Also, choose an orthonormal basis {|ei⟩}i for ℋA. (This could be a "continuously indexed basis" or a mixture of continuous and discrete indexes, in which case we would have to use a rigged Hilbert space and be more careful about what we mean by orthonormal, but that's an inessential detail for expository purposes.) Then, we can expand

U(|ψ1⟩⊗|in⟩)
and

U(|ψ2⟩⊗|in⟩)
uniquely as

∑i|ei⟩⊗|f1i⟩
and

∑i|ei⟩⊗|f2i⟩
respectively. One thing to realize is that the environment contains a huge number of degrees of freedom, a good number of them interacting with each other all the time. This makes the following assumption reasonable in a handwaving way, which can be shown to be true in some simple toy models. Assume that there exists a basis for ℋϵ such that |f1i⟩ and |f1j⟩ are all approximately orthogonal to a good degree if i ≠ j and the same thing for |f2i⟩ and |f2j⟩ and also for |f1i⟩ and |f2j⟩ for any i and j (the decoherence property).
This often turns out to be true (as a reasonable conjecture) in the position basis because how A interacts with the environment would often depend critically upon the position of the objects in A. Then, if we take the partial trace over the environment, we would find the density state is approximately described by

∑i(⟨f1i|f1i⟩+⟨f2i|f2i⟩)|ei⟩⟨ei|,
that is, we have a diagonal mixed state, there is no constructive or destructive interference, and the "probabilities" add up classically. The time it takes for U(t) (the unitary operator as a function of time) to display the decoherence property is called the decoherence time.


== Experimental observations ==


=== Quantitative measurement ===
The decoherence rate depends on a number of factors, including temperature or uncertainty in position, and many experiments have tried to measure it depending on the external environment.
The process of a quantum superposition gradually obliterated by decoherence was quantitatively measured for the first time by Serge Haroche and his co-workers at the École Normale Supérieure in Paris in 1996. Their approach involved sending individual rubidium atoms, each in a superposition of two states, through a microwave-filled cavity. The two quantum states both cause shifts in the phase of the microwave field, but by different amounts, so that the field itself is also put into a superposition of two states. Due to photon scattering on cavity-mirror imperfection, the cavity field loses phase coherence to the environment. Haroche and his colleagues measured the resulting decoherence via correlations between the states of pairs of atoms sent through the cavity with various time delays between the atoms.
In July 2011, researchers from University of British Columbia and University of California, Santa Barbara showed that applying high magnetic fields to single molecule magnets suppressed two of three known sources of decoherence. They were able to measure the dependence of decoherence on temperature and magnetic field strength.


== Prevention ==


=== Characterization of coherence in quantum processors ===

Decoherence is a central challenge for the practical realization of quantum computers, which rely on evolution of quantum systems isolated from the environment to perform computation. Two timescales, T₁ and T₂, characterise this challenge and serve as standard metrics for qubit fidelity across most platforms.
The relaxation time T₁ characterizes how quickly a qubit loses energy to its environment as it decays from the excited state |1⟩ to the ground state |0⟩. The excited-state population decays exponentially as

P|1⟩(t)=P|1⟩(0)e−t/T1
The dephasing time T₂ characterizes how quickly phase coherence in the qubit's state decays. In the Bloch sphere picture, T₂ corresponds to the decay of the off-diagonal density matrix elements, which evolve as

ρ01(t)=ρ01(0)e−t/T2
T₂ is commonly measured via the Ramsey interference experiment, in which a qubit is prepared in a superposition state and freely evolves, precessing, for a variable interval. the decay of the resulting oscillation envelope yields T₂, as shown at right. The two timescales are related by

T2≤2T1
with equality only when energy relaxation is the sole source of decoherence. Because gate operations must complete before the quantum states decohere, the timescales T₁ and T₂ together set a practical upper bound on the size of quantum circuits. Extending these times is a major goal of quantum processor engineering.
Typical T₂ values vary substantially across qubit platforms and have improved significantly over time. In superconducting transmon qubits, T₂ values of 50–200 μs are routinely achieved, representing an improvement of roughly five orders of magnitude over the nanosecond-scale coherence of the first charge qubit demonstrated in 1999. Millisecond-scale T₂ times have been demonstrated in fluxonium qubits, where the circuit design suppresses the dominant noise channels of the transmon. Through improvements in fabrication, two-dimensional transmon devices have been able to achieve millisecond T₂ times as well. Trapped ion qubits achieve significantly longer coherence, with T₂ on the order of seconds to even minutes under ideal conditions. Semiconductor spin qubits typically exhibit T₂ in the microsecond range, extendable to hundreds of microseconds through decoupling techniques such as spin echo. Wide variation across platforms reflects differences in the dominant noise mechanisms and operating frequencies of each implementation.


=== Methods and tools ===
Researchers have developed many methods and tools to mitigate or eliminate the negative influences from decoherence. Several typical ways are listed below.


==== Isolation from environment ====
The most basic and direct way to reduce decoherence is to prevent the quantum system from interacting with the environment by any type of isolation. Here are some typical examples of isolation methods.

High vacuum: Placing qubits in an ultra-high vacuum environment to minimize interaction with air molecules.
Cryogenic cooling: Operating quantum systems at extremely low temperatures to reduce thermal vibrations and noise.
Electromagnetic shielding: Enclosing quantum systems in materials that block external electromagnetic fields - such as mu-metal or superconducting materials - reduces decoherence caused by unwanted electromagnetic interference.
Shielding cosmic rays: In August 2020 scientists reported that ionizing radiation from environmental radioactive materials and cosmic rays may substantially limit the coherence times of qubits if they aren't shielded adequately which may be critical for realizing fault-tolerant superconducting quantum computers in the future.
Better materials: Fabricating qubits from special materials, like highly pure or isotopically enriched ones, to minimize intrinsic noise of the material, including noise from defects or nuclear spins.
Circuit design: Optimizing the coherence ability when designing the construction of quantum circuits, similar to the concern in classical circuits.
Mechanical and optical isolation: Using equipment like vibration isolation tables and acoustic isolation materials, reducing sources of mechanical noise, and shielding against external light—common in physical experiments.


==== Quantum error correction ====

One of the most powerful tools for combating quantum decoherence is Quantum error correction (QEC). QEC schemes encode quantum information redundantly across multiple physical qubits, allowing for the detection and correction of errors without directly measuring the quantum state. These QEC protocols rely on the assumption that errors affect only a small fraction of qubits at any given time, enabling the detection and correction of errors through redundant encoding. Here are some representative QEC protocols.

Shor code: One of the first quantum error correction codes, it encodes a single qubit into nine physical qubits to protect against both bit-flip and phase-flip errors.
Steane code: A 7-qubit code that provides error correction for arbitrary errors.
Surface codes: A more scalable error correction code that uses a 2D lattice of qubits with high threshold for errors.
Bosonic codes: A type of quantum error-correcting code designed specifically to protect quantum information in continuous-variable systems.
However, QEC comes at a significant cost: it requires a large number of physical qubits to encode a single logical qubit, and fault-tolerant error correction methods introduce additional computational overhead.


==== Dynamical decoupling ====
Dynamical decoupling (DD) is another typical quantum control technique used against decoherence, especially for systems that are coupled to noisy environments. DD involves applying an external sequence of control pulses to the quantum system at strategically timed intervals to average out environmental interactions. This technique effectively manipulates the irreversible component of quantum systems interact with surrounding environment by the external controllable interactions. Dynamical decoupling has been experimentally demonstrated in various systems, including trapped ions and superconducting qubits. Here are some examples of representative sequences.

Spin echo (SE): SE is the consisting of a single π-pulse, which inverts the state of system.
Periodic dynamical decoupling (PDD): Applying control pulse periodically, PDD averages out the influence of the environment and decoupling the qubit.
Carr–Purcell–Meiboom–Gill (CPMG) sequence: CPMG is an extension of SE. It applies a series of π-pulses.


== See also ==


== References ==


== Further reading ==
Bacciagaluppi, Guido (21 April 2020) [3 November 2003]. "The Role of Decoherence in Quantum Mechanics". Stanford Encyclopedia of Philosophy. Retrieved 3 January 2022.
Collins, Graham P. (17 October 2005). "Quantum Bug: Qubits might spontaneously decay in seconds". Scientific American.
Schlosshauer, Maximilian (2007). Decoherence and the Quantum-to-Classical Transition (1st ed.). Berlin/Heidelberg: Springer. Bibcode:2007dqct.book.....S.
Joos, E.; et al. (2003). Decoherence and the Appearance of a Classical World in Quantum Theory (2nd ed.). Berlin: Springer.
Omnes, R. (1999). Understanding Quantum Mechanics. Princeton: Princeton University Press.
Zurek, Wojciech H. (2003). "Decoherence and the transition from quantum to classical – REVISITED", arXiv:quant-ph/0306072 (An updated version of PHYSICS TODAY, 44:36–44 (1991) article)
Schlosshauer, Maximilian (23 February 2005). "Decoherence, the Measurement Problem, and Interpretations of Quantum Mechanics". Reviews of Modern Physics. 76 (2004): 1267–1305. arXiv:quant-ph/0312059. Bibcode:2004RvMP...76.1267S. doi:10.1103/RevModPhys.76.1267. S2CID 7295619.
Halliwell, J. J.; Perez-Mercader, J.; Zurek, Wojciech H., eds. (21 March 1996). The Physical Origins of Time Asymmetry. Part 3: Decoherence. ISBN 0-521-56837-4.
Berthold-Georg Englert, Marlan O. Scully & Herbert Walther, Quantum Optical Tests of Complementarity, Nature, Vol 351, pp 111–116 (9 May 1991) and (same authors) The Duality in Matter and Light Scientific American, pg 56–61, (December 1994). Demonstrates that complementarity is enforced, and quantum interference effects destroyed, by irreversible object-apparatus correlations, and not, as was previously popularly believed, by Heisenberg's uncertainty principle itself.
Mario Castagnino, Sebastian Fortin, Roberto Laura and Olimpia Lombardi, A general theoretical framework for decoherence in open and closed systems, Classical and Quantum Gravity, 25, pp. 154002–154013, (2008). A general theoretical framework for decoherence is proposed, which encompasses formalisms originally devised to deal just with open or closed systems.
