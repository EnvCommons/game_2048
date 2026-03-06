import asyncio
import os
from env import Game2048Environment, MoveParams


def get_secrets():
    env_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env")
    secrets = {}
    if os.path.exists(env_path):
        with open(env_path) as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    key, val = line.split("=", 1)
                    secrets[key.strip().lower()] = val.strip()
    return secrets


async def smoke_test():
    print("=== Smoke Testing: 2048 ===\n")

    tasks = Game2048Environment.list_tasks(split="test")
    print(f"Test tasks: {len(tasks)}")
    print(f"First task: {tasks[0]}")

    secrets = get_secrets()
    env = Game2048Environment(task_spec=tasks[0], secrets=secrets)

    prompt = await env.get_prompt()
    print(f"\nPrompt ({len(prompt[0].text)} chars):")
    print(prompt[0].text[:500])

    result = await env.move(MoveParams(direction="up"))
    print(f"\nmove('up') result:")
    print(f"  Reward: {result.reward}")
    print(f"  Finished: {result.finished}")
    print(f"  Output: {result.blocks[0].text[:300]}")

    print("\n=== Smoke test PASSED ===")


if __name__ == "__main__":
    asyncio.run(smoke_test())
