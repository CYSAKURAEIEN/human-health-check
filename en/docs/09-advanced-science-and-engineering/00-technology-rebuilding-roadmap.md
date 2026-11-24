# Technology Rebuilding Roadmap

> **Technology is not a set of separate inventions but a tree: each one stands on others. Only when you know the shape of the tree do you know which part to grow first**

## ⚠️ What this chapter is for

This chapter is the "map" of the whole handbook. It links the parts on food, metallurgy, pharmaceuticals, energy and scientific knowledge into one route, and explains **what each technology needs first, where it gets stuck, and what shortcuts you can take**.

```
Be realistic:
- Modern industry depends on a global division of labour: one mobile phone
  needs the cooperation of dozens of countries and millions of people.
  A small community cannot rebuild that
- The realistic goal is: secure survival first, then gradually recover to roughly
  the technology level of the late 19th century
  (agriculture, iron and steel making, steam power, basic electricity and chemical
  industry, medicine and hygiene guided by germ theory)
- Every step needs enough people and enough division of labour: a few dozen people
  can sustain only simple farming and crafts; metallurgy, chemical industry and
  machine building need a larger society

The three most important rules:
1. Survival first: water, food, shelter, hygiene, medical care. Until these are
   stable, nothing else matters
2. Preserve and use first, make later: the steel, copper wire and books in the ruins
   are far better than anything you can make yourself
3. Knowledge is the biggest shortcut: we know the answers, so we do not need to
   repeat thousands of years of our ancestors' detours
```

---

## 1. Overview of the technology tree

```
Stage 0  Survival
         Water · Food · Shelter · Hygiene · First aid · Fire
            │
Stage 1  Agriculture and basic crafts
         Crops and livestock · Seed saving · Food preservation · Pottery ·
         Textiles · Woodworking · Lime · Soap making · Charcoal
            │
Stage 2  Metallurgy and machinery
         Copper and bronze → Iron → Steel
         Waterwheels · Windmills · Gears · Lathes · Standard gauges
            │
Stage 3  Basic chemicals and materials
         Alkali · Sulphuric acid · Glass · Cement · Paper and printing · Refractories
            │
Stage 4  Power
         Boilers · Steam engines · (Stirling engines)
            │
Stage 5  Electricity
         Batteries · Generators · Electric motors · Telegraph · Electric light
            │
Stage 6  Advanced chemicals and medicine
         Electrolysis (chlor-alkali) · Fertiliser · Drug purification ·
         Microscopes and microbiology
            │
Stage 7  Electronics
         Vacuum tubes · Semiconductors · Radio · Computers
         (Extremely hard to make from scratch; the realistic approach is to use
          components that have survived)
```

The stages do not follow one another strictly. Knowing about electromagnetic induction lets people generate electricity from water power before they have steam engines, and knowing germ theory saves lives at Stage 0.

![Technology rebuilding roadmap: built upwards stage by stage from Stage 0 Survival to Stage 7 Electronics. Red arrows are the prerequisites stated in the text (iron smelting needs charcoal, glass needs lime, boilers need steel plate, steam engines need precisely machined cylinders, generators need copper wire and magnets, fertiliser needs sulphuric acid, electrolysis needs electricity, glass makes lenses and vacuum tubes); the blue dashed line is the shortcut of generating electricity from water and wind power without waiting for the steam engine](../../images/tech-roadmap.svg)

*Figure: the technology tree is built from the bottom up; the stages do not follow one another strictly, and only the main dependencies are shown*

---

## 2. Key points of each stage

| Stage | Key technologies | Prerequisites | Main bottleneck | Related chapters in this handbook |
|------|---------|---------|---------|---------------|
| 0 Survival | Water purification, shelter, first aid | None | Knowledge | [Wilderness Survival](../03-wilderness-survival/README.md), [First Aid and Family Health](../01-first-aid-and-family-health/README.md) |
| 1 Agriculture and crafts | Grain, seed saving, preservation, pottery, woodworking | Seed, land, tools | Seed (traditional varieties), soil fertility | [Growing Plants and Raising Animals](../04-farming-and-animal-husbandry/README.md), [Everyday Living Skills](../07-everyday-living-skills/README.md) |
| 2 Metallurgy and machinery | Iron and steel making, forging, waterwheels, lathes | Charcoal (large forests), ore, refractories | Fuel, precision machining | [Metallurgy](../05-metallurgy/README.md), [Engineering Mechanics and Materials](01-engineering-mechanics-and-materials.md) |
| 3 Basic chemicals | Alkali, acid, glass, cement, paper | High-temperature kilns and furnaces, raw materials | Sulphuric acid, high temperature | [Chemistry](../08-basic-science/03-chemistry.md) |
| 4 Power | Boilers, steam engines | Steel plate, precisely machined cylinders | Boiler safety, machining accuracy | [Thermodynamics and Engines](03-thermodynamics-and-engines.md) |
| 5 Electricity | Generators, batteries, telegraph | Copper wire, insulating materials, magnets | Copper, insulation | [Electrical Engineering and Electronics](02-electrical-engineering-and-electronics.md) |
| 6 Chemicals and medicine | Chlor-alkali, fertiliser, purification | Electricity, glassware | Scale, purity | [Pharmaceuticals](../06-pharmaceuticals/README.md) |
| 7 Electronics | Semiconductors, radio | Materials of extremely high purity, vacuum | Almost everything | [Electrical Engineering and Electronics](02-electrical-engineering-and-electronics.md) |

---

## 3. Key bottlenecks

### 3.1 Fuel and energy

```
Every technology needs energy:
- Iron smelting: the charcoal needed to make 1 kg of iron is often several times
  the weight of the iron; one iron furnace burns through a large area of forest a year
- In history, many regions cut down all their forests to make charcoal for iron

What to do:
✓ Rotational felling of woodland: divide the woodland into many plots and cut only
  one each year; after cutting, let the stumps sprout again (many broadleaf trees can),
  going round the full cycle in a dozen or so years
✓ Find coal: coal has a high calorific value but contains sulphur, and using it
  directly to smelt iron makes the iron brittle (historically it first had to be made into coke)
✓ Water and wind power: use them for blowing air, hammering and grinding,
  saving labour and fuel
✓ Save energy: good stoves and furnaces, insulation, using waste heat
```

For the calorific values of fuels see [Physics – Heat](../08-basic-science/02-physics.md#5-heat); for woodland and charcoal see [Lighting and Energy – Storing fuel safely](../07-everyday-living-skills/06-lighting-and-energy.md#storing-fuel-safely).

For estimating firewood use and woodland area, and coppice rotation, see [Firewood and Woodland Management](../04-farming-and-animal-husbandry/09-firewood-and-woodland-management.md).

### 3.2 Precision machining: the "mother machine" of machines

```
The cylinder of a steam engine must fit closely around the piston, the rotor of a
generator must not touch the stator, and screws and nuts must be interchangeable —
all of these need precision. And precision is "bootstrapped":

1. Flat surfaces: the three-plate lapping method
   - Prepare three cast-iron plates (or hard stone slabs). Lap A against B, B against C
     and C against A, in turn
   - Lapping two plates against each other only makes them fit each other
     (one may be concave and the other convex)
   - When three plates are lapped in turn, the only shape that lets all three pairs
     fit is a flat plane
   - You can get very flat surfaces from nothing, without any existing precision tools

2. Straight lines and right angles: once you have a flat surface, you can make
   straightedges and squares

3. The lathe: called "the mother of machine tools"
   - It can turn cylinders and round holes, and with a lead screw it can cut threads
   - With a lathe of ordinary accuracy you can make parts of higher accuracy,
     and use those parts to build a better lathe

4. Standard gauges: standard rules, standard threads and gauges shared by the
   whole community
   → parts become interchangeable; when a machine breaks you replace a part
     instead of rebuilding the whole machine
```

For hands-on filing, drilling, tapping, scraping and lathe work see [Bench Work and Machining](../05-metallurgy/09-bench-work-and-machining.md); for setting up measurement standards see [Measurement and the Scientific Method](../08-basic-science/00-measurement-and-scientific-method.md); for machine elements see [Engineering Mechanics and Materials – Machine elements](01-engineering-mechanics-and-materials.md#11-machine-elements).

### 3.3 Sulphuric acid

```
Called "the mother of the chemical industry": treating ores, making fertiliser,
storage batteries, and making other acids and many chemicals all need it
In ancient times small amounts were made by heating green vitriol (iron(II) sulphate);
in modern times it was mass-produced by burning sulphur, then oxidising and absorbing
the gas (see the Chemistry chapter)
⚠️ Concentrated sulphuric acid is extremely corrosive, the production process gives off
   toxic gases, and it needs acid-resistant equipment (lead, glass, ceramics)
```

### 3.4 Glass

```
Without glass there are no: lenses (spectacles, microscopes, telescopes), laboratory
glassware, thermometers, vacuum tubes, or sealed medicine bottles
Needs: quartz sand, soda ash (or plant ash), lime, and a kiln reaching about 1400-1500°C
```

For how to make it see [Pottery, Glass and Papermaking](../07-everyday-living-skills/11-pottery-glass-and-papermaking.md#glass).

### 3.5 Paper and printing: spreading knowledge

```
Knowledge that exists only in a few people's heads is very fragile
✓ Papermaking: pound plant fibres (bark, hemp, bamboo, rice straw) into pulp →
  lift a thin layer with a screen → press and dry in the sun
✓ Printing: woodblocks, movable type
✓ Education: get more people able to read, do arithmetic and understand scientific principles
```

For paper and ink see [Pottery, Glass and Papermaking – Papermaking](../07-everyday-living-skills/11-pottery-glass-and-papermaking.md#papermaking); for teaching and preserving records see [Education and Knowledge Preservation](../07-everyday-living-skills/12-education-and-knowledge-preservation.md).

### 3.6 People

```
In the end, technology lives in people. More important than any machine are:
- Literacy and arithmetic
- The habit of recording and passing things on
- Organisation for division of labour and cooperation
- Apprenticeship: experienced people training the young is how crafts survive
```

See [Education and Knowledge Preservation](../07-everyday-living-skills/12-education-and-knowledge-preservation.md) and [Record-keeping, Trade and Division of Labour](../07-everyday-living-skills/13-record-keeping-trade-and-division-of-labour.md).

---

## 4. Resources in the ruins: use first, make later

For a long time after civilisation collapses, **the modern materials preserved in the ruins are better than anything you can make yourself**.

For identifying, sorting, safely dismantling and melting down metals, see [Scrap Metal Recycling and Aluminium Casting](../05-metallurgy/05-scrap-metal-recycling-and-aluminium-casting.md).

| Resource | Source | Use |
|------|------|------|
| Steel | Reinforcing bar, structural sections, car chassis, springs | Forging tools and blades (car leaf springs are very good tool steel) |
| Copper wire | Electric wires and cables, coils of electric motors and transformers | Generators, motors, telegraph |
| Magnets | Loudspeakers, electric motors, hard drives | Generators, compasses |
| Generators | Car alternators | Driven by water or wind power to charge 12 V batteries |
| Electric motors | All kinds of appliances, electric vehicles, treadmills | A permanent-magnet DC motor turned backwards is a generator |
| Storage batteries | Cars, electric vehicles, uninterruptible power supplies | Store electrical energy; the lead can be recycled |
| Solar panels | Rooftops, street lights | Generating electricity (they can last for decades) |
| Bearings, gears, chains | Cars, bicycles, machinery | Waterwheels, windmills, machines |
| Glass | Windows, bottles | Containers, greenhouses; remelting needs high temperature |
| Books | Libraries, schools, bookshops | **The most valuable**: secondary-school and university science and engineering textbooks, manuals on agriculture, medicine and engineering |
| Hand tools | Hardware shops, homes | Saws, hammers, chisels, files, pliers, spanners, hand drills |
| Seeds | Seed shops, farms | Traditional varieties first (you can save seed from them) |

```
⚠️ Safety when dismantling:
- Collapse: do not go into badly damaged buildings
- Asbestos: insulation in old buildings, asbestos roofing sheets. Do not break them
  and do not breathe in the dust
- Chemicals: do not open anything you do not recognise, and do not mix anything
- Batteries: the acid in lead-acid batteries is corrosive; damaged lithium batteries can catch fire
- Capacitors: large capacitors (such as inside a microwave oven) can still store
  a lethal charge after the power is off
- Refrigerants: they leak out when you take apart air conditioners and fridges
```

---

## 5. Shortcuts you can take

We know history's "answers", so many detours need not be repeated:

```
✓ Germ theory: go straight to handwashing, boiling, disinfection and isolation,
  without passing through the "miasma theory"
✓ Nutrition: know straight away that bean sprouts prevent scurvy, brown rice
  prevents beriberi and iodised salt prevents goitre
✓ Mature designs: build overshot waterwheels, improved ploughs and steam engines
  with a separate condenser straight away, without starting from the most primitive versions
✓ Electromagnetic induction: once you know the principle, all you need is copper wire
  and magnets (which you can get from the ruins) to generate electricity from water
  and wind power before you have steam engines
✓ The scientific method: controlled experiments and records make every attempt add to knowledge
✓ Unified weights, measures and standards: unify them from the start, without going through
  a stage of conflicting local standards

What you cannot skip:
✗ Materials: without good enough steel, copper and glass, knowing the principle
  will not let you build the machine
✗ Precision: it has to be bootstrapped step by step
✗ Scale: many technologies only pay off at a large enough scale
✗ Skills: crafts such as forging, firing kilns and woodworking can only be
  mastered by practising again and again
```

---

## 6. What a small community can achieve

| Community size | Technology it can realistically sustain |
|---------|-------------------|
| A few households to a few dozen people | Farming, livestock, seed saving, food preservation, woodworking, textiles, soap making, simple pottery, first aid and hygiene; using materials and tools from the ruins |
| A few hundred people | In addition: small-scale iron smelting and forging, waterwheels and windmills, lime burning, brick making, simple machining, small-scale power generation, schools |
| A few thousand people or more | In addition: steel making, glass, papermaking and printing, basic chemical industry, steam engines, telegraph, fairly complete medical care |
| Cooperation over a larger region | Fertiliser industry, iron and steel industry, power grids, pharmaceutical industry, electronics industry |

---

## 7. Knowledge and items to preserve first

```
Books (in order of priority):
- [ ] This handbook (a printed paper copy)
- [ ] Agriculture: crop growing, soil and fertilisers, pests and diseases,
      animal husbandry and veterinary medicine
- [ ] Medicine: first aid, manuals for primary-care doctors, drug handbooks, nursing
- [ ] Secondary-school mathematics, physics, chemistry and biology textbooks (the full set)
- [ ] Basic university textbooks: higher mathematics, general physics, general chemistry,
      machine design, electrical engineering
- [ ] Engineering handbooks: machine design handbook, building structures, electricians' handbook
- [ ] Crafts: casting, forging, welding, woodworking, ceramics, glass

Items:
- [ ] Seeds of traditional varieties
- [ ] Hand tools
- [ ] Measuring tools: steel tape measure, vernier calipers, square, spirit level,
      thermometer, balance and weights
- [ ] Magnifying glass, microscope (if you have one)
- [ ] Copper wire, magnets, small generators, storage batteries, solar panels
```

---

## Related chapters

- ⏭️ [Engineering Mechanics and Materials](01-engineering-mechanics-and-materials.md) - structures, materials, machine elements
- ⏭️ [Electrical Engineering and Electronics](02-electrical-engineering-and-electronics.md) - generation, transmission, telegraph, semiconductors
- ⏭️ [Thermodynamics and Engines](03-thermodynamics-and-engines.md) - steam engines, internal combustion engines, refrigeration, wind and water power
- ⏭️ [Higher Mathematics](04-higher-mathematics.md), [Advanced Chemistry](05-advanced-chemistry.md), [Modern Physics](06-modern-physics.md) - deeper theoretical tools
- 🔗 [Basic Science](../08-basic-science/README.md) - the foundations of mathematics, physics, chemistry and biology
- 🔗 [Long-term Collapse Survival](../03-wilderness-survival/06-long-term-collapse-survival.md) - the overall strategy for long-term survival

---

**Remember: survive first, then preserve knowledge, then build upwards step by step. Every generation stands on the shoulders of the one before — do not let those shoulders break.**
