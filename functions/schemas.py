schema_get_files_info = {
    "type": "function",
    "function": {
        "name": "get_files_info",
        "description": "Lists files in a specified directory relative to the working directory, providing file size and directory status",
        "parameters": {
            "type": "object",
            "properties": {
                "directory": {
                    "type": "string",
                    "description": "Directory path to list files from, relative to the working directory (default is the working directory itself)",
                },
            },
        },
    },
}


schema_get_file_content = {
    "type": "function",
    "function": {
        "name": "get_file_content",
        "description": "Get the content of a file in a specified directory relative to the working directory, limited to MAX_CHARS characters.",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Path to the file to get the content from, relative to the working directory."
                },
            },
            "required": ["file_path"]
        },
    },
}


schema_run_python_file = {
    "type": "function",
    "function": {
        "name": "run_python_file",
        "description": "Run a Python file in the specified directory, with optional arguments. The file must be a regular Python file (ending in .py).",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Path to the Python file to run, relative to the working directory.",
                },
                "args": {
                    "type": "array",
                    "description": "Optional arguments to pass to the Python file.",
                    "items": {"type": "string"},
                },
            },
            "required": ["file_path"],
        },
    },
}


schema_write_file = {
    "type": "function",
    "function": {
        "name": "write_file",
        "description": "Write or overwrite content to a specified file.",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Path to the file to write to, relative to the working directory.",
                },
                "content": {
                    "type": "string",
                    "description": "The text content to write into the file.",
                },
            },
            "required": ["file_path", "content"],
        },
    },
}
