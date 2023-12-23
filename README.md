# Favorite Sites Management Script

This Python script facilitates the management of a list of favorite sites, providing the ability to add, remove, change the name, and change the address of sites. It can also display the list of favorite sites and open a specific site in the browser.

## Requirements

- Python 3.x
- Google Chrome (or adjust the browser executable path as needed)

## Usage

### Run the Script

\```bash
python script.py <command> [arguments]
\```

### Available Commands

- **\`add\`**: Add a new site to the list.
  \```bash
  python script.py add <link> <description>
  \```

- **\`remove\`**: Remove a site from the list.
  \```bash
  python script.py remove <index>
  \```

- **\`change_name\`**: Change the name of a site in the list.
  \```bash
  python script.py change_name <index> <new_name>
  \```

- **\`change_address\`**: Change the address of a site in the list.
  \```bash
  python script.py change_address <index> <new_address>
  \```

- **\`list\`** (or **\`l\`**, **\`list\`**): Display the list of favorite sites.
  \```bash
  python script.py list
  \```

- No command: Display the list of favorite sites and open a specific site in the browser.
  \```bash
  python script.py
  \```

## Contributions

Contributions are welcome! If you find bugs or have improvement suggestions, feel free to open an issue or submit a pull request.

# google_browser
Repository that contains the code that allows doing optimized google searches trhough the terminal 

## Where does this idea come from?: 

This code comes from this video:
https://www.youtube.com/watch?v=6wwHv-cyOd0
