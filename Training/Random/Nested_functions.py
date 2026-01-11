
def full_name (first_name, last_name):
    def format_name (full_name):
        spaces_removed = full_name.strip()
        final_name = spaces_removed.capitalize()
        return final_name
    full = format_name(first_name)+ " " +format_name(last_name)
    return full

formatted_full_name = full_name("   john", "    Smith")
print(formatted_full_name)