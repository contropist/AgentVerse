from agentverse.agentverse import AgentVerse
from argparse import ArgumentParser

parser = ArgumentParser()
# parser.add_argument("--task", type=str, default="nlp_classroom_9players")
# parser.add_argument("--task", type=str, default="nlp_classroom_3players_nolc")

parser.add_argument("--task", type=str, default="prisoner_dilema")
args = parser.parse_args()
agentverse = AgentVerse.from_task(args.task)
agentverse.run()