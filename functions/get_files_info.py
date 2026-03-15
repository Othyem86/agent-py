import os

def get_files_info(working_directory: str, directory=".") -> str:
    try:
        abs_working_dir = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(abs_working_dir, directory))
        is_target_valid = os.path.commonpath([abs_working_dir, target_dir]) == abs_working_dir
        
        if not is_target_valid:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'
        
        items: list[str] = []
        for item in os.listdir(target_dir):
            item_path = os.path.join(target_dir, item)
            item_size = os.path.getsize(item_path)
            is_item_dir = os.path.isdir(item_path)
            item_info = f"- {item}: file_size={item_size} bytes, is_dir={is_item_dir}"
            items.append(item_info)
        return "\n".join(items)
    
    except Exception as e:
        return f'Error: {e}'