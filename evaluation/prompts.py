demo_prompt_extract = """
I am providing you a response from a model to a math problem, termed 'Model Response'. You should extract the answer from the response as 'Extracted Answer'. Directly output the extracted answer with no explanation.

1.
Model response: 'Rounded to two decimal places, the perimeter of the sector is approximately:\n\n(-2, 1)'
Extracted Answer: (-2, 1)

2.
Model response: 'at those points.\n\nTherefore, the correct option that represents the meaning of the intersection points of the graphs is:\n\nD. They give the solutions to the equation $f(t)=g(t)$.",'
Extracted Answer: D

3.
Model response: ' at 1 (there's a closed circle at y = 1), the range in interval notation is \\((-4, 1]\\).\n\nFinal values:\nDomain: \\((-3, 3]\\)\nRange: \\((-4, 1]\\)'
Extracted Answer: Domain: \\((-3, 3]\\)\nRange: \\((-4, 1]\\)

4.
Model response: 'As it stands, I cannot provide the correct option letter because there isn't enough information to solve for 'y'.'
Extracted Answer: null

5.
Model response: 'Given that AB = 17.6 meters, we can now substitute into the equation:\n\nd = 17.6 / cos(38\u00b0)\n\nTherefore, to one decimal place, the distance d between Ned and Bart is approximately 22.3 meters.'
Extracted answer: 22.3

6.
Model response:  have all the coefficients for the quadratic function:\n\\( f(x) = ax^2 + bx + c \\)\n\\( f(x) = -1x^2 - 2x + 1 \\)\n\nTherefore, the equation for the graphed function \\( f \\) is:\n\\( f(x) = -x^2 - 2x + 1 \\)"'
Extracted answer: f(x) = -x^2 - 2x + 1

7.
"""

# Model response: 'value for \\( x \\) is given, this is the expression for \\( L \\) in terms of \\( x \\):\n\n\\( L = 2 \\sqrt{(5x + 7)^2 - (2x + 3)^2} \\)'
# Official Answer: \\frac{5\\left(5x+7\\right)}{2x+3} units
# Extracted answer: \\( L = 2 \\sqrt{(5x + 7)^2 - (2x + 3)^2} \\)
# Whether '\\frac{5\\left(5x+7\\right)}{2x+3} units' and '\\( L = 2 \\sqrt{(5x + 7)^2 - (2x + 3)^2} \\)' are consistent: False

# Model response: 'To summarize, $\\tan (\\pi+\\theta)$ and $\\tan (2 \\pi-\\theta)$ are the expressions that are opposite to $\\tan (\\theta)$. Hence, the correct choices are:\n\nA and C'
# Official answer: C\nD
# Extracted answer: A and C
# Whether 'C\nD' and 'A and C' are consistent: False
        

demo_prompt_score = """
Below are two answers to a math question. Question is [Question], [Standard Answer] is the standard answer to the question, and [Model_answer] is the answer extracted from a model's output to this question.  Determine whether these two answers are consistent.
Please note that only when the [Model_answer] completely matches the [Standard Answer] means they are consistent. For non-multiple-choice questions, if the meaning is expressed in the same way, it is also considered consistent, for example, 0.5m and 50cm.
If they are consistent, Judement is 1; if they are different, Judement is 0.

[Question]: Write the set of numbers represented on the number line in interval notation.
[Standard Answer]: (-2,1]
[Model_answer] : Extracted Answer: \\((-2, 1)\\)
Judgement: 0

[Question]: Find the domain and range of the function f using interval notation.
[Standard Answer]: domain: [-4, 0) and range: (-3, 1]
[Model_answer] : Range: \\((-4, 1]\\)
Judgement: 0


[Question]: Two curves are symmetrical about the x-axis. Use the vertical line test to determine if this relation is a function.\nChoices:\nA:This is a function\nB:This is not a function
[Standard Answer]: B
[Model_answer] : This is not a function
Judgement: 1

[Question]: Given the graph of the ellipse that intersects with x-axis at 9 and -9 and with y-axis at 3 and -3, determine its equation.A. \\frac{{x^2}}{{81}} + \\frac{{y^2}}{{9}} = 1 B. Can not determine.\n
[Standard Answer]: A
[Model_answer] : \\frac{{x^2}}{{81}} + \\frac{{y^2}}{{9}} = 1
Judgement: 1

[Question]: {question}
[Standard Answer]: {gt}
[Model_answer] : {extraction}
Judgement: """

# Model response: 'value for \\( x \\) is given, this is the expression for \\( L \\) in terms of \\( x \\):\n\n\\( L = 2 \\sqrt{(5x + 7)^2 - (2x + 3)^2} \\)'
# Official Answer: \\frac{5\\left(5x+7\\right)}{2x+3} units
# Extracted answer: \\( L = 2 \\sqrt{(5x + 7)^2 - (2x + 3)^2} \\)
# Whether '\\frac{5\\left(5x+7\\right)}{2x+3} units' and '\\( L = 2 \\sqrt{(5x + 7)^2 - (2x + 3)^2} \\)' are consistent: False

# Model response: 'To summarize, $\\tan (\\pi+\\theta)$ and $\\tan (2 \\pi-\\theta)$ are the expressions that are opposite to $\\tan (\\theta)$. Hence, the correct choices are:\n\nA and C'
# Official answer: C\nD
# Extracted answer: A and C
# Whether 'C\nD' and 'A and C' are consistent: False