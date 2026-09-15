import os


def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))

        is_valid = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs

        if not is_valid:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'

        output_lines = []
        for item in os.listdir(target_dir):
            full_path = os.path.join(target_dir, item)
            is_dir = os.path.isdir(full_path)
            full_size = os.path.getsize(full_path)

            line = f"- {item}: file_size={full_size} bytes, is_dir={is_dir}"
            output_lines.append(line)

        return "\n".join(output_lines)

    except Exception as e:
        return f"Error: {str(e)}"
