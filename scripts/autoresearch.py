#!/usr/bin/env python3
"""
Autoresearch harness for Contentos skills.
Uses OpenCode CLI to run skills and evaluate outputs.

Usage:
    python autoresearch.py --skill customer-avatar --iterations 10
"""

import argparse
import os
import sys
import json
import subprocess
import re
import shutil
from datetime import datetime
from pathlib import Path

# Paths
REPO_ROOT = Path("/Users/guestr/Desktop/system")
CONTEXT_PATH = REPO_ROOT / "context" / "context.md"
ANSWERS_PATH = REPO_ROOT / "context" / "answers.md"
LOG_PATH = REPO_ROOT / "results" / "autoresearch-log.tsv"
SKILLS_DIR = REPO_ROOT / ".claude" / "skills"

# Map skill names to evals files
SKILL_TO_EVALS = {
    "customer-avatar": "avatar-evals.md",
    "offer-builder": "offer-evals.md",
}


def run_opencode(prompt: str, timeout: int = 120) -> str:
    """Run OpenCode CLI with a prompt and return the output."""
    result = subprocess.run(
        ["opencode", "run"],
        input=prompt,
        capture_output=True,
        text=True,
        timeout=timeout,
        cwd=str(REPO_ROOT),
    )

    if result.returncode != 0:
        raise RuntimeError(f"OpenCode failed: {result.stderr}")

    # Output is in stdout
    return result.stdout.strip()


def run_skill(skill_name: str) -> str:
    """Run the skill and return its output."""
    skill_path = SKILLS_DIR / skill_name / "SKILL.md"

    if not skill_path.exists():
        raise FileNotFoundError(f"Skill not found: {skill_path}")

    # Read the skill
    with open(skill_path, "r") as f:
        skill_content = f.read()

    # Read context
    with open(CONTEXT_PATH, "r") as f:
        context = f.read()

    # Build prompt for OpenCode
    prompt = f"""You are executing the {skill_name} skill.

Read the context below and produce the skill output.

## Context (READ ONLY - do not modify)
{context}

## Skill to Execute
```
{skill_content}
```

Execute this skill and output ONLY the final result. No commentary, no explanation. Just the output."""

    return run_opencode(prompt)


def evaluate_output(output: str, skill_name: str) -> tuple[int, int, list[str]]:
    """
    Evaluate output against binary criteria.
    Returns (passed, total, details)
    """
    # Get the correct evals file
    evals_filename = SKILL_TO_EVALS.get(skill_name, f"{skill_name}-evals.md")
    evals_path = SKILLS_DIR / skill_name / "evals" / evals_filename

    if not evals_path.exists():
        print(f"  WARNING: No evals file found at {evals_path}")
        return 0, 0, []

    # Parse evals
    with open(evals_path, "r") as f:
        evals_content = f.read()

    # Extract binary criteria (lines starting with - [ ])
    criteria = []
    for line in evals_content.split("\n"):
        if line.strip().startswith("- ["):
            # Extract the question/assertion
            match = re.search(r"- \[ \] (.+)", line)
            if match:
                criteria.append(match.group(1).strip())

    total = len(criteria)
    passed = 0
    details = []

    # Evaluate each criterion using OpenCode
    for i, criterion in enumerate(criteria):
        eval_prompt = f"""Evaluate this output against the binary criterion:

Criterion #{i + 1}: {criterion}

Output to evaluate:
{output[:2500]}

Respond with EXACTLY one word: PASS if the criterion is met, FAIL if not. No other words."""

        try:
            response = run_opencode(eval_prompt, timeout=30).strip().upper()
            is_pass = "PASS" in response
            passed += 1 if is_pass else 0
            details.append(f"{'PASS' if is_pass else 'FAIL'}: {criterion[:50]}...")
        except Exception as e:
            print(f"    Eval error for criterion {i + 1}: {e}")
            details.append(f"ERROR: {criterion[:50]}...")

    return passed, total, details


def load_evals(skill_name: str) -> list[str]:
    """Load eval criteria from file."""
    evals_filename = SKILL_TO_EVALS.get(skill_name, f"{skill_name}-evals.md")
    evals_path = SKILLS_DIR / skill_name / "evals" / evals_filename

    if not evals_path.exists():
        return []

    with open(evals_path, "r") as f:
        content = f.read()

    criteria = []
    for line in content.split("\n"):
        if line.strip().startswith("- ["):
            match = re.search(r"- \[ \] (.+)", line)
            if match:
                criteria.append(match.group(1).strip())

    return criteria


def mutate_skill(
    skill_name: str,
    current_output: str,
    pass_rate: float,
    iteration: int,
    failed_evals: list[str],
) -> str:
    """
    Use OpenCode to mutate the skill prompt based on eval failures.
    Returns a summary of what changed.
    """
    skill_path = SKILLS_DIR / skill_name / "SKILL.md"

    with open(skill_path, "r") as f:
        current_skill = f.read()

    failed_str = (
        "\n".join([f"- {e}" for e in failed_evals])
        if failed_evals
        else "No specific failures - improve generally"
    )

    mutation_prompt = f"""You are improving the {skill_name} skill based on eval results.

The current output had a {pass_rate:.0%} pass rate.

FAILED EVALUATIONS:
{failed_str}

CURRENT SKILL (first 3000 chars):
{current_skill[:3000]}

Based on what failed, propose modifications to the SKILL.md that would improve output quality.
Focus on:
1. Better instructions for the failed criteria
2. More specific constraints
3. Clearer output format requirements

Respond with ONLY the modified skill content. Keep the same YAML frontmatter format.
Make minimal, targeted changes - don't rewrite everything."""

    try:
        result = run_opencode(mutation_prompt, timeout=90)

        # Save mutated skill
        with open(skill_path, "w") as f:
            f.write(result)

        return f"Mutated based on {len(failed_evals)} failed evals"
    except Exception as e:
        raise RuntimeError(f"Mutation failed: {e}")


def save_skill_version(skill_name: str, iteration: int):
    """Save a backup of the current skill version."""
    skill_path = SKILLS_DIR / skill_name / "SKILL.md"
    backup_dir = SKILLS_DIR / skill_name / "autosearch_backups"
    backup_dir.mkdir(exist_ok=True)

    backup_file = backup_dir / f"v{iteration}.md"
    shutil.copy2(skill_path, backup_file)


def log_result(
    timestamp: str,
    skill: str,
    iteration: int,
    pass_rate: float,
    mutation_summary: str,
    result: str,
):
    """Append a row to the log file."""
    row = f"{timestamp}\t{skill}\t{iteration}\t{pass_rate:.2f}\t{mutation_summary}\t{result}\n"

    with open(LOG_PATH, "a") as f:
        f.write(row)


def git_commit(skill: str, iteration: int, pass_rate: float):
    """Git commit after successful mutation."""
    message = f"autoresearch: {skill} iteration {iteration} pass_rate {pass_rate:.2f}"

    # Stage the skill file
    skill_path = SKILLS_DIR / skill / "SKILL.md"

    result = subprocess.run(
        ["git", "add", str(skill_path)], cwd=REPO_ROOT, capture_output=True, text=True
    )

    if result.returncode != 0:
        print(f"  Warning: git add failed: {result.stderr}")
        return

    result = subprocess.run(
        ["git", "commit", "-m", message], cwd=REPO_ROOT, capture_output=True, text=True
    )

    if result.returncode == 0:
        print(f"  Committed: {message}")
    else:
        # Check if there's nothing to commit
        if "nothing to commit" in result.stderr:
            print(f"  No changes to commit")
        else:
            print(f"  Warning: git commit failed: {result.stderr}")


def main():
    parser = argparse.ArgumentParser(description="Autoresearch for Contentos skills")
    parser.add_argument(
        "--skill",
        required=True,
        choices=["customer-avatar", "offer-builder"],
        help="Skill to optimize",
    )
    parser.add_argument(
        "--iterations", type=int, default=10, help="Number of iterations to run"
    )
    parser.add_argument(
        "--dry-run", action="store_true", help="Run one iteration without mutating"
    )

    args = parser.parse_args()

    skill_name = args.skill

    print(f"=== Autoresearch: {skill_name} ===")
    print(f"Iterations: {args.iterations}")
    print(f"Dry run: {args.dry_run}")
    print()

    # Check max evals constraint
    evals = load_evals(skill_name)
    print(f"Eval criteria: {len(evals)}")

    if len(evals) > 6:
        print(f"WARNING: {len(evals)} evals exceeds max of 6.")

    if args.dry_run:
        print("\n=== DRY RUN MODE ===\n")

    # Track best pass rate
    best_pass_rate = 0.0
    best_skill_content = None

    # Load original skill
    skill_path = SKILLS_DIR / skill_name / "SKILL.md"
    with open(skill_path, "r") as f:
        original_skill = f.read()
    best_skill_content = original_skill

    timestamp = datetime.now().isoformat()

    for i in range(1, args.iterations + 1):
        print(f"\n--- Iteration {i}/{args.iterations} ---")

        try:
            # Run skill
            print(f"Running skill...")
            output = run_skill(skill_name)
            print(f"Skill output received ({len(output)} chars)")
            if len(output) < 100:
                print(f"  Output preview: {output[:200]}")

            # Evaluate output
            print(f"Evaluating output...")
            passed, total, details = evaluate_output(output, skill_name)

            if total == 0:
                print(f"  ERROR: No evals found - cannot evaluate")
                log_result(timestamp, skill_name, i, 0.0, "No evals file", "error")
                continue

            pass_rate = passed / total
            print(f"  Pass rate: {passed}/{total} = {pass_rate:.1%}")

            # Print eval details
            for d in details:
                print(f"    {d}")

            # Identify failed evals
            failed_evals = [d for d in details if d.startswith("FAIL")]

            # Decision: mutate or revert
            if pass_rate > best_pass_rate:
                print(f"  WIN! {pass_rate:.1%} > {best_pass_rate:.1%}")

                if not args.dry_run:
                    # Save previous best
                    save_skill_version(skill_name, i)

                    # Mutate skill
                    mutation_summary = mutate_skill(
                        skill_name, output, pass_rate, i, failed_evals
                    )
                    best_skill_content = open(skill_path).read()

                    # Log and commit
                    log_result(
                        timestamp, skill_name, i, pass_rate, mutation_summary, "win"
                    )
                    git_commit(skill_name, i, pass_rate)
                else:
                    log_result(
                        timestamp,
                        skill_name,
                        i,
                        pass_rate,
                        "Dry run - no mutation",
                        "win_dry",
                    )

                best_pass_rate = pass_rate

            else:
                print(f"  No improvement: {pass_rate:.1%} <= {best_pass_rate:.1%}")

                if not args.dry_run:
                    # Revert to best
                    with open(skill_path, "w") as f:
                        f.write(best_skill_content)
                    print(f"  Reverted to best version")
                    log_result(
                        timestamp,
                        skill_name,
                        i,
                        pass_rate,
                        "No improvement - reverted",
                        "revert",
                    )
                else:
                    log_result(
                        timestamp,
                        skill_name,
                        i,
                        pass_rate,
                        "Dry run - no mutation",
                        "no_change",
                    )

        except subprocess.TimeoutExpired:
            print(f"  ERROR: Timeout")
            if not args.dry_run and best_skill_content:
                with open(skill_path, "w") as f:
                    f.write(best_skill_content)
                log_result(timestamp, skill_name, i, 0.0, "Timeout", "error")
            else:
                log_result(timestamp, skill_name, i, 0.0, "Timeout", "error")

        except Exception as e:
            print(f"  ERROR: {e}")

            if not args.dry_run and best_skill_content:
                # Revert on crash
                with open(skill_path, "w") as f:
                    f.write(best_skill_content)
                print(f"  Reverted to best version after error")
                log_result(
                    timestamp, skill_name, i, 0.0, f"Error: {str(e)[:50]}", "error"
                )
            else:
                log_result(
                    timestamp, skill_name, i, 0.0, f"Error: {str(e)[:50]}", "error"
                )

    print(f"\n=== Complete ===")
    print(f"Best pass rate: {best_pass_rate:.1%}")
    print(f"Estimated cost: $0.00 (local model)")


if __name__ == "__main__":
    main()
