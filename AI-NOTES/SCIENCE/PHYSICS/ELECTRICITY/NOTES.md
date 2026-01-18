# Electricity - Class 10 Physics Notes (CBSE)

## Quick Definitions List

**Electric current (I)** - Rate of flow of electric charge through a conductor; measured in amperes (A)

**Electric charge (Q)** - Fundamental property of matter; measured in coulombs (C); 1 C = charge of 6 × 10¹⁸ electrons

**Electron** - Negatively charged particle; charge = 1.6 × 10⁻¹⁹ C; actual charge carrier in metals

**Conventional current** - Assumed flow of positive charges; direction opposite to electron flow

**Electric circuit** - Closed, continuous path for electric current to flow

**Potential difference (V)** - Work done per unit charge to move charge between two points; measured in volts (V)

**Voltage** - Another term for potential difference; the "electrical pressure" that pushes charges

**Resistance (R)** - Property of conductor that opposes flow of current; measured in ohms (Ω)

**Resistor** - Component with appreciable resistance; used to control current in circuits

**Ohm's law** - At constant temperature: V = IR (voltage directly proportional to current)

**Resistivity (ρ)** - Intrinsic property of material determining its resistance; measured in Ω m

**Conductors** - Materials with low resistivity (metals); allow easy flow of current

**Insulators** - Materials with very high resistivity (rubber, glass); block current flow

**Series connection** - Components connected end-to-end; same current through all

**Parallel connection** - Components connected across same two points; same voltage across all

**Equivalent resistance** - Single resistance that can replace a combination of resistors

**Ammeter** - Instrument measuring current; connected in series

**Voltmeter** - Instrument measuring potential difference; connected in parallel

**Electric power (P)** - Rate of consumption of electrical energy; measured in watts (W)

**Joule's heating effect** - Heat produced when current flows through resistance: H = I²Rt

**Kilowatt-hour (kWh)** - Commercial unit of electrical energy; 1 kWh = 3.6 × 10⁶ J

**Fuse** - Safety device that melts when current exceeds safe limit

---

```diff
! FUNDAMENTAL PRINCIPLE: Electric Current is Moving Charges
! Current exists because charges (electrons) move through conductors
! To make them move, we need "electrical pressure" (potential difference)
! Resistance opposes this motion, converting electrical energy to heat
```

---

## 1. Electric Current - The Foundation

### What Really IS Electric Current?

**The Microscopic Picture:**

In a metallic conductor:
- Metal atoms arranged in lattice
- Outer electrons of atoms are "free" - not bound to specific atoms
- These free electrons move randomly at high speeds
- **Random motion → No net flow → NO current**

**When Battery Connected:**
- Battery creates electric field in wire
- Electric field exerts force on electrons
- Electrons drift in direction opposite to field
- **Organized drift → Net flow → CURRENT exists**

```diff
! KEY INSIGHT: Current is NOT individual electron speed
! It's the net DRIFT of electrons in one direction
! Random motion: ~10⁶ m/s
! Drift velocity: ~10⁻⁴ m/s (very slow!)
! But effect is instantaneous because all electrons move together
```

---

### The Water-Pipe Analogy (Done Right)

**NCERT mentions this briefly, but here's the complete picture:**

| Water Flow | Electric Current |
|------------|------------------|
| Water molecules | Electrons |
| Pipe | Wire (conductor) |
| Pump | Battery/cell |
| Water pressure difference | Potential difference (voltage) |
| Flow rate (liters/sec) | Current (coulombs/sec = amperes) |
| Narrow pipe/obstacles | Resistance |
| Water heating due to friction | Joule heating |

**Critical Parallel:**
- Water flows HIGH pressure → LOW pressure
- Charges flow HIGH potential → LOW potential
- **Difference in pressure/potential CAUSES flow**
- **NO difference → NO flow** (like horizontal pipe with no height difference)

---

### Conventional vs Actual Current Direction

**Historical Accident:**

**Before 1900:**
- Electricity discovered
- Direction convention established
- Assumed positive charges flow
- Direction: Positive terminal → Negative terminal

**After 1900:**
- Electrons discovered
- Found: ELECTRONS actually move
- Electrons are NEGATIVE
- Actual flow: Negative terminal → Positive terminal

**Result: Opposite Directions!**

```
Battery Circuit:

Conventional Current: (+) ============> (-)
                              
Electron Flow:        (+) <============ (-)
                              ↑
                         (Actual physical motion)
```

```diff
! IMPORTANT: Both conventions work mathematically
! We use CONVENTIONAL current (positive flow)
! Just remember: Electrons move opposite direction
! For calculations: Doesn't matter which you imagine
! For physics understanding: Remember actual carriers are electrons
```

---

### Defining Current Mathematically

**Question: How do we MEASURE current?**

**Answer: Count charges passing per second**

**Definition:**
```
Current (I) = Charge (Q) / Time (t)

I = Q/t
```

**Units:**
- I in amperes (A)
- Q in coulombs (C)
- t in seconds (s)

**What is 1 Ampere?**
```diff
+ 1 A = 1 coulomb of charge flowing per second
+ If 1 C charge passes through wire in 1 s → Current is 1 A
```

---

**What is 1 Coulomb?**

```diff
! 1 Coulomb = Charge of approximately 6 × 10¹⁸ electrons
! (Exactly: 6.242 × 10¹⁸ electrons)
```

**Why this number?**
- One electron charge = 1.6 × 10⁻¹⁹ C
- So 1 C = 1/(1.6 × 10⁻¹⁹) electrons
- = 6.25 × 10¹⁸ electrons

**Practical Currents:**
- Small currents: milliamperes (mA = 10⁻³ A) or microamperes (μA = 10⁻⁶ A)
- Example: LED → 20 mA
- Phone charger → 1-2 A
- Electric iron → 5 A
- House wiring limit → 15-20 A

---

### Example 11.1 Deep Dive

**Given:** Current I = 0.5 A for time t = 10 min

**Find:** Charge Q that flows

**Why this matters:** Understanding relationship between I, Q, t

**Solution:**

**Step 1: Convert time to SI units**
```
t = 10 min = 10 × 60 s = 600 s
```
```diff
! CRITICAL: Always convert to seconds for calculations
! Formula uses seconds, not minutes
```

**Step 2: Use I = Q/t**
```
Rearranging: Q = I × t
Q = 0.5 A × 600 s
Q = 300 C
```

**Step 3: Interpret physically**
```
300 C = 300 coulombs
Number of electrons = 300 / (1.6 × 10⁻¹⁹)
                    ≈ 1.875 × 10²¹ electrons
```

**That's nearly 2 billion trillion electrons!**

```diff
+ Key Insight: Even "small" currents involve enormous numbers of electrons
+ 0.5 A seems small, but billions of trillions of electrons flow
+ Each electron carries tiny charge, so need huge numbers
```

---

### What Makes Current Flow? (Building to Potential Difference)

**Thought Experiment:**

**Case 1: Wire alone**
- Just copper wire, no battery
- Free electrons present
- Random motion exists
- **No current** (no net drift)

**Case 2: Wire with battery**
- Battery connected
- Free electrons still present
- **Current flows!**

**What changed?** 

**The battery!**

**What does battery do?**
- Creates **electric field** in wire
- Electric field exerts **force** on electrons  
- Force causes **organized drift**
- Drift = current

**But what maintains the electric field?**

**POTENTIAL DIFFERENCE!**

---

## 2. Electric Potential and Potential Difference - The "Why" of Current

### The Gravity Analogy (Building Intuition)

**Water on Hill:**

**High elevation:**
- Water has gravitational potential energy
- Can flow down, do work (turn wheel)
- "Potential" to do work

**Low elevation:**
- Less gravitational potential energy
- Water flows high → low
- **Difference in height DRIVES flow**

---

**Electric Charges:**

**High potential point:**
- Charges have electric potential energy
- Can move, do work (light bulb)
- "Potential" to do work

**Low potential point:**
- Less electric potential energy
- Charges flow high → low potential
- **Difference in potential DRIVES current**

```diff
! FUNDAMENTAL: Potential Difference is the CAUSE of current
! Current is the EFFECT
! No potential difference → No current (like horizontal pipe)
```

---

### Defining Potential Difference

**Question:** How much "electrical pressure" between two points?

**Answer:** How much work needed to move a charge between them

**Definition:**
```
Potential Difference (V) = Work done (W) / Charge moved (Q)

V = W/Q
```

**Units:**
- V in volts (V)
- W in joules (J)
- Q in coulombs (C)

**What is 1 Volt?**

```diff
+ 1 Volt = Potential difference when 1 joule of work is done
+          to move 1 coulomb of charge between two points
```

```
1 V = 1 J/C
```

---

### Why "Potential DIFFERENCE" and not just "Potential"?

**Critical Understanding:**

**Absolute potential is meaningless**
- Like asking "what's the height?" (height above what?)
- Need reference point

**Only DIFFERENCE matters**
- Height difference = 100 m (meaningful)
- Potential difference = 12 V (meaningful)

**In circuits:**
- We always measure voltage BETWEEN two points
- Usually reference is negative terminal (taken as 0 V)
- Positive terminal then has +V relative to negative

```diff
! Voltage = Potential Difference = PD (all same thing)
! Always measured BETWEEN two points
! Voltmeter has two probes for this reason
```

---

### What Battery Actually Does

**Chemical to Electrical Energy Conversion:**

**Inside battery:**
- Chemical reactions occur
- Reactions separate charges
- Positive charges accumulate at positive terminal
- Negative charges (electrons) accumulate at negative terminal

**Result:**
- **Potential difference** created between terminals
- Positive terminal: HIGH potential
- Negative terminal: LOW potential (reference, 0 V)

**When circuit connected:**
- Potential difference creates electric field in wire
- Field pushes charges (current flows)
- Battery does work moving charges through itself
- Chemical energy → Electrical energy → Other forms

```diff
+ Battery is NOT source of charges (electrons)
+ Wire already has free electrons
+ Battery provides ENERGY to move existing charges
+ Battery creates and maintains potential difference
```

---

### Example 11.2 Deep Dive

**Given:** Charge Q = 2 C moved across potential difference V = 12 V

**Find:** Work done W

**Conceptual Setup:**

**What's happening?**
- Moving 2 coulombs of charge
- From low potential to high potential (against electric field)
- Like lifting water uphill
- Requires work input

**Solution:**

**Use V = W/Q**
```
Rearranging: W = V × Q
W = 12 V × 2 C
W = 24 J
```

**Physical Interpretation:**
```diff
! 24 joules of energy converted
! Chemical energy (battery) → Electric potential energy (charges)
! This energy will be released when charges flow back through circuit
! Powers devices in circuit
```

**Alternative scenario:** If charges flow from high to low potential
- Then they RELEASE 24 J of energy
- This energy can light bulb, run motor, etc.

---

### Measuring Potential Difference - The Voltmeter

**How Voltmeter Works (simplified):**
- Contains high-resistance coil
- When connected across two points
- Tiny current flows through voltmeter
- Current proportional to potential difference
- Coil deflects, pointer shows voltage

**Connection:**
```diff
! ALWAYS connect voltmeter in PARALLEL
! Place probes across two points
! Measures potential DIFFERENCE between those points
```

**Why parallel?**
- Want to measure voltage across component
- Parallel connection: Same two points as component
- Minimal current through voltmeter (high resistance)
- Doesn't disturb circuit

**Contrast with Ammeter:**
- Ammeter: Series connection (current flows through it)
- Voltmeter: Parallel connection (measures across it)

---

## 3. Resistance - The Opposition to Current

### What IS Resistance, Really?

**NCERT says:** "Property of conductor to resist flow of charges"

**But WHY does it resist?**

**Microscopic Picture:**

**Electron Journey Through Wire:**

**Step 1:** Electric field accelerates electron

**Step 2:** Electron gains speed (kinetic energy)

**Step 3:** Electron **COLLIDES** with metal atom

**Step 4:** Electron loses energy to atom (atom vibrates more = heat)

**Step 5:** Electron slowed down

**Step 6:** Field accelerates again

**Step 7:** Another collision...

**Result:**
- Net drift is SLOW (despite accelerations)
- Energy continuously lost to collisions
- This opposition to flow = **RESISTANCE**

```diff
! Resistance is NOT friction (common misconception)
! It's repeated collisions of electrons with atoms
! Collisions convert electrical energy → thermal energy
! More collisions → Higher resistance
```

---

### Temperature and Resistance

**Logical Connection:**

**Higher temperature:**
- Atoms vibrate more vigorously
- Larger "targets" for electrons
- More frequent collisions
- **Higher resistance**

**Lower temperature:**
- Atoms vibrate less
- Electrons have easier path
- Fewer collisions
- **Lower resistance**

**At absolute zero (0 K = -273°C):**
- Some materials: Resistance drops to ZERO
- Superconductivity
- No collisions, no energy loss

```diff
+ For metals: Resistance increases with temperature
+ For semiconductors: Resistance decreases with temperature
+ (Different mechanisms, not in Class 10 syllabus)
```

---

### Defining Resistance Mathematically

**From Ohm's Law (coming next section):**

```
Resistance (R) = Potential Difference (V) / Current (I)

R = V/I
```

**Units:**
```
1 ohm (Ω) = 1 volt / 1 ampere

1 Ω = 1 V/A
```

**What is 1 Ohm?**

```diff
+ 1 Ω resistance means:
+ When 1 volt is applied, current of 1 ampere flows
+ Higher ohms → Harder for current to flow
+ Lower ohms → Easier for current to flow
```

**Practical Resistances:**
- Copper wire (1 m): ~0.001 Ω
- Light bulb filament: 200-1000 Ω
- Human body (dry skin): ~100,000 Ω
- Voltmeter: Millions of ohms

---

## 4. Ohm's Law - The Fundamental Relationship

### Activity 11.1 - What's Really Happening

**Setup:** Nichrome wire, adjustable voltage (1 to 4 cells), ammeter, voltmeter

**Procedure:**
- Start with 1 cell (1.5 V)
- Measure V and I
- Add cells to increase V
- Measure V and I each time

**Typical Results:**

| Cells | Voltage (V) | Current (I) | V/I (Ω) |
|-------|-------------|-------------|---------|
| 1 | 1.5 | 0.15 | 10 |
| 2 | 3.0 | 0.30 | 10 |
| 3 | 4.5 | 0.45 | 10 |
| 4 | 6.0 | 0.60 | 10 |

**Observations:**

**1. V and I both increase**
- Double voltage → Double current
- Triple voltage → Triple current

**2. Ratio V/I is CONSTANT**
- Always 10 Ω in this example
- Regardless of voltage applied

**3. Graph of V vs I is straight line**
- Passes through origin
- Slope = constant = R

---

### Ohm's Law Statement

**Georg Simon Ohm (1827):**

```diff
! OHM'S LAW:
! At constant temperature, the current through a conductor
! is directly proportional to the potential difference across it
!
! V ∝ I
! or
! V = I × R (where R is a constant called resistance)
```

**Alternative Forms:**
```
V = IR
I = V/R  
R = V/I
```

**Critical Condition:**
```diff
- "At constant temperature"
- Why? Because resistance changes with temperature
- Law only works if R stays constant
- R stays constant only if temperature constant
```

---

### Understanding the V-I Graph

**Straight Line Through Origin:**

```
V (volts)
  ↑
6 |           /
  |          /
4 |        /
  |      /  ← Slope = R
2 |    /
  |  /
0 |/____________→ I (amps)
  0    0.5   1.0
```

**What the graph tells us:**

**1. Linear relationship**
- Straight line = directly proportional
- V ∝ I

**2. Passes through origin**
- No voltage → No current
- Makes sense!

**3. Slope = Resistance**
- Steeper slope → Higher resistance
- Gentler slope → Lower resistance

**Different Conductors:**
```
V
↑
|     Wire A (low R)
|    /
|   /    Wire B (high R)
|  /    /
| /   /
|/  /
|/_/_______________→ I

Wire B has steeper slope → Higher R
```

---

### Why Does Ohm's Law Work?

**Deeper Understanding:**

**For metallic conductors at constant temperature:**

**More voltage applied:**
- Stronger electric field in wire
- Greater force on electrons
- Faster drift velocity
- More current

**Relationship:**
- Drift velocity ∝ Electric field
- Electric field ∝ Voltage
- Current ∝ Drift velocity
- **Therefore: Current ∝ Voltage**

**The resistance:**
- Determined by collision rate
- At constant temperature, collision rate constant
- So resistance constant
- Ratio V/I remains same

---

### Non-Ohmic Devices (Important!)

**Not everything obeys Ohm's law:**

**Ohmic (linear):**
- Metal wires
- Fixed resistors
- Carbon resistors
- V-I graph: Straight line

**Non-Ohmic (non-linear):**
- Filament bulb (heats up, R increases)
- Diode (allows current in only one direction)
- Transistors
- V-I graph: Curved

**Activity 11.2 demonstrates this:**
- Nichrome wire: Ohmic (straight line)
- Torch bulb: Non-ohmic (curved, R increases as it glows)
- Different materials, different behaviors

```diff
! Ohm's Law applies to ohmic conductors only
! But formula R = V/I always defines resistance
! For non-ohmic devices, R is not constant
```

---

### Example 11.3 Deep Dive

**Part (a): Electric bulb**

**Given:** V = 220 V, R = 1200 Ω

**Find:** Current I

**Solution:**
```
Using I = V/R
I = 220 V / 1200 Ω
I = 0.183 A ≈ 0.18 A
```

**Interpretation:**
- Small current (183 mA)
- High resistance bulb
- Typical for lighting

---

**Part (b): Electric heater**

**Given:** V = 220 V, R = 100 Ω

**Find:** Current I

**Solution:**
```
I = V/R
I = 220 V / 100 Ω
I = 2.2 A
```

**Interpretation:**
- Much larger current (2.2 A)
- Lower resistance
- More power consumed

---

**Critical Comparison:**

```diff
! Same voltage (220 V)
! Bulb: High R → Low I → Low power → Light
! Heater: Low R → High I → High power → Heat
```

**Power difference:**
- Bulb: P = VI = 220 × 0.18 = 40 W
- Heater: P = VI = 220 × 2.2 = 484 W
- Heater uses 12 times more power!

**Lesson:** Resistance determines how much current flows, hence how much power is consumed

---

### Example 11.4 Deep Dive

**Given:** 
- Initially: V₁ = 60 V, I₁ = 4 A
- Then: V₂ = 120 V, I₂ = ?

**Conceptual Question:** Does resistance change?

**Answer:** NO! (Assuming temperature constant)
- Resistance is property of heater
- Doesn't change with applied voltage

**Solution:**

**Step 1: Find resistance**
```
R = V₁/I₁ = 60 V / 4 A = 15 Ω
```

**Step 2: Apply Ohm's law at new voltage**
```
I₂ = V₂/R = 120 V / 15 Ω = 8 A
```

**Key Insight:**
```diff
+ Voltage doubled (60 V → 120 V)
+ Current doubled (4 A → 8 A)
+ Resistance unchanged (15 Ω)
+ This is Ohm's law in action!
```

---

## 5. Factors Affecting Resistance

### Activity 11.3 - Systematic Investigation

**What the activity reveals:**

**Test 1: Length Dependence**
- Wire (1): Length l, current I
- Wire (2): Length 2l (double), current I/2 (half)
- **Doubling length halves current**
- Since V same, R must double
- **R ∝ l**

**Test 2: Area Dependence**
- Wire (3): Thicker (larger area), current increases
- Thicker wire = easier path
- Less resistance
- **R ∝ 1/A**

**Test 3: Material Dependence**
- Wire (4): Copper (same l, same A as nichrome)
- Much more current through copper
- Copper has lower resistance
- **R depends on material**

---

### The Resistance Formula

**Combining observations:**

```
R ∝ l          (longer → more resistance)
R ∝ 1/A        (thicker → less resistance)
R ∝ material   (different materials different R)
```

**Combined:**
```
R = ρ × (l/A)

where:
ρ (rho) = resistivity (material property)
l = length
A = cross-sectional area
```

---

### Understanding Each Factor

**1. Length (l):**

**Why R ∝ l?**

**Think of it as obstacles:**
- Longer wire = more atoms to collide with
- More collisions = more resistance
- Like longer corridor with more people to navigate through

**Analogy:**
- Water pipe: Longer pipe → more friction → less flow
- Wire: Longer wire → more collisions → less current

```diff
+ Double length → Double resistance
+ Triple length → Triple resistance
+ R ∝ l (direct proportion)
```

---

**2. Area of Cross-Section (A):**

**Why R ∝ 1/A?**

**Think of it as parallel paths:**
- Thicker wire = more cross-sectional area
- More area = more space for electrons
- Like wider road carries more traffic

**Analogy:**
- Water pipe: Wider pipe → less resistance → more flow
- Wire: Thicker wire → less resistance → more current

```diff
+ Double area → Half resistance
+ Triple area → One-third resistance  
+ R ∝ 1/A (inverse proportion)
```

**Mathematical:**
- A larger → (l/A) smaller → R smaller

---

**3. Resistivity (ρ):**

**What is resistivity?**

**Definition:** Resistance of unit length, unit area conductor

```
ρ = R × (A/l)

Units: Ω m (ohm-meter)
```

**NOT "per meter" - it's "ohm-meter"**

**Physical meaning:**
- Intrinsic property of material
- Independent of shape/size
- Characteristic of how material opposes current
- Depends on:
  - Atomic structure
  - Number of free electrons
  - Temperature

---

### Resistivity Values (Table 11.2 Analysis)

**Conductors (Low ρ):**

```
Silver:      1.60 × 10⁻⁸ Ω m  (best conductor)
Copper:      1.62 × 10⁻⁸ Ω m  (nearly as good, cheaper)
Aluminum:    2.63 × 10⁻⁸ Ω m  (light, used in power lines)
Iron:        10.0 × 10⁻⁸ Ω m  (higher, but strong)
```

**Why metals are good conductors:**
- Many free electrons
- Low resistivity
- Easy current flow

---

**Alloys (Medium ρ):**

```
Constantan:  49 × 10⁻⁶ Ω m
Manganin:    44 × 10⁻⁶ Ω m  
Nichrome:    100 × 10⁻⁶ Ω m (highest among alloys shown)
```

**Key Observation:**
```diff
! Alloys have MUCH higher resistivity than pure metals
! Example: Nichrome (alloy) ~ 1000 times more resistive than copper
! Why? Irregular atomic structure → more collisions
```

**Why use alloys in heating elements:**
- High resistance → more heat
- Don't oxidize at high temperatures
- Stronger than pure metals

---

**Insulators (Very High ρ):**

```
Glass:       10¹⁰ - 10¹⁴ Ω m
Rubber:      10¹³ - 10¹⁶ Ω m
Ebonite:     10¹⁵ - 10¹⁷ Ω m
```

**Comparison:**
- Insulators: 10²⁰ times more resistive than metals!
- Almost no free electrons
- Current essentially cannot flow

---

### Example 11.5 Deep Dive

**Given:**
- Length l = 1 m
- Diameter d = 0.3 mm = 0.3 × 10⁻³ m = 3 × 10⁻⁴ m
- Resistance R = 26 Ω

**Find:** Resistivity ρ and identify material

---

**Solution:**

**Step 1: Find area A**

Wire is cylindrical, so cross-section is circle:
```
A = πr² = π(d/2)²

r = d/2 = (3 × 10⁻⁴)/2 = 1.5 × 10⁻⁴ m

A = π × (1.5 × 10⁻⁴)²
A = π × 2.25 × 10⁻⁸
A = 7.07 × 10⁻⁸ m²
```

---

**Step 2: Use R = ρl/A**

```
Rearranging: ρ = R × A/l

ρ = 26 Ω × (7.07 × 10⁻⁸ m²) / 1 m

ρ = 26 × 7.07 × 10⁻⁸

ρ = 183.8 × 10⁻⁸

ρ = 1.84 × 10⁻⁶ Ω m
```

---

**Step 3: Identify material**

From Table 11.2:
- Manganese: 1.84 × 10⁻⁶ Ω m ✓

**Answer: Manganese**

---

**Key Skills Demonstrated:**
1. Unit conversion (mm → m)
2. Area calculation (circle)
3. Formula rearrangement
4. Scientific notation arithmetic
5. Table lookup

```diff
! Common Mistakes to Avoid:
! - Forgetting to convert diameter to radius (r = d/2)
! - Using diameter instead of radius in area formula
! - Not converting mm to m
! - Arithmetic errors with powers of 10
```

---

### Example 11.6 Deep Dive

**First wire:**
- Length: l
- Area: A
- Resistance: R₁ = 4 Ω

**Second wire (same material):**
- Length: l/2 (half the length)
- Area: 2A (double the area)
- Resistance: R₂ = ?

---

**Conceptual Approach:**

**What affects R₂ compared to R₁?**

**Length effect:**
- Half the length → Half the resistance
- Factor: 1/2

**Area effect:**
- Double the area → Half the resistance  
- Factor: 1/2

**Combined:**
- R₂ = R₁ × (1/2) × (1/2) = R₁/4

---

**Mathematical Approach:**

**For first wire:**
```
R₁ = ρ × (l/A) = 4 Ω
```

**For second wire:**
```
R₂ = ρ × [(l/2)/(2A)]
R₂ = ρ × [l/(4A)]
R₂ = (1/4) × ρ × (l/A)
R₂ = (1/4) × R₁
R₂ = 4 Ω / 4
R₂ = 1 Ω
```

---

**Key Insight:**
```diff
+ Same material → Same ρ
+ Length halved → Resistance halved
+ Area doubled → Resistance halved  
+ Combined effect: R divided by 4
```

**Quick Method:**
```
R₂/R₁ = (l₂/l₁) × (A₁/A₂)
R₂/4 = (1/2) × (1/2) = 1/4
R₂ = 1 Ω
```

---

## 6. Resistors in Series

### Activity 11.4 - What Happens to Current

**Setup:** Three resistors (R₁, R₂, R₃) connected end-to-end

**Key Observation:**
```diff
! Ammeter reading is SAME everywhere in series circuit
! Current through each resistor is IDENTICAL
! This is the DEFINING property of series connection
```

**Why is current same?**

**Conservation of charge:**
- Charges can't accumulate in wire
- Charges can't disappear
- Whatever enters one resistor must exit
- Same rate in, same rate out
- **Same current everywhere**

---

### Activity 11.5 - Voltage Distribution

**Setup:** Measure voltages across each resistor and total

**Results:**
- V₁ across R₁
- V₂ across R₂
- V₃ across R₃
- V across all three

**Key Finding:**
```diff
! Total voltage = Sum of individual voltages
! V = V₁ + V₂ + V₃
```

**Why?**

**Energy perspective:**
- Battery gives energy to each charge
- This energy is potential energy (voltage × charge)
- Energy used up progressively through each resistor
- Total energy used = Sum of energies in each resistor
- Since Q same, voltages add

**Analogy:**
- Water falling down steps
- Total height drop = Sum of each step
- Each step: Some potential energy lost
- Total: All potential energy lost

---

### Deriving Series Resistance Formula

**Given:**
- Three resistors: R₁, R₂, R₃ in series
- Current I through all (same)
- Voltages V₁, V₂, V₃ across each
- Total voltage V

**Find:** Equivalent resistance R_s

---

**Step 1: Apply Ohm's law to each resistor**

```
V₁ = I × R₁
V₂ = I × R₂
V₃ = I × R₃
```

---

**Step 2: Apply Ohm's law to whole combination**

```
V = I × R_s
```

where R_s is equivalent (series) resistance

---

**Step 3: Use voltage addition**

```
V = V₁ + V₂ + V₃

Substituting:
I × R_s = I × R₁ + I × R₂ + I × R₃

Dividing by I:
R_s = R₁ + R₂ + R₃
```

---

**CRITICAL RESULT:**

```diff
! SERIES COMBINATION:
! R_s = R₁ + R₂ + R₃ + ... + R_n
!
! Equivalent resistance = SUM of individual resistances
! R_s is GREATER than any individual resistance
```

**Why greater?**
- Like adding obstacles in path
- Electrons must pass through all
- Total opposition is sum of individual oppositions

---

### Example 11.7 Complete Analysis

**Circuit:**
- Electric lamp: R₁ = 20 Ω
- Conductor: R₂ = 4 Ω
- Battery: V = 6 V
- Series connection

**Questions:**
(a) Total resistance
(b) Current through circuit
(c) Potential difference across each component

---

**Part (a): Total Resistance**

```
R_s = R₁ + R₂
R_s = 20 Ω + 4 Ω
R_s = 24 Ω
```

```diff
+ Series resistances simply ADD
+ 24 Ω is greater than both 20 Ω and 4 Ω (as expected)
```

---

**Part (b): Current**

```
Using V = I × R_s:
I = V / R_s
I = 6 V / 24 Ω
I = 0.25 A = 250 mA
```

**This current flows through BOTH components** (series property)

---

**Part (c): Voltage Across Each**

**Across lamp (R₁ = 20 Ω):**
```
V₁ = I × R₁
V₁ = 0.25 A × 20 Ω
V₁ = 5 V
```

**Across conductor (R₂ = 4 Ω):**
```
V₂ = I × R₂
V₂ = 0.25 A × 4 Ω
V₂ = 1 V
```

---

**Verification:**
```
V₁ + V₂ = 5 V + 1 V = 6 V = V ✓
```

**Insights:**

```diff
! Component with HIGHER resistance gets MORE voltage
! R₁ = 20 Ω gets 5 V (5/6 of total)
! R₂ = 4 Ω gets 1 V (1/6 of total)
! Ratio of voltages = Ratio of resistances
! V₁/V₂ = R₁/R₂ = 20/4 = 5/1
```

**This is voltage division:**
```
V₁ = V × [R₁/(R₁+R₂)]
V₂ = V × [R₂/(R₁+R₂)]
```

---

### Properties of Series Circuits (Summary)

**1. Current:**
```diff
+ Same current through all components
+ I₁ = I₂ = I₃ = I
+ This is how we identify series connection
```

**2. Voltage:**
```diff
+ Total voltage = Sum of voltages
+ V = V₁ + V₂ + V₃
+ Voltage divides proportionally to resistance
```

**3. Resistance:**
```diff
+ Total resistance = Sum of resistances
+ R_s = R₁ + R₂ + R₃
+ R_s > any individual R
```

**4. Applications:**
- Voltage dividers
- Christmas lights (old type)
- Switches (must be in series)

**5. Disadvantages:**
```diff
- If one component fails (opens), entire circuit breaks
- All components must be on/off together
- Not suitable for household wiring
```

---

## 7. Resistors in Parallel

### Activity 11.6 - Voltage Across Parallel Resistors

**Setup:** Three resistors connected across same two points X and Y

**Key Observation:**
```diff
! Voltage across each resistor is SAME
! V₁ = V₂ = V₃ = V
! This is the DEFINING property of parallel connection
```

**Why is voltage same?**

**Same two points:**
- All resistors connected between X and Y
- Potential at X is fixed
- Potential at Y is fixed
- Potential difference from X to Y is same for all
- All resistors "see" same voltage

**Analogy:**
- Water pipes from same reservoir to same drain
- All pipes have same pressure difference
- Parallel connection

---

### Current Distribution in Parallel

**From Activity:**
- Total current from battery: I
- Current through R₁: I₁
- Current through R₂: I₂
- Current through R₃: I₃

**Key Finding:**
```diff
! Total current = Sum of branch currents
! I = I₁ + I₂ + I₃
```

**Why?**

**Conservation of charge:**
- Current splits at junction X
- Each branch carries some current
- Currents rejoin at junction Y
- Total current out = Total current in
- Like river splitting into streams

---

### Deriving Parallel Resistance Formula

**Given:**
- Three resistors: R₁, R₂, R₃ in parallel
- Same voltage V across all
- Currents I₁, I₂, I₃ through each
- Total current I

**Find:** Equivalent resistance R_p

---

**Step 1: Apply Ohm's law to each resistor**

```
I₁ = V / R₁
I₂ = V / R₂
I₃ = V / R₃
```

---

**Step 2: Apply Ohm's law to whole combination**

```
I = V / R_p
```

where R_p is equivalent (parallel) resistance

---

**Step 3: Use current addition**

```
I = I₁ + I₂ + I₃

Substituting:
V/R_p = V/R₁ + V/R₂ + V/R₃

Dividing by V:
1/R_p = 1/R₁ + 1/R₂ + 1/R₃
```

---

**CRITICAL RESULT:**

```diff
! PARALLEL COMBINATION:
! 1/R_p = 1/R₁ + 1/R₂ + 1/R₃ + ... + 1/R_n
!
! Reciprocal of equivalent resistance = SUM of reciprocals
! R_p is LESS than any individual resistance
```

**Why less?**
- Like adding parallel paths
- More paths → Easier for current to flow
- Total opposition decreases

---

### Special Case: Two Resistors in Parallel

**Formula:**
```
1/R_p = 1/R₁ + 1/R₂

Getting common denominator:
1/R_p = (R₂ + R₁)/(R₁ × R₂)

Inverting:
R_p = (R₁ × R₂)/(R₁ + R₂)
```

**Mnemonic: "Product over Sum"**

---

**Special Sub-case: Two EQUAL resistors**

If R₁ = R₂ = R:
```
R_p = (R × R)/(R + R) = R²/2R = R/2
```

```diff
+ Two equal resistors in parallel: R_p = R/2
+ Three equal resistors in parallel: R_p = R/3
+ n equal resistors in parallel: R_p = R/n
```

---

### Example 11.8 Complete Analysis

**Given:**
- R₁ = 5 Ω
- R₂ = 10 Ω
- R₃ = 30 Ω
- V = 12 V
- All in parallel

**Find:**
(a) Current through each resistor
(b) Total current
(c) Total resistance

---

**Part (a): Current Through Each**

**All resistors have same voltage V = 12 V across them**

```
I₁ = V/R₁ = 12 V / 5 Ω = 2.4 A
I₂ = V/R₂ = 12 V / 10 Ω = 1.2 A
I₃ = V/R₃ = 12 V / 30 Ω = 0.4 A
```

**Observation:**
```diff
! Resistor with LOWEST resistance gets HIGHEST current
! R₁ = 5 Ω (smallest) gets I₁ = 2.4 A (largest)
! R₃ = 30 Ω (largest) gets I₃ = 0.4 A (smallest)
! Current divides INVERSELY proportional to resistance
```

---

**Part (b): Total Current**

```
I = I₁ + I₂ + I₃
I = 2.4 A + 1.2 A + 0.4 A
I = 4.0 A
```

---

**Part (c): Total Resistance**

**Method 1: Using 1/R_p formula**

```
1/R_p = 1/R₁ + 1/R₂ + 1/R₃

1/R_p = 1/5 + 1/10 + 1/30

Finding common denominator (LCM of 5, 10, 30 is 30):
1/R_p = 6/30 + 3/30 + 1/30
1/R_p = 10/30 = 1/3

Therefore:
R_p = 3 Ω
```

**Method 2: Using I = V/R_p**

```
R_p = V/I = 12 V / 4 A = 3 Ω ✓
```

---

**Verification and Insights:**

```diff
! R_p = 3 Ω < R₁ = 5 Ω (smallest individual R)
! Parallel resistance is ALWAYS less than smallest individual resistance
! Adding parallel resistors DECREASES total resistance
! Opposite of series (where adding resistors increases total R)
```

**Why this makes sense:**
- Adding parallel resistor = Adding another current path
- More paths = Lower total resistance
- Like opening more checkout lanes → faster flow

---

### Example 11.9 - Mixed Series-Parallel

**Circuit Analysis:**

```
   ┌─[R₁=10Ω]─┬─[R₃=30Ω]──┐
   |          |            |
   |      [R₂=40Ω]    [R₄=20Ω]
   |          |            |
   |          └─[R₅=60Ω]───┘
   |                       |
   └───────────────────────┘
        12V Battery
```

**Analysis Strategy:** Simplify step by step

---

**Step 1: Identify parallel groups**

**Group 1:** R₁ and R₂ in parallel
**Group 2:** R₃, R₄, R₅ in parallel

---

**Step 2: Find equivalent of Group 1 (R₁ ∥ R₂)**

```
1/R' = 1/R₁ + 1/R₂
1/R' = 1/10 + 1/40
1/R' = 4/40 + 1/40 = 5/40
R' = 40/5 = 8 Ω
```

---

**Step 3: Find equivalent of Group 2 (R₃ ∥ R₄ ∥ R₅)**

```
1/R" = 1/R₃ + 1/R₄ + 1/R₅
1/R" = 1/30 + 1/20 + 1/60

Common denominator = 60:
1/R" = 2/60 + 3/60 + 1/60 = 6/60 = 1/10

R" = 10 Ω
```

---

**Step 4: Simplified circuit**

Now we have:
- R' = 8 Ω (equivalent of Group 1)
- R" = 10 Ω (equivalent of Group 2)
- These are in SERIES

```
Total R = R' + R" = 8 Ω + 10 Ω = 18 Ω
```

---

**Step 5: Total current**

```
I = V/R = 12 V / 18 Ω = 0.67 A
```

---

**Key Skills:**
1. Identify parallel vs series connections
2. Simplify parallel groups first
3. Then combine series resistances
4. Work systematically, step by step

```diff
! For complex circuits:
! - Identify groups (parallel or series)
! - Replace each group with equivalent
! - Repeat until one resistance remains
! - Then calculate current/voltage
```

---

### Properties of Parallel Circuits (Summary)

**1. Voltage:**
```diff
+ Same voltage across all components
+ V₁ = V₂ = V₃ = V
+ This is how we identify parallel connection
```

**2. Current:**
```diff
+ Total current = Sum of branch currents
+ I = I₁ + I₂ + I₃
+ Current divides inversely proportional to resistance
```

**3. Resistance:**
```diff
+ Reciprocals add
+ 1/R_p = 1/R₁ + 1/R₂ + 1/R₃
+ R_p < any individual R
```

**4. Applications:**
- Household wiring (essential!)
- Parallel circuits in electronics
- Multiple devices operating independently

**5. Advantages:**
```diff
+ If one component fails, others continue working
+ Each device can be controlled independently
+ Each device gets full voltage
+ Adding devices doesn't affect voltage of existing ones
```

---

### Why Home Wiring is Parallel

**Imagine Series Home Wiring (Hypothetical):**

**Problems:**
1. All appliances share 220 V
   - 10 bulbs → Each gets 22 V → Won't light properly
   
2. All must be on/off together
   - Can't turn off one bulb while keeping others on
   
3. If one fails, all stop working
   - One fused bulb → Entire house goes dark
   
4. Same current through all
   - Would limit what appliances you can use

**With Parallel Wiring (Reality):**

**Advantages:**
1. Each appliance gets full 220 V
   - Works at designed power
   
2. Independent control
   - Each has its own switch
   
3. If one fails, others unaffected
   - One bulb fuses → Others still work
   
4. Each draws its needed current
   - Can use any combination of appliances

```diff
! This is why EVERY electrical installation uses parallel wiring
! Not an option - it's a necessity!
```

---

## 8. Heating Effect of Electric Current

### Why Does Current Produce Heat?

**Back to Electron Collisions:**

**Electron's Journey:**
1. Electric field accelerates electron
2. Electron gains kinetic energy
3. Electron collides with atom
4. **Energy transferred to atom**
5. Atom vibrates more
6. Vibration = Heat
7. Process repeats

**Energy Conversion:**
```
Electrical Energy → Kinetic Energy of Electrons → Heat Energy (Vibrations)
```

```diff
! Heating is INEVITABLE consequence of current flow
! Cannot have current without some heating
! In resistors, ALL electrical energy → Heat
```

---

### Deriving Joule's Law

**Energy considerations:**

**Potential energy of charge Q at voltage V:**
```
PE = Q × V
```

**When charge flows through resistor:**
- Loses potential energy
- Energy converted to heat

**Charge flowing in time t:**
```
Q = I × t
```

**Energy dissipated = Heat produced:**
```
H = Q × V
H = (I × t) × V
H = V × I × t
```

---

**Using Ohm's law V = I × R:**

```
H = (I × R) × I × t
H = I² × R × t
```

**This is Joule's Law of Heating:**

```diff
! H = I²Rt
!
! where:
! H = Heat produced (joules)
! I = Current (amperes)
! R = Resistance (ohms)
! t = Time (seconds)
```

---

### Understanding Joule's Law

**The I² Factor:**

```diff
! Heat depends on SQUARE of current
! Double current → 4 times heat
! Triple current → 9 times heat
! Very sensitive to current!
```

**Example:**
- 1 A through 10 Ω for 10 s:
  ```
  H = 1² × 10 × 10 = 100 J
  ```

- 2 A through 10 Ω for 10 s:
  ```
  H = 2² × 10 × 10 = 400 J (4 times more!)
  ```

**The R Factor:**
```diff
+ Heat proportional to resistance
+ Higher resistance → More heat (for same current)
+ This is why heating elements have high resistance
```

**The t Factor:**
```diff
+ Heat proportional to time
+ Longer current flows → More heat accumulated
+ Why leaving heater on overnight is expensive
```

---

### Alternative Forms of Heating Formula

**Form 1 (Joule's Law):**
```
H = I²Rt
```
**Use when:** I and R are known

---

**Form 2 (using V = IR):**
```
H = VIt
```
**Use when:** V and I are known

**Derivation:**
```
Since V = IR,
H = I²Rt = I × (IR) × t = VIt
```

---

**Form 3 (using I = V/R):**
```
H = (V²/R) × t
```
**Use when:** V and R are known

**Derivation:**
```
H = I²Rt
Since I = V/R,
H = (V/R)² × R × t
H = (V²/R²) × R × t
H = (V²/R) × t
```

---

**Summary of Forms:**

| Known Quantities | Formula to Use |
|------------------|----------------|
| I and R | H = I²Rt |
| V and I | H = VIt |
| V and R | H = V²t/R |

---

### Example 11.10 Complete Analysis

**Electric Iron:**
- **Maximum heating:** P_max = 840 W at V = 220 V
- **Minimum heating:** P_min = 360 W at V = 220 V

**Find:** Current and resistance in each case

---

**Understanding the Question:**

**Why different power ratings?**
- Electric iron has heating control
- Switch selects different resistance coils
- High heat: Low resistance coil
- Low heat: High resistance coil

---

**Part (a): Maximum Heating (840 W)**

**Find current:**
```
P = VI
I = P/V
I = 840 W / 220 V
I = 3.82 A
```

**Find resistance:**
```
Method 1: R = V/I
R = 220 V / 3.82 A = 57.6 Ω

Method 2: P = V²/R
R = V²/P
R = (220)² / 840
R = 48,400 / 840 = 57.6 Ω ✓
```

---

**Part (b): Minimum Heating (360 W)**

**Find current:**
```
I = P/V = 360 W / 220 V = 1.64 A
```

**Find resistance:**
```
R = V/I = 220 V / 1.64 A = 134.15 Ω
```

---

**Comparison:**

| Mode | Power | Current | Resistance |
|------|-------|---------|------------|
| Max heat | 840 W | 3.82 A | 57.6 Ω |
| Min heat | 360 W | 1.64 A | 134.1 Ω |

**Insights:**
```diff
! More heat → Lower resistance → Higher current
! Less heat → Higher resistance → Lower current
! For same voltage, P ∝ I and P ∝ 1/R
```

**Mechanism:**
- Switch connects different resistance coils
- Low R coil: More current, more heat
- High R coil: Less current, less heat

---

### Example 11.11 Deep Dive

**Given:**
- Heat H = 100 J per second (i.e., 100 J in t = 1 s)
- Resistance R = 4 Ω

**Find:** Potential difference V

---

**Solution Strategy:**

**Step 1: Find current using H = I²Rt**

```
H = I²Rt
100 J = I² × 4 Ω × 1 s

I² = 100 / 4 = 25
I = √25 = 5 A
```

---

**Step 2: Find voltage using V = IR**

```
V = I × R
V = 5 A × 4 Ω
V = 20 V
```

---

**Alternative Method (Direct):**

Using H = V²t/R:
```
100 = V² × 1 / 4
V² = 400
V = 20 V ✓
```

---

**Physical Interpretation:**

**Power dissipated:**
```
P = H/t = 100 J / 1 s = 100 W
```

**Check using P = VI:**
```
P = 20 V × 5 A = 100 W ✓
```

**This 4 Ω resistor:**
- Carries 5 A current
- Has 20 V across it
- Dissipates 100 W power
- Produces 100 J heat per second

---

## 9. Applications of Heating Effect

### Devices Using Joule Heating

**Principle:** Convert electrical energy to heat efficiently

**Common Heating Appliances:**

1. **Electric Iron**
   - Resistance coil heats metal plate
   - Temperature control via different resistances
   - Typical power: 750-1000 W

2. **Electric Heater**
   - Nichrome coil glows red-hot
   - Heat by radiation and convection
   - Typical power: 1000-2000 W

3. **Electric Kettle**
   - Heating element inside water
   - Direct heat transfer
   - Typical power: 1500-2000 W

4. **Electric Toaster**
   - Nichrome wire gets very hot
   - Toasts bread by radiation
   - Typical power: 600-1200 W

5. **Electric Oven**
   - Multiple heating elements
   - Temperature controlled
   - Typical power: 2000-5000 W

---

### Electric Bulb (Incandescent)

**Special Case: Heat → Light**

**Construction:**
- Tungsten filament
- Glass bulb filled with inert gas (nitrogen, argon)
- Very thin wire → Very high resistance

**Operation:**
```
Current → Heating → Very high temperature (2500-3000°C) → Light emission
```

**Why Tungsten?**

```diff
+ Highest melting point of metals: 3380°C
+ Can reach very high temperatures without melting
+ Emits light when hot
+ Strong, doesn't sag when hot
```

**Why Inert Gas?**
- Prevents oxidation of filament
- Tungsten would burn in oxygen at high temperature
- Extends bulb life

**Inefficiency:**
```diff
! Only 5% of electrical energy → Light
! 95% wasted as heat!
! That's why LED bulbs replacing incandescent
```

**Modern Alternative (LED):**
- Much more efficient (20-30% efficiency)
- Little heat produced
- Longer life
- Based on different principle (electroluminescence, not heating)

---

### Electric Fuse - Critical Safety Application

**Purpose:** Protect circuit from excessive current

**Construction:**
- Thin wire of alloy (typically tin-lead)
- Low melting point (~200°C)
- Rated for specific current (1A, 5A, 15A, etc.)
- Enclosed in ceramic/glass cartridge

**How It Works:**

**Normal Operation:**
```
Current within limit → Wire carries safely → Circuit intact
```

**Overload/Short Circuit:**
```
Excessive current → I² heating large → Temperature exceeds melting point → Fuse melts → Circuit breaks → Protection
```

---

**Why Low Melting Point Material?**

```diff
! Fuse must melt BEFORE house wiring gets dangerously hot
! House wiring: Copper (melting point 1085°C)
! Fuse wire: Tin-lead alloy (melting point ~200°C)
! Fuse melts first, protecting expensive wiring
```

**Material Properties:**

| Material | Melting Point | Usage |
|----------|---------------|-------|
| Tin-Lead Alloy | ~200°C | Fuse wire |
| Copper | 1085°C | House wiring |
| Aluminum | 660°C | Power lines |

**Fuse melts, sacrificing itself to protect circuit**

---

**Fuse Rating:**

**Example: 5A Fuse**
```diff
+ Designed to carry up to 5A safely
+ If current exceeds ~6-7A, starts to heat excessively
+ At higher currents, melts within seconds
+ Breaks circuit before damage occurs
```

**How to Select Fuse:**
1. Calculate normal operating current
2. Select fuse rating slightly higher (10-20% safety margin)
3. Much lower than wire capacity

**Example:**
- Circuit normally uses 4 A
- Select 5 A fuse
- House wire capacity: 15 A
- If current reaches 8 A → Fuse blows → Wire protected

---

**Two Situations Causing Fuse to Blow:**

**1. Short Circuit**

**What Happens:**
- Live and neutral wires touch directly
- Resistance ≈ 0 Ω
- Current I = V/R → ∞ (theoretically)

**Example:**
```
Normal: R = 100 Ω, I = 220V/100Ω = 2.2 A
Short circuit: R ≈ 0 Ω, I = 220V/0Ω → Very large!
```

**Causes:**
- Damaged insulation
- Wire insulation melts and bare wires touch
- Faulty appliance
- Rodents chewing wires

**Danger without fuse:**
- Wires heat up instantly
- Insulation catches fire
- House fire

---

**2. Overloading**

**What Happens:**
- Too many appliances on single circuit
- Total current exceeds circuit capacity

**Example:**
- 5 A circuit (with 5 A fuse)
- Connect:
  - 2 bulbs: 0.2 A each = 0.4 A
  - Fan: 0.3 A
  - TV: 0.5 A
  - Heater: 5 A
  - **Total: 6.2 A**
- Exceeds 5 A rating
- Fuse blows

**Prevention:**
```diff
! Don't connect too many appliances to one socket
! Heavy appliances (AC, heater, geyser) need separate circuits
! Use 15A circuit for high-power devices
```

---

**Modern Replacement: MCB (Miniature Circuit Breaker)**

**Advantages over Fuse:**
1. **Reusable**
   - Fuse: Melts, must replace
   - MCB: Trips, can reset

2. **Faster response**
   - Electromagnetic mechanism
   - Trips in milliseconds

3. **More reliable**
   - Mechanical device
   - Precise current cutoff

4. **Convenient**
   - No replacement needed
   - Just flip switch to reset

**But Principle Same:**
- Detects overcurrent
- Breaks circuit
- Protects wiring and appliances

---

## 10. Electric Power

### Definition and Understanding

**Power = Rate of energy consumption**

```
Power (P) = Energy (E) / Time (t)

P = E/t
```

**In electrical context:**

**Energy consumed by current:**
```
E = VIt  (from H = VIt, as heat is energy)
```

**Power:**
```
P = E/t = VIt/t = VI
```

```diff
! P = VI
!
! Power = Voltage × Current
```

**Units:**
```
P in watts (W)
V in volts (V)
I in amperes (A)

1 W = 1 V × 1 A
```

---

### What is 1 Watt?

```diff
+ 1 Watt of power is consumed when:
+ 1 Ampere current flows
+ At 1 Volt potential difference
```

**Equivalently:**
- 1 W = 1 Joule per second
- Device consuming 1 W uses 1 J of energy every second

**Practical Powers:**
- LED bulb: 5-10 W
- CFL bulb: 15-25 W
- Incandescent bulb: 60-100 W
- Ceiling fan: 50-80 W
- Refrigerator: 100-400 W
- Air conditioner: 1000-2000 W
- Electric kettle: 1500-2000 W

---

### Alternate Forms of Power Formula

**Form 1 (Basic):**
```
P = VI
```
**Use when:** V and I are known

---

**Form 2 (using Ohm's law V = IR):**
```
P = VI = (IR) × I = I²R
```
**Use when:** I and R are known

---

**Form 3 (using I = V/R):**
```
P = VI = V × (V/R) = V²/R
```
**Use when:** V and R are known

---

**Summary:**

| Known Quantities | Formula |
|------------------|---------|
| V and I | P = VI |
| I and R | P = I²R |
| V and R | P = V²/R |

**These are all equivalent, just choose based on what you know**

---

### Kilowatt and Larger Units

**Watt is too small for many applications:**

**Kilowatt (kW):**
```
1 kW = 1000 W
```

**Examples:**
- Electric iron: 1 kW
- Geyser: 2 kW
- Air conditioner: 1.5 kW
- Household: 2-5 kW total

**Megawatt (MW):**
```
1 MW = 1000 kW = 10⁶ W
```
Used for large motors, power plants

**Gigawatt (GW):**
```
1 GW = 1000 MW = 10⁹ W
```
Used for power stations
- Typical coal plant: 500-1000 MW
- Nuclear plant: 1000-1500 MW

---

## 11. Electrical Energy and its Commercial Unit

### Energy vs Power

**Critical Distinction:**

```diff
! Power = Rate of energy consumption (how fast)
! Energy = Total amount consumed (how much)
!
! Power × Time = Energy
```

**Analogy:**
- Speed vs Distance
- Power vs Energy
- Speed × Time = Distance
- Power × Time = Energy

---

### Units of Electrical Energy

**SI Unit: Joule (J)**

```
Energy (J) = Power (W) × Time (s)
```

**Too small for practical use:**
- 100 W bulb for 1 hour:
  ```
  E = 100 W × 3600 s = 360,000 J
  ```
- Inconvenient large numbers

---

### Commercial Unit: Kilowatt-hour (kWh)

**Definition:**
```diff
+ 1 kWh = Energy consumed when 1 kW power is used for 1 hour
```

**Calculation:**
```
1 kWh = 1 kW × 1 hour
      = 1000 W × 3600 s
      = 3,600,000 J
      = 3.6 × 10⁶ J
      = 3.6 MJ (megajoules)
```

**Also called:**
- "Unit" of electricity
- Electricity meter measures in kWh
- Your electricity bill charges per kWh

**Typical Costs (India, 2024):**
- Domestic: ₹5-8 per kWh
- Commercial: ₹8-12 per kWh
- Industrial: ₹6-10 per kWh

---

### Calculating Electricity Consumption

**Formula:**
```
Energy (kWh) = Power (kW) × Time (hours)
```

**Examples:**

**1. 100 W bulb for 10 hours:**
```
Power = 100 W = 0.1 kW
Time = 10 hours
Energy = 0.1 kW × 10 h = 1 kWh
```

**2. 1500 W heater for 2 hours:**
```
Power = 1500 W = 1.5 kW
Time = 2 hours
Energy = 1.5 kW × 2 h = 3 kWh
```

**3. 750 W TV for 5 hours daily for 30 days:**
```
Daily: 0.75 kW × 5 h = 3.75 kWh
Monthly: 3.75 kWh × 30 = 112.5 kWh
```

---

### Example 11.12 Analysis

**Given:** 
- Bulb: P = 220 V, I = 0.50 A

**Find:** Power

**Solution:**
```
P = VI
P = 220 V × 0.50 A
P = 110 W
```

**Interpretation:**
- Bulb consumes 110 watts
- In 1 hour: 0.11 kWh
- In 10 hours: 1.1 kWh
- At ₹6/kWh: 10 hours costs ₹6.60

---

### Example 11.13 Complete Analysis

**Given:**
- Refrigerator: 400 W
- Usage: 8 hours/day
- Duration: 30 days
- Rate: ₹3.00 per kWh

**Find:** Total cost

---

**Solution:**

**Step 1: Convert power to kW**
```
P = 400 W = 0.4 kW
```

**Step 2: Calculate daily energy**
```
Daily energy = P × t
             = 0.4 kW × 8 h
             = 3.2 kWh/day
```

**Step 3: Calculate monthly energy**
```
Monthly energy = 3.2 kWh/day × 30 days
               = 96 kWh
```

**Step 4: Calculate cost**
```
Cost = Energy × Rate
     = 96 kWh × ₹3.00/kWh
     = ₹288.00
```

---

**Practical Insights:**

**Daily cost:**
```
3.2 kWh × ₹3 = ₹9.60/day
```

**Yearly cost:**
```
96 kWh/month × 12 months × ₹3 = ₹3,456/year
```

**If rate increases to ₹5/kWh:**
```
96 kWh × ₹5 = ₹480/month
```

```diff
! This shows why energy-efficient appliances matter
! 30% more efficient refrigerator saves ~₹100/month
! Over 10-year life: ₹12,000 saved!
```

---

## 12. Common Misconceptions Clarified

### Misconception 1: Current Gets "Used Up"

```diff
- Wrong: "Current decreases as it goes through resistors"
+ Correct: Current is SAME throughout series circuit
+ Charges don't disappear
+ Same rate in = Same rate out
+ Energy gets used, not current
```

---

### Misconception 2: Voltage "Flows"

```diff
- Wrong: "Voltage flows through the wire"
+ Correct: CURRENT flows, voltage is potential DIFFERENCE
+ Voltage is like height difference
+ Water flows downhill, but height doesn't flow
+ Similarly, current flows through voltage difference
```

---

### Misconception 3: Higher Resistance = More Heat

```diff
- Wrong: "Always choose high R for more heat"
+ Correct: Depends on whether V or I is constant
+ If current I constant: H = I²Rt → Higher R → More heat ✓
+ If voltage V constant: H = V²t/R → Higher R → LESS heat ✗
+ In household (V = 220V constant): Lower R → More heat
```

**Example:**
- Two heaters across 220 V
- Heater A: R = 50 Ω
- Heater B: R = 100 Ω

```
Heater A: P = V²/R = (220)²/50 = 968 W (More heat)
Heater B: P = V²/R = (220)²/100 = 484 W (Less heat)

Lower R produces MORE heat when voltage is constant!
```

---

### Misconception 4: Battery "Stores Current"

```diff
- Wrong: "Battery contains current"
+ Correct: Battery stores CHEMICAL ENERGY
+ Creates potential difference
+ Potential difference pushes existing electrons in wire
+ Battery doesn't supply electrons, wire already has them
```

---

### Misconception 5: Parallel Resistors Always Have More Resistance

```diff
- Wrong: "Adding resistor always increases total R"
+ Correct: 
+ Series: Adding R increases total (R_s = R₁ + R₂)
+ Parallel: Adding R decreases total (1/R_p = 1/R₁ + 1/R₂)
+ Parallel: R_p always < smallest individual R
```

---

### Misconception 6: Ammeter and Voltmeter Are Interchangeable

```diff
- Wrong: "Can connect either in series or parallel"
+ Correct:
+ Ammeter: ALWAYS series (measures current through)
+ Voltmeter: ALWAYS parallel (measures voltage across)
+ Wrong connection can damage instrument or give wrong readings
```

---

### Misconception 7: Power and Energy Are the Same

```diff
- Wrong: "100 W bulb uses 100 units per hour"
+ Correct:
+ Power = 100 W (rate of energy consumption)
+ Energy = Power × Time = 100 W × 1 h = 0.1 kWh
+ 0.1 kWh = 0.1 units
+ Not 100 units!
```

---

## 13. Summary Tables

### Formula Quick Reference

| Quantity | Formula(s) | Unit |
|----------|-----------|------|
| **Current** | I = Q/t | Ampere (A) |
| **Voltage** | V = W/Q | Volt (V) |
| **Resistance** | R = V/I = ρl/A | Ohm (Ω) |
| **Power** | P = VI = I²R = V²/R | Watt (W) |
| **Energy** | E = Pt = VIt = I²Rt = V²t/R | Joule (J) or kWh |
| **Heat** | H = I²Rt = VIt = V²t/R | Joule (J) |
| **Series R** | R_s = R₁ + R₂ + R₃ | Ohm (Ω) |
| **Parallel R** | 1/R_p = 1/R₁ + 1/R₂ + 1/R₃ | Ohm (Ω) |

---

### Series vs Parallel Comparison

| Property | Series | Parallel |
|----------|--------|----------|
| **Current** | Same through all (I₁ = I₂ = I) | Divides (I = I₁ + I₂ + I₃) |
| **Voltage** | Divides (V = V₁ + V₂ + V₃) | Same across all (V₁ = V₂ = V) |
| **Resistance** | R_s = R₁ + R₂ + R₃ | 1/R_p = 1/R₁ + 1/R₂ + 1/R₃ |
| **Total R vs Individual** | R_s > any R | R_p < smallest R |
| **Effect of Adding R** | Increases total R | Decreases total R |
| **One Component Fails** | All stop working | Others keep working |
| **Application** | Switches, voltage dividers | Home wiring, current dividers |

---

### Units and Conversions

| Quantity | Units | Conversions |
|----------|-------|-------------|
| **Current** | 1 A | = 10³ mA = 10⁶ μA |
| **Voltage** | 1 V | = 1 J/C |
| **Resistance** | 1 Ω | = 1 V/A |
| **Power** | 1 W | = 1 J/s = 1 V·A |
|  | 1 kW | = 10³ W |
| **Energy** | 1 J | = 1 W·s |
|  | 1 kWh | = 3.6 × 10⁶ J = 3.6 MJ |
| **Charge** | 1 C | = charge of 6.24 × 10¹⁸ electrons |

---

### Resistivity Values (Key Materials)

| Material | Type | Resistivity (Ω m) | Application |
|----------|------|------------------|-------------|
| **Silver** | Conductor | 1.6 × 10⁻⁸ | Best conductor (expensive) |
| **Copper** | Conductor | 1.62 × 10⁻⁸ | Wiring (good, affordable) |
| **Aluminum** | Conductor | 2.63 × 10⁻⁸ | Power lines (light) |
| **Tungsten** | Conductor | 5.2 × 10⁻⁸ | Bulb filaments (high melting point) |
| **Nichrome** | Alloy | 100 × 10⁻⁸ | Heaters (high R, doesn't oxidize) |
| **Glass** | Insulator | 10¹⁰ - 10¹⁴ | Insulation |
| **Rubber** | Insulator | 10¹³ - 10¹⁶ | Wire coating |

---

## 14. Problem-Solving Strategies

### Type 1: Basic Ohm's Law Problems

**Given:** Any two of V, I, R

**Find:** Third quantity

**Strategy:**
1. Write down V = IR
2. Identify what's known
3. Solve for unknown

**Example:**
- V = 12 V, R = 6 Ω, find I
- I = V/R = 12/6 = 2 A

---

### Type 2: Series Circuit Problems

**Approach:**
1. Find total resistance: R_s = R₁ + R₂ + ...
2. Find total current: I = V/R_s
3. Same current flows through all resistors
4. Find individual voltages: V₁ = IR₁, V₂ = IR₂, ...
5. Verify: V = V₁ + V₂ + ...

---

### Type 3: Parallel Circuit Problems

**Approach:**
1. Find equivalent resistance: 1/R_p = 1/R₁ + 1/R₂ + ...
2. Find total current: I = V/R_p
3. Same voltage across all resistors
4. Find branch currents: I₁ = V/R₁, I₂ = V/R₂, ...
5. Verify: I = I₁ + I₂ + ...

---

### Type 4: Mixed Series-Parallel

**Approach:**
1. Identify parallel groups
2. Find equivalent of each parallel group
3. Identify series combinations
4. Simplify step by step
5. Calculate current/voltage working backwards

---

### Type 5: Heating/Power Problems

**Strategy:**

**Choose correct formula based on what's given:**

| Given | For Power | For Heat/Energy |
|-------|-----------|-----------------|
| V and I | P = VI | E = VIt |
| I and R | P = I²R | E = I²Rt |
| V and R | P = V²/R | E = V²t/R |

**Energy problems:**
1. Calculate power first
2. Multiply by time: E = P × t
3. Convert units if needed (W to kW, s to h)

---

### Type 6: Electrical Cost Problems

**Steps:**
1. Convert power to kW (divide watts by 1000)
2. Calculate energy: E (kWh) = Power (kW) × Time (hours)
3. Calculate cost: Cost = Energy (kWh) × Rate (₹/kWh)

**Template:**
```
Power = ___ W = ___ kW
Daily usage = ___ hours
Daily energy = ___ kW × ___ h = ___ kWh
Monthly energy = ___ kWh × 30 days = ___ kWh
Cost = ___ kWh × ₹___/kWh = ₹___
```

---

## 15. Exam-Important Questions

### 3-Mark Questions

**Q1: State Ohm's law. Draw V-I graph for ohmic conductor. What does slope represent?**

**Answer:**
1. **Statement:** At constant temperature, current through conductor is directly proportional to potential difference across it. V ∝ I or V = IR

2. **Graph:** Straight line through origin

3. **Slope:** Represents resistance R

---

**Q2: An electric iron of resistance 20 Ω takes current of 5 A. Calculate heat developed in 30 s.**

**Answer:**
```
Given: R = 20 Ω, I = 5 A, t = 30 s

Using H = I²Rt:
H = (5)² × 20 × 30
H = 25 × 20 × 30
H = 15,000 J = 15 kJ
```

---

### 5-Mark Questions

**Q1: Derive expression for equivalent resistance when three resistors are connected in series.**

**Answer:**
1. **Diagram:** Show three resistors R₁, R₂, R₃ in series with battery V
2. **Current:** Same through all: I₁ = I₂ = I₃ = I
3. **Voltage:** V = V₁ + V₂ + V₃ (across series)
4. **Ohm's law for each:**
   - V₁ = IR₁
   - V₂ = IR₂
   - V₃ = IR₃
5. **Total:** V = IR_s
6. **Substitution:** IR_s = IR₁ + IR₂ + IR₃
7. **Cancelling I:** R_s = R₁ + R₂ + R₃
8. **Conclusion:** Equivalent series resistance equals sum

---

**Q2: Why is series arrangement not used for domestic circuits? Explain with reasons.**

**Answer:**

**Problems with series:**
1. **Voltage division**
   - 220 V divides among appliances
   - Each gets less than rated voltage
   - Won't operate properly

2. **Same current**
   - All appliances must use same current
   - Not practical (bulb needs 0.2 A, heater needs 5 A)

3. **Dependent operation**
   - All must be on/off together
   - No individual control

4. **Single point failure**
   - One appliance fails → All stop
   - One bulb fuses → Entire house dark

**Parallel connection solves all these:**
- Each appliance gets full 220 V
- Each draws its required current
- Independent control
- Failure of one doesn't affect others

---

## 16. Practical Tips for Exams

### Must-Know Formulas

**Memorize these (and know when to use each):**

```diff
! CRITICAL FORMULAS:
! 
! 1. Ohm's Law: V = IR
! 2. Resistance: R = ρl/A
! 3. Series: R_s = R₁ + R₂ + R₃
! 4. Parallel: 1/R_p = 1/R₁ + 1/R₂ + 1/R₃
! 5. Power: P = VI = I²R = V²/R
! 6. Energy: E = Pt = VIt
! 7. Heating: H = I²Rt = VIt = V²t/R
! 8. Current: I = Q/t
! 9. Voltage: V = W/Q
! 10. Energy unit: 1 kWh = 3.6 × 10⁶ J
```

---

### Common Calculation Mistakes

**1. Unit conversion errors**
```diff
- Don't forget: mm → m, mA → A, kW → W
+ Always convert to SI units before calculating
```

**2. Parallel resistance**
```diff
- Don't directly add: R_p ≠ R₁ + R₂
+ Add reciprocals: 1/R_p = 1/R₁ + 1/R₂
+ Then invert: R_p = 1/(1/R₁ + 1/R₂)
```

**3. Power formulas**
```diff
- Don't confuse: P = I²R with P = V²R
+ Correct: P = I²R or P = V²/R (note denominator!)
```

**4. Energy vs Power**
```diff
- Don't confuse: 100 W bulb doesn't use 100 kWh in 1 hour
+ Correct: 100 W = 0.1 kW; Energy = 0.1 kW × 1 h = 0.1 kWh
```

---

### Drawing Circuit Diagrams

**Use standard symbols (Table 11.1):**
- Don't draw actual pictures
- Use conventional symbols
- Label all components clearly
- Show current direction
- Mark voltage measurement points

**For series:**
- Draw components in line (one after another)

**For parallel:**
- Draw branches clearly
- Show common connection points

---

### Numerical Problem Tips

**Before calculating:**
1. Write "Given" - list all known quantities
2. Write "Find" - what you need to calculate
3. Write "Formula" - which equation to use
4. Then substitute values

**While calculating:**
1. Show all steps
2. Don't skip steps (lose marks for "no working")
3. Keep units throughout
4. Round to appropriate precision (2-3 decimal places)

**After calculating:**
1. Check if answer makes sense
2. Verify units are correct
3. State answer clearly

---

### Quick Mental Checks

**Series:**
- Total R should be > largest individual R
- Current same through all
- Sum of voltages = Total voltage

**Parallel:**
- Total R should be < smallest individual R
- Current into junction = Current out
- Voltage same across all

**Power/Heating:**
- More current/voltage → More power
- Longer time → More energy
- Check if answer magnitude reasonable

---

## 17. Connections to Real Life

### Why Some Appliances Are "Heavy Appliances"

**Heavy (High Power):**
- Electric iron: 1000 W
- Geyser: 2000 W
- AC: 1500 W

**Why called heavy?**
- Draw more current (at 220 V)
- Need thicker wires
- Separate circuit recommended
- More expensive to run

**Light (Low Power):**
- LED bulb: 10 W
- CFL bulb: 15 W
- Phone charger: 10 W

**Why light?**
- Less current
- Can share circuits
- Economical

---

### Why Transmission Lines Use High Voltage

**Problem:** Power loss in transmission

**Loss in wires:**
```
P_loss = I²R_wire
```

**Same power delivered:**
```
P = VI

Higher V → Lower I (for same P)
Lower I → Much lower I²R loss
```

**Example:**
- Deliver 1000 kW
- At 1000 V: I = 1000 A → Loss = I²R (huge!)
- At 100,000 V: I = 10 A → Loss = I²R (100× less!)

**This is why:**
- Power lines: 11,000 V to 400,000 V
- Then stepped down to 220 V at homes

---

### Why Electrical Wiring Gets Hot When Overloaded

**Ohm's law + Joule heating:**

**Normal operation:**
- Wire R = 0.1 Ω
- Current I = 10 A
- Heat = I²Rt = 100 × 0.1 × t = 10t watts

**Overloaded:**
- Same wire R = 0.1 Ω  
- Current I = 20 A (doubled)
- Heat = I²Rt = 400 × 0.1 × t = 40t watts (4× more!)

```diff
! Current doubles → Heat quadruples! (I² factor)
! Wire temperature rises
! Insulation melts
! Fire hazard!
! This is why fuses/MCBs critical
```

---

### Why LED Bulbs Save Money

**Comparison for same brightness:**

| Type | Power | Daily (5h) | Monthly | Cost @ ₹6/kWh |
|------|-------|------------|---------|---------------|
| **Incandescent** | 60 W | 0.3 kWh | 9 kWh | ₹54 |
| **CFL** | 15 W | 0.075 kWh | 2.25 kWh | ₹13.50 |
| **LED** | 10 W | 0.05 kWh | 1.5 kWh | ₹9 |

**Yearly saving (LED vs Incandescent):**
```
₹54 - ₹9 = ₹45 per month
₹45 × 12 = ₹540 per year per bulb!
```

**For 10 bulbs in house: ₹5,400/year saved!**

---

*End of Electricity Notes - Master these concepts and you'll excel in understanding and applying electrical principles!*