import markdown
import os
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext

def convert_md_to_html(md_content, file_path=None):
    """Converts Markdown content to HTML and returns it."""
    try:
        html_content = markdown.markdown(md_content)
        
        if file_path:  
            html_file_path = file_path.replace(".md", ".html")
            with open(html_file_path, "w", encoding="utf-8") as html_file:
                html_file.write(html_content)
            messagebox.showinfo("Success", f"Conversion successful! HTML file saved at: {html_file_path}")
        
        return html_content
    except Exception as e:
        messagebox.showerror("Error", f"Error converting file: {e}")
        return ""

def open_file():
    """Opens a Markdown file and loads its content into the text area."""
    file_path = filedialog.askopenfilename(filetypes=[("Markdown files", "*.md")])
    if file_path:
        with open(file_path, "r", encoding="utf-8") as file:
            md_text_area.delete(1.0, tk.END)
            md_text_area.insert(tk.END, file.read())
        convert_and_display()

def save_html():
    """Saves the converted HTML content to a file."""
    file_path = filedialog.asksaveasfilename(defaultextension=".html", filetypes=[("HTML files", "*.html")])
    if file_path:
        html_content = html_text_area.get(1.0, tk.END)
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(html_content)
        messagebox.showinfo("Success", "HTML file saved successfully!")

def convert_and_display():
    """Converts Markdown text from the text area and displays the HTML output."""
    md_content = md_text_area.get(1.0, tk.END)
    html_output = convert_md_to_html(md_content)
    html_text_area.delete(1.0, tk.END)
    html_text_area.insert(tk.END, html_output)

def main():
    global md_text_area, html_text_area
    
    root = tk.Tk()
    root.title("Markdown to HTML Converter")
    root.geometry("800x550")
    root.configure(bg="#1E1E1E")
    
    # Title Label
    title_label = tk.Label(root, text="Markdown to HTML Converter", font=("Helvetica", 20, "bold"), fg="#F1C40F", bg="#1E1E1E")
    title_label.pack(pady=10)
    
    frame = tk.Frame(root, bg="#2C3E50")
    frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
    
    # Markdown Input Area
    tk.Label(frame, text="Markdown Input:", font=("Helvetica", 12, "bold"), fg="#F1C40F", bg="#2C3E50").pack(anchor="w")
    md_text_area = scrolledtext.ScrolledText(frame, height=10, wrap=tk.WORD, font=("Courier", 12), bg="#ECF0F1", fg="#2C3E50")
    md_text_area.pack(fill=tk.BOTH, expand=True, pady=5)
    
    # Convert Button
    convert_btn = tk.Button(frame, text="Convert to HTML", command=convert_and_display, font=("Helvetica", 12, "bold"), fg="white", bg="#E74C3C", padx=20, pady=5, relief="raised")
    convert_btn.pack(pady=5)
    
    # HTML Output Area
    tk.Label(frame, text="HTML Output:", font=("Helvetica", 12, "bold"), fg="#F1C40F", bg="#2C3E50").pack(anchor="w")
    html_text_area = scrolledtext.ScrolledText(frame, height=10, wrap=tk.WORD, font=("Courier", 12), bg="#ECF0F1", fg="#2C3E50")
    html_text_area.pack(fill=tk.BOTH, expand=True, pady=5)
    
    # Buttons Frame
    btn_frame = tk.Frame(root, bg="#1E1E1E")
    btn_frame.pack(pady=10)
    
    open_btn = tk.Button(btn_frame, text="Open File", command=open_file, font=("Helvetica", 12, "bold"), fg="white", bg="#3498DB", padx=15, pady=5, relief="raised")
    open_btn.grid(row=0, column=0, padx=10)
    
    save_btn = tk.Button(btn_frame, text="Save HTML", command=save_html, font=("Helvetica", 12, "bold"), fg="white", bg="#27AE60", padx=15, pady=5, relief="raised")
    save_btn.grid(row=0, column=1, padx=10)
    
    root.mainloop()
    
if __name__ == "__main__":
    main()
