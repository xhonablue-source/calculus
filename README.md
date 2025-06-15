# 🧠 MathCraft: Interactive Calculus Explorer

**An immersive, interactive learning platform for introductory calculus concepts**

Created by **Xavier Honablue, M.Ed**

---

## 🎯 Overview

MathCraft is a comprehensive Streamlit-based educational application designed to make calculus concepts accessible and engaging through interactive visualizations and hands-on manipulatives. Students can explore limits, asymptotes, and the Fundamental Theorem of Calculus through dynamic graphs, real-time calculations, and guided practice problems.

## ✨ Key Features

### 🎛️ Interactive Manipulatives
- **Real-time sliders** for modifying function coefficients
- **Dynamic graphing** with instant updates
- **Step-by-step mathematical solutions**
- **Custom function builder** with polynomial term controls

### 📊 Comprehensive Visualizations
- **Interactive Plotly graphs** with zoom, pan, and hover functionality
- **Asymptote highlighting** and analysis
- **Riemann sum approximations** with adjustable precision
- **Side-by-side function comparisons**

### 🎓 Educational Modules

#### 1. **Interactive Limits Explorer**
- Modify rational function coefficients with sliders
- Observe real-time limit behavior
- Step-by-step algebraic solutions
- Visual asymptote identification

#### 2. **Asymptote Explorer**
- Compare horizontal, vertical, and oblique asymptotes
- Degree comparison analysis
- Interactive examples with explanations

#### 3. **Function Builder**
- Create custom rational functions term by term
- Real-time mathematical analysis
- Instant graphing and asymptote detection

#### 4. **FTC Visualizer**
- Explore both parts of the Fundamental Theorem of Calculus
- Interactive area accumulation demonstrations
- Connection between derivatives and integrals

#### 5. **Quiz Mode**
- Interactive practice problems
- Instant feedback with detailed explanations
- Progress tracking and performance analytics
- Randomized question selection

### 🔧 Advanced Tools
- **Limit Calculator** with symbolic computation
- **Complete Asymptote Finder** for any rational function
- **Riemann Sum Visualizer** with multiple approximation methods
- **Domain and behavior analysis**

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/mathcraft-calculus-explorer.git
   cd mathcraft-calculus-explorer
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   streamlit run app.py
   ```

4. **Open in browser:**
   - The app will automatically open at `http://localhost:8501`
   - If not, navigate to the URL shown in your terminal

## 📚 Usage Guide

### Navigation
Use the **sidebar menu** to navigate between different learning modules:
- 🏠 **Overview** - Introduction and feature summary
- 🎯 **Interactive Limits** - Hands-on limit exploration
- 📊 **Asymptote Explorer** - Comprehensive asymptote analysis
- 🔧 **Function Builder** - Custom function creation tool
- 🧮 **FTC Visualizer** - Fundamental Theorem demonstrations
- 🎮 **Quiz Mode** - Interactive practice and assessment

### Interactive Controls
- **Sliders:** Adjust function coefficients in real-time
- **Dropdown menus:** Select different function types and examples
- **Checkboxes:** Toggle visual elements (asymptotes, solution steps)
- **Input fields:** Enter custom functions for analysis

### Mathematical Notation
- Use standard mathematical notation: `x**2` for x², `sin(x)`, `exp(x)`, etc.
- Fractions: Use `/` for division
- Powers: Use `**` for exponentiation
- Functions: `sin`, `cos`, `tan`, `log`, `exp`, `sqrt`

## 🎓 Educational Objectives

Students will learn to:

### **Limits and Asymptotes**
- Evaluate limits at infinity using algebraic techniques
- Identify horizontal asymptotes through degree comparison
- Understand the relationship between limits and asymptotic behavior
- Apply the "divide by highest power" method

### **Fundamental Theorem of Calculus**
- Understand the connection between derivatives and integrals
- Apply FTC Part 1: d/dx[∫f(t)dt] = f(x)
- Use FTC Part 2 for definite integral evaluation
- Visualize area accumulation functions

### **Mathematical Reasoning**
- Develop intuition through interactive exploration
- Connect algebraic manipulation with graphical representation
- Practice systematic problem-solving approaches

## 🛠️ Technical Details

### Built With
- **Streamlit** - Web application framework
- **SymPy** - Symbolic mathematics library
- **NumPy** - Numerical computing
- **Plotly** - Interactive visualization
- **Matplotlib** - Additional plotting capabilities
- **Pandas** - Data manipulation

### Architecture
```
mathcraft-calculus-explorer/
├── app.py                 # Main application file
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
└── assets/               # Static assets (if any)
```

### Performance Features
- **Efficient computation** with NumPy vectorization
- **Responsive UI** with Streamlit's reactive framework
- **Interactive graphics** with Plotly's WebGL acceleration
- **Memory optimization** for large datasets

## 🎨 Customization

### Adding New Functions
To add new function examples, modify the function dictionaries in the respective sections:

```python
# Example: Adding a new function type
new_functions = {
    "rational": lambda x, a, b: (a*x**2 + 1)/(x**2 + b),
    "exponential": lambda x, a: a * np.exp(-x),
    # Add more as needed
}
```

### Styling
Customize the appearance by modifying the CSS in the `st.markdown()` sections:

```python
st.markdown("""
<style>
    .custom-class {
        background-color: #your-color;
        border-radius: 10px;
        # Add your styles
    }
</style>
""", unsafe_allow_html=True)
```

## 📈 Future Enhancements

### Planned Features
- [ ] **Multi-variable calculus** modules
- [ ] **3D function visualization**
- [ ] **Student progress tracking** with user accounts
- [ ] **Instructor dashboard** with class analytics
- [ ] **Mobile-responsive design** improvements
- [ ] **Export functionality** for graphs and solutions
- [ ] **Collaborative features** for group learning

### Advanced Modules
- [ ] **Differential equations** solver
- [ ] **Series and sequences** explorer
- [ ] **Vector calculus** visualization
- [ ] **Real-world applications** scenarios

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. **Fork the repository**
2. **Create a feature branch:** `git checkout -b feature-name`
3. **Commit changes:** `git commit -am 'Add new feature'`
4. **Push to branch:** `git push origin feature-name`
5. **Submit a pull request**

### Contribution Guidelines
- Follow PEP 8 style guidelines
- Add docstrings to new functions
- Include unit tests for new features
- Update documentation as needed

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Streamlit Team** - For the excellent web app framework
- **SymPy Developers** - For powerful symbolic mathematics
- **Plotly Team** - For interactive visualization capabilities
- **Educational Community** - For feedback and feature suggestions

## 📞 Support

### Getting Help
- **Documentation:** Check this README and inline code comments
- **Issues:** Report bugs or request features via GitHub Issues
- **Discussions:** Join community discussions in GitHub Discussions

### Contact
- **Creator:** Xavier Honablue, M.Ed
- **Email:** [your-email@domain.com]
- **Website:** [your-website.com]

---

## 🌟 Star this repository if you find it helpful!

**Made with ❤️ for mathematics education**
