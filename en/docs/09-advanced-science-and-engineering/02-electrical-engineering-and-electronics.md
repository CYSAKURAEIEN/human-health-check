# Electrical Engineering and Electronics

> **Electricity lets energy be sent over long distances and shared out whenever it is needed, and lets information travel at the speed of light. Starting from a copper wire and a magnet, you can walk into the age of electricity**

## ⚠️ Safety first

- ⚡ 220 V alternating current can kill; high voltage can arc to you and injure you even if you do not touch it, just by getting close
- ⚡ Large capacitors can still store a lethal charge after the power is off; discharge them before dismantling or repairing anything
- 🔥 A short-circuited storage battery produces an enormous current: the wires instantly glow red and catch fire; damaged lithium batteries can catch fire and explode
- 🔥 Wires that are too thin and loose connections heat up and cause fires
- ✓ When modifying or connecting household wiring, or connecting a generator, always disconnect from the outside grid (to stop power feeding back and injuring others)

For everyday electrical safety see [Household Electrical Safety](../../../docs/07-日常生活技能/08-家庭用电安全.md); for the basics of voltage, current and Ohm's law see [Physics – Electricity and magnetism](../../../docs/08-基础科学知识/02-物理.md#七电与磁).

---

## 1. Further DC circuits

### 1.1 Kirchhoff's laws

```
Current law: the sum of currents flowing into a node = the sum of currents flowing out
(charge does not pile up)
Voltage law: going once round any closed loop, the sum of voltage rises = the sum of voltage drops

With these two laws plus Ohm's law, you can work out the current and voltage at
every point in any circuit, however complicated
```

### 1.2 Internal resistance of a source

```
Every real battery and generator has an internal resistance r:
  Terminal voltage = EMF - current × r
→ The more current it delivers, the more the terminal voltage drops
→ When a battery is nearly flat its internal resistance rises, and the voltage
  collapses as soon as a load is connected
```

![DC circuits: Ohm's law U = I × R; in series the current is the same everywhere, total resistance adds up, U = U₁ + U₂; in parallel every branch has the same voltage, 1/R_total = 1/R₁ + 1/R₂, I = I₁ + I₂; a real battery has internal resistance, terminal voltage = EMF − current × r; a lead-acid battery is about 2 V per cell, 6 cells in series = 12 V](../../images/dc-circuits.svg)

*Figure: the voltages and currents in series and parallel circuits are the simplest cases of Kirchhoff's two laws; the current drawn by a 220 V, 1100 W electric kettle = 1100 ÷ 220 = 5 A*

### 1.3 Capacitors and inductors

```
Capacitor: two conductors separated by an insulating layer; it stores charge
  Charge Q = C × U; energy stored = ½ × C × U²
  How fast it charges and discharges: time constant τ = R × C
  (after about 5τ it is essentially fully charged or discharged)
  → blocks DC, passes AC; filtering; energy storage

Inductor (coil): opposes changes in current
  Energy stored = ½ × L × I²
  → suddenly breaking a circuit that contains inductance (electric motors, relay coils)
    produces a very high reverse voltage, and sparks appear at the switch
```

---

## 2. Alternating current

### 2.1 Basic concepts

```
The voltage and current of alternating current vary periodically as a sine wave:
  u = Um × sin(2π × f × t)

Grid in China: frequency 50 Hz (50 cycles per second)
RMS value: the value of direct current that would produce the same heating effect
  RMS value = peak value ÷ √2
  Household 220 V is the RMS value; the peak is about 311 V

Why use alternating current: a transformer can easily step it up or down (see below),
which suits transmission over long distances
```

### 2.2 Inductors and capacitors in AC circuits

```
Inductive reactance XL = 2π × f × L (the higher the frequency, the more a coil
"blocks" the current)
Capacitive reactance XC = 1 ÷ (2π × f × C) (the higher the frequency, the more easily
it passes through a capacitor)

When current and voltage are out of step (there is a phase difference):
  Real power P = U × I × cos φ (the part that actually does work)
  cos φ is called the power factor
  → inductive loads such as electric motors have a lower power factor,
    so the line has to carry more current
```

### 2.3 Three-phase power

```
Three live wires, whose voltages are each 1/3 of a cycle apart
  Phase voltage (live to neutral) 220 V, line voltage (between live wires) 380 V
  Line voltage = √3 × phase voltage

Why industry uses three-phase power:
- Three-phase motors are simple, start by themselves and run smoothly
- Transmitting the same power uses less wire
```

---

## 3. Generators

### 3.1 Principle

```
Electromagnetic induction: when the magnetic flux through a coil changes,
a voltage appears across the coil
  Induced voltage ∝ number of turns × rate of change of flux

Alternator: a magnet (or electromagnet) and a coil turn relative to each other,
giving alternating current
DC generator (dynamo): a commutator (brushes + a segmented copper ring) turns the AC
into current that always flows the same way
  You can also use an alternator + rectifier diodes (see section 10)

The output voltage depends on: speed of rotation, number of turns in the coil,
strength of the magnetic field
```

### 3.2 Speed and frequency

```
Output frequency of an alternator: f = number of pole pairs × revolutions per minute ÷ 60
  One pair of poles (2 poles) needs 3000 revolutions per minute to give 50 Hz
  The more poles, the lower the speed needed
→ Waterwheels and windmills turn very slowly: either step up the speed with gears or belts,
  or build a generator with many poles
```

### 3.3 Small-scale generation that is realistic

```
Option 1: a car alternator (salvaged from a scrapped car)
- Built-in rectifier and voltage regulator; outputs about 14 V DC,
  just right for charging a 12 V battery
- Needs a fairly high speed to generate, so usually needs a pulley to step up the speed
- Excitation needs the battery to supply a little current first
  (wire it as it was in the car)

Option 2: run a permanent-magnet DC motor backwards as a generator
- The permanent-magnet motors from treadmills, power tools and electric vehicles generate
  electricity when turned by an outside force
- The faster it turns, the higher the voltage
- Usually add a diode so current from the battery cannot flow back and turn the motor

Option 3: make your own
- Wind coils from enamelled wire and use salvaged strong magnets (neodymium magnets)
  to build a disc-type (axial-flux) generator
- Needs patient adjustment of the gap between magnets and coils

Power sources: waterwheels, windmills, bicycles (human power about 75-100 W,
only enough for a little lighting and charging)
```

For estimating water and wind power see [Thermodynamics and Engines – Other power sources](../../../docs/09-进阶科学与工程/03-热力学与动力机械.md#八水力风力和畜力).

![Generator principle: a magnet and a coil turning relative to each other give alternating current; a commutator turns AC into current that always flows the same way; frequency equals pole pairs times revolutions per minute divided by 60; a permanent-magnet DC motor run backwards generates electricity, with a diode to stop battery current flowing back](../../images/generator-principle.svg)

*Figure: one pair of poles needs 3000 revolutions per minute to give 50 Hz; waterwheels and windmills turn slowly, so step up the speed with belts or gears; when connecting to household wiring, always disconnect from the outside grid*

---

## 4. Electric motors

```
Principle: a current-carrying wire in a magnetic field feels a force → the coil turns
DC motor: a commutator keeps switching the direction of current in the coil so it keeps
turning one way
Three-phase induction motor (the most common industrial motor):
  Three-phase current produces a rotating magnetic field that drags the rotor round,
  turning slightly slower than the field
  Field speed (synchronous speed) = 60 × f ÷ number of pole pairs
  (3000 rpm at 50 Hz with 2 poles)
  → simple, robust and durable, needing almost no maintenance

Motors and generators are the same machine: feed in electrical energy and it turns;
turn it with an outside force and it generates electricity
```

---

## 5. Transformers

```
Two coils wound on the same iron core:
  U₁ ÷ U₂ = N₁ ÷ N₂ (ratio of voltages = ratio of turns)
  I₁ ÷ I₂ = N₂ ÷ N₁ (ratio of currents = inverse ratio of turns)
  → power is essentially unchanged (efficiency is usually above 95%)

✓ Only works with alternating current (the magnetic field of DC does not change,
  so nothing is induced)
✓ The core is a stack of thin, insulated silicon-steel sheets, to reduce heating
  from eddy currents in the core
⚠️ A transformer can turn low voltage into high voltage, which can just as well kill
```

---

## 6. Transmission and distribution

### 6.1 Why transmit at high voltage

```
Power lost in the line = I² × R
For a given power transmitted, the higher the voltage, the smaller the current
and the smaller the loss

Example: send 10 kW over two copper wires, each 1 km long and 10 mm²
  Resistance of the copper = 1.7 × 10⁻⁸ × 1000 ÷ (10 × 10⁻⁶) ≈ 1.7 Ω;
  out and back, two wires about 3.4 Ω

  At 220 V: current about 45 A, line loss = 45² × 3.4 ≈ 6900 W,
    voltage drop along the line about 150 V → it simply cannot be delivered
  At 2200 V: current about 4.5 A, line loss = 4.5² × 3.4 ≈ 69 W → less than 1% lost
```

### 6.2 Wires and protection

```
✓ Choose wire size by current: household socket circuits usually use 2.5 mm² copper wire
  (with a 16 A breaker)
  The longer the run, the thicker the wire must be (voltage drop)
✓ Every circuit must have a fuse or circuit breaker to prevent fires from short circuits
  and overloads
✓ Tighten and wrap joints well; copper joined directly to aluminium corrodes and heats up
✓ Earthing: earth the metal casings of appliances, so that leakage current flows into
  the ground rather than through a person
✓ A residual-current device (30 mA) protects against electric shock
```

For practical household wiring see [Household Electrical Safety](../../../docs/07-日常生活技能/08-家庭用电安全.md).

### 6.3 Small off-grid power systems

```
Generation (solar panels / wind / water)
  → charge controller (prevents overcharging and over-discharging)
  → battery bank (storage)
  → DC appliances (12 V or 24 V lights, charging)
  → or through an inverter to 220 V AC

Estimating energy: daily use (Wh) = Σ (power of each appliance × hours used per day)
  Battery capacity must cover several days of use when it is cloudy and windless
```

For installing a solar system see [Lighting and Energy – Small-scale solar power](../../../docs/07-日常生活技能/06-照明与能源.md#小型太阳能).

---

## 7. Batteries and energy storage

| Type | Voltage per cell | Characteristics | Cautions |
|------|---------|------|------|
| Lead-acid battery | About 2.0 V (6 cells = 12 V) | Cheap, recyclable, simple technology | Gives off hydrogen when charging, so ventilate; do not discharge deeply (recharging at about half discharged makes it last much longer) |
| Lithium-ion battery | About 3.6-3.7 V (4.2 V fully charged) | Light, stores a lot of energy | Catches fire if overcharged, over-discharged, damaged or overheated; must have a protection circuit |
| Nickel-iron battery | About 1.2 V | Extremely durable, lasts decades, tolerates overcharging and over-discharging | Lower efficiency, high self-discharge |
| Dry cell (zinc-manganese) | About 1.5 V | Cannot be recharged | |

```
Capacity: Ah (ampere-hours); energy stored (Wh) = voltage (V) × capacity (Ah)
  A 12 V, 100 Ah battery ≈ 1200 Wh (only about half is really usable,
  to protect the battery)

Charging voltage for lead-acid batteries: about 13.8-14.4 V (12 V battery)
⚠️ The sulphuric acid in lead-acid batteries is corrosive and lead is toxic;
   wear gloves and goggles when removing or fitting them
```

For battery safety see [Lighting and Energy – Battery safety](../../../docs/07-日常生活技能/06-照明与能源.md#蓄电池安全).

---

## 8. The telegraph and communication

### 8.1 The telegraph

```
The simplest long-distance communication: one wire (with the earth as the return path),
a battery, a key and a receiver
  - The receiver can be a buzzer driven by an electromagnet, or a coil that
    deflects a compass needle
  - Letters and numbers are represented by combinations of long and short signals
    (Morse code)
  → by the mid-19th century it already linked the continents
```

### 8.2 Morse code

| Letter | Code | Letter | Code | Letter | Code |
|------|------|------|------|------|------|
| A | ·— | J | ·——— | S | ··· |
| B | —··· | K | —·— | T | — |
| C | —·—· | L | ·—·· | U | ··— |
| D | —·· | M | —— | V | ···— |
| E | · | N | —· | W | ·—— |
| F | ··—· | O | ——— | X | —··— |
| G | ——· | P | ·——· | Y | —·—— |
| H | ···· | Q | ——·— | Z | ——·· |
| I | ·· | R | ·—· | | |

| Number | Code | Number | Code |
|------|------|------|------|
| 1 | ·———— | 6 | —···· |
| 2 | ··——— | 7 | ——··· |
| 3 | ···—— | 8 | ———·· |
| 4 | ····— | 9 | ————· |
| 5 | ····· | 0 | ————— |

```
Rules: a dash (—) is 3 times as long as a dot (·); pause 3 dot-lengths between letters
and 7 dot-lengths between words
SOS: ···———··· (sent continuously, with no pauses inside)
Chinese: historically the "Chinese telegraph code" was used: each Chinese character
corresponds to a four-digit number, and the digits are sent in Morse code

Morse code can also be sent by light, flag signals, tapping or whistle
```

For distress signals see [Basic Survival Skills – Distress signals](../../../docs/03-野外生存/00-基础生存技能.md#求救信号).

### 8.3 How the telephone works

```
Microphone: sound causes vibration → changes a resistance (carbon-granule microphone)
or induces a current in a coil → the current varies with the sound
Earpiece: the varying current passes through an electromagnet → attracts a thin iron
diaphragm and makes it vibrate → produces sound
```

### 8.4 Radio

```
When a current changes rapidly it radiates electromagnetic waves into space,
travelling at the speed of light
  Wavelength = speed of light ÷ frequency (λ = c ÷ f)
  Aerial length is usually 1/4 or 1/2 of the wavelength

LC oscillating circuit: made of a coil and a capacitor; it oscillates at its natural frequency
  f = 1 ÷ (2π × √(L × C))
  → a transmitter uses it to produce waves of a particular frequency,
    and a receiver uses it to select a station (tuning)

Modulation: "adding" sound to a high-frequency electromagnetic wave
  Amplitude modulation (AM): varies the strength of the wave;
  frequency modulation (FM): varies the frequency

Crystal radio (needs no power supply):
  long aerial + earth wire + coil and variable capacitor (tuning) + diode (detection)
  + high-impedance earphone
  → can receive fairly strong nearby medium-wave broadcasts

⚠️ Receiving radio needs no licence; transmitting requires a licence obtained under the law.
   Transmitting without permission interferes with important communications
   such as aviation and emergency services
```

For emergency communication see [Emergency Communication and Family Reunification](../../../docs/02-灾难应对/06-应急通信与寻亲.md).

---

## 9. Electrical measurement

```
Galvanometer: a coil placed beside a magnet (or a compass); the needle deflects
when current flows
  Simple version: wind a few dozen turns of wire round the outside of a compass;
  the needle deflects when current flows
Ammeter: galvanometer + a very small resistance in parallel (a shunt)
Voltmeter: galvanometer + a very large resistance in series

Multimeter: measures voltage, current and resistance (find one among salvaged goods;
very useful)
  ⚠️ To measure current, the multimeter goes in series with the circuit; to measure
     voltage, it goes in parallel. Measuring voltage on the current range
     is a direct short circuit
```

If you have no meter you can trust, calibrate current by electrolytic copper deposition and voltage with a Daniell cell or by electrical heating; see [Rebuilding Measurement Standards – Electrical](../../../docs/08-基础科学知识/09-计量基准的重建.md#72-电学).

---

## 10. Semiconductors and electronics

### 10.1 Semiconductors

```
Conductors (copper, aluminium): conduct well
Insulators (rubber, glass, ceramics, dry wood): conduct almost not at all
Semiconductors (silicon, germanium): in between, and their conductivity can be controlled

Doping: adding a tiny amount of another element to pure silicon
  N-type: extra free electrons; P-type: extra "holes"

⚠️ Making semiconductor devices needs silicon of extremely high purity (impurities below
   one part in a billion), a clean environment and precision equipment; starting from
   scratch is almost impossible
   → the realistic approach: preserve and salvage existing electronic components
```

### 10.2 Diodes

```
P-type and N-type semiconductor joined together (a PN junction): current can flow
in one direction only
  When conducting, a silicon diode has a voltage drop of about 0.7 V across it

Uses:
- Rectification: turning AC into DC (a bridge rectifier uses 4 diodes,
  then a capacitor for smoothing)
- Stopping current flowing backwards (a generator charging a battery)
- Detection (radio)
- Light-emitting diodes (LEDs): light up when current flows; efficient and long-lasting
- Solar cells: essentially a large-area PN junction that produces a voltage in light
```

### 10.3 Transistors

```
A small current (or voltage) controls a large current:
- As an amplifier: makes weak signals stronger (radios, loudspeaker amplifiers)
- As a switch: on or off → the basis of digital circuits
```

### 10.4 From switches to computers

```
Logic gates: built from transistors (or relays, vacuum tubes)
  AND gate: output is 1 only when both inputs are 1
  OR gate: output is 1 when either input is 1
  NOT gate: output is the opposite of the input
  NAND gate: every other logic circuit can be built from this one kind of gate alone

From logic gates you can build: adders (binary addition), memory (flip-flops)
→ combine these and you have a computer's processor

Historical order: relay computers → vacuum-tube computers → transistors → integrated circuits
Relays (switches worked by electromagnets) are slow but simple, and are an option
  for building logic circuits when there are no semiconductors
```

For binary see [Mathematics – Practical algorithms](../../../docs/08-基础科学知识/01-数学.md#十实用算法).

### 10.5 Vacuum tubes

```
The earliest electronic amplifying device in history: in an evacuated glass tube,
a heated cathode emits electrons, and a grid controls the current flowing to the anode
Needs: glassworking, a vacuum pump, metal wire, sealing techniques
→ easier than semiconductors, but still needs a fairly high level of industry
```

---

## Related chapters

- ⏮️ [Technology Rebuilding Roadmap](../../../docs/09-进阶科学与工程/00-技术重建路线图.md) - where electric power fits in the whole picture; electrical equipment that can be salvaged from the ruins
- ⏮️ [Engineering Mechanics and Materials](../../../docs/09-进阶科学与工程/01-工程力学与材料.md)
- ⏭️ [Thermodynamics and Engines](../../../docs/09-进阶科学与工程/03-热力学与动力机械.md) - power to drive generators
- 🔗 [Physics – Electricity and magnetism](../../../docs/08-基础科学知识/02-物理.md#七电与磁) - Ohm's law, basics of electromagnetic induction
- 🔗 [Lighting and Energy](../../../docs/07-日常生活技能/06-照明与能源.md) - using generators, solar power and batteries in practice
- 🔗 [Household Electrical Safety](../../../docs/07-日常生活技能/08-家庭用电安全.md)
- 🔗 [Sheet and Wire – Wire](../../../docs/05-冶金技术/11-板材与线材.md#四线材) - drawing copper wire, insulating electric wire

---

**Remember: a magnet, a coil of copper wire and a waterwheel can light the first lamp; a wire and a telegraph key can send a message far away.**
