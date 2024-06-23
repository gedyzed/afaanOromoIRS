# afaanOromoIRS

Afaan Oromo Information Retrieval System (IRS) Project

This project implements a comprehensive Information Retrieval System using text processing techniques to extract, index, and search through a collection of documents. It includes modules for text extraction, word frequency analysis, inverted index creation, and query-based document retrieval. A graphical user interface (GUI) built with Tkinter provides a user-friendly interface for performing searches and viewing results.

## Project Structure

### Files and Directories
- **textProcessor.py**: Contains `Tokenizer`, `StopWord`, and `Stemmer` classes for text preprocessing.
- **textExtractor.py**: Contains the `Binary` class for reading and writing binary data.
- **WordFrequency.py**: Contains the `WordFrequency` class for analyzing word frequencies.
- **Indexing.py**: Contains the `InvertedIndex` class for creating and managing an inverted index.
- **similarityCalculator.py**: Contains the `SimilarityCalculator` class for computing TF-IDF and cosine similarity between queries and documents.
- **IRSystem.py**: Contains the `MiniRetrievalSystem` class for integrating the various components and performing searches.
- **IRGui.py**: Contains the `IRGui` class for the Tkinter-based GUI.
- **documents**: Directory containing the PDF documents to be indexed and searched.

### Classes and Methods

#### Tokenizer Class
- **tokenize(word)**: Tokenizes and normalizes the input word.

#### StopWord Class
- **__init__(wordFrequency)**: Initializes with a word frequency dictionary.
- **remove()**: Removes stop words based on frequency criteria.

#### Stemmer Class
- **apply_cluster_rules(word)**: Applies stemming rules to a word.
- **measure(word)**: Measures vowel-consonant sequences.
- **stem(word)**: Stems the input word.

#### TextExtractor Class
- **extractText(directory_path)**: Extracts text from documents in a directory.
- **Binary Class**
- **save(data, filename)**: Saves data to a binary file.
- **read(filename)**: Reads data from a binary file.

#### WordFrequency Class
- **sortedWordFrequency()**: Returns a sorted dictionary of word frequencies.
- **drawGraph()**: Plots a bar graph of the top 200 words.
- **plot_zipf_log_log()**: Plots a log-log graph illustrating Zipf's law.

#### InvertedIndex Class
- **getInvertedIndex(documentWords, document_ids)**: Creates an inverted index from document words.
- **writeInvertedIndexToFile(invertedIndex)**: Writes the inverted index to a file.

#### SimilarityCalculator Class
- **calculate_tf(term, document)**: Calculates term frequency.
- **calculate_idf(term)**: Calculates inverse document frequency.
- **calculate_tfidf(term, document)**: Calculates TF-IDF.
- **calculate_cosine_similarity(query, document)**: Calculates cosine similarity.
- **process_query(query)**: Processes a query and returns a list of similar documents.

#### MiniRetrievalSystem Class
- **search(query)**: Searches for documents similar to the query.

#### IRGui Class (Tkinter GUI)
- **perform_search()**: Handles the search action.
- **display_search_results(results)**: Displays search results.
- **open_document(file_name)**: Opens a document.
- **display_pdf(file_path)**: Displays PDF content.
- **update_history_listbox()**: Updates search history listbox.
- **reset_search()**: Resets the search field and results.
- **delete_history_item()**: Deletes a selected history item.
- **delete_history_popup(event)**: Shows a popup menu for deleting history items.
- **show_search_history()**: Toggles the display of search history.
- **plotGraph()**: Plots a word frequency graph.

## Usage

1. **Extract Text from Documents**:
   Extract text from documents and save it to a binary file.
   ```python
   text_extractor = TextExtractor()
   text_extractor.extractText('path_to_documents')
   ```

2. **Analyze Word Frequencies**:
   Analyze and visualize word frequencies.
   ```python
   word_frequency = WordFrequency()
   word_frequency.drawGraph()
   word_frequency.plot_zipf_log_log()
   ```

3. **Create Inverted Index**:
   Create and save an inverted index.
   ```python
   inverted_index = InvertedIndex()
   inverted_index.getInvertedIndex(documentWords, document_ids)
   inverted_index.writeInvertedIndexToFile(invertedIndex)
   ```

4. **Search for Documents**:
   Use the GUI to perform searches and view results.
   ``` python
   if __name__ == "__main__":
       app = IRGui()
       app.mainloop()
   ```


