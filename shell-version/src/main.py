"""Main CLI file for Task List Application."""

import click

import src.cli.tasklist_commands as tc


@click.group()
def main():
    """Manage tasks group in the Task List CLI."""
    pass


def commands():
    """
    Register subcommands with the main CLI.

    This function registers all the available subcommands with
        the main CLI group.
    """
    main.add_command(tc.add_task)
    main.add_command(tc.remove_task_by_name)
    main.add_command(tc.remove_task_by_id)

    main.add_command(tc.set_due_date_by_name)
    main.add_command(tc.set_due_date_by_id)

    main.add_command(tc.set_description_by_name)
    main.add_command(tc.set_description_by_id)

    main.add_command(tc.set_task_completion_by_name)
    main.add_command(tc.set_task_completion_by_id)

    main.add_command(tc.complete_task_by_name)
    main.add_command(tc.complete_task_by_id)

    main.add_command(tc.display_tasks)
    main.add_command(tc.display_tasks_by_completion)


if __name__ == "__main__":
    commands()
    main()
