#! /usr/bin/env python3

import re
import sys

def expand_inline_or_self_closing(line):
    """
    Expand single-line self-closing or inline tags with =, space, or {payload}.
    """
    pattern = re.compile(r'^(\s*)\[(\w+)(.*?)\s*(/?)\]\s*$')
    match = pattern.match(line)
    if not match:
        return line
    indent, tag, content, slash = match.groups()
    # Expand if self-closing, inline with = or space, or if it contains {macro}
    expand = slash == "/" or "=" in content or " " in content or (content.startswith("{") and content.endswith("}"))
    content = content.strip()
    if not expand:
        return line
    if content:
        args: list[str] = []
        for arg in re.split(r"\s+", content):
            if (tag == "specials"):
                args.append(f"{{WEAPON_SPECIAL_{arg.upper()}}}")
            elif (tag == "abilities"):
                args.append(f"{{ABILITY_{arg.upper()}}}")
            else:
                args.append(arg)

        content_body = "\n".join(f"{indent}    {a}" for a in args)
        return f"{indent}[{tag}]\n{content_body}\n{indent}[/{tag}]"
    else:
        return f"{indent}[{tag}]\n{indent}[/{tag}]"

def process_file(input_file, output_file=None):
    if output_file is None:
        output_file = input_file
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = [l.rstrip('\n') for l in f.readlines()]
    # Pass 1: expand self-closing / inline tags
    lines = [expand_inline_or_self_closing(l) for l in lines]
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("\n".join(lines) + "\n")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python wml_expand.py input_file [output_file]")
        sys.exit(1)
    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None
    process_file(input_file, output_file)
    print(f"Processed {input_file} -> {output_file or input_file}")
