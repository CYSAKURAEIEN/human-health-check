# Engineering Mechanics and Materials

> **Will the house fall down, how much can the bridge carry, will the shaft break — engineering mechanics lets you work these out in advance, instead of finding out when it collapses**

## ⚠️ What this chapter is for

This chapter explains the principles and basic calculations behind structural and mechanical design, to help you understand "why doing it this way is stronger".

```
⚠️ Important:
- The calculations in this chapter are simplified, for understanding and rough estimates
- Houses that people live in, bridges, lifting equipment and pressure vessels cause
  injury and death if they fail:
  have them designed by professionals if you can; if you cannot, use a larger
  safety factor and test first
- The material strengths given are typical values; real materials (especially home-made
  iron, salvaged old material, and timber with knots) may be much weaker
```

For the mathematics and physics you need, see [Mathematics](../../../docs/08-基础科学知识/01-数学.md) and [Physics – Motion and force](../../../docs/08-基础科学知识/02-物理.md#一运动与力).

---

## 1. Combining and resolving forces

```
A force has a size and a direction, and forces can be added like arrows
(the parallelogram rule)

A force at a slant can be resolved into a horizontal and a vertical component:
  Horizontal component = F × cos θ
  Vertical component = F × sin θ

Example: pull a box with a rope angled 30° upwards, with a pull of 100 N
  Force pulling the box horizontally = 100 × cos30° ≈ 87 N
  Force lifting it upwards = 100 × sin30° = 50 N
```

### 1.1 The wider the angle between ropes, the greater the tension

```
Lift a load with two ropes, with angle α between the two ropes:
  Tension in each rope = weight ÷ (2 × cos(α/2))

  Angle 0° (both ropes vertical): each carries half the weight
  Angle 120°: tension in each rope = the whole weight
  Angle approaching 180° (ropes almost horizontal): tension tends to infinity

⚠️ When lifting, keep the angle between the ropes below about 90°. Do not pull
   washing lines or rope bridges too flat: the flatter the rope,
   the greater the force on it and the more easily it breaks
```

---

## 2. Static equilibrium and moments

```
Conditions for an object to stay still (equilibrium):
1. The resultant of all forces is zero (it does not move)
2. The sum of all moments is zero (it does not turn)

Moment = force × lever arm (the perpendicular distance from the line of the force
to the turning point)

Example: a 4 m beam supported at both ends, with a 400 kg load hung 1 m from the left end
  Take moments about the left end: force at right support × 4 = 400 × 1
  → the right end carries 100 kg
  The left end carries 400 - 100 = 300 kg
  → whichever end the load is nearer, that support carries more
```

---

## 3. Stress and strain

### 3.1 Stress

```
Stress = force ÷ cross-sectional area (σ = F ÷ A), unit pascal (Pa)
  1 MPa (megapascal) = 1 N/mm² ≈ about 10 kg carried on each cm²

Whether a material fails depends on the stress, not on the size of the force:
  under the same pull, a thick rope is safer than a thin one
```

### 3.2 Strain and elasticity

```
Strain = extension ÷ original length (ε = ΔL ÷ L), no unit

Hooke's law: within the elastic range, stress = elastic modulus × strain (σ = E × ε)
  The larger the elastic modulus E, the "stiffer" the material
  and the less it deforms under load

Beyond the elastic limit: it does not return to its original shape when unloaded
(plastic deformation); further still, it breaks
  - Ductile materials (steel, copper, wrought iron): bend and deform visibly before
    breaking, giving warning
  - Brittle materials (cast iron, stone, glass, concrete): break suddenly
    with almost no deformation
```

### 3.3 Properties of common materials (typical values)

| Material | Elastic modulus E (GPa) | Tensile strength (MPa) | Compressive strength (MPa) | Characteristics |
|------|-----------------|---------------|---------------|------|
| Mild steel | About 200 | About 370-500 (yield about 235) | Similar to tensile | Tough; structural steel |
| Grey cast iron | About 100 | About 150-250 | About 600-1000 | Good in compression, poor in tension; brittle |
| Copper (annealed) | About 110-120 | About 200-250 | | Extremely ductile; conducts electricity |
| Aluminium alloy | About 70 | About 150-300 | | Light |
| Pine, Chinese fir (along the grain, clear wood) | About 10 | About 60-100 | About 30-50 | Strength drops greatly with knots or across the grain |
| Bamboo | About 10-20 | Often over 100 | About 40-80 | Light and tough; good in tension |
| Concrete | About 25-30 | About 2-4 | About 20-40 | Good in compression; can take almost no tension |
| Brick masonry | | Very low | About 2-10 | Compression only |
| Granite | About 50 | About 5-15 | About 100-250 | Compression only |

```
⚠️ The values above are "the limit it can bear"; in design you must also divide
   by a safety factor (see below)
⚠️ The design strength of timber is usually taken as only a fraction of that of small
   clear specimens (knots, cracks, moisture content, long-term loads)
```

### 3.4 Safety factors

```
Allowable working stress = ultimate strength of the material ÷ safety factor

Choosing a safety factor (rule-of-thumb ranges):
- Consistent material quality and well-known loads (e.g. certified steel structures): about 1.5-2
- Timber structures, home-made or salvaged materials: 3 or more
- Ropes and chains for lifting: 5 or more
- Where people are underneath or failure would be serious: larger still
- Shock loads (dropping, impact): the real force may be several times the static weight

✓ Test a newly made load-bearing member first with a load heavier than it will
  actually carry, with everyone standing well clear
```

---

## 4. Members in compression and buckling

```
A short, thick column: fails by being crushed (depends on compressive strength)
A long, slender column: suddenly bows to one side and becomes unstable long before
reaching its compressive strength ("buckling")

Euler's formula (slender bar pinned at both ends):
  Critical load P = π² × E × I ÷ L²
  I: second moment of area of the cross-section
     (rectangle I = width × height³ ÷ 12; circle I = π × diameter⁴ ÷ 64)
  L: length

→ Double the length and the load it can carry falls to 1/4
→ To prevent buckling: make it thicker, or add cross-braces or diagonal braces partway
  (dividing a long column into several short ones)
→ When using bamboo poles or thin wooden poles as props, tie them together sideways in the middle
```

---

## 5. Bending of beams

### 5.1 Bending moment

```
A beam bends under load: the bottom is stretched and the top is squashed
(simply supported beam)

Maximum bending moment of a simply supported beam (resting on supports at both ends):
  A single point load P at mid-span:  M = P × L ÷ 4
  A uniformly distributed load q (N/m): M = q × L² ÷ 8

→ Double the span and the bending moment becomes 4 times as large (distributed load)
```

### 5.2 Cross-section: why a plank should be "on edge"

```
Maximum bending stress in a beam σ = M ÷ W
  W: section modulus; for a rectangular section W = width × height² ÷ 6

Strength is proportional to the square of the depth, but only proportional to the width:
  A 10 cm × 20 cm timber beam
  - On edge (20 cm deep): W = 0.1 × 0.2² ÷ 6 ≈ 6.7 × 10⁻⁴ m³
  - Laid flat (10 cm deep): W = 0.2 × 0.1² ÷ 6 ≈ 3.3 × 10⁻⁴ m³
  → On edge it is twice as strong as laid flat, and 4 times as stiff (resists bending)

I-beams and channel sections are made in these shapes for the same reason: they put
the material at the top and bottom edges, as far from the centre as possible,
to get the most strength from the least material
```

### 5.3 Estimating how much a timber beam can carry

```
Example: a pine beam with a 4 m span, section 10 cm wide and 20 cm deep (on edge),
    using an allowable design stress of 10 MPa (safety factor already included)
  Allowable bending moment M = 10 × 10⁶ × 6.7 × 10⁻⁴ ≈ 6700 N·m
  Distributed load q = 8M ÷ L² = 8 × 6700 ÷ 16 ≈ 3350 N/m
  → about 340 kg/m (you must still subtract the self-weight of the beam and floor)

Deflection (how far it sags) must also be limited: for floor beams usually
no more than about 1/250 of the span, otherwise the floor bounces when you
walk on it and the plaster cracks
```

### 5.4 Cantilever beams

```
Fixed at one end and free at the other (balconies, overhanging eaves, jib arms):
  With a point load P at the end, the bending moment at the fixed end M = P × L
  → For the same load and length, a cantilever's bending moment is 4 times that of
    a simply supported beam; the fixed end must be very solid
```

---

## 6. Triangles and trusses

```
The triangle is the only polygon whose shape cannot change as long as its side
lengths stay the same
  - A four-sided frame turns into a parallelogram when you push it
  - Add one diagonal brace to divide it into two triangles, and it becomes stable

Truss: a structure made of many triangles (roof trusses, bridge trusses, towers)
  - Each member is only in tension or only in compression, not in bending,
    so thin members can span great distances
  - The joints must be firmly connected
  - The simplest triangular roof truss: when load presses down from above,
    the two sloping members are in compression and the bottom tie is in tension
    (it holds the two feet together so the truss does not spread outwards)

✓ The wall frames and roof trusses of timber houses all need diagonal braces
✓ Add triangular wooden blocks to the corners of door frames and wooden boxes
```

For timber construction methods see [Long-term Shelter – Simple timber framing](../../../docs/07-日常生活技能/05-长期住所.md#简易木结构).

![Triangles and trusses: a four-sided frame turns into a parallelogram when pushed; a triangle keeps its shape as long as its sides stay the same length; adding a diagonal brace divides the frame into two triangles and makes it stable; in a triangular roof truss the sloping members are in compression and the tie is in tension; a bridge truss is made of many triangles](../../images/truss-triangle.svg)

*Figure: the members of a truss are only in tension or only in compression, not in bending, and the joints must be firmly connected; add diagonal braces to wall frames and roof trusses, and triangular wooden blocks to the corners of door frames and wooden boxes*

---

## 7. Arches, domes and walls

### 7.1 Arches

```
Stone, brick and concrete are very strong in compression and very weak in tension
The shape of an arch turns the load into compression along the arch, carried to both
ends, so the material is only in compression
  → even stone, which cannot take tension, can span great distances

The ideal arch shape: hang a chain by both ends and let it sag naturally into a curve
  (a catenary); turn that upside down and you have the ideal arch, in pure
  compression with no bending

⚠️ An arch pushes outwards at both sides: the abutments and walls at the ends must be
   thick and heavy enough, or tie rods must hold the two ends together; otherwise the
   feet of the arch slide outwards and it collapses

Zhaozhou Bridge (Sui dynasty, about 1400 years ago): a single-span stone arch with small
  arches opened in its shoulders, which both reduce its self-weight and let floodwater
  through; it still stands today
```

### 7.2 Masonry walls

```
✓ Compression only, no tension: walls must be vertical, and the load must bear on
  the middle of the wall
✓ Lay bricks and stones with staggered joints (vertical joints in one course offset from
  those in the course below), never with continuous vertical joints
✓ Wall height and thickness must be in proportion: a tall, thin wall falls over easily
✓ Openings for doors and windows need a lintel or an arch above them
✓ Earthquake zones: ring beams and tie columns "hoop" the walls together
  (see Long-term Shelter – earthquake resistance)
```

For earthquake-resistance measures see [Long-term Shelter – Earthquake resistance: life or death for earth houses](../../../docs/07-日常生活技能/05-长期住所.md#抗震-生土房屋的生死线).

---

## 8. Suspension cables and ropes

```
Ropes can only take tension
Suspension bridges and ropeways: anchored at both ends, sagging in the middle

Under a uniform load, the horizontal tension in a suspension cable ≈ q × L² ÷ (8 × f)
  q: load per m (N/m); L: span; f: depth of sag in the middle
→ The smaller the sag (the flatter the cable), the greater the tension
→ The sag is usually about 1/10 of the span
→ The anchor points at both ends must carry the full tension and must be very solid

Knots weaken a rope (at the knot it may keep only about half its strength)
```

---

## 9. Foundations

```
The weight of a building is finally carried by the soil under its foundation

Approximate bearing capacity of different soils (pressure per unit area it can carry,
rough ranges):
- Silt, soft soil, backfill: very low; do not build directly on it
- Ordinary clay, silty soil: about 100-200 kPa (about 10-20 t/m²)
- Dense sand, gravel: about 200-400 kPa
- Rock: higher

Foundation base area = total weight carried down from the building ÷ bearing capacity
  → the softer the soil, the wider the foundation must be

✓ Dig down to undisturbed natural soil; do not build on backfill
✓ The base of the foundation must be below the frost line (in northern China); otherwise
  frost heave in winter will crack the walls
✓ Provide good drainage: when the ground is soaked and softened,
  its bearing capacity drops sharply
```

For choosing a site and wall foundations see [Long-term Shelter](../../../docs/07-日常生活技能/05-长期住所.md).

---

## 10. Materials science

### 10.1 Why metals can be forged

```
A metal is made of many small grains; inside each crystal, rows of atoms can slip
  → metals can bend, be forged and be drawn into wire without breaking (plasticity)

Work hardening: metal becomes harder and more brittle after repeated bending and hammering
  (iron wire breaks if you bend it back and forth)
Annealing: heat it and cool it slowly to remove the hardening and restore plasticity
  → put the work back in the fire partway through forging; cold-worked copper must be
    annealed before you can keep working it
```

### 10.2 Iron and steel: carbon decides everything

```
By carbon content (the division used in this handbook's metallurgy part):
  Wrought iron: carbon < 0.2%        soft and tough, easy to forge, cannot be hardened
  Steel:        carbon about 0.2-2%  can be quench-hardened; both strong and tough
  Pig iron:     carbon about 2-4%    low melting point, can be cast, but very brittle;
                                     cannot be forged

  The more carbon, the harder and more brittle; the less carbon, the softer and tougher
```

### 10.3 Principles of heat-treating steel

```
Above about 727°C steel changes into another crystal structure (austenite),
in which carbon can dissolve

Quenching: heat to about 780-850°C (carbon steel), then plunge quickly into water or oil
  → the carbon atoms have no time to get out and are "frozen" in the crystal lattice,
    forming a very hard, very brittle structure (martensite)

Tempering: after quenching, reheat to a lower temperature (about 200-350°C)
  and hold it there for a while
  → reduces brittleness and restores some toughness; the higher the tempering
    temperature, the tougher and less hard it becomes

Annealing: heat, then cool slowly in the furnace → softest, easiest to work
Normalising: heat, then cool in air → a uniform structure

A handy trick for judging the quenching temperature:
  Steel loses its magnetism above about 770°C
  → hold a magnet against it while heating; when the magnet just stops sticking,
    the temperature is close to the quenching temperature
```

For the hands-on procedure and tempering colours see [Metalworking](../../../docs/05-冶金技术/04-金属加工技术.md).

### 10.4 Common alloys

| Alloy | Composition | Characteristics and uses |
|------|------|-----------|
| Bronze | Copper + tin (about 10%) | Harder than copper, corrosion-resistant, casts well; bells, bearings |
| Brass | Copper + zinc | Easy to machine, corrosion-resistant; valves, parts |
| Solder | Tin + lead (or lead-free solders such as tin + copper) | Low melting point; for soldering wires and sheet iron; ⚠️ lead solder is toxic |
| Stainless steel | Iron + chromium (10.5% or more) + nickel etc. | Does not rust easily |
| Cast iron | Iron + carbon (2-4%) + silicon | Cast pots, stoves, machine-tool beds |

### 10.5 Ceramics and refractories

```
Earthenware: ordinary clay, fired at about 800-1000°C; porous and lets water through
Porcelain: kaolin (china clay) + feldspar + quartz, fired at about 1200-1300°C or more;
  dense and watertight
Bricks: clay shaped, dried in the sun, then fired; underfired bricks are weak
  and are damaged by water

Refractories: the linings of smelting furnaces, kilns and boilers must withstand
high temperatures
  - Fireclay (clay high in alumina), kaolin
  - Mix in grog — already fired material (crushed old firebrick, broken porcelain) —
    to reduce shrinkage and cracking
  - Furnace linings are one of the bottlenecks of metallurgy: ordinary clay melts and
    softens at high temperatures
```

### 10.6 Concrete

```
Cement + sand + gravel + water → as the cement hydrates, it binds the sand and stones
into a solid mass

A common rough mix (by volume): cement : sand : gravel ≈ 1 : 2 : 3
  More water makes it easier to pour but weaker; use just enough,
  do not add water freely

Curing: after pouring, keep it damp for at least 7 days (cover with straw mats and
  sprinkle with water); do not let it dry out quickly
  Below 5°C in winter it gains strength very slowly, and freezing damages it

Reinforced concrete: concrete takes the compression, steel bars take the tension
  The reinforcing bars in a beam go on the side in tension (at the bottom in a
  simply supported beam), so the two work together
```

For salvaging cement and recycled aggregate see [Lime and Building Materials – Cement and concrete](../../../docs/07-日常生活技能/16-石灰与建筑材料.md#水泥和混凝土-先回收).

### 10.7 Timber

```
✓ Strong along the grain; weak across the grain and splits easily
✓ Moisture content affects strength and movement: dry it before use
  (see Woodworking and Tool Maintenance)
✓ Knots, sloping grain and cracks greatly reduce strength; for load-bearing members
  choose straight-grained timber without large knots
✓ Preventing rot: keep it dry and ventilated, and off the ground
  (stand wooden posts on stone bases)
```

For drying timber see [Woodworking and Tool Maintenance – Timber](../../../docs/07-日常生活技能/09-木工与工具维护.md#木材).

---

## 11. Machine elements

### 11.1 Shafts and bearings

```
Plain bearings: the shaft turns in a hole, with lubricating oil between them
  - Materials: bronze, cast iron, hardwood (oil-soaked hardwood makes low-speed bearings)
  - Must be kept lubricated and clean; running dry wears them out and heats them quickly
Rolling bearings: balls or rollers, very low friction (salvage them from old machinery)
```

### 11.2 Gears

```
Two meshing gears must have the same tooth size (module)
  Pitch circle diameter = module × number of teeth
  Speed ratio = inverse ratio of the numbers of teeth
  Torque transmitted = inverse ratio of the speeds (ignoring friction)

Wooden gears: traditional waterwheels, windmills and mills all used hardwood gears;
when a tooth wears, you can replace that single wooden tooth
```

### 11.3 Belts and chains

```
Belt drives: simple, cushion shocks, and slip when overloaded, protecting the machine;
  speed ratio of two pulleys = inverse ratio of their diameters
Chain drives: do not slip and transmit large forces (bicycle chains can be salvaged and reused)
```

### 11.4 Crank and connecting rod

```
Turns back-and-forth straight-line motion into rotation (steam engines, treadle
sewing machines), or the other way round (reciprocating pumps, sawmills)
```

### 11.5 Flywheels

```
A heavy wheel that stores energy as it turns
(kinetic energy = ½ × moment of inertia × angular velocity²)
→ turns intermittent power (one push of the piston at a time) into smooth rotation
```

### 11.6 Threads and fasteners

```
Pitch: the distance a thread advances in one turn
Only a common thread standard lets bolts and nuts be interchanged
✓ From the very start, fix a few standard thread sizes for the whole community,
  and make standard taps and dies
```

For bootstrapping precision machining (lapping three plates against each other, the lathe) see [Technology Rebuilding Roadmap – Precision machining](../../../docs/09-进阶科学与工程/00-技术重建路线图.md#32-精密加工-机器的母机).

---

## Related chapters

- ⏮️ [Technology Rebuilding Roadmap](../../../docs/09-进阶科学与工程/00-技术重建路线图.md) - where structures and machinery fit in the whole picture
- ⏭️ [Electrical Engineering and Electronics](../../../docs/09-进阶科学与工程/02-电气工程与电子学.md)
- ⏭️ [Thermodynamics and Engines](../../../docs/09-进阶科学与工程/03-热力学与动力机械.md)
- 🔗 [Metalworking](../../../docs/05-冶金技术/04-金属加工技术.md) - hands-on heat treatment
- 🔗 [Long-term Shelter](../../../docs/07-日常生活技能/05-长期住所.md) - building houses
- 🔗 [Physics](../../../docs/08-基础科学知识/02-物理.md) - forces, levers, simple machines

---

**Remember: a good structure lets every material do what it does best — stone in compression, steel and rope in tension, triangles holding their shape. Calculate first, then test, and only then let people stand on it.**
