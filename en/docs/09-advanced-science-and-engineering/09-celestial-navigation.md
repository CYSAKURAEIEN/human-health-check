# Advanced Celestial Navigation

> **Without satellites or maps, the sky is your clock, calendar and map: the positions of the Sun and stars tell us what time it is, what day it is and where we are**

## ⚠️ What this chapter covers

```
Contents of this chapter:
1. Celestial coordinates: how to describe the position of a star
2. Finding direction: more precise methods
3. Measuring latitude and longitude
4. Making angle-measuring instruments (the quadrant; how the sextant works)
5. Dead reckoning: estimating your position when no celestial body can be seen
6. Making a calendar: fixing the solar terms, leap years and leap months
7. Laws of celestial motion: Kepler's laws, orbits, solar and lunar eclipses

Note:
- With simple measurements on land, latitude is usually accurate to about 1° (about
  111 km), enough to tell your rough position
- Precise navigation at sea needs precision instruments, an accurate clock,
  astronomical tables and a great deal of practice
```

For basic ways of finding direction see [Basic Survival Skills – Navigation and orientation](../../../docs/03-野外生存/00-基础生存技能.md#导航与定向); for the basics of the seasons, the calendar and measuring latitude see [Physics – Astronomy and the Earth](../../../docs/08-基础科学知识/02-物理.md#九天文与地球).

---

## 1. The celestial sphere and coordinates

### 1.1 The celestial sphere

```
Imagine a huge sphere around the Earth with all the stars stuck on its surface
- The Earth rotates from west to east → the celestial sphere appears to turn from east
  to west, once a day
- The axis of the sphere's rotation passes through the north and south celestial poles;
  the Pole Star is near the north celestial pole
- Celestial equator: the great circle where the Earth's equator, extended outwards,
  meets the celestial sphere
- Ecliptic: the path the Sun follows across the celestial sphere over a year, at an
  angle of about 23.4° to the celestial equator
```

### 1.2 Two coordinate systems

```
Horizontal coordinates (change with the observer's place and the time):
  Altitude: the angle of a body above the horizon (0° on the horizon, 90° overhead)
  Azimuth: the angle measured clockwise from due north (due east 90°, due south 180°,
    due west 270°)

Equatorial coordinates (a star's "address", which hardly changes):
  Declination: the angle of a body from the celestial equator, like latitude in the sky
  Right ascension: like longitude in the sky, given in hours (0-24 hours)
  → Star catalogues list the right ascension and declination of each star
```

### 1.3 Sidereal day and solar day

```
Sidereal day (a star returns to the same position): about 23 hours 56 minutes 4 seconds
Solar day (the Sun returns to the same position): 24 hours
→ At the same clock time each day, the stars are about 4 minutes further on than the
  day before
→ That is why different constellations are seen at night in different seasons

The Moon rises about 50 minutes later each day than the day before
```

---

## 2. Finding direction precisely

### 2.1 The Pole Star

```
Finding the Pole Star:
  Take the line through the two stars at the lip of the bowl of the Plough (Big Dipper),
  Dubhe and Merak, and extend it from the lip about 5 times that distance
  Or: Cassiopeia (W-shaped) is on the other side of the Pole Star, facing the Plough
  across it
The Pole Star is less than 1° from the true north celestial pole and is the handiest
marker of due north

The Plough turns anticlockwise around the Pole Star at about 15° an hour
  → Once you know it well, you can use it to estimate the time of night roughly
```

### 2.2 Southern hemisphere: the Southern Cross

```
Extend the long axis of the Southern Cross downwards (the long bar of the cross) about
4.5 times its length to find roughly the south celestial pole
(in the low-latitude south of China, the Southern Cross can be seen close to the
southern horizon on spring nights)
```

### 2.3 Finding true north–south with a shadow stick (precise method)

```
1. Stand a vertical stick on level ground (straighten it with a plumb line)
2. At some time in the morning, mark the tip of the stick's shadow, and draw a circle
   through that point centred on the foot of the stick
3. In the afternoon, when the tip of the shadow falls on the circle again, mark that point
4. The line joining the two points runs due east–west; the line from its midpoint to
   the foot of the stick runs due north–south
→ Ancient China used this method to orient buildings
```

### 2.4 Magnetic declination

```
A compass points to "magnetic north", not to true geographic north
The angle between them is called magnetic declination; it differs from place to place
and changes slowly
  In most of China it is west, roughly 2° to 11° (smaller in the south, larger in
  the north-east)
→ When you need a precise direction, first find true north with the Pole Star or a
  shadow stick, then see how far the compass differs from it, and write this down as
  the local correction
```

---

## 3. Measuring latitude

### 3.1 The Pole Star method

```
Northern hemisphere: altitude of the Pole Star ≈ local latitude (error under 1°)
  Example: the Pole Star is 40° above the horizon → about 40° N (near Beijing)
```

### 3.2 The noon Sun method (works on any day)

```
Steps:
1. Measure the Sun's altitude h at noon that day (when the Sun is highest)
2. Look up (or calculate) the Sun's declination δ for that day
3. In the northern hemisphere, with the Sun to the south: latitude = 90° - h + δ

Approximate calculation of the Sun's declination:
  δ ≈ 23.44° × sin[360° × (N - 81) ÷ 365]
  N: the day of the year (1 January is 1)
  - Spring equinox (about 21 March): δ ≈ 0°
  - Summer solstice (about 21 June): δ ≈ +23.44°
  - Autumn equinox (about 23 September): δ ≈ 0°
  - Winter solstice (about 22 December): δ ≈ -23.44°

Example: at noon on 21 June the Sun's altitude is 80°
  latitude = 90 - 80 + 23.44 ≈ 33.4° → about 33° N
```

![Measuring latitude: sight the Pole Star along the two sighting holes of a quadrant, and the plumb line's reading on the arc is its altitude; in the northern hemisphere the Pole Star's altitude is about the local latitude. Noon Sun method: latitude = 90° − h + δ; with the Sun 80° high at noon on 21 June, about 33° N](../../images/latitude-polaris.svg)

*Figure: For how to make the quadrant see [5.1 The quadrant](#51-the-quadrant-for-use-on-land); the drawing shows the reading for a Pole Star altitude of 40°. When measuring the Sun, never look at it directly and never put your eye to the sighting holes*

### 3.3 Corrections (for precise measurement)

```
- When measuring the Sun you sight its lower edge, so add the Sun's radius, about
  0.27° (16′)
- At sea the sea horizon is the reference; the higher your eye, the "lower" the horizon,
  so subtract the "dip": about 1.76′ × √(eye height in m)
- Near the horizon, atmospheric refraction makes a body look higher than it is:
  about 0.5° too high on the horizon, about 0.1° at 10° altitude; negligible above 20°
→ Measure bodies more than 20° above the horizon whenever possible
```

---

## 4. Measuring longitude

### 4.1 The principle: longitude is a time difference

```
The Earth turns 15° an hour (1° every 4 minutes)
The difference between local noon and noon at a reference place of known longitude
gives the difference in longitude

Example: with an accurate clock keeping Beijing time (based on 120° E),
  you find the Sun is highest locally at 12:40 Beijing time
  → 40 minutes later than noon at 120° E → longitude difference = 40 ÷ 4 = 10°
  → The place is at about 110° E
```

### 4.2 Equation of time correction

```
True solar noon does not fall at exactly 12:00 by the clock every day
Over a year the difference reaches about 16 minutes (solar noon early in early
November, late in mid-February)
→ For precise longitude, correct with an "equation of time" table, or the error can
  reach 4°

Also, the Sun's altitude changes very slowly around noon, so the "highest moment" is
hard to judge exactly:
→ Note the two times, morning and afternoon, when the Sun is at the same altitude, and
  take their average as noon
```

### 4.3 The clock is the key

```
Every minute the clock is out puts the longitude out by 1/4° (about 28 km at the equator)
→ Only the invention of the marine chronometer in the 18th century (a clock that stays
  accurate on board ship) made precise longitude possible on ocean voyages
→ Before that, the "lunar distance method" was used (measure the angle between the Moon
  and a star, then work out the time from tables), and the calculation was very complicated

Without an accurate clock: if you stay in one place for a long time, you can set the
  clock at noon each day; when travelling, record the direction and distance covered
  (dead reckoning)
```

---

## 5. Angle-measuring instruments

### 5.1 The quadrant (for use on land)

```
Making one:
1. Take a quarter-circle board and mark a 0°-90° scale along its curved edge
2. Fit two small holes or a thin tube along one straight edge as a sight
3. Hang a fine thread from the centre of the circle with a small weight tied to it
   (a plumb line)

Using it:
- Sight a star along the sight (⚠️ never look straight at the Sun); the reading where
  the plumb line crosses the arc is the altitude
- For the Sun: let sunlight pass through the front hole so the spot of light falls on
  the rear hole; do not look with your eye
- Accuracy is about 0.5-1°; the larger the scale, the more accurate
```

### 5.2 How the sextant (for use at sea) works

```
Two mirrors: a fixed half-silvered horizon mirror, and an index mirror that turns with
the index arm
- Look at the sea horizon through the horizon mirror, while the image of the celestial
  body reflected from the index mirror appears in the same view
- Turn the index arm until the body's image "sits" on the horizon
- Law of reflection: the mirror turns through half the angle the light ray turns through
  → The scale arc is only 60° (one sixth of a circle), yet it measures angles up to
    120°, hence the name "sextant"
- Advantage: when the ship rolls, the body and the horizon move together, so you can
  still line them up; accuracy can reach 1′ (one minute of arc)

⚠️ You must use a filter when observing the Sun; looking straight at the Sun causes
   permanent eye damage
```

---

## 6. Dead reckoning

```
When no celestial body can be seen, work out your present position from your starting
point, direction, speed and time:
  distance covered = speed × time
  On a map (or squared paper), draw that distance from the starting point in that direction

Units:
  1 nmi (nautical mile) = 1852 m = the length of 1′ of latitude (minute of arc, 1/60°)
  1 kn (knot) = 1 nmi/h
  1° of latitude ≈ 111 km

On land: measure distance by pacing (see the Measurement chapter), find direction with
  a compass, and record each leg as you go
At sea: throw a board tied to a line knotted at equal intervals into the sea and count
  how many knots run out in a set time to get the ship's speed (this is where the unit
  "knot" comes from)

⚠️ Errors accumulate: currents, wind and errors in direction; correct with landmarks or
   celestial bodies at every leg whenever you can
```

For pacing see [Measurement and the Scientific Method – Estimating distance](../../../docs/08-基础科学知识/00-度量衡与科学方法.md#44-估算距离).

---

## 7. Making a calendar

### 7.1 Fixing the winter solstice and the tropical year with a gnomon

```
The guibiao (gnomon and shadow scale): a vertical pole (the taller, the more accurate)
and, on the ground, a graduated scale (the gui) running due north–south
- Measure the length of the pole's shadow at noon every day
- The day of the longest shadow is the winter solstice, the shortest the summer solstice
- Measure over many years; the average number of days between winter solstices is the
  tropical year: about 365.2422 days
```

### 7.2 Leap years in the solar calendar

```
A leap year (29 days in February) every 4 years, except century years, which are leap
years only if divisible by 400
  → 97 leap years in 400 years, an average year of 365.2425 days, very close to the
    tropical year
```

### 7.3 The Chinese calendar: a lunisolar calendar

```
Months in the Chinese calendar follow the phases of the Moon: the new moon (Moon not
visible) is the first day of the month; one synodic month is about 29.53 days
  → long months have 30 days, short months 29
12 synodic months are about 354 days, about 11 days short of a year
→ Leap months are added: 19 tropical years ≈ 235 synodic months, so 7 leap months are
   added in those 19 years
   (19 × 12 = 228, 235 - 228 = 7)
→ The 24 solar terms are set by the Sun's position (see Physics – Calendar);
  a month that contains no zhongqi (major solar term) becomes the leap month, keeping
  the months in step with the seasons
```

---

## 8. Laws of celestial motion

### 8.1 Kepler's three laws

```
1. A planet's orbit around the Sun is an ellipse, with the Sun at one focus
2. A planet moves faster when close to the Sun and slower when far away
   (the line joining planet and Sun sweeps out equal areas in equal times)
3. The square of a planet's orbital period is proportional to the cube of the
   semi-major axis of its orbit
   T² ∝ a³
   Example: Mars's semi-major axis is about 1.52 times the Earth's → period about
   √(1.52³) ≈ 1.88 years

Newton derived these three laws from his law of universal gravitation
```

### 8.2 Artificial satellites

```
Circling the Earth in a low orbit needs about 7.9 km/s (first cosmic velocity)
Escaping the Earth's gravity needs about 11.2 km/s (second cosmic velocity, escape velocity)
Geostationary orbit: altitude about 35786 km, with a period equal to the Earth's rotation,
  so from the ground the satellite seems to stand still in the sky (communications and
  weather satellites)

Circular orbital speed: v = √(G × M ÷ r); the further from the Earth's centre, the slower
the speed and the longer the period
```

### 8.3 Planets visible to the naked eye

```
Mercury, Venus, Mars, Jupiter, Saturn
- Planets do not twinkle like stars; their light is steadier
- They move slowly among the constellations
- They all stay near the ecliptic
- Venus is the brightest and appears only in the west after dusk ("Changgeng", the
  evening star) or in the east before dawn ("Qiming", the morning star)
```

### 8.4 Solar and lunar eclipses

```
Solar eclipse: the Moon blocks the Sun; happens only at new moon (the first day of the
  lunar month)
Lunar eclipse: the Earth's shadow falls on the Moon; happens only at full moon (around
  the 15th of the lunar month)
They do not happen every month, because the Moon's orbit is tilted about 5° to the ecliptic

Saros cycle: about 18 years 11 days; eclipses repeat roughly on this cycle
  → Ancient astronomers used it to predict eclipses

⚠️ Never look straight at the Sun during an eclipse (even when only a sliver is left);
   pinhole projection (prick a small hole in a sheet of paper and project the Sun's
   image onto another sheet) is the safest way
```

---

## 9. Keeping observation records

```
✓ Record for every observation: date, time (and the clock's error), place, the body
  measured, the reading, the weather
✓ Keep it up for the long term: many patterns (the length of the tropical year, the
  precession of the stars, the periods of comets) can only be found from records
  accumulated over decades or centuries
✓ Ancient China kept the world's most continuous records of celestial events (eclipses,
  comets, novae, sunspots), which astronomers still use today
```

---

## Related chapters

- ⏮️ [Computing and Information](../../../docs/09-进阶科学与工程/08-计算与信息.md)
- ⏮️ [Higher Mathematics](../../../docs/09-进阶科学与工程/04-高等数学.md) - trigonometric functions, series
- ⏮️ [Modern Physics](../../../docs/09-进阶科学与工程/06-现代物理.md) - spectra, stars
- 🔗 [Physics – Astronomy and the Earth](../../../docs/08-基础科学知识/02-物理.md#九天文与地球) - basics of the seasons, the calendar and measuring latitude
- 🔗 [Trip Preparation and Calling for Rescue – Reading maps and contour lines](../../../docs/03-野外生存/07-户外出行准备与求救.md#看懂地图和等高线)
- 🔗 [Technology Rebuilding Roadmap](../../../docs/09-进阶科学与工程/00-技术重建路线图.md)

---

**Remember: the sky is humanity's oldest clock, calendar and map, and it never has a power cut. Learn to read it and, wherever you are, you will know the time and the direction.**
