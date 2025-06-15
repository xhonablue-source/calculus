import streamlit as st
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import pandas as pd

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="MathCraft: Intro to Calculus", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #4B0082, #8A2BE2);
        padding: 2rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
    }
    .concept-card {
        background: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #4B0082;
        margin: 1rem 0;
    }
    .interactive-section {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1rem;
        border-radius: 10px;
        color: white;
        margin: 1rem 0;
    }
    .formula-box {
        background: #e3f2fd;
        padding: 1rem;
        border-radius: 8px;
        border: 2px solid #2196f3;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# --- HEADER ---
st.markdown("""
<div class='main-header'>
    <h1>🧠 MathCraft: Interactive Calculus Explorer</h1>
    <h3>Limits, Asymptotes, and the Fundamental Theorem</h3>
    <p style='font-size: 1.1rem;'>Built by <strong>Xavier Honablue, M.Ed</strong></p>
</div>
""", unsafe_allow_html=True)

# --- SIDEBAR NAVIGATION ---
st.sidebar.title("📚 Navigation")
section = st.sidebar.selectbox(
    "Choose a section:",
    ["🏠 Overview", "🎯 Interactive Limits", "📊 Asymptote Explorer", "🔧 Function Builder", "🧮 FTC Visualizer", "🎮 Quiz Mode"]
)

# --- MAIN CONTENT BASED ON SELECTION ---

if section == "🏠 Overview":
    st.header("📖 Course Overview")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class='concept-card'>
        <h4>🎯 What You'll Learn</h4>
        <ul>
        <li><strong>Limits at Infinity:</strong> How functions behave as x approaches ±∞</li>
        <li><strong>Horizontal Asymptotes:</strong> Lines that functions approach but never touch</li>
        <li><strong>Interactive Visualization:</strong> See math concepts come alive</li>
        <li><strong>Fundamental Theorem:</strong> The bridge between derivatives and integrals</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class='concept-card'>
        <h4>🛠️ Interactive Tools</h4>
        <ul>
        <li><strong>Function Manipulatives:</strong> Drag sliders to change coefficients</li>
        <li><strong>Real-time Graphing:</strong> See functions update instantly</li>
        <li><strong>Step-by-step Solutions:</strong> Work through problems together</li>
        <li><strong>Quiz Mode:</strong> Test your understanding</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

elif section == "🎯 Interactive Limits":
    st.header("🎯 Interactive Limits Explorer")
    
    st.markdown("""
    <div class='interactive-section'>
    <h4>🔍 Explore Limits at Infinity</h4>
    <p>Use the controls below to modify rational functions and observe their limiting behavior!</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Interactive controls
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("Numerator Coefficients")
        a2 = st.slider("x² coefficient", -10, 10, 3, key="num_x2")
        a1 = st.slider("x coefficient", -10, 10, 0, key="num_x1")
        a0 = st.slider("constant", -10, 10, 0, key="num_const")
    
    with col2:
        st.subheader("Denominator Coefficients")
        b2 = st.slider("x² coefficient", -10, 10, 1, key="den_x2")
        b1 = st.slider("x coefficient", -10, 10, 0, key="den_x1")
        b0 = st.slider("constant", -10, 10, -1, key="den_const")
    
    with col3:
        st.subheader("View Settings")
        x_range = st.slider("X-axis range", 1, 50, 20)
        show_asymptote = st.checkbox("Show Horizontal Asymptote", True)
        show_steps = st.checkbox("Show Solution Steps", True)
    
    # Create the function
    if b2 != 0:  # Avoid division by zero in denominator leading coefficient
        # Generate function expression
        x = sp.Symbol('x')
        numerator = a2*x**2 + a1*x + a0
        denominator = b2*x**2 + b1*x + b0
        func = numerator / denominator
        
        # Display the function
        st.markdown(f"""
        <div class='formula-box'>
        <h4>Current Function:</h4>
        <p style='font-size: 1.2em; text-align: center;'>
        f(x) = ({a2}x² + {a1}x + {a0}) / ({b2}x² + {b1}x + {b0})
        </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Calculate limit
        limit_val = a2 / b2 if b2 != 0 else float('inf')
        
        # Show step-by-step solution
        if show_steps:
            st.markdown("""
            <div class='concept-card'>
            <h4>📝 Step-by-Step Solution</h4>
            """, unsafe_allow_html=True)
            
            st.markdown(f"""
            **Step 1:** Identify the highest power of x in both numerator and denominator.
            - Highest power: x²
            
            **Step 2:** Divide both numerator and denominator by x²:
            $$\\frac{{{a2} + \\frac{{{a1}}}{{x}} + \\frac{{{a0}}}{{x^2}}}}{{{b2} + \\frac{{{b1}}}{{x}} + \\frac{{{b0}}}{{x^2}}}}$$
            
            **Step 3:** Take the limit as x → ∞:
            - Terms with x in denominator approach 0
            - Result: {a2}/{b2} = {limit_val:.3f}
            
            **Conclusion:** The horizontal asymptote is y = {limit_val:.3f}
            """)
            st.markdown("</div>", unsafe_allow_html=True)
        
        # Create interactive plot
        x_vals = np.linspace(-x_range, x_range, 1000)
        x_vals = x_vals[np.abs(x_vals) > 0.1]  # Avoid points too close to potential vertical asymptotes
        
        try:
            y_vals = (a2*x_vals**2 + a1*x_vals + a0) / (b2*x_vals**2 + b1*x_vals + b0)
            
            # Remove points where function is undefined or too large
            mask = np.isfinite(y_vals) & (np.abs(y_vals) < 100)
            x_vals = x_vals[mask]
            y_vals = y_vals[mask]
            
            fig = go.Figure()
            
            # Add function curve
            fig.add_trace(go.Scatter(
                x=x_vals, y=y_vals,
                mode='lines',
                name='f(x)',
                line=dict(color='blue', width=3)
            ))
            
            # Add horizontal asymptote
            if show_asymptote and np.isfinite(limit_val):
                fig.add_hline(
                    y=limit_val,
                    line_dash="dash",
                    line_color="red",
                    annotation_text=f"y = {limit_val:.3f}",
                    annotation_position="top right"
                )
            
            fig.update_layout(
                title="Interactive Function Graph",
                xaxis_title="x",
                yaxis_title="f(x)",
                height=500,
                showlegend=True
            )
            
            st.plotly_chart(fig, use_container_width=True)
            
        except:
            st.error("Unable to plot function with current parameters. Try different values!")

elif section == "📊 Asymptote Explorer":
    st.header("📊 Asymptote Explorer")
    
    st.markdown("""
    <div class='interactive-section'>
    <h4>🔍 Understanding Different Types of Asymptotes</h4>
    <p>Explore horizontal, vertical, and oblique asymptotes with interactive examples!</p>
    </div>
    """, unsafe_allow_html=True)
    
    asymptote_type = st.selectbox(
        "Choose asymptote type to explore:",
        ["Horizontal Asymptotes", "Vertical Asymptotes", "Oblique Asymptotes"]
    )
    
    if asymptote_type == "Horizontal Asymptotes":
        st.subheader("Horizontal Asymptotes: Degree Comparison")
        
        col1, col2 = st.columns(2)
        
        with col1:
            degree_num = st.selectbox("Degree of numerator", [0, 1, 2, 3], index=2)
            degree_den = st.selectbox("Degree of denominator", [0, 1, 2, 3], index=2)
        
        with col2:
            if degree_num < degree_den:
                result = "Horizontal asymptote at y = 0"
                color = "green"
            elif degree_num == degree_den:
                result = "Horizontal asymptote at y = (leading coefficient ratio)"
                color = "blue"
            else:
                result = "No horizontal asymptote (function grows without bound)"
                color = "red"
            
            st.markdown(f"""
            <div style='padding: 1rem; background-color: {color}20; border-radius: 8px; border-left: 4px solid {color};'>
            <h4 style='color: {color};'>Result:</h4>
            <p>{result}</p>
            </div>
            """, unsafe_allow_html=True)
        
        # Generate example functions based on degrees
        examples = []
        if degree_num == 1 and degree_den == 2:
            examples = ["(2x + 1)/(x² - 4)", "(3x - 5)/(2x² + x + 1)"]
        elif degree_num == 2 and degree_den == 2:
            examples = ["(3x² + 2x)/(x² - 1)", "(x² + 5)/(2x² - 3x + 1)"]
        elif degree_num == 3 and degree_den == 2:
            examples = ["(x³ + 2x)/(x² - 1)", "(2x³ - x²)/(3x² + 4)"]
        
        if examples:
            selected_example = st.selectbox("Try these examples:", examples)
            
            # Parse and plot the selected example
            try:
                x = sp.Symbol('x')
                func_expr = sp.sympify(selected_example)
                
                x_vals = np.linspace(-10, 10, 1000)
                y_vals = []
                
                for x_val in x_vals:
                    try:
                        y_val = float(func_expr.subs(x, x_val))
                        if np.isfinite(y_val) and abs(y_val) < 50:
                            y_vals.append(y_val)
                        else:
                            y_vals.append(np.nan)
                    except:
                        y_vals.append(np.nan)
                
                fig = go.Figure()
                fig.add_trace(go.Scatter(
                    x=x_vals, y=y_vals,
                    mode='lines',
                    name=f'f(x) = {selected_example}',
                    line=dict(width=3)
                ))
                
                # Add horizontal asymptote if applicable
                if degree_num <= degree_den:
                    if degree_num < degree_den:
                        fig.add_hline(y=0, line_dash="dash", line_color="red", 
                                     annotation_text="y = 0")
                
                fig.update_layout(
                    title=f"Graph of f(x) = {selected_example}",
                    xaxis_title="x",
                    yaxis_title="f(x)",
                    height=400
                )
                
                st.plotly_chart(fig, use_container_width=True)
                
            except:
                st.write("Example function visualization")

elif section == "🔧 Function Builder":
    st.header("🔧 Interactive Function Builder")
    
    st.markdown("""
    <div class='interactive-section'>
    <h4>🎨 Build Your Own Rational Functions</h4>
    <p>Create custom functions and observe their behavior!</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Function builder interface
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📝 Function Components")
        
        # Numerator builder
        st.write("**Numerator:**")
        num_terms = st.number_input("Number of terms in numerator", 1, 5, 3)
        
        numerator_coeffs = []
        numerator_powers = []
        
        for i in range(num_terms):
            col_a, col_b = st.columns(2)
            with col_a:
                coeff = st.number_input(f"Coefficient {i+1}", -10.0, 10.0, 1.0, key=f"num_coeff_{i}")
                numerator_coeffs.append(coeff)
            with col_b:
                power = st.number_input(f"Power of x {i+1}", 0, 5, max(0, num_terms-i-1), key=f"num_pow_{i}")
                numerator_powers.append(power)
        
        # Denominator builder
        st.write("**Denominator:**")
        den_terms = st.number_input("Number of terms in denominator", 1, 5, 2)
        
        denominator_coeffs = []
        denominator_powers = []
        
        for i in range(den_terms):
            col_a, col_b = st.columns(2)
            with col_a:
                coeff = st.number_input(f"Coefficient {i+1}", -10.0, 10.0, 1.0, key=f"den_coeff_{i}")
                denominator_coeffs.append(coeff)
            with col_b:
                power = st.number_input(f"Power of x {i+1}", 0, 5, max(0, den_terms-i-1), key=f"den_pow_{i}")
                denominator_powers.append(power)
    
    with col2:
        st.subheader("📊 Function Analysis")
        
        # Build function string
        num_str = " + ".join([f"{coeff}*x^{power}" if power > 0 else str(coeff) 
                             for coeff, power in zip(numerator_coeffs, numerator_powers)])
        den_str = " + ".join([f"{coeff}*x^{power}" if power > 0 else str(coeff) 
                             for coeff, power in zip(denominator_coeffs, denominator_powers)])
        
        st.markdown(f"""
        <div class='formula-box'>
        <h4>Your Function:</h4>
        <p>f(x) = ({num_str}) / ({den_str})</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Analyze the function
        max_num_power = max(numerator_powers) if numerator_powers else 0
        max_den_power = max(denominator_powers) if denominator_powers else 0
        
        if max_num_power < max_den_power:
            asymptote_analysis = "Horizontal asymptote at y = 0"
        elif max_num_power == max_den_power:
            leading_num_coeff = numerator_coeffs[numerator_powers.index(max_num_power)]
            leading_den_coeff = denominator_coeffs[denominator_powers.index(max_den_power)]
            ratio = leading_num_coeff / leading_den_coeff
            asymptote_analysis = f"Horizontal asymptote at y = {ratio:.3f}"
        else:
            asymptote_analysis = "No horizontal asymptote"
        
        st.markdown(f"""
        <div class='concept-card'>
        <h4>Analysis:</h4>
        <p><strong>Degree of numerator:</strong> {max_num_power}</p>
        <p><strong>Degree of denominator:</strong> {max_den_power}</p>
        <p><strong>Asymptote:</strong> {asymptote_analysis}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Plot the function
        if st.button("🎨 Graph Function"):
            try:
                x_vals = np.linspace(-10, 10, 1000)
                y_vals = []
                
                for x_val in x_vals:
                    num_val = sum(coeff * (x_val ** power) for coeff, power in zip(numerator_coeffs, numerator_powers))
                    den_val = sum(coeff * (x_val ** power) for coeff, power in zip(denominator_coeffs, denominator_powers))
                    
                    if abs(den_val) > 1e-10:
                        y_val = num_val / den_val
                        if abs(y_val) < 100:
                            y_vals.append(y_val)
                        else:
                            y_vals.append(np.nan)
                    else:
                        y_vals.append(np.nan)
                
                fig = go.Figure()
                fig.add_trace(go.Scatter(
                    x=x_vals, y=y_vals,
                    mode='lines',
                    name='f(x)',
                    line=dict(width=3, color='purple')
                ))
                
                # Add horizontal asymptote if it exists
                if "y = " in asymptote_analysis and "No" not in asymptote_analysis:
                    y_asymptote = float(asymptote_analysis.split("y = ")[1])
                    fig.add_hline(y=y_asymptote, line_dash="dash", line_color="red",
                                 annotation_text=f"y = {y_asymptote:.3f}")
                
                fig.update_layout(
                    title="Your Custom Function",
                    xaxis_title="x",
                    yaxis_title="f(x)",
                    height=400
                )
                
                st.plotly_chart(fig, use_container_width=True)
                
            except Exception as e:
                st.error(f"Error plotting function: {str(e)}")

elif section == "🧮 FTC Visualizer":
    st.header("🧮 Fundamental Theorem of Calculus Visualizer")
    
    st.markdown("""
    <div class='interactive-section'>
    <h4>🔗 Connecting Derivatives and Integrals</h4>
    <p>See the beautiful relationship between differentiation and integration!</p>
    </div>
    """, unsafe_allow_html=True)
    
    # FTC Part selection
    ftc_part = st.selectbox("Choose FTC part to explore:", ["Part 1: Derivative of Integral", "Part 2: Evaluation Theorem"])
    
    if ftc_part == "Part 1: Derivative of Integral":
        st.subheader("FTC Part 1: d/dx[∫f(t)dt] = f(x)")
        
        # Function selection
        func_choice = st.selectbox("Choose function f(t):", ["t²", "sin(t)", "e^t", "1/(1+t²)"])
        
        # Create interactive visualization
        x_vals = np.linspace(0, 5, 100)
        
        if func_choice == "t²":
            f_vals = x_vals**2
            F_vals = (x_vals**3) / 3  # Integral from 0 to x
            title = "f(t) = t², F(x) = x³/3"
        elif func_choice == "sin(t)":
            f_vals = np.sin(x_vals)
            F_vals = 1 - np.cos(x_vals)  # Integral from 0 to x
            title = "f(t) = sin(t), F(x) = 1 - cos(x)"
        elif func_choice == "e^t":
            f_vals = np.exp(x_vals)
            F_vals = np.exp(x_vals) - 1  # Integral from 0 to x
            title = "f(t) = e^t, F(x) = e^x - 1"
        else:  # 1/(1+t²)
            f_vals = 1 / (1 + x_vals**2)
            F_vals = np.arctan(x_vals)  # Integral from 0 to x
            title = "f(t) = 1/(1+t²), F(x) = arctan(x)"
        
        # Create subplot
        fig = make_subplots(
            rows=2, cols=1,
            subplot_titles=['f(t) - Original Function', 'F(x) = ∫₀ˣf(t)dt - Accumulated Area'],
            vertical_spacing=0.12
        )
        
        # Original function
        fig.add_trace(
            go.Scatter(x=x_vals, y=f_vals, mode='lines', name='f(t)', line=dict(color='blue', width=3)),
            row=1, col=1
        )
        
        # Integral function (accumulated area)
        fig.add_trace(
            go.Scatter(x=x_vals, y=F_vals, mode='lines', name='F(x) = ∫f(t)dt', line=dict(color='red', width=3)),
            row=2, col=1
        )
        
        fig.update_layout(height=600, title_text=title)
        st.plotly_chart(fig, use_container_width=True)
        
        st.markdown("""
        <div class='concept-card'>
        <h4>🔍 Key Insight:</h4>
        <p>Notice how the <strong>slope</strong> of the integral function F(x) (bottom graph) 
        matches the <strong>value</strong> of the original function f(t) (top graph) at each point!</p>
        <p>This is exactly what FTC Part 1 tells us: <strong>F'(x) = f(x)</strong></p>
        </div>
        """, unsafe_allow_html=True)
    
    else:  # Part 2
        st.subheader("FTC Part 2: ∫ₐᵇf(x)dx = F(b) - F(a)")
        
        # Interactive area calculation
        col1, col2 = st.columns(2)
        
        with col1:
            a = st.slider("Lower bound (a)", -5.0, 5.0, 0.0, 0.1)
            b = st.slider("Upper bound (b)", -5.0, 5.0, 3.0, 0.1)
            func_choice = st.selectbox("Function:", ["x²", "sin(x)", "x³ - 2x"])
        
        with col2:
            x_vals = np.linspace(-5, 5, 1000)
            
            if func_choice == "x²":
                y_vals = x_vals**2
                antiderivative = lambda x: x**3 / 3
                func_latex = "x^2"
                anti_latex = "\\frac{x^3}{3}"
            elif func_choice == "sin(x)":
                y_vals = np.sin(x_vals)
                antiderivative = lambda x: -np.cos(x)
                func_latex = "\\sin(x)"
                anti_latex = "-\\cos(x)"
            else:  # x³ - 2x
                y_vals = x_vals**3 - 2*x_vals
                antiderivative = lambda x: x**4/4 - x**2
                func_latex = "x^3 - 2x"
                anti_latex = "\\frac{x^4}{4} - x^2"
            
            # Calculate definite integral
            integral_value = antiderivative(b) - antiderivative(a)
            
            st.markdown(f"""
            <div class='formula-box'>
            <h4>Calculation:</h4>
            <p>∫{func_latex} dx = {anti_latex} + C</p>
            <p>∫ₐᵇ{func_latex} dx = [{anti_latex}]ₐᵇ</p>
            <p>= {anti_latex}|ₓ₌{b} - {anti_latex}|ₓ₌{a}</p>
            <p>= {antiderivative(b):.3f} - {antiderivative(a):.3f}</p>
            <p><strong>= {integral_value:.3f}</strong></p>
            </div>
            """, unsafe_allow_html=True)
        
        # Create visualization with shaded area
        fig = go.Figure()
        
        # Function curve
        fig.add_trace(go.Scatter(
            x=x_vals, y=y_vals,
            mode='lines',
            name=f'f(x) = {func_choice}',
            line=dict(color='blue', width=3)
        ))
        
        # Shaded area
        x_fill = np.linspace(a, b, 100)
        if func_choice == "x²":
            y_fill = x_fill**2
        elif func_choice == "sin(x)":
            y_fill = np.sin(x_fill)
        else:
            y_fill = x_fill**3 - 2*x_fill
        
        fig.add_trace(go.Scatter(
            x=np.concatenate([x_fill, [b, a]]),
            y=np.concatenate([y_fill, [0, 0]]),
            fill='toself',
            fillcolor='rgba(255, 0, 0, 0.3)',
            mode='lines',
            name=f'Area = {integral_value:.3f}',
            line=dict(color='red', width=2)
        ))
        
        # Vertical lines at bounds
        fig.add_vline(x=a, line_dash="dash", line_color="green", annotation_text=f"x = {a}")
        fig.add_vline(x=b, line_dash="dash", line_color="green", annotation_text=f"x = {b}")
        
        fig.update_layout(
            title=f"Definite Integral: ∫[{a:.1f} to {b:.1f}] {func_choice} dx = {integral_value:.3f}",
            xaxis_title="x",
            yaxis_title="f(x)",
            height=500
        )
        
        st.plotly_chart(fig, use_container_width=True)

elif section == "🎮 Quiz Mode":
    st.header("🎮 Interactive Quiz Mode")
    
    st.markdown("""
    <div class='interactive-section'>
    <h4>🧠 Test Your Understanding!</h4>
    <p>Practice problems with instant feedback and explanations.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Initialize session state for quiz
    if 'quiz_score' not in st.session_state:
        st.session_state.quiz_score = 0
    if 'quiz_question' not in st.session_state:
        st.session_state.quiz_question = 0
    
    # Quiz questions database
    questions = [
        {
            "question": "What is lim(x→∞) (3x² + 2x + 1)/(x² - 5)?",
            "options": ["0", "3", "∞", "Does not exist"],
            "correct": 1,
            "explanation": "Since both numerator and denominator have degree 2, the limit equals the ratio of leading coefficients: 3/1 = 3"
        },
        {
            "question": "What is lim(x→∞) (2x + 1)/(x² + 3x)?",
            "options": ["0", "2", "1/3", "∞"],
            "correct": 0,
            "explanation": "The denominator has higher degree than numerator, so the limit is 0."
        },
        {
            "question": "According to FTC Part 1, what is d/dx[∫₀ˣ t² dt]?",
            "options": ["x²", "x³/3", "2x", "0"],
            "correct": 0,
            "explanation": "FTC Part 1 states that d/dx[∫ₐˣ f(t) dt] = f(x). Here f(t) = t², so the answer is x²."
        },
        {
            "question": "If f(x) = (x³ + 2x)/(x³ - 1), what is its horizontal asymptote?",
            "options": ["y = 0", "y = 1", "y = 2", "No horizontal asymptote"],
            "correct": 1,
            "explanation": "Both numerator and denominator have degree 3. The ratio of leading coefficients is 1/1 = 1, so y = 1."
        },
        {
            "question": "What does ∫₁³ 2x dx equal using FTC Part 2?",
            "options": ["8", "6", "4", "10"],
            "correct": 0,
            "explanation": "∫2x dx = x² + C. So ∫₁³ 2x dx = [x²]₁³ = 3² - 1² = 9 - 1 = 8."
        }
    ]
    
    # Display current question
    if st.session_state.quiz_question < len(questions):
        current_q = questions[st.session_state.quiz_question]
        
        st.subheader(f"Question {st.session_state.quiz_question + 1} of {len(questions)}")
        st.write(f"**Score: {st.session_state.quiz_score}/{st.session_state.quiz_question}**")
        
        st.markdown(f"""
        <div class='concept-card'>
        <h4>{current_q['question']}</h4>
        </div>
        """, unsafe_allow_html=True)
        
        # Answer choices
        user_answer = st.radio("Choose your answer:", current_q['options'], key=f"q_{st.session_state.quiz_question}")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("Submit Answer"):
                selected_index = current_q['options'].index(user_answer)
                if selected_index == current_q['correct']:
                    st.success("✅ Correct!")
                    st.session_state.quiz_score += 1
                else:
                    st.error(f"❌ Incorrect. The correct answer is: {current_q['options'][current_q['correct']]}")
                
                st.info(f"**Explanation:** {current_q['explanation']}")
                
        with col2:
            if st.button("Next Question"):
                st.session_state.quiz_question += 1
                st.experimental_rerun()
        
        with col3:
            if st.button("Reset Quiz"):
                st.session_state.quiz_score = 0
                st.session_state.quiz_question = 0
                st.experimental_rerun()
    
    else:
        # Quiz completed
        percentage = (st.session_state.quiz_score / len(questions)) * 100
        
        st.markdown(f"""
        <div class='interactive-section'>
        <h2>🎉 Quiz Complete!</h2>
        <h3>Final Score: {st.session_state.quiz_score}/{len(questions)} ({percentage:.1f}%)</h3>
        </div>
        """, unsafe_allow_html=True)
        
        if percentage >= 80:
            st.balloons()
            st.success("🌟 Excellent work! You've mastered these concepts!")
        elif percentage >= 60:
            st.info("👍 Good job! Review the topics you missed and try again.")
        else:
            st.warning("📚 Keep studying! Review the interactive sections and try the quiz again.")
        
        if st.button("Restart Quiz"):
            st.session_state.quiz_score = 0
            st.session_state.quiz_question = 0
            st.experimental_rerun()
    
    # Study hints section
    st.markdown("""
    <div class='concept-card'>
    <h4>💡 Study Hints</h4>
    <ul>
    <li><strong>Horizontal Asymptotes:</strong> Compare degrees of numerator and denominator</li>
    <li><strong>Degree < Degree:</strong> Horizontal asymptote at y = 0</li>
    <li><strong>Degree = Degree:</strong> Horizontal asymptote at y = (leading coefficients ratio)</li>
    <li><strong>Degree > Degree:</strong> No horizontal asymptote</li>
    <li><strong>FTC Part 1:</strong> d/dx[∫ₐˣ f(t) dt] = f(x)</li>
    <li><strong>FTC Part 2:</strong> ∫ₐᵇ f(x) dx = F(b) - F(a) where F'(x) = f(x)</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

# --- ADDITIONAL MANIPULATIVES SECTION ---
st.markdown("---")
st.header("🎛️ Additional Mathematical Manipulatives")

# Expandable sections for more tools
with st.expander("🔍 Limit Calculator"):
    st.subheader("Step-by-Step Limit Solver")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**Enter your function:**")
        user_function = st.text_input("f(x) = ", "3*x**2/(x**2 - 1)", help="Use Python syntax: x**2 for x², sin(x), exp(x), etc.")
        limit_point = st.selectbox("Evaluate limit as x approaches:", ["∞", "-∞", "0", "1", "-1", "Custom"])
        
        if limit_point == "Custom":
            custom_point = st.number_input("Enter custom point:", value=0.0)
            limit_point = custom_point
    
    with col2:
        if st.button("🧮 Calculate Limit"):
            try:
                x = sp.Symbol('x')
                expr = sp.sympify(user_function.replace('^', '**'))
                
                if limit_point == "∞":
                    limit_val = sp.limit(expr, x, sp.oo)
                elif limit_point == "-∞":
                    limit_val = sp.limit(expr, x, -sp.oo)
                else:
                    limit_val = sp.limit(expr, x, float(limit_point))
                
                st.success(f"lim(x→{limit_point}) {user_function} = {limit_val}")
                
                # Show steps for rational functions
                if "/" in user_function and limit_point in ["∞", "-∞"]:
                    st.info("💡 For rational functions at infinity, divide by the highest power of x in the denominator!")
                
            except Exception as e:
                st.error(f"Error calculating limit: {str(e)}")

with st.expander("📐 Asymptote Finder"):
    st.subheader("Complete Asymptote Analysis")
    
    func_input = st.text_input("Enter function for asymptote analysis:", "(x**2 + 1)/(x**2 - 4)")
    
    if st.button("🔍 Find All Asymptotes"):
        try:
            x = sp.Symbol('x')
            expr = sp.sympify(func_input.replace('^', '**'))
            
            st.write("**Analysis Results:**")
            
            # Horizontal asymptotes
            ha_pos = sp.limit(expr, x, sp.oo)
            ha_neg = sp.limit(expr, x, -sp.oo)
            
            if ha_pos == ha_neg and ha_pos.is_finite:
                st.write(f"🔸 **Horizontal Asymptote:** y = {ha_pos}")
            elif ha_pos.is_finite or ha_neg.is_finite:
                st.write(f"🔸 **Horizontal Asymptotes:** x→+∞: y = {ha_pos}, x→-∞: y = {ha_neg}")
            else:
                st.write("🔸 **No Horizontal Asymptotes**")
            
            # Vertical asymptotes (find zeros of denominator)
            if "/" in func_input:
                num, den = func_input.split("/")
                den_expr = sp.sympify(den.strip().strip("()"))
                zeros = sp.solve(den_expr, x)
                
                if zeros:
                    st.write(f"🔸 **Potential Vertical Asymptotes at:** x = {zeros}")
                else:
                    st.write("🔸 **No Vertical Asymptotes**")
            
            # Domain
            try:
                domain = sp.calculus.util.continuous_domain(expr, x, sp.S.Reals)
                st.write(f"🔸 **Domain:** {domain}")
            except:
                st.write("🔸 **Domain:** Analysis not available")
                
        except Exception as e:
            st.error(f"Error in analysis: {str(e)}")

with st.expander("🎯 Interactive Riemann Sums"):
    st.subheader("Visualize Integration as Area Under Curve")
    
    col1, col2 = st.columns(2)
    
    with col1:
        riemann_func = st.selectbox("Choose function:", ["x**2", "sin(x)", "x**3 - 2*x", "1/x"])
        a_bound = st.slider("Lower bound (a)", -5.0, 5.0, 0.0, 0.1, key="riemann_a")
        b_bound = st.slider("Upper bound (b)", -5.0, 5.0, 2.0, 0.1, key="riemann_b")
        n_rectangles = st.slider("Number of rectangles", 1, 100, 10)
    
    with col2:
        method = st.selectbox("Riemann sum method:", ["Left", "Right", "Midpoint"])
        
        if st.button("🎨 Create Visualization"):
            try:
                # Generate data
                x_vals = np.linspace(a_bound, b_bound, 1000)
                
                if riemann_func == "x**2":
                    y_vals = x_vals**2
                elif riemann_func == "sin(x)":
                    y_vals = np.sin(x_vals)
                elif riemann_func == "x**3 - 2*x":
                    y_vals = x_vals**3 - 2*x_vals
                else:  # 1/x
                    y_vals = 1/x_vals
                    x_vals = x_vals[x_vals != 0]  # Avoid division by zero
                    y_vals = y_vals[np.isfinite(y_vals)]
                
                fig = go.Figure()
                
                # Original function
                fig.add_trace(go.Scatter(
                    x=x_vals, y=y_vals,
                    mode='lines',
                    name=f'f(x) = {riemann_func}',
                    line=dict(color='blue', width=3)
                ))
                
                # Riemann rectangles
                dx = (b_bound - a_bound) / n_rectangles
                riemann_sum = 0
                
                for i in range(n_rectangles):
                    x_left = a_bound + i * dx
                    x_right = a_bound + (i + 1) * dx
                    
                    if method == "Left":
                        x_eval = x_left
                    elif method == "Right":
                        x_eval = x_right
                    else:  # Midpoint
                        x_eval = (x_left + x_right) / 2
                    
                    # Calculate height
                    if riemann_func == "x**2":
                        height = x_eval**2
                    elif riemann_func == "sin(x)":
                        height = np.sin(x_eval)
                    elif riemann_func == "x**3 - 2*x":
                        height = x_eval**3 - 2*x_eval
                    else:  # 1/x
                        if x_eval != 0:
                            height = 1/x_eval
                        else:
                            continue
                    
                    riemann_sum += height * dx
                    
                    # Add rectangle
                    fig.add_shape(
                        type="rect",
                        x0=x_left, y0=0, x1=x_right, y1=height,
                        fillcolor="rgba(255, 0, 0, 0.3)",
                        line=dict(color="red", width=1)
                    )
                
                fig.update_layout(
                    title=f"Riemann Sum ({method}): {riemann_sum:.4f} with {n_rectangles} rectangles",
                    xaxis_title="x",
                    yaxis_title="f(x)",
                    height=400
                )
                
                st.plotly_chart(fig, use_container_width=True)
                st.info(f"🧮 Riemann Sum Approximation: {riemann_sum:.6f}")
                
            except Exception as e:
                st.error(f"Error creating visualization: {str(e)}")

# --- FOOTER ---
st.markdown("---")
st.markdown("""
<div style='text-align: center; padding: 2rem; background: linear-gradient(90deg, #4B0082, #8A2BE2); border-radius: 10px; color: white;'>
    <h3>🎓 MathCraft: Interactive Learning Platform</h3>
    <p style='font-size: 1.1rem;'>Empowering students through interactive mathematics</p>
    <p>Created by <strong>Xavier Honablue, M.Ed</strong> | All rights reserved</p>
    <p style='font-size: 0.9rem;'>Built with Streamlit, SymPy, and Plotly</p>
</div>
""", unsafe_allow_html=True)
