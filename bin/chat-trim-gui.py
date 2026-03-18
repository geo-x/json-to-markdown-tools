#!/usr/bin/env python3
"""
Chat Export Trimmer - GUI Version (Improved)
Handles macOS Tkinter deprecation and rendering issues
"""

import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from tkinter import font as tkFont
import json
from datetime import datetime
from pathlib import Path
import sys
import os
from collections import defaultdict

# Suppress Tkinter deprecation warning on macOS
os.environ['TK_SILENCE_DEPRECATION'] = '1'


class ChatTrimmerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Chat Export Trimmer")
        self.root.geometry("680x620")
        self.root.resizable(False, False)
        
        # Set style
        style = ttk.Style()
        style.theme_use('aqua' if sys.platform == 'darwin' else 'clam')
        
        self.input_file = tk.StringVar()
        self.output_dir = tk.StringVar(value=str(Path.home()))
        self.start_date = tk.StringVar()
        self.end_date = tk.StringVar()
        self.output_format = tk.StringVar(value="md")
        self.split_by_day = tk.BooleanVar(value=False)
        
        self.setup_ui()
        
        # Force window to front on macOS
        if sys.platform == 'darwin':
            self.root.after(100, self.root.lift)
            self.root.after(100, self.root.attributes, '-topmost', True)
            self.root.after(200, self.root.attributes, '-topmost', False)
    
    def setup_ui(self):
        """Setup the user interface"""
        main_frame = ttk.Frame(self.root, padding="15")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Title
        title_font = tkFont.Font(family="Helvetica", size=14, weight="bold")
        title = ttk.Label(main_frame, text="Chat Export Trimmer", font=title_font)
        title.grid(row=0, column=0, columnspan=3, pady=15)
        
        # Input file selection
        ttk.Label(main_frame, text="Input JSON File:").grid(row=1, column=0, sticky=tk.W, pady=8)
        ttk.Entry(main_frame, textvariable=self.input_file, width=45).grid(row=1, column=1, padx=5)
        ttk.Button(main_frame, text="Browse", command=self.browse_input, width=10).grid(row=1, column=2, padx=5)
        
        # Output directory
        ttk.Label(main_frame, text="Output Directory:").grid(row=2, column=0, sticky=tk.W, pady=8)
        ttk.Entry(main_frame, textvariable=self.output_dir, width=45).grid(row=2, column=1, padx=5)
        ttk.Button(main_frame, text="Browse", command=self.browse_output, width=10).grid(row=2, column=2, padx=5)
        
        # Date range section
        date_frame = ttk.LabelFrame(main_frame, text="Date Range", padding="12")
        date_frame.grid(row=3, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=12)
        
        ttk.Label(date_frame, text="Start Date (YYYY-MM-DD):").grid(row=0, column=0, sticky=tk.W, pady=6)
        ttk.Entry(date_frame, textvariable=self.start_date, width=25).grid(row=0, column=1, padx=5, sticky=tk.W)
        
        ttk.Label(date_frame, text="End Date (YYYY-MM-DD):").grid(row=1, column=0, sticky=tk.W, pady=6)
        ttk.Entry(date_frame, textvariable=self.end_date, width=25).grid(row=1, column=1, padx=5, sticky=tk.W)
        ttk.Label(date_frame, text="(optional - defaults to today)", font=("Helvetica", 9)).grid(row=1, column=2, sticky=tk.W, padx=5)
        
        # Format selection
        format_frame = ttk.LabelFrame(main_frame, text="Output Format", padding="12")
        format_frame.grid(row=4, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=12)
        
        ttk.Radiobutton(format_frame, text="Markdown (.md)", variable=self.output_format, value="md").grid(row=0, column=0, sticky=tk.W, pady=4)
        ttk.Radiobutton(format_frame, text="JSON (.json)", variable=self.output_format, value="json").grid(row=1, column=0, sticky=tk.W, pady=4)
        ttk.Radiobutton(format_frame, text="Both (.md and .json)", variable=self.output_format, value="both").grid(row=2, column=0, sticky=tk.W, pady=4)
        
        # Split by day option
        split_frame = ttk.LabelFrame(main_frame, text="Advanced Options", padding="12")
        split_frame.grid(row=5, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=12)
        
        ttk.Checkbutton(split_frame, text="Split into daily files (organized by month)", 
                       variable=self.split_by_day).grid(row=0, column=0, sticky=tk.W, pady=4)
        ttk.Label(split_frame, text="When enabled: creates YYYY-MM/DD.{format} per day", 
                 font=("Helvetica", 9), foreground="gray").grid(row=1, column=0, sticky=tk.W, padx=20)
        
        # Buttons
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=6, column=0, columnspan=3, pady=20)
        
        ttk.Button(button_frame, text="Process", command=self.process, width=12).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Clear", command=self.clear, width=12).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Exit", command=self.root.quit, width=12).pack(side=tk.LEFT, padx=5)
        
        # Status
        self.status_var = tk.StringVar(value="Ready")
        status_label = ttk.Label(main_frame, textvariable=self.status_var, foreground="blue")
        status_label.grid(row=7, column=0, columnspan=3, pady=10)
    
    def browse_input(self):
        """Browse for input file"""
        file = filedialog.askopenfilename(
            title="Select JSON Chat Export",
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
        )
        if file:
            self.input_file.set(file)
    
    def browse_output(self):
        """Browse for output directory"""
        directory = filedialog.askdirectory(title="Select Output Directory")
        if directory:
            self.output_dir.set(directory)
    
    def validate_inputs(self):
        """Validate user inputs"""
        if not self.input_file.get():
            messagebox.showerror("Error", "Please select an input file")
            return False
        
        if not Path(self.input_file.get()).exists():
            messagebox.showerror("Error", "Input file does not exist")
            return False
        
        if not self.start_date.get():
            messagebox.showerror("Error", "Please enter a start date")
            return False
        
        try:
            start = datetime.strptime(self.start_date.get(), '%Y-%m-%d')
            if self.end_date.get():
                end = datetime.strptime(self.end_date.get(), '%Y-%m-%d')
                if start > end:
                    messagebox.showerror("Error", "Start date must be before end date")
                    return False
        except ValueError:
            messagebox.showerror("Error", "Invalid date format. Use YYYY-MM-DD")
            return False
        
        return True
    
    def split_requests_by_day(self, requests):
        """Group requests by day"""
        daily_groups = defaultdict(list)
        
        for req in requests:
            timestamp = req.get('timestamp', 0)
            date_obj = datetime.fromtimestamp(timestamp/1000).date()
            daily_groups[date_obj].append(req)
        
        return dict(sorted(daily_groups.items()))
    
    def create_day_markdown(self, requests, date_obj):
        """Create markdown for a single day"""
        if not requests:
            return "# No messages for this day\n"
        
        date_str = date_obj.strftime('%B %d, %Y')
        md_content = f"# Chat Log: {date_str}\n\n"
        md_content += f"**Total Messages:** {len(requests)}\n\n"
        md_content += "---\n\n"
        
        for i, req in enumerate(requests, 1):
            timestamp = req.get('timestamp', 0)
            time_str = datetime.fromtimestamp(timestamp/1000).strftime('%H:%M:%S')
            
            # Extract user message (handle both text and parts format)
            message = req.get('message', {})
            if isinstance(message, dict):
                if 'text' in message:
                    message_text = message['text']
                elif 'parts' in message:
                    message_text = '\n'.join([p.get('text', '') for p in message['parts'] if p.get('text')])
                else:
                    message_text = str(message)
            else:
                message_text = str(message)
            
            md_content += f"## {i}. {time_str}\n\n"
            md_content += f"**User:**\n{message_text}\n\n"
            
            # Extract ALL response content (thinking blocks, code, everything)
            response_list = req.get('response', [])
            
            for resp_item in response_list:
                kind = resp_item.get('kind', '')
                value = resp_item.get('value', '')
                
                if kind == 'thinking':
                    # Include thinking/reasoning blocks
                    if value and value.strip():
                        md_content += f"**Reasoning:**\n{value}\n\n"
                elif kind == 'mcpServersStarting':
                    # Skip internal server markers
                    continue
                elif isinstance(value, str) and value.strip():
                    # Regular response text
                    md_content += f"**Assistant:**\n{value}\n\n"
            
            # Include code blocks if present in metadata
            result = req.get('result', {})
            metadata = result.get('metadata', {})
            code_blocks = metadata.get('codeBlocks', [])
            
            if code_blocks:
                md_content += f"**Code Generated:**\n"
                for j, block in enumerate(code_blocks, 1):
                    language = block.get('language', 'text')
                    filename = block.get('filename', '')
                    content = block.get('content', '')
                    
                    if filename:
                        md_content += f"\n{j}. `{filename}` ({language}):\n"
                    else:
                        md_content += f"\n{j}. Code ({language}):\n"
                    
                    md_content += f"```{language}\n{content}\n```\n"
            
            md_content += "---\n\n"
        
        return md_content
    
    def process(self):
        """Process the chat export"""
        if not self.validate_inputs():
            return
        
        try:
            self.status_var.set("Processing...")
            self.root.update()
            
            # Load JSON
            with open(self.input_file.get(), 'r') as f:
                data = json.load(f)
            
            # Parse dates
            start_date = datetime.strptime(self.start_date.get(), '%Y-%m-%d')
            end_date = datetime.strptime(self.end_date.get(), '%Y-%m-%d') if self.end_date.get() else datetime.now()
            
            # Filter requests
            start_ts = start_date.timestamp() * 1000
            end_ts = end_date.timestamp() * 1000
            
            requests = data.get('requests', [])
            filtered_requests = [
                req for req in requests 
                if start_ts <= req.get('timestamp', 0) <= end_ts
            ]
            
            if not filtered_requests:
                messagebox.showwarning("No Results", "No messages found in the specified date range")
                self.status_var.set("Ready")
                return
            
            output_dir = Path(self.output_dir.get())
            input_path = Path(self.input_file.get())
            date_range = f"{start_date.strftime('%d_%m_%y')}_to_{end_date.strftime('%d_%m_%y')}"
            base_name = f"{input_path.stem}_{date_range}"
            
            # Handle split-by-day mode
            if self.split_by_day.get():
                daily_groups = self.split_requests_by_day(filtered_requests)
                total_days = len(daily_groups)
                
                for day_idx, (date_obj, day_requests) in enumerate(daily_groups.items(), 1):
                    # Create year-month subdirectory
                    year_month_dir = output_dir / f"{date_obj.strftime('%Y-%m')}"
                    year_month_dir.mkdir(parents=True, exist_ok=True)
                    
                    # Get day number
                    day_num = date_obj.strftime('%d')
                    
                    # Create files
                    if self.output_format.get() in ['json', 'both']:
                        filtered_data = data.copy()
                        filtered_data['requests'] = day_requests
                        json_path = year_month_dir / f"{day_num}.json"
                        with open(json_path, 'w') as f:
                            json.dump(filtered_data, f, indent=2)
                    
                    if self.output_format.get() in ['md', 'both']:
                        md_content = self.create_day_markdown(day_requests, date_obj)
                        md_path = year_month_dir / f"{day_num}.md"
                        with open(md_path, 'w') as f:
                            f.write(md_content)
                
                # Show summary
                summary = f"""✓ Split Complete!

Total Days: {total_days}
Total Messages: {len(filtered_requests)}
Output Directory: {output_dir}
Organization: YYYY-MM/DD.{self.output_format.get() if self.output_format.get() != 'both' else 'md|json'}

Files organized by month for easy access!"""
                
                messagebox.showinfo("Success", summary)
                self.status_var.set(f"✓ Split {len(filtered_requests)} messages into {total_days} daily file(s)")
            
            else:
                # Regular mode (single combined output)
                output_dir.mkdir(parents=True, exist_ok=True)
                
                # Save outputs
                if self.output_format.get() in ['json', 'both']:
                    filtered_data = data.copy()
                    filtered_data['requests'] = filtered_requests
                    json_path = output_dir / f"{base_name}.json"
                    with open(json_path, 'w') as f:
                        json.dump(filtered_data, f, indent=2)
                
                if self.output_format.get() in ['md', 'both']:
                    md_content = self.create_markdown(filtered_requests)
                    md_path = output_dir / f"{base_name}.md"
                    with open(md_path, 'w') as f:
                        f.write(md_content)
                
                # Show summary
                first_date = datetime.fromtimestamp(filtered_requests[0]['timestamp']/1000)
                last_date = datetime.fromtimestamp(filtered_requests[-1]['timestamp']/1000)
                
                summary = f"""✓ Processing Complete!

Messages: {len(filtered_requests)}
Date Range: {first_date.strftime('%B %d, %Y')} to {last_date.strftime('%B %d, %Y')}
Output Directory: {output_dir}
Format: {self.output_format.get().upper()}"""
                
                messagebox.showinfo("Success", summary)
                self.status_var.set(f"✓ Processed {len(filtered_requests)} messages")
            
        except json.JSONDecodeError:
            messagebox.showerror("Error", "Invalid JSON file")
            self.status_var.set("Error: Invalid JSON")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
            self.status_var.set("Error occurred")
    
    def create_markdown(self, requests):
        """Convert requests to markdown with all nuance preserved"""
        if not requests:
            return "# Chat Export\n\nNo messages found.\n"
        
        first_date = datetime.fromtimestamp(requests[0]['timestamp']/1000)
        last_date = datetime.fromtimestamp(requests[-1]['timestamp']/1000)
        
        md_content = f"# Chat Export: {first_date.strftime('%B %d, %Y')} to {last_date.strftime('%B %d, %Y')}\n\n"
        md_content += f"**Total Messages:** {len(requests)}\n"
        md_content += f"**Date Range:** {first_date.strftime('%B %d, %Y')} - {last_date.strftime('%B %d, %Y')}\n\n"
        md_content += "---\n\n"
        
        for i, req in enumerate(requests, 1):
            timestamp = req.get('timestamp', 0)
            date_str = datetime.fromtimestamp(timestamp/1000).strftime('%B %d, %Y at %H:%M:%S')
            
            # Extract user message (handle both text and parts format)
            message = req.get('message', {})
            if isinstance(message, dict):
                if 'text' in message:
                    message_text = message['text']
                elif 'parts' in message:
                    message_text = '\n'.join([p.get('text', '') for p in message['parts'] if p.get('text')])
                else:
                    message_text = str(message)
            else:
                message_text = str(message)
            
            md_content += f"## Message {i}\n"
            md_content += f"**Time:** {date_str}\n\n"
            md_content += f"### User\n{message_text}\n\n"
            
            # Extract ALL response content (thinking blocks, code, everything)
            response_list = req.get('response', [])
            
            for resp_item in response_list:
                kind = resp_item.get('kind', '')
                value = resp_item.get('value', '')
                
                if kind == 'thinking':
                    # Include thinking/reasoning blocks
                    if value and value.strip():
                        md_content += f"**🧠 Reasoning:**\n{value}\n\n"
                elif kind == 'mcpServersStarting':
                    # Skip internal server markers
                    continue
                elif isinstance(value, str) and value.strip():
                    # Regular response text
                    md_content += f"### GitHub Copilot\n{value}\n\n"
            
            # Include code blocks if present in metadata
            result = req.get('result', {})
            metadata = result.get('metadata', {})
            code_blocks = metadata.get('codeBlocks', [])
            
            if code_blocks:
                md_content += f"**Code Blocks:**\n"
                for j, block in enumerate(code_blocks, 1):
                    language = block.get('language', 'text')
                    filename = block.get('filename', '')
                    content = block.get('content', '')
                    
                    if filename:
                        md_content += f"\n{j}. `{filename}` ({language}):\n"
                    else:
                        md_content += f"\n{j}. Code ({language}):\n"
                    
                    md_content += f"```{language}\n{content}\n```\n"
            
            md_content += "---\n\n"
        
        return md_content
    
    def clear(self):
        """Clear all inputs"""
        self.input_file.set("")
        self.output_dir.set(str(Path.home()))
        self.start_date.set("")
        self.end_date.set("")
        self.output_format.set("md")
        self.split_by_day.set(False)
        self.status_var.set("Ready")


def main():
    root = tk.Tk()
    app = ChatTrimmerGUI(root)
    root.mainloop()


if __name__ == '__main__':
    main()
