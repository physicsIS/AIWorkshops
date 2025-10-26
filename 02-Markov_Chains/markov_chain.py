import random
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

class MarkovChainVisualizer:
    def __init__(self):
        """
        Initialize the Markov chain.
        """
        self.transitions = {
            'My': [('name', 0.5), ('business', 0.25), ('people', 0.25)],
            'name': [('is', 1.0)],
            'is': [('Sherlock', 0.5), ('My', 0.5)],
            'It': [('is', 1.0)],
            'Holmes': [('It', 1.0)],
            #'Sherlock': [('Holmes', 1.0)],
            'Sherlock': [('Holmes', 0.5), ('is', 0.5)],
            #'business': [('to', 1.0)],
            'business': [('to', 0.5), ('is', 0.5)],
            'to': [('know', 1.0)],
            'know': [('what', 1.0)],
            'what': [('other', 1.0)],
            #'people': [('do', 1.0)],
            'people': [('do', 0.75), ('is', 0.25)],
            'do': [('not', 1.0)],
            'not': [('know', 1.0)],
            'other': [('people', 1.0)]
        }
        
        self.states = list(self.transitions.keys())
    
    def get_transition_matrix(self):
        """
        Convert the transition dictionary to a matrix.
        """
        n = len(self.states)
        matrix = np.zeros((n, n))
        state_to_idx = {state: i for i, state in enumerate(self.states)}
        
        for state, transitions in self.transitions.items():
            i = state_to_idx[state]
            for next_state, prob in transitions:
                j = state_to_idx[next_state]
                matrix[i][j] = prob
        
        return matrix, state_to_idx
    
    def get_next_state(self, current_state):
        """Get the next state based on transition probabilities."""
        if current_state not in self.transitions:
            return None
        
        next_states, probabilities = zip(*self.transitions[current_state])
        return random.choices(next_states, weights=probabilities)[0]
    
    def random_walk(self, start_state, max_steps=20):
        """Perform a random walk starting from start_state."""
        if start_state not in self.states:
            return []
        
        path = [start_state]
        current = start_state
        visited_count = {state: 0 for state in self.states}
        visited_count[start_state] = 1
        
        for _ in range(max_steps):
            next_state = self.get_next_state(current)
            if next_state is None:
                break
            
            path.append(next_state)
            visited_count[next_state] += 1
            
            # Stop if we're in a cycle (visited same state 3+ times)
            if visited_count[next_state] >= 3:
                break
            
            current = next_state
        
        return path
    
    def generate_multiple_walks(self, start_state, num_walks=5, max_steps=20):
        """Generate multiple random walks from the same starting point."""
        walks = []
        for _ in range(num_walks):
            walk = self.random_walk(start_state, max_steps)
            walks.append(walk)
        return walks
    
    def print_transition_matrix(self):
        """Print the transition matrix."""
        matrix, state_to_idx = self.get_transition_matrix()
        
        print("\nTransition Matrix:")
        print("=" * 100)
        
        # Header
        header = "From \\ To"
        print(f"{header:<12}", end="")
        for state in self.states:
            print(f"{state:<8}", end="")
        print()
        print("-" * 100)
        
        # Rows
        for from_state in self.states:
            print(f"{from_state:<12}", end="")
            i = state_to_idx[from_state]
            for j in range(len(self.states)):
                prob = matrix[i][j]
                if prob > 0:
                    print(f"{prob:<8.2f}", end="")
                else:
                    print(f"{'—':<8}", end="")
            print()
        print("=" * 100)


def explore_markov_chain():
    """Interactive exploration of the Markov chain."""
    mc = MarkovChainVisualizer()
    
    print("╔" + "═" * 68 + "╗")
    print("║" + " " * 15 + "MARKOV CHAIN SENTENCE GENERATOR" + " " * 22 + "║")
    print("╚" + "═" * 68 + "╝")
    
    # Show transition matrix
    mc.print_transition_matrix()
    
    # Generate sentences from different starting points
    starting_points = {
        'My': "Introduction phrases (My name is...)",
        'It': "Statement phrases (It is Sherlock...)",
        'Sherlock': "Direct continuation",
        'people': "Mid-sentence start"
    }
    
    print("\n" + "═" * 70)
    print("SENTENCE GENERATION FROM DIFFERENT STARTING POINTS")
    print("═" * 70)
    
    for start_state, description in starting_points.items():
        print(f"\n📍 Starting point: '{start_state}' - {description}")
        print("-" * 70)
        
        walks = mc.generate_multiple_walks(start_state, num_walks=5, max_steps=25)
        
        for i, walk in enumerate(walks, 1):
            sentence = ' '.join(walk)
            print(f"  {i}. {sentence}")
    
    # Analyze common patterns
    print("\n" + "═" * 70)
    print("Common Patterns")
    print("═" * 70)
    
    # Run many walks and find common endings
    common_patterns = {}
    for start in ['My', 'people']:
        patterns = []
        for _ in range(20):
            walk = mc.random_walk(start, max_steps=17)
            sentence = ' '.join(walk)
            patterns.append(sentence)
        
        # Find most common pattern
        from collections import Counter
        pattern_counts = Counter(patterns)
        most_common = pattern_counts.most_common(2)
        
        print(f"\n📊 Starting from '{start}':")
        for pattern, count in most_common:
            print(f"  • [{count}/20] {pattern}")
    



if __name__ == "__main__":
    random.seed(42)
    explore_markov_chain()
    
    print("\n" + "╔" + "═" * 68 + "╗")
    print("║" + " " * 10 + "To use interactively, create an instance:" + " " * 17 + "║")
    print(" " + " " * 10 + "mc = MarkovChainVisualizer()" + " " * 28 + " ")
    print(" " + " " * 10 + "sentence = ' '.join(mc.random_walk('My', 20))" + " " * 9 + " ")
    print("╚" + "═" * 68 + "╝")
    #mc = MarkovChainVisualizer()
    #sentence = ' '.join(mc.random_walk('My', 20))
    #print(sentence)
