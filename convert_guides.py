#!/usr/bin/env python3
import os
import re
from datetime import datetime

# Mapping of guide files to MDC rules
guide_mappings = {
    '/home/ubuntu/new-mdc-rules/database-best-practices.md': {
        'number': '70',
        'name': 'database-standards',
        'title': 'Database Standards and Best Practices',
        'description': 'Comprehensive database standards for PostgreSQL, MySQL, SQLite, MongoDB, and Supabase with performance optimization',
        'globs': ['**/*.sql', '**/*.py', '**/*.js', '**/*.ts', '**/migrations/**', '**/models/**', '**/database/**', '**/db/**'],
        'activation': 'onLanguage:sql,python,javascript,typescript'
    },
    '/home/ubuntu/new-mdc-rules/traefik-configuration.md': {
        'number': '71',
        'name': 'traefik-proxy',
        'title': 'Traefik Proxy Configuration',
        'description': 'Traefik reverse proxy setup with Docker, SSL termination, and load balancing best practices',
        'globs': ['**/traefik/**', '**/docker-compose*.yml', '**/Dockerfile*', '**/*.toml', '**/proxy/**'],
        'activation': 'onLanguage:yaml,toml,dockerfile'
    },
    '/home/ubuntu/new-mdc-rules/memory-optimization.md': {
        'number': '72',
        'name': 'memory-optimization',
        'title': 'Memory Optimization and Performance',
        'description': 'Memory management, caching strategies, and performance optimization techniques across languages',
        'globs': ['**/*.py', '**/*.js', '**/*.ts', '**/*.go', '**/*.rs', '**/*.java', '**/cache/**', '**/performance/**'],
        'activation': 'onLanguage:python,javascript,typescript,go,rust,java'
    },
    '/home/ubuntu/new-mdc-rules/rule-authoring-meta.md': {
        'number': '73',
        'name': 'rule-authoring',
        'title': 'MDC Rule Authoring Guidelines',
        'description': 'Meta-practices and standards for creating effective Cursor MDC rules and documentation',
        'globs': ['**/*.mdc', '**/rules/**', '**/docs/**', '**/*.md'],
        'activation': 'onLanguage:markdown'
    },
    '/home/ubuntu/new-mdc-rules/fullstack-development.md': {
        'number': '74',
        'name': 'fullstack-patterns',
        'title': 'Full-Stack Development Patterns',
        'description': 'Modern full-stack architectures, SOLID principles, and CI/CD pipeline best practices',
        'globs': ['**/*.py', '**/*.js', '**/*.ts', '**/*.jsx', '**/*.tsx', '**/src/**', '**/api/**', '**/frontend/**', '**/backend/**'],
        'activation': 'onLanguage:python,javascript,typescript,jsx,tsx'
    }
}

def truncate_content(content, max_lines=450):
    """Truncate content to stay under 500 lines total (including front-matter)"""
    lines = content.split('\n')
    if len(lines) <= max_lines:
        return content
    
    # Keep first part and add truncation notice
    truncated = '\n'.join(lines[:max_lines-5])
    truncated += '\n\n---\n**Note**: Content truncated for brevity. See full documentation for complete details.\n---'
    return truncated

def clean_markdown_content(content):
    """Clean and optimize markdown content for MDC format"""
    # Remove excessive whitespace
    content = re.sub(r'\n{3,}', '\n\n', content)
    
    # Convert headers to be more concise
    content = re.sub(r'^# (.+)$', r'## \1', content, flags=re.MULTILINE)
    content = re.sub(r'^## (.+)$', r'### \1', content, flags=re.MULTILINE)
    
    # Add reference placeholders
    content = content.replace('database best practices', 'database best practices (@ref:70-database-standards)')
    content = content.replace('Traefik configuration', 'Traefik configuration (@ref:71-traefik-proxy)')
    content = content.replace('memory optimization', 'memory optimization (@ref:72-memory-optimization)')
    content = content.replace('rule authoring', 'rule authoring (@ref:73-rule-authoring)')
    content = content.replace('fullstack patterns', 'fullstack patterns (@ref:74-fullstack-patterns)')
    
    return content

def create_mdc_rule(guide_path, rule_info):
    """Convert markdown guide to MDC rule format"""
    
    # Read the original guide
    try:
        with open(guide_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Warning: Guide file not found: {guide_path}")
        return None
    
    # Clean and optimize content
    content = clean_markdown_content(content)
    content = truncate_content(content)
    
    # Create front-matter
    front_matter = f"""---
title: "{rule_info['title']}"
description: "{rule_info['description']}"
globs: {rule_info['globs']}
activation: "{rule_info['activation']}"
version: "2.0"
created: "{datetime.now().strftime('%Y-%m-%d')}"
updated: "{datetime.now().strftime('%Y-%m-%d')}"
---

"""
    
    # Combine front-matter with content
    mdc_content = front_matter + content
    
    # Write to .cursor/rules/ directory
    output_path = f".cursor/rules/{rule_info['number']}-{rule_info['name']}.mdc"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(mdc_content)
    
    print(f"Created: {output_path}")
    return output_path

# Convert all guides
created_files = []
for guide_path, rule_info in guide_mappings.items():
    result = create_mdc_rule(guide_path, rule_info)
    if result:
        created_files.append(result)

print(f"\nSuccessfully created {len(created_files)} MDC rules:")
for file in created_files:
    print(f"  - {file}")

