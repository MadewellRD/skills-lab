# Operator Field Verification

Use when `deploy.model` is `operator_run`: the agent is forbidden by policy or invariant from executing the deploy, and must not route around that. The agent prepares, the operator executes, the agent verifies from what landed on disk.

## Shape

Two blocks, each a single paste for the operator, each writing every output to an evidence folder (`work/<packet>-field/`, ignored by the repository) so the agent reads results from files, never from pasted narrative.

Block 1 (changes nothing on the running system):
1. Check out the merged tip; record the sha; assert tree-equality to the receipt sha (`git diff --quiet`, exit code recorded).
2. Snapshot the running system: process list with session and parent, installed artifact hash, release artifact hash, the running build identity from its own endpoint.
3. Run the deploy script in plan-only mode and write the plan.
The agent verifies the plan from disk and only then issues block 2.

Block 2 (the change):
1. Copy the gate-built artifacts to a per-sha folder and hash them; refuse to continue on mismatch (the block prints a stop line and touches nothing).
2. Run the deploy script against the copies with machine-readable output.
3. Snapshot the system again: process list, installed hash, build identity, leftover aside images.

## Verification from disk

The agent reads the evidence files and checks, at minimum: deploy exit code; the identity verdict in the script's own output; installed hash equals the gate artifact hash; the running build identity equals the receipt sha; a new service process, in the expected session, owning the listener; processes that must survive (client connectors) present before and after with the same ids; expected leftovers only. Then the agent runs its own behavioral probes through the governed surface where policy allows, and records them in the same folder.

Closure is written with the evidence paths. A deploy "verified" from the operator's description is not verified.

## Rules

- The deploy script must never run as a child of the service it manages; a plan-only run through the governed surface is still a child.
- If the operator's checkout is also an agent's working tree, block 1's checkout can switch the branch under the agent. The profile's worktree rule exists for this; until it is in force, pause the agent before block 1 and have it re-check out its branch after block 2.
- Roll back by the script's own printed rollback commands, never by killing processes.
