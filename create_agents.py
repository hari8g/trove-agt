import os

def create_agents_folder():
    # Define the root directory for the agents
    root_dir = "agents_trove"
    
    # List of scripts to create
    scripts = [
        "trove_agent.py",
        "trove_agent_rearrange.py",
        "trove_concurrent_workflows.py",
        "trove_forest.py",
        "trove_group_chat.py",
        "trove_hierarchical.py",
        "trove_parallel.py",
        "trove_sequential.py",
        "trove_spreadsheet.py",
        "trove_swarm_router.py"
    ]
    
    # Ensure the agents directory exists
    os.makedirs(root_dir, exist_ok=True)
    
    # Create empty Python scripts in the agents directory
    for script in scripts:
        script_path = os.path.join(root_dir, script)
        if not os.path.exists(script_path):
            with open(script_path, "w") as f:
                f.write("# {}\n".format(script))
            print(f"Created {script_path}")
        else:
            print(f"{script_path} already exists")

if __name__ == "__main__":
    create_agents_folder()
