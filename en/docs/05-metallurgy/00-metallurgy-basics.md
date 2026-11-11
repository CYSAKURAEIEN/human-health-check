# Metallurgy Basics

> **An introduction to metallurgy - learning the basics of smelting metal from scratch**

## ⚠️ Safety first

**Metallurgy is high-risk work! Before you start, you must understand:**

- 🔥 Working temperatures can exceed 1300°C
- ☠️ Risk of carbon monoxide poisoning (colourless, odourless and highly toxic)
- 💥 Molten metal spatters explosively on contact with water
- 🌡️ Severe burns from high temperatures
- 🏭 Heavy-metal pollution
- ☠️ Metal fumes: the white fumes from heating galvanised parts or melting brass cause "metal fume fever"; roasting sulphide ores releases choking sulphur dioxide, and some ores also give off white fumes containing arsenic
- ☠️ **Do not touch lead or mercury**: do not melt lead, do not use mercury to extract gold, and keep pregnant women and children away from every smelting site

**Always work outdoors, in a well-ventilated place, away from where people live!**

```
What this chapter is for:
- It covers the basics common to all smelting: principles, furnaces, charcoal,
  judging temperature by the colour of the fire, identifying ore, safety
- The actual steps for smelting iron and copper are in later chapters
- In the first few decades after civilisation collapses, the steel, copper and
  aluminium in the ruins are far quicker to get and better in quality than
  anything home-smelted. Salvage, re-forge and remelt first; smelting from ore
  is the long-term plan for when salvaged material runs out
```

For salvaging scrap metal see [Scrap metal recovery and aluminium casting](../../../docs/05-冶金技术/05-废旧金属回收与铝铸造.md); for how to build blowing equipment in detail see [Blowing equipment and forges](../../../docs/05-冶金技术/08-鼓风设备与锻炉.md).

---

## 1. Basic principles of metallurgy

### 1.1 What is metallurgy?

**In short:** the process of extracting metal from ore.

**The chemistry:**
```
Metal oxide + carbon (reducing agent) → metal + carbon dioxide
Example: Fe₂O₃ + 3C → 2Fe + 3CO↑
```

```
What actually happens in the furnace:
1. The air blown in burns the charcoal: C + O₂ → CO₂, giving off a lot of heat
2. The CO₂ rises through the glowing charcoal and is reduced to carbon monoxide:
   CO₂ + C → 2CO
3. The carbon monoxide rises and strips the oxygen from the ore:
   Fe₂O₃ + 3CO → 2Fe + 3CO₂
4. Mud, sand and other impurities in the ore combine with the flux and melt into
   slag, which runs off; the metal stays behind

→ The real reducing agent is mainly carbon monoxide, so the furnace must be
  "rich in carbon, short of oxygen"
→ This is also why carbon monoxide is very concentrated around the furnace mouth
  and the slag hole
```

**The two kinds of ore are treated differently:**
- Oxide ores (magnetite, haematite, limonite, malachite, cassiterite): smelt directly with charcoal
- Sulphide ores (chalcopyrite, chalcocite, galena, pyrite): first roast them in air to burn off the sulphur and turn them into oxides, then smelt (see [5.4 Ore concentration](#54-ore-concentration))

For the basics of chemical reactions see [Chemistry](../../../docs/08-基础科学知识/03-化学.md).

### 1.2 Key elements

| Element | Role | Notes |
|------|------|------|
| **Ore** | Raw material | A natural mineral containing metal |
| **Fuel** | Provides heat | Charcoal, coke |
| **Reducing agent** | Takes away the oxygen | Usually carbon (charcoal) |
| **Flux** | Lowers the melting point | Limestone, quartz |
| **Forced air** | Raises the temperature | Supplies more oxygen |

**How to choose a flux:**
- Ore with a lot of mud and sand (quartz) → add limestone or shells; the two combine into a slag that melts easily
- Ore with a lot of lime → add quartz sand
- In bloomery smelting the iron and quartz in the ore itself combine into slag (losing some of the iron); beginners can leave out the flux at first, watch how the slag flows, and adjust
- Find the right amount by experience; record the proportions and how the slag ran every time

**What slag does:** it carries the impurities away and also covers the metal, stopping it from being oxidised again. Slag that flows well (like thin syrup, able to run out of the slag hole) shows the temperature and proportions are right; slag that is thick and sticky and clogs the furnace shows the temperature is too low or the flux is wrong.

### 1.3 Temperatures needed

| Metal | Melting point | Furnace temperature needed | Difficulty |
|------|------|----------|------|
| Copper | 1085°C | 1200°C | ⭐⭐ Easy |
| Gold | 1064°C | 1200°C | ⭐⭐ Easy |
| Silver | 962°C | 1100°C | ⭐⭐ Easy |
| Iron (bloomery) | Does not melt | 1100-1300°C | ⭐⭐⭐ Fairly hard |
| Iron (liquid pig iron) | About 1150°C (4% carbon) | 1300-1400°C | ⭐⭐⭐⭐ Hard |
| Tin (melting tin metal) | 232°C | 300°C | ⭐ Very easy |
| Tin (smelting from cassiterite) | 232°C | Above about 1000°C | ⭐⭐⭐ Needs forced air and strong reduction |

**Key:**
- Open charcoal fire: ~700-800°C (not enough)
- Charcoal + forced air: 1200-1400°C (can smelt copper)
- Charcoal + strong forced air + refractory materials: 1300-1400°C (can make liquid pig iron)

> Pure iron melts at 1538°C, but ironmaking does not need to reach that temperature: the bloomery process reduces the iron to sponge iron while it stays solid; pig iron, because it contains about 4% carbon, melts at around 1150°C.

**Why the "furnace temperature needed" is higher than the melting point:** the metal has to be heated right through, the slag has to flow, and the metal cools as it is poured, so the furnace is usually 100-200°C hotter than the melting point. For the melting points and pouring temperatures of lead, zinc, aluminium and other metals see [Advanced casting – Melting points and pouring temperatures of common metals](../../../docs/05-冶金技术/07-铸造进阶.md#11-常用金属的熔点和浇注温度).

---

## 2. Building a smelting furnace

### 2.1 Simple clay furnace (beginner)

**Suitable for:** copper, tin, lead and other low-melting-point metals

> ⚠️ Lead is toxic. This book does not recommend smelting or melting lead yourself; for the reasons see [Other metals – Lead](../../../docs/05-冶金技术/10-其他金属.md#三铅).

#### Materials:
- Clay: 50-100 kg
- Sand: 20 kg (mixed into the clay to strengthen it)
- Rice straw / hay: 1-2 kg (prevents cracking)
- Stones: a number of them (for the furnace base)

**Which soil will do:** soil that is sticky when wet and can be rolled into a coil as thick as a chopstick and bent into a ring without breaking will do. If there is too much sand it will not roll into a coil; pure clay that is too sticky cracks easily as it dries, so mix in more sand. For how to find clay see [Pottery, glass and papermaking – What kind of soil makes pottery](../../../docs/07-日常生活技能/11-陶瓷玻璃与造纸.md#什么样的土能做陶).

#### Building steps:

**Step 1: Choose the site**
- Level ground, cleared of anything that burns
- No buildings within 10 m, and no houses downwind
- Close to water (for safety)

```
More on choosing the site:
✓ Slightly raised, well-drained sandy ground; not in a hollow where water
  collects, and not on concrete
  (damp in the ground and water in concrete burst the furnace floor and the
  ground when heated)
✓ Put up a tall shelter, open on all sides, to keep off the rain; its roof at
  least 2 m above the furnace mouth, and not made of thatch
✓ The water is for putting out fires and rinsing burns: keep buckets in a fixed
  place a few m away, never in front of the furnace or near the slag hole or the
  pouring area
✓ Keep away from haystacks, woodpiles and the edge of woodland; no houses
  downwind of the prevailing wind
```

**Step 2: Lay the foundation**
```
[Top view]
○ = air inlet
═ = stones

   Front
   ║
 ╔═══╗
 ║ ○ ║← air inlet (10 cm across)
 ╚═══╝
 ┌───┐
 │base│← raised 30 cm on stones
 └───┘
```

- Raise it 30-50 cm on stones (keeps out damp)
- Leave an air inlet

**Step 3: Mix the fireclay**
```
Recipe:
- Clay: 70%
- Fine sand: 25%
- Chopped rice straw: 5%
- Water: as needed, until it is plastic
```

**Mixing:** tread and knead it repeatedly for 30 minutes

```
How to tell the clay is ready:
✓ Squeeze a handful into a ball: it does not stick to your hand, and when broken
  the inside is even, with no dry lumps or air bubbles
✓ Roll a coil as thick as your thumb and bend it into a U: only fine cracks on
  the outside, and it does not break
✗ It runs as soon as you squeeze it → too much water; spread it out to dry a while
✗ It snaps when bent → too dry or too much sand; add water or clay
✓ Once mixed, cover with a damp cloth or plastic sheet overnight and knead it
  again the next day for a more even mix
```

**Step 4: Build the furnace wall**
- Wall thickness: 10-15 cm
- Inside diameter: 30-40 cm
- Height: 50-60 cm
- Floor: sloping, so slag can be drained

```
How to build it:
1. On the foundation, coil clay strips round and round upwards, each round
   about 5 cm high; press and smear each round into the one below with your
   fingers, do not just stack them
2. Each time it is about 15 cm higher, pause to let the lower part firm up a
   little before carrying on, or it will slump
3. You can also use a wooden bucket, a woven basket or a tightly tied bundle of
   straw as an inner form, then pull it out or burn it out afterwards
4. Tuyere: leave a hole about 10-15 cm above the floor, angled slightly
   downwards at the centre of the hearth
5. Slag hole / copper tap hole: leave a small hole at the lowest point of the
   floor, plugged with clay during smelting
6. Smooth the inner wall; the outer wall can be left rougher
```

**Step 5: Drying (crucial!)**
- Dry in the shade for 3-5 days (direct sun makes it crack)
- Then bake slowly over a low fire for 2-3 days
- Day 1: low fire for 30 minutes, let it go out, repeat 3 times
- Day 2: low fire for 2 hours
- Day 3: medium fire for 4 hours

```
Why so slowly: water in the wall turning suddenly into steam swells and cracks
the wall, and can even blow pieces off
How to tell it is dry right through:
✓ The colour has gone from dark to light, evenly all over, with no dark damp patches
✓ It does not feel cold to the touch, and sounds crisp rather than dull when tapped
✗ The wall gives off a lot of steam while baking, or damp marks appear on the
  outside → not dry yet; keep the fire low
In rain or humid weather, dry it for a few more days
```

**Step 6: High-temperature firing**
- Fire it hard for 6-8 hours
- The clay hardens and shrinks slightly
- Patch any cracks with clay

```
Patching cracks: fine cracks (under about 2 mm) can be left; for wide cracks,
  once the furnace has cooled, scrape the crack wider, wet it, press in clay of
  the same mix until full, then dry it over a low fire
Check before every smelt: if the wall has thinned or a crack goes right
  through, repair or rebuild it
```

#### Blowing equipment

**Simple bellows (essential!):**

```
[Side view]

Moving board ↓
┌─────┐
│     │  leather / cloth
│  □  │  ←air
└──║──┘
   ║← bamboo tube / wooden pipe
   ↓
 furnace
```

**How to make it:**
1. Wooden frame: 40×30×15 cm
2. Cover the top with leather or heavy canvas
3. Make an opening in the bottom and connect a bamboo tube
4. Put the bamboo tube into the furnace's air inlet
5. Compress the air by hand or foot

```
⚠️ Note:
- Bamboo tubes and wooden pipes must not go straight into the furnace; they will
  burn. Set a pipe of fired fireclay (the tuyere) into the furnace wall, and run
  the bamboo tube only to the outer end of the tuyere
- The bellows needs an intake valve (a flap of leather over the intake hole,
  closed when you press down and open when you lift), or each stroke will suck
  hot gas from the furnace back into the bellows
- A single bellows blows in puffs, so the furnace temperature rises and falls;
  the simplest fix is two bellows worked in turn
```

**Advanced version:**
- Double-chamber bellows (blows on both the press and the release)
- Continuous blast, more efficient

For how to make skin bellows, pot bellows, double-acting piston bellows and water-powered bellows, and tuyere sizes, see [Blowing equipment and forges](../../../docs/05-冶金技术/08-鼓风设备与锻炉.md#三各种风箱的做法).

### 2.2 High-temperature furnace (for iron)

**Materials:**
- Firebricks or fireclay (ordinary clay is not good enough)
- Fireclay recipe (recommended recipe A): bauxite or kaolin 50%, quartz sand 30%, fireclay 15%, crushed firebrick 5%

**Structural improvements:**
- Thicker walls (20-30 cm)
- Taller shaft (100-150 cm)
- Preheated blast (using the waste gas to heat the incoming air)
- Charging in layers

**Furnace shape:** narrow at the top, widest at the middle (the bosh), narrowing gradually down to the tuyere; below the tuyere are the hearth and the tap hole. For dimensions and a cross-section see the links below.

```
Why taller and thicker:
- The taller the shaft, the longer the rising hot gas and carbon monoxide have,
  as they pass up through the charge, to give their heat and reducing power to
  the ore → saves charcoal and reduces the ore more completely
- The thicker the wall, the less heat is lost; ordinary clay softens at around
  1300°C, sticks to the slag and burns through
- Beginners need not build a big furnace at once: practise first with a small
  shaft furnace about 1 m tall to get the rhythm of blowing, charging and
  tapping slag
```

For the dimensions of the shaft furnace, two refractory clay recipes and a building schedule see [Iron smelting – Simple shaft furnace](../../../docs/05-冶金技术/01-铁的冶炼.md#21-简易竖炉推荐) and [Iron smelting – Preparing refractory materials](../../../docs/05-冶金技术/01-铁的冶炼.md#22-耐火材料配制); for firing firebricks and crucibles see [Pottery, glass and papermaking – Crucibles and firebricks](../../../docs/07-日常生活技能/11-陶瓷玻璃与造纸.md#坩埚和耐火砖).

---

## 3. Making fuel

### 3.1 Why charcoal matters

**Why charcoal is a must:**
- ✗ Firewood: contains water and impurities, burns cooler (an open flame is generally only about 600-900°C)
- ✓ Charcoal: mainly carbon (fixed carbon generally about 70-90%); with forced air it burns hot (1200-1400°C)
- ✓ Charcoal is smokeless, and gives a steadier carbon monoxide concentration

**Two more points:**
- Charcoal contains almost no sulphur or phosphorus, so the iron made with it is less likely to be brittle; coal contains sulphur, and using it directly makes iron brittle (see [Q4](#q4-can-coal-be-used-instead-of-charcoal))
- Charcoal is porous and keeps its shape; in the furnace it does not flare and collapse like firewood, so the charge stays permeable to air

### 3.2 Making charcoal (smouldering method)

**Principle:** heat wood with the air kept out; the volatile matter escapes and carbon is left.

```
⚠️ Safety when making charcoal:
- The smoke from a charcoal kiln is full of carbon monoxide and tar; stand
  upwind and do not put your head near the smoke hole
- Never climb into a kiln pit that has not cooled completely
- Freshly drawn charcoal may hold hidden embers and can reignite or even catch
  fire by itself
- Never heat a room or tent by burning charcoal
```

**Preparing the wood:**
- Hardwoods (oak, chestnut, elm, pagoda tree and so on) give hard, long-burning charcoal suitable for smelting; pine, poplar and willow give lighter, softer charcoal, usable for the forge and everyday use
- The wood must be dry: after felling, split it and stack it off the ground to dry for several months or more; wet wood gives less charcoal and takes longer
- Remove rotten parts, keep the thickness as even as possible, and split pieces that are too thick

For how to dry firewood and how much a piece of woodland can yield, see [Firewood and woodland management – Dry wood](../../../docs/04-动植物培育/09-薪柴与林地管理.md#柴要干).

#### Earth kiln (large-scale production)

**Steps:**

**1. Dig the pit:**
- 2-3 m across
- 1-1.5 m deep
- Dig a flue at the centre of the bottom

**2. Stack the wood:**
- Stand the wood upright (5-15 cm thick)
- Leave a gap in the centre as a chimney
- When full, cover the top with small branches

```
Stacking tips:
- Pack it as tightly as you can, thick pieces in the middle and thin ones round
  the outside (the middle is hotter, the outside burns more slowly)
- Fill the gaps between pieces with short offcuts; where there are big gaps the
  wood burns to ash
- Put dry grass and kindling in the central gap to light it
```

**3. Seal with earth:**
- Cover with 10-20 cm of damp earth
- Leave air holes at the top and bottom
- Do not seal it completely

```
First lay a layer of dry grass or leaves over the woodpile, then the earth, so
the earth does not fall into the gaps; pat the earth down firmly so there are no
cracks. If the earth cracks and smokes while smouldering, patch it with damp
earth at once —
wherever air leaks in, the charcoal burns to ash
```

**4. Light it:**
- Light it from the top
- Once the fire is steady, gradually make the top air hole smaller

**5. Smoulder:**
- Lasts 3-7 days
- Watch the colour of the smoke:
  - White smoke (steam) → early stage
  - Yellow smoke (wood tar) → middle stage
  - Bluish smoke (nearly done)
  - Clear hot air (done)

```
While it smoulders:
- Keep watch day and night in shifts, mainly checking whether the earth cover
  has slumped, cracked or is showing flame
- Thick, wet white smoke (it forms droplets on something cold held in it) means
  the wood is still drying; do not hurry
- Yellow smoke with a sharp tarry smell means the wood is carbonising
- If one side's smoke turns bluish first, that side is nearly done; seal that
  side's bottom air hole first
- A sudden flame → air is leaking in somewhere; seal it at once
```

**6. Put it out:**
- Seal every air hole completely
- Wait 2-3 days for it to cool
- Dig it open and take out the charcoal

```
Drawing the charcoal:
- Open one side; feel the temperature with the back of your hand outside the
  opening, and if it is still too hot to touch, seal it again and wait
- Spread the charcoal out on open ground with water and sand ready beside it,
  and watch it for at least 24 hours for any reignition before bagging and
  storing it
- Pick out half-burnt "brands" (brown in section, still showing wood grain) and
  burn them again in the next kiln
```

**Yield:**
- 1 t of air-dried wood → about 150-250 kg of charcoal (earth kilns average about 160 kg; a well-run kiln can give over 250 kg)
- Good hardwood (such as oak) gives a higher yield

#### Simple steel-drum method (small-scale production)

**Steps:**
1. Take a large steel drum and make small holes in the lid (to vent)
2. Fill it with pieces of wood
3. Turn it upside down over a fire and heat it
4. When smoke comes from the small holes, light it (to burn the combustible gas)
5. When the smoke clears, take away the fire and let it cool
6. Take out the charcoal

**Time:** 4-8 hours

```
Tips:
- Cut the wood into fist-sized pieces of equal length and pack them tightly
- If the smoke from the holes in step 4 can be lit and forms small flames, the
  wood is carbonising; these combustible gases also heat the drum and save
  firewood
- When the flames shrink and go out and no more smoke comes → carbonising is
  finished
- After removing the fire, bury the edge of the drum in earth to keep out the
  air; do not open it before it is completely cool, or the charcoal will catch
  fire
- Do not use drums that have held paint, pesticides or chemicals; burn out an
  old drum outdoors first to remove residues
```

**Common problems:**

| Problem | Cause | Remedy |
|------|------|------|
| Very little charcoal; most of it has turned to ash | The earth cover leaks, or the air holes are open too wide | Pat the earth down firmly; patch cracks as they appear |
| Lots of unburnt wood in the charcoal | Wood too wet or too thick, or not smouldered long enough | Dry it, split it thinner, smoulder longer |
| Soft charcoal that crumbles when squeezed | Softwood, or smouldered too hot and too fast | Choose hardwood; open the air holes less |
| The charcoal pile smokes and catches fire after drawing | Taken out before it had cooled | Wait a few more days; spread it out and watch it after drawing |

### 3.3 Checking charcoal quality

**Good charcoal:**
- ✓ Black with a metallic sheen
- ✓ Rings clearly when struck
- ✓ Clear grain in section
- ✓ Burns with no smoke or little smoke

**Poor charcoal:**
- ✗ Brown, or not fully carbonised
- ✗ A lot of ash
- ✗ Crumbles easily

```
Storage:
- Keep it in a dry, ventilated, roofed place, some distance from houses and
  woodpiles, protected from rain and damp
  (damp charcoal cools the furnace and bursts in it)
- A large heap of charcoal can catch fire by itself; do not pile it too high or
  too tightly, and check regularly for heating
- Sieve it before smelting: fragments and dust block the passages in the
  furnace; use the sieved fines for the forge or everyday use
```

---
