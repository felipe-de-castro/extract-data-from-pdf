# Extracting data from PDfs

In this small project, I undertook the task of extracting specific data fields from a collection of PDF documents. The data fields of interest included the individual's name, CPF (Brazilian national identification number), date of birth, and a field called "julgados."

To achieve this, I developed a set of functions that utilize various Python libraries. Each function is responsible for extracting a particular piece of information from the PDF documents:

- Name Extraction: I created a function to extract the names of individuals from the PDFs. This involved locating patterns and structures in the text that typically represent names.

- CPF Extraction: Another function was designed to extract CPF numbers from the PDFs. This required identifying the specific format and structure of CPFs within the documents.

- Date of Birth Extraction: A function was developed to extract date of birth information from the PDFs. This involved recognizing date patterns and handling variations in date formats.

- Julgados Extraction: I created a function to extract the "julgados" field from the PDFs. This might involve identifying specific keywords or structures within the text that pertain to judgments or legal decisions.

After extracting the relevant information, I organized it into a DataFrame. This DataFrame allowed for easier manipulation and analysis of the extracted data.

To provide further insights, I calculated the age of each individual based on their date of birth. This age information was added as an additional column in the DataFrame, allowing for more comprehensive analysis.

Overall, this project demonstrates the application of Python programming and libraries in extracting, cleaning, and organizing data from a collection of PDF documents. The resulting DataFrame with extracted and processed data can serve as a valuable resource for further analysis and decision-making.
