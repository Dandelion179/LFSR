def lfsr(initial_state, taps, steps):
    state = initial_state.copy()
    output = []

    for _ in range(steps):
        # Calculate the new bit as the XOR of the specified taps
        new_bit = 0
        for tap in taps:
            new_bit ^= state[tap]
        
        # Append the current state to the output
        output.append(state)
        
        # Shift the register and insert the new bit at the beginning
        state = [new_bit] + state[:-1]

    return output

# LFSR parameters
n = 8  # Number of bits in the LFSR
taps = [7, 5, 4, 3]  # Positions of the taps (0-based index, so 8 -> 7, 6 -> 5, etc.)

# Initial state (all bits set to 1)
initial_state = [1, 1, 1, 1, 1, 1, 1, 1]

print(initial_state)

# Number of steps to simulate
steps = 20

# Run the LFSR simulation
output = lfsr(initial_state, taps, steps)

for x in output:
    print(x)