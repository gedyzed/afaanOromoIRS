import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from pdfminer.high_level import extract_text
from similarityCalculator import SimilarityCalculator
from Indexing import InvertedIndex
from textExtractor import Binary
from WordFrequency import  WordFrequency
import os

class MiniRetrievalSystem:
    def __init__(self):
        self.binary = Binary()
        self.documentWords = self.binary.read('corpusWords.bin')

        # Assigning id to each document
        self.document_ids = [f"doc_{index+1}" for index in range(len(self.documentWords))]

        # Create instance of InvertedIndex     
        self.indexing = InvertedIndex()
        self.invertedIndex = self.indexing.getInvertedIndex(self.documentWords, self.document_ids)

        self.similarityMeasure = SimilarityCalculator(self.documentWords, self.invertedIndex, self.document_ids)


    def search(self, query):
        return self.similarityMeasure.process_query(query)

class IRGui(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Information Retrieval System")
        self.geometry("800x600")

        self.search_history = []

        # Initialize the MiniRetrievalSystem
        self.ir_system = MiniRetrievalSystem()

        self.style = ttk.Style(self)
        self.configure_gui()

        self.title_label = ttk.Label(self, text="Information Retrieval System", style="Title.TLabel")
        self.title_label.pack(pady=(20, 10))

        self.search_panel_frame = ttk.Frame(self)
        self.search_panel_frame.pack(pady=10, padx=10)

        self.search_label = ttk.Label(self.search_panel_frame, text="Search", style="TLabel")
        self.search_label.grid(row=0, column=0)

        self.search_entry = ttk.Entry(self.search_panel_frame, width=50)
        self.search_entry.grid(row=0, column=1, padx=(0, 10))

        self.search_button = ttk.Button(self.search_panel_frame, text="Search", command=self.perform_search)
        self.search_button.grid(row=0, column=2, padx=(0, 5))

        self.reset_button = ttk.Button(self.search_panel_frame, text="Clear", command=self.reset_search)
        self.reset_button.grid(row=0, column=3)

        self.results_frame = ttk.Frame(self)
        self.results_frame.pack(pady=10, fill=tk.BOTH, expand=True)

        self.results_scrollbar = ttk.Scrollbar(self.results_frame, orient="vertical")
        self.results = tk.Text(self.results_frame, height=10, width=70, bg='#f0f8ff', fg='#000000', yscrollcommand=self.results_scrollbar.set)
        self.results_scrollbar.config(command=self.results.yview)
        self.results.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.results_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.search_history_button = ttk.Button(self, text="Search History", command=self.show_search_history)
        self.search_history_button.pack(side=tk.LEFT, padx=5)

        self.history_frame = ttk.Frame(self)
        self.history_frame.pack(pady=10, fill=tk.BOTH, expand=True)

        self.history_scrollbar = ttk.Scrollbar(self.history_frame, orient="vertical")
        self.history_listbox = tk.Listbox(self.history_frame, height=10, width=70, yscrollcommand=self.history_scrollbar.set)
        self.history_scrollbar.config(command=self.history_listbox.yview)
        self.history_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.history_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.history_listbox.bind("<Button-3>", self.delete_history_popup)

        self.history_buttons_frame = ttk.Frame(self)
        self.history_buttons_frame.pack(pady=10)

        self.delete_history_button = ttk.Button(self.history_buttons_frame, text="Delete History", command=self.delete_history_item)
        self.delete_history_button.pack(side=tk.LEFT, padx=5)

        self.history_frame.pack_forget()        
        

    def configure_gui(self):
        self.configure(bg='#d3d3d3')

        self.style.configure('TLabel', background='#d3d3d3', foreground='#000000', font=('Arial', 12))
        self.style.configure('Title.TLabel', background='#d3d3d3', foreground='#4682B9', font=('Arial', 18, 'bold'))
        self.style.configure('TFrame', background='#d3d3d3')
        self.style.configure('TButton', font=('Arial', 10))

    def perform_search(self):
        query = self.search_entry.get()
        if query:
            self.search_history.append(query)
            self.update_history_listbox()
            # Perform search using the IR system
            results = self.ir_system.search(query)
            self.display_search_results(results)

    def display_search_results(self, results):
        self.results.delete(1.0, tk.END)
        if not results:
            self.results.insert(tk.END, "No results found.\n")
        else:
            for index, document in enumerate(results):
                self.results.insert(tk.END, f"{index + 1}. {document}\n")
                tag_name = f"link{index}"
                self.results.insert(tk.END, f"[Open Document]\n", tag_name)
                self.results.tag_bind(tag_name, "<Button-1>", lambda e, doc=document: self.open_document(doc))

    def open_document(self, file_name):
        if file_name:
            directory_path = "C:\\Users\\ETHIOPIA\\Desktop\\IR project\\IR project\\documents"  
            file_path = os.path.join(directory_path, file_name)
            if os.path.isfile(file_path):
                self.display_pdf(file_path)
            else:
                print(f"The file {file_name} does not exist in the directory.")


    def display_pdf(self, file_path):
        # Extract text from the PDF using pdfminer.six
        pdf_text = extract_text(file_path)

        # Create a new window to display the PDF text
        pdf_window = tk.Toplevel(self)
        pdf_window.title(file_path)

        pdf_text_widget = tk.Text(pdf_window, wrap=tk.WORD)
        pdf_text_widget.insert(tk.END, pdf_text)
        pdf_text_widget.pack(fill=tk.BOTH, expand=True)

        # Add a scrollbar to the text widget
        pdf_scrollbar = ttk.Scrollbar(pdf_window, orient=tk.VERTICAL, command=pdf_text_widget.yview)
        pdf_text_widget.config(yscrollcommand=pdf_scrollbar.set)
        pdf_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    def update_history_listbox(self):
        self.history_listbox.delete(0, tk.END)
        for item in self.search_history:
            self.history_listbox.insert(tk.END, item)

    def reset_search(self):
        self.search_entry.delete(0, tk.END)
        self.results.delete(1.0, tk.END)

    def delete_history_item(self):
        try:
            selected_index = self.history_listbox.curselection()[0]
            del self.search_history[selected_index]
            self.update_history_listbox()
        except IndexError:
            pass

    def delete_history_popup(self, event):
        self.history_listbox.selection_clear(0, tk.END)
        self.history_listbox.selection_set(self.history_listbox.nearest(event.y))
        self.history_menu = tk.Menu(self, tearoff=0)
        self.history_menu.add_command(label="Delete", command=self.delete_history_item)
        self.history_menu.tk_popup(event.x_root, event.y_root)

    def show_search_history(self):
        if self.history_frame.winfo_ismapped():
            self.history_frame.pack_forget()
        else:
            self.history_frame.pack(pady=10, fill=tk.BOTH, expand=True)
    def plotGraph(self):
        words = WordFrequency ()
        words.drawGraph()
        
if __name__ == "__main__":
    app = IRGui()
    app.mainloop()
