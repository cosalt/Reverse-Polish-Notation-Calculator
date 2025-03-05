# Reverse Polish Notation (RPN) Calculator

A stack-based calculator that evaluates arithmetic expressions in Reverse Polish Notation (postfix notation). This implementation demonstrates the classic use of stack data structure for efficient expression evaluation.

## Features

- Evaluate basic arithmetic expressions in RPN format
- Supports four fundamental operations:
  - Addition (`+`)
  - Subtraction (`-`)
  - Multiplication (`*`)
  - Division (`/`)
- Error handling for invalid expressions and operations
- Clear stack-based implementation demonstrating data structure fundamentals

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/cosalt/Reverse-Polish-Notation-Calculator.git
   ```
2. Navigate to the project directory:
   ```
   cd Reverse-Polish-Notation-Calculator
   ```

## Usage

Enter numbers and operators separated by spaces in postfix notation. The calculator processes input tokens sequentially using a stack.

**Example input:**
```
5 1 2 + 4 * + 3 -
```

**Expected output:**
```
14
```

### Example Calculation
For expression `3 4 + 5 *`:
1. Push 3 → [3]
2. Push 4 → [3, 4]
3. Apply '+' → 3+4=7 → [7]
4. Push 5 → [7, 5]
5. Apply '*' → 7*5=35 → [35]

## How It Works

The calculator implements the standard stack-based algorithm for RPN evaluation:

1. Create an empty stack
2. Split input into tokens
3. For each token:
   - If number: push to stack
   - If operator:
     - Pop top two numbers from stack
     - Apply operation (second-popped [operator] first-popped)
     - Push result back to stack
4. Final result remains in stack

This approach ensures O(n) time complexity for n tokens.

## Error Handling

The calculator detects and reports:
- Insufficient operands for operations
- Invalid/non-numeric input tokens
- Division by zero attempts
- Empty input expressions
- Mismatched operations (multiple values remaining in stack)

## Contributing

Contributions are welcome! Please open an issue first to discuss proposed changes.

1. Fork the repository
2. Create your feature branch (```git checkout -b feature/your-feature```)
3. Commit your changes (```git commit -am 'Add some feature'```)
5. Push to the branch (```git push origin feature/your-feature```)
6. Open a Pull Request

## License

[MIT](LICENSE) (Add appropriate license file to your repository)
