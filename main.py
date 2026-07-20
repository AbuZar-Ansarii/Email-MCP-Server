from fastmcp import FastMCP
import random

mcp = FastMCP("funny-mcp")


ROASTS = [
    "Your code runs perfectly... after 17 Stack Overflow tabs.",
    "Congratulations! You've invented a new programming paradigm: 'Works On My Machine'.",
    "Your laptop fan just filed a complaint with HR.",
    "Your AI agent is one prompt away from demanding a salary.",
    "You've written so much Python that your keyboard automatically types 'import'.",
    "Your Docker containers have been running longer than some relationships.",
    "Your GPU saw your prompts and requested overtime pay.",
    "Your Git history looks like: 'fix', 'fix2', 'final', 'final_final', 'please_work'.",
    "Your TODO list has become a historical document.",
    "Your code is like a mystery novel—nobody knows how it works, including you.",
]


@mcp.tool()
def roast_me(name: str = "Developer") -> str:
    """
    Generates a light-hearted roast for the user.
    """
    return f"{name}, {random.choice(ROASTS)}"


@mcp.tool()
def rate_project(project_name: str) -> str:
    """
    Gives a completely unreliable project rating.
    """
    score = random.randint(1, 10)

    comments = [
        "Would accidentally become a startup.",
        "Impressive! Investors are already pretending to understand it.",
        "Looks like a weekend project that turned into a life commitment.",
        "Your future self will hate maintaining this.",
        "This belongs in a GitHub repository with 500 stars.",
        "Even ChatGPT is slightly concerned about this idea."
    ]

    return (
        f"Project: {project_name}\n"
        f"Score: {score}/10\n"
        f"Verdict: {random.choice(comments)}"
    )


@mcp.tool()
def excuse_generator() -> str:
    """
    Generates a random developer excuse.
    """
    excuses = [
        "The bug only appears when Mercury is in retrograde.",
        "It worked before the deployment, I swear.",
        "The server is shy today.",
        "That's not a bug; it's an undocumented feature.",
        "My AI assistant told me to do it.",
        "The code was written by my past self, and we are no longer on speaking terms.",
    ]

    return random.choice(excuses)


if __name__ == "__main__":
    mcp.run(transport ='http', host ='0.0.0.0', port =8000)
