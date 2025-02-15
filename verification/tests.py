"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [[1, 2, 3, 4, 5]],
            "answer": [5, 4, 3, 2, 1],
        },
        {
            "input": [[5, 7, 10, 4, 2, 7, 8, 1, 3]],
            "answer": [10, 7, 5, 4, 8, 7, 2, 3, 1],
        },
        {
            "input": [[5, 4, 3, 2, 1]],
            "answer": [5, 4, 3, 2, 1],
        },
        {
            "input": [[]],
            "answer": [],
        },
        {
            "input": [[1]],
            "answer": [1],
        },
        {
            "input": [[1, 1]],
            "answer": [1, 1],
        },
        {
            "input": [[1, 1, 2]],
            "answer": [1, 2, 1],
        }
    ],
    "Extra": [
        {
            "input": [[1, 2, 2, 3]],
            "answer": [2, 1, 3, 2],
        },
        {
            "input": [[1, 1, 1]],
            "answer": [1, 1, 1],
        }
    ]
}
