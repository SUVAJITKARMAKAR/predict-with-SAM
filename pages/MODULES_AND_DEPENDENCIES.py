import streamlit as stream 

# SETTING PAGE CONFIGURATION
stream.set_page_config(page_title="MODULES",
            layout="wide",
            page_icon=":page"
)


def main():
      stream.header("MODULES AND DEPENDENCIES")

      stream.warning("STREAMLIT")
      stream.write("`Streamlit` is an open-source Python library used for building interactive web applications with minimal effort. With Streamlit, developers can create intuitive and visually appealing interfaces for data exploration, machine learning models, and more, directly from Python scripts. The library simplifies the process by automatically handling tasks like layout design, widget creation, and reactive updates. Streamlit's intuitive API allows users to quickly prototype ideas and share insights with others. It's widely appreciated for its simplicity, flexibility, and seamless integration with popular data science libraries like Pandas, Matplotlib, and TensorFlow.")


      stream.warning("PICKEL")
      stream.write("The Python module `pickle` provides functionality for serializing and deserializing Python objects. It enables easy conversion of complex data structures into a byte stream, which can be stored or transmitted efficiently.Pickle facilitates object persistence, allowing objects to be saved to disk and loaded back into memory effortlessly.")


      stream.warning("PANDAS")
      stream.write("`Pandas` is a powerful Python library designed for data manipulation and analysis. It provides easy-to-use data structures and functions, primarily DataFrame, which resembles a spreadsheet with rows and columns. Pandas allows for efficient handling of large datasets, offering functionalities for data cleaning, exploration, transformation, and visualization. It seamlessly integrates with other libraries like NumPy and Matplotlib, making it a cornerstone tool for data scientists and analysts. With its intuitive syntax and comprehensive documentation, Pandas simplifies complex data tasks, enabling users to extract valuable insights and drive informed decisions in various domains, including finance, research, and machine learning.")
      

      stream.warning("SCIKIT - LEARN")
      stream.write("`Scikit-learn` is a powerful Python module for machine learning. It offers a wide range of algorithms for tasks like classification, regression, clustering, and dimensionality reduction. With user-friendly interfaces and extensive documentation, scikit-learn simplifies the process of building and deploying machine learning models for both beginners and experts.")


      stream.warning("NUMPY")
      stream.write("`NumPy` is a powerful Python library for numerical computing, offering support for arrays, matrices, and mathematical functions. It provides efficient data structures for handling large datasets and performing operations such as sorting, reshaping, and statistical analysis. NumPy's array operations are optimized for speed, making it a cornerstone for scientific computing and data analysis tasks. Its seamless integration with other Python libraries like SciPy and Matplotlib enhances its versatility for various applications including machine learning, image processing, and computational physics. Overall, NumPy serves as a fundamental tool for high-performance computation and data manipulation in Python programming.")

if __name__ == '__main__':
      main()
