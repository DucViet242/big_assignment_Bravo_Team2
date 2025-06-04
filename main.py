import tkinter as tk
from tkinter import ttk

from Variable import constants
from UI.Dasboard import setup_dashboard
from UI.Setup_add_screen import setup_add_screen
from UI.Setup_delete_screen import setup_delete_screen
from UI.Setup_update_screen import setup_update_screen
from UI.Setup_search_screen import setup_search_screen
from UI.event_handling import refresh_all
from other_functions.file_processing import create_directory_file


def main():
    # Ensure necessary folders and metadata file exist
    create_directory_file()

    # Initialize main window and notebook
    constants.root = tk.Tk()
    constants.root.title("Bravo Project Manager")

    constants.notebook = ttk.Notebook(constants.root)
    constants.dashboard_frame = ttk.Frame(constants.notebook)
    constants.add_frame = ttk.Frame(constants.notebook)
    constants.delete_frame = ttk.Frame(constants.notebook)
    constants.update_frame = ttk.Frame(constants.notebook)
    constants.search_frame = ttk.Frame(constants.notebook)

    constants.notebook.add(constants.dashboard_frame, text="Dashboard")
    constants.notebook.add(constants.add_frame, text="Add Project")
    constants.notebook.add(constants.delete_frame, text="Delete Project")
    constants.notebook.add(constants.update_frame, text="Update Project")
    constants.notebook.add(constants.search_frame, text="Search Project")
    constants.notebook.pack(fill=tk.BOTH, expand=True)

    # Setup each screen
    setup_dashboard()
    setup_add_screen()
    setup_delete_screen()
    setup_update_screen()
    setup_search_screen()

    # Perform initial synchronization and refresh
    refresh_all()

    constants.root.mainloop()


if __name__ == "__main__":
    main()
