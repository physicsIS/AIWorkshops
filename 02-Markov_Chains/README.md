# Markov Chains Homework

## Objective

Learn how to construct and use Markov chains for text generation by building a word-level Markov chain from a given sentence and performing random walks to generate new sentences.

## Assignment

**Turn the following sentence into a Markov chain and perform random walks:**

> "My name is Sherlock Holmes. It is my business to know what other people do not know."

### Tasks

1. **Build a Markov Chain**
   - Create a transition dictionary where each word (state) maps to possible next words with their transition probabilities
   - Calculate the transition probabilities based on word frequencies in the sentence

2. **Implement Random Walk**
   - Start from a given word (e.g., "My", "It", "Sherlock")
   - Follow the transition probabilities to generate new sentences
   - Stop after a maximum number of steps or when a cycle is detected

3. **Generate Multiple Sentences**
   - Perform several random walks from different starting points
   - Observe how different starting states lead to different sentence variations

4. **Analyze Results**
   - Print the transition matrix
   - Compare generated sentences with the original
   - Identify common patterns or cycles

## Background: What is a Markov Chain?

A **Markov chain** is a stochastic process where:
- The system moves from one state to another
- The next state depends **only** on the current state (memoryless property)
- Each transition has an associated probability

For text generation:
- **States** = words in the vocabulary
- **Transitions** = which word can follow which
- **Probabilities** = how likely each transition is

### Example

In the sentence "My name is Sherlock Holmes. It is my business...", the word "is" appears multiple times and can transition to different words:
- "is" → "Sherlock" (appears 1 time)
- "is" → "my" (appears 1 time)

So the transition probabilities would be:
- P(is → Sherlock) = 0.5
- P(is → my) = 0.5

## Implementation Guidelines

### 1. Data Structure

Create a dictionary to represent transitions:

```python
transitions = {
    'My': [('name', probability)],
    'name': [('is', probability)],
    # ... etc
}
```

### 2. Calculate Probabilities

For each word, count how many times it transitions to each possible next word, then normalize to get probabilities.

### 3. Random Walk Function

```python
def random_walk(start_state, max_steps=20):
    path = [start_state]
    current = start_state

    for _ in range(max_steps):
        # Get next state based on probabilities
        next_state = choose_next_state(current)
        path.append(next_state)
        current = next_state

    return path
```

### 4. Sentence Generation

Join the path from your random walk to create a sentence:

```python
sentence = ' '.join(path)
```

## Expected Output

Your program should be able to:

1. **Display the transition matrix** showing all possible transitions and their probabilities

2. **Generate sentences** starting from different words, for example:
   - Starting from "My": "My name is Sherlock Holmes It is my business to know..."
   - Starting from "It": "It is my business to know what other people do not know..."
   - Starting from "people": "people do not know what other people do not know..."

3. **Show variation** - running the random walk multiple times from the same starting point should produce different sentences (due to the randomness in following probabilities)

## Deliverables

Submit a Python file that includes:

1. A class or functions to:
   - Build the Markov chain from the given sentence
   - Perform random walks
   - Generate and print sentences

2. Example output showing:
   - The transition matrix
   - At least 5 generated sentences from different starting points
   - Analysis of common patterns

3. Comments explaining your approach

## Bonus Challenges

- **Cycle Detection**: Stop the random walk when it enters a loop (same sequence of words repeating)
- **Visualization**: Create a graph showing states and transitions
- **N-grams**: Extend to 2-word states (bigrams) instead of single words
- **Temperature Parameter**: Add control over randomness (deterministic vs random)

## Resources

- Reference implementation: `markov_chain.py` (check only after you tried yourself!)
- The key insight: In a word-level Markov chain, we're modeling the probability distribution of what word comes next given the current word

## Testing Your Solution

Ask yourself:
1. Do all transition probabilities from a state sum to 1.0?
2. Can you generate sentences that make grammatical sense?
3. Do you observe different outputs from the same starting point?
4. Does your random walk eventually stop or detect cycles?

