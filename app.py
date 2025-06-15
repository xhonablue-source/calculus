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
    ["🏠 Overview", "🎯 Interactive Limits", "📊 Asymptote Explorer", "🔧 Function Builder", "🧮 FTC Visualizer", "📐 MVT Explorer", "🎮 Quiz Mode"]
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
            $\\frac{{{a2} + \\frac{{{a1}}}{{x}} + \\frac{{{a0}}}{{x^2}}}}{{{b2} + \\frac{{{b1}}}{{x}} + \\frac{{{b0}}}{{x^2}}}}$
            
            **Step 3:** Take the limit as x → ∞:
            - Terms with x in denominator approach 0
            - Result: {a2}/{b2} = {limit_val:.3f}
            
            **Conclusion:** The horizontal asymptote is y = {limit_val:.3f}
            """)
            st.markdown("</div>", unsafe_allow_html=True)
    
    # Real-world applications section
    st.markdown("""
    <div class='interactive-section'>
    <h4>🌍 Real-World Applications of Limits & Asymptotes</h4>
    </div>
    """, unsafe_allow_html=True)
    
    limit_col1, limit_col2 = st.columns(2)
    
    with limit_col1:
        st.markdown("""
        <div style='background: #e3f2fd; padding: 1.5rem; border-radius: 10px; border-left: 5px solid #2196f3;'>
        <h5>📱 Technology & Engineering</h5>
        <p><strong>Internet Speed:</strong> Your internet connection has a maximum bandwidth (horizontal asymptote). No matter how many devices you add, your total speed approaches but never exceeds this limit.</p>
        <p><strong>CPU Performance:</strong> Computer processors have thermal limits - performance approaches maximum capacity as temperature increases.</p>
        </div>
        
        <div style='background: #f3e5f5; padding: 1.5rem; border-radius: 10px; border-left: 5px solid #9c27b0; margin-top: 1rem;'>
        <h5>🧬 Biology & Medicine</h5>
        <p><strong>Drug Saturation:</strong> When taking medication, your blood concentration approaches a maximum level (asymptote) - taking more doesn't increase effectiveness.</p>
        <p><strong>Population Growth:</strong> Animal populations approach carrying capacity of their environment - they can't grow indefinitely.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with limit_col2:
        st.markdown("""
        <div style='background: #e8f5e8; padding: 1.5rem; border-radius: 10px; border-left: 5px solid #4caf50;'>
        <h5>💰 Economics & Business</h5>
        <p><strong>Market Saturation:</strong> Sales of a new product approach a maximum market size - there's a limit to how many customers exist.</p>
        <p><strong>Learning Curves:</strong> Employee productivity improves quickly at first, then approaches a maximum skill level asymptotically.</p>
        </div>
        
        <div style='background: #fff3e0; padding: 1.5rem; border-radius: 10px; border-left: 5px solid #ff9800; margin-top: 1rem;'>
        <h5>🌡️ Physics & Chemistry</h5>
        <p><strong>Terminal Velocity:</strong> Falling objects approach a maximum speed due to air resistance - they can't accelerate indefinitely.</p>
        <p><strong>Chemical Reactions:</strong> Reaction rates approach zero as reactants are consumed - the reaction effectively "stops."</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style='background: linear-gradient(135deg, #ff6b6b 0%, #4ecdc4 100%); padding: 1.5rem; border-radius: 10px; color: white; margin: 1rem 0;'>
    <h5>🎯 Everyday Examples You've Experienced</h5>
    <ul>
    <li>📶 <strong>Cell Phone Signal:</strong> Bars approach maximum as you get closer to tower</li>
    <li>🔋 <strong>Phone Charging:</strong> Battery percentage approaches 100% more slowly near the end</li>
    <li>☕ <strong>Coffee Temperature:</strong> Hot coffee approaches room temperature asymptotically</li>
    <li>🚗 <strong>Car Acceleration:</strong> Your car approaches its top speed but can't exceed it</li>
    <li>💡 <strong>Learning a Skill:</strong> Improvement rate slows as you approach mastery</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
        
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
    
    # Historical context and real-world applications
    st.markdown("""
    <div class='interactive-section'>
    <h4>🏛️ Historical Context & Development</h4>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='concept-card'>
    <h4>📜 The Great Mathematical Revolution</h4>
    <p>The Fundamental Theorem of Calculus represents one of the most profound discoveries in mathematics, 
    connecting two seemingly unrelated concepts: <strong>differentiation</strong> (rates of change) and 
    <strong>integration</strong> (accumulation). This connection revolutionized mathematics, science, and engineering.</p>
    
    <h5>🧑‍🔬 Key Historical Figures:</h5>
    </div>
    """, unsafe_allow_html=True)
    
    hist_col1, hist_col2 = st.columns(2)
    
    with hist_col1:
        st.markdown("""
        <div style='background: #e3f2fd; padding: 1.5rem; border-radius: 10px; border-left: 5px solid #2196f3;'>
        <h5>🇬🇧 Isaac Newton (1642-1727)</h5>
        <p><strong>Motivation:</strong> Needed to solve physics problems - planetary motion, gravity, optics</p>
        <p><strong>Approach:</strong> Developed "method of fluxions" - thinking of derivatives as "flowing quantities"</p>
        <p><strong>Key Insight:</strong> Realized that finding areas (integration) was the inverse of finding slopes (differentiation)</p>
        </div>
        
        <div style='background: #f3e5f5; padding: 1.5rem; border-radius: 10px; border-left: 5px solid #9c27b0; margin-top: 1rem;'>
        <h5>🇩🇪 Gottfried Leibniz (1646-1716)</h5>
        <p><strong>Motivation:</strong> Philosophical interest in infinite processes and logical reasoning</p>
        <p><strong>Approach:</strong> Created the notation we still use: dx, ∫, d/dx</p>
        <p><strong>Key Contribution:</strong> Made calculus more systematic and teachable through better notation</p>
        </div>
        """, unsafe_allow_html=True)
    
    with hist_col2:
        st.markdown("""
        <div style='background: #e8f5e8; padding: 1.5rem; border-radius: 10px; border-left: 5px solid #4caf50;'>
        <h5>⚔️ The Great Calculus War</h5>
        <p><strong>The Conflict:</strong> Newton and Leibniz developed calculus independently, leading to a bitter priority dispute</p>
        <p><strong>Newton's Claim:</strong> Developed it earlier (1665-1666) but didn't publish</p>
        <p><strong>Leibniz's Claim:</strong> Published first (1684) with better notation</p>
        <p><strong>Resolution:</strong> Both credited as co-inventors, each contributed essential elements</p>
        </div>
        
        <div style='background: #fff3e0; padding: 1.5rem; border-radius: 10px; border-left: 5px solid #ff9800; margin-top: 1rem;'>
        <h5>🎯 Why Was This Revolutionary?</h5>
        <p><strong>Before FTC:</strong> Finding areas and slopes were completely separate, tedious problems</p>
        <p><strong>After FTC:</strong> One unified theory solved both problems efficiently</p>
        <p><strong>Impact:</strong> Enabled the Scientific Revolution and modern engineering</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='formula-box'>
    <h4>🔗 The Revolutionary Connection</h4>
    <p>The FTC revealed that <strong>differentiation and integration are inverse operations</strong> - like addition and subtraction, or multiplication and division. This wasn't obvious before!</p>
    
    <p style='text-align: center; font-size: 1.2em;'>
    <strong>Problem:</strong> Find the area under f(x) = x² from 0 to 3
    </p>
    
    <p><strong>Before FTC:</strong> Use geometric methods, exhausting approximations → Hours of work</p>
    <p><strong>After FTC:</strong> Find antiderivative F(x) = x³/3, compute F(3) - F(0) = 9 → Seconds!</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Real-world applications
    st.markdown("""
    <div class='interactive-section'>
    <h4>🌍 Real-World Applications of the Fundamental Theorem</h4>
    </div>
    """, unsafe_allow_html=True)
    
    ftc_col1, ftc_col2 = st.columns(2)
    
    with ftc_col1:
        st.markdown("""
        <div style='background: #e3f2fd; padding: 1.5rem; border-radius: 10px; border-left: 5px solid #2196f3;'>
        <h5>🚀 Space Exploration</h5>
        <p><strong>Rocket Trajectories:</strong> NASA uses FTC to calculate fuel consumption (integrate burn rate) and predict orbital paths (integrate velocity to get position).</p>
        <p><strong>Example:</strong> Mars rover landing - integrate deceleration profile to ensure safe touchdown velocity.</p>
        </div>
        
        <div style='background: #f3e5f5; padding: 1.5rem; border-radius: 10px; border-left: 5px solid #9c27b0; margin-top: 1rem;'>
        <h5>💰 Financial Markets</h5>
        <p><strong>Options Pricing:</strong> Black-Scholes model uses FTC to calculate option values by integrating probability distributions over possible stock prices.</p>
        <p><strong>Portfolio Analysis:</strong> Total return calculation by integrating dividend and price change rates over time.</p>
        </div>
        
        <div style='background: #e8f5e8; padding: 1.5rem; border-radius: 10px; border-left: 5px solid #4caf50; margin-top: 1rem;'>
        <h5>🎵 Audio Engineering</h5>
        <p><strong>Digital Music:</strong> Converting between sound waves (continuous) and digital files (discrete) using FTC principles.</p>
        <p><strong>Noise Cancellation:</strong> Headphones integrate incoming sound waves to generate precise canceling waves.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with ftc_col2:
        st.markdown("""
        <div style='background: #fff3e0; padding: 1.5rem; border-radius: 10px; border-left: 5px solid #ff9800;'>
        <h5>🏥 Medical Technology</h5>
        <p><strong>MRI/CT Scans:</strong> Image reconstruction uses FTC to build 3D body images from 2D slice data by integrating cross-sectional information.</p>
        <p><strong>Pharmacokinetics:</strong> Drug dosing schedules calculated by integrating absorption and elimination rates.</p>
        </div>
        
        <div style='background: #ffebee; padding: 1.5rem; border-radius: 10px; border-left: 5px solid #f44336; margin-top: 1rem;'>
        <h5>🌍 Climate Science</h5>
        <p><strong>Global Warming Models:</strong> Climate scientists integrate temperature changes over time and geography to predict future conditions.</p>
        <p><strong>Carbon Footprint:</strong> Total emissions calculated by integrating emission rates across activities and time.</p>
        </div>
        
        <div style='background: #e0f2f1; padding: 1.5rem; border-radius: 10px; border-left: 5px solid #009688; margin-top: 1rem;'>
        <h5>🎮 Video Games & Animation</h5>
        <p><strong>Physics Engines:</strong> Game physics use FTC to calculate realistic motion - integrate acceleration to get velocity, integrate velocity to get position.</p>
        <p><strong>3D Animation:</strong> Smooth character movement by integrating motion paths and deformation rates.</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style='background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 1.5rem; border-radius: 10px; color: white; margin: 1rem 0;'>
    <h5>🎯 Why FTC Changed Everything</h5>
    <p><strong>Before FTC:</strong> Mathematics was largely geometric and arithmetic</p>
    <p><strong>After FTC:</strong> Mathematics became the language of change and motion</p>
    
    <p><strong>This enabled:</strong></p>
    <ul>
    <li>🏭 <strong>Industrial Revolution:</strong> Steam engines, manufacturing optimization</li>
    <li>⚡ <strong>Electrical Age:</strong> Circuit analysis, electromagnetic theory</li>
    <li>✈️ <strong>Modern Transportation:</strong> Aerodynamics, automotive engineering</li>
    <li>💻 <strong>Digital Age:</strong> Signal processing, computer graphics, AI</li>
    <li>🌌 <strong>Space Age:</strong> Orbital mechanics, rocket science</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
    
    # Modern perspective
    st.markdown("""
    <div class='concept-card'>
    <h4>🔬 Modern Perspective: Why Students Should Care</h4>
    
    <h5>📱 Technology You Use Daily:</h5>
    <ul>
    <li><strong>GPS Navigation:</strong> Your phone integrates velocity data to track your location</li>
    <li><strong>Streaming Video:</strong> Compression algorithms use calculus to optimize file sizes</li>
    <li><strong>Battery Management:</strong> Your phone predicts battery life by integrating power consumption</li>
    <li><strong>Camera Autofocus:</strong> Calculus optimizes lens position for sharpest image</li>
    </ul>
    
    <h5>🎯 Career Applications:</h5>
    <ul>
    <li><strong>Data Science:</strong> Machine learning algorithms optimize by finding where derivatives equal zero</li>
    <li><strong>Engineering:</strong> Every engineering field uses calculus for design and analysis</li>
    <li><strong>Business:</strong> Optimization problems in logistics, marketing, and finance</li>
    <li><strong>Medicine:</strong> Medical imaging, drug development, and biomechanics</li>
    </ul>
    
    <p><strong>Bottom Line:</strong> The FTC isn't just math history - it's the foundation of the modern technological world!</p>
    </div>
    """, unsafe_allow_html=True)
            
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

elif section == "📐 MVT Explorer":
    st.header("📐 Mean Value Theorem Explorer")
    
    st.markdown("""
    <div class='interactive-section'>
    <h4>🎯 Understanding the Mean Value Theorem</h4>
    <p>Explore how the instantaneous rate of change equals the average rate of change!</p>
    </div>
    """, unsafe_allow_html=True)
    
    # MVT Statement
    st.markdown("""
    <div class='formula-box'>
    <h4>📜 Mean Value Theorem Statement</h4>
    <p>If f(x) is <strong>continuous</strong> on [a,b] and <strong>differentiable</strong> on (a,b), then there exists at least one point c in (a,b) such that:</p>
    <p style='text-align: center; font-size: 1.3em;'><strong>f'(c) = [f(b) - f(a)] / (b - a)</strong></p>
    <p>In other words: <em>instantaneous rate of change = average rate of change</em></p>
    </div>
    """, unsafe_allow_html=True)
    
    # Interactive MVT demonstration
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🎛️ Function Controls")
        mvt_function = st.selectbox("Choose function:", [
            "x²", "x³ - 3x", "sin(x)", "x³ - 2x² + x + 1", "ln(x+2)"
        ])
        
        if mvt_function in ["x²", "x³ - 3x", "x³ - 2x² + x + 1"]:
            a_mvt = st.slider("Left endpoint (a)", -3.0, 3.0, -1.0, 0.1, key="mvt_a")
            b_mvt = st.slider("Right endpoint (b)", -3.0, 3.0, 2.0, 0.1, key="mvt_b")
        elif mvt_function == "sin(x)":
            a_mvt = st.slider("Left endpoint (a)", -2*np.pi, 2*np.pi, 0.0, 0.1, key="mvt_a_sin")
            b_mvt = st.slider("Right endpoint (b)", -2*np.pi, 2*np.pi, np.pi, 0.1, key="mvt_b_sin")
        else:  # ln(x+2)
            a_mvt = st.slider("Left endpoint (a)", -1.5, 5.0, 0.0, 0.1, key="mvt_a_ln")
            b_mvt = st.slider("Right endpoint (b)", -1.5, 5.0, 3.0, 0.1, key="mvt_b_ln")
        
        if a_mvt >= b_mvt:
            st.error("⚠️ Please ensure a < b")
        else:
            show_tangent = st.checkbox("Show tangent line at c", True)
            show_secant = st.checkbox("Show secant line", True)
            show_calculation = st.checkbox("Show calculations", True)
    
    with col2:
        if a_mvt < b_mvt:
            # Define function and its derivative
            x_sym = sp.Symbol('x')
            if mvt_function == "x²":
                f_expr = x_sym**2
                f_prime_expr = 2*x_sym
                func_title = "f(x) = x²"
            elif mvt_function == "x³ - 3x":
                f_expr = x_sym**3 - 3*x_sym
                f_prime_expr = 3*x_sym**2 - 3
                func_title = "f(x) = x³ - 3x"
            elif mvt_function == "sin(x)":
                f_expr = sp.sin(x_sym)
                f_prime_expr = sp.cos(x_sym)
                func_title = "f(x) = sin(x)"
            elif mvt_function == "x³ - 2x² + x + 1":
                f_expr = x_sym**3 - 2*x_sym**2 + x_sym + 1
                f_prime_expr = 3*x_sym**2 - 4*x_sym + 1
                func_title = "f(x) = x³ - 2x² + x + 1"
            else:  # ln(x+2)
                f_expr = sp.log(x_sym + 2)
                f_prime_expr = 1/(x_sym + 2)
                func_title = "f(x) = ln(x+2)"
            
            # Calculate values
            f_a = float(f_expr.subs(x_sym, a_mvt))
            f_b = float(f_expr.subs(x_sym, b_mvt))
            avg_rate = (f_b - f_a) / (b_mvt - a_mvt)
            
            # Find c value(s) where f'(c) = average rate
            equation = sp.Eq(f_prime_expr, avg_rate)
            try:
                c_values = sp.solve(equation, x_sym)
                # Filter for real values in the interval (a,b)
                valid_c_values = []
                for c_val in c_values:
                    if c_val.is_real:
                        c_float = float(c_val)
                        if a_mvt < c_float < b_mvt:
                            valid_c_values.append(c_float)
                
                if valid_c_values:
                    c_mvt = valid_c_values[0]  # Use first valid value
                else:
                    c_mvt = (a_mvt + b_mvt) / 2  # Fallback
            except:
                c_mvt = (a_mvt + b_mvt) / 2  # Fallback
            
            f_c = float(f_expr.subs(x_sym, c_mvt))
            
            if show_calculation:
                st.markdown(f"""
                <div class='concept-card'>
                <h4>📊 Calculations</h4>
                <p><strong>f(a) = f({a_mvt:.2f}) = {f_a:.3f}</strong></p>
                <p><strong>f(b) = f({b_mvt:.2f}) = {f_b:.3f}</strong></p>
                <p><strong>Average rate = (f(b)-f(a))/(b-a) = {avg_rate:.3f}</strong></p>
                <p><strong>MVT point: c = {c_mvt:.3f}</strong></p>
                <p><strong>f'(c) = {float(f_prime_expr.subs(x_sym, c_mvt)):.3f}</strong></p>
                <p style='color: green;'><strong>✓ f'(c) = average rate!</strong></p>
                </div>
                """, unsafe_allow_html=True)
    
    # Create the visualization
    if a_mvt < b_mvt:
        # Generate function values
        x_vals = np.linspace(min(a_mvt-1, -5), max(b_mvt+1, 5), 1000)
        
        # Calculate y values based on function
        if mvt_function == "x²":
            y_vals = x_vals**2
        elif mvt_function == "x³ - 3x":
            y_vals = x_vals**3 - 3*x_vals
        elif mvt_function == "sin(x)":
            y_vals = np.sin(x_vals)
        elif mvt_function == "x³ - 2x² + x + 1":
            y_vals = x_vals**3 - 2*x_vals**2 + x_vals + 1
        else:  # ln(x+2)
            y_vals = np.log(x_vals + 2)
            # Only plot where x+2 > 0
            mask = x_vals > -2
            x_vals = x_vals[mask]
            y_vals = y_vals[mask]
        
        fig = go.Figure()
        
        # Main function
        fig.add_trace(go.Scatter(
            x=x_vals, y=y_vals,
            mode='lines',
            name=func_title,
            line=dict(color='blue', width=3)
        ))
        
        # Points at a and b
        fig.add_trace(go.Scatter(
            x=[a_mvt, b_mvt],
            y=[f_a, f_b],
            mode='markers',
            name='Endpoints',
            marker=dict(color='red', size=8)
        ))
        
        # Point at c
        fig.add_trace(go.Scatter(
            x=[c_mvt],
            y=[f_c],
            mode='markers',
            name=f'MVT point c = {c_mvt:.3f}',
            marker=dict(color='green', size=10, symbol='star')
        ))
        
        # Secant line
        if show_secant:
            secant_x = np.linspace(a_mvt - 0.5, b_mvt + 0.5, 100)
            secant_y = f_a + avg_rate * (secant_x - a_mvt)
            fig.add_trace(go.Scatter(
                x=secant_x, y=secant_y,
                mode='lines',
                name=f'Secant line (slope = {avg_rate:.3f})',
                line=dict(color='red', width=2, dash='dash')
            ))
        
        # Tangent line at c
        if show_tangent:
            tangent_slope = float(f_prime_expr.subs(x_sym, c_mvt))
            tangent_x = np.linspace(c_mvt - 1, c_mvt + 1, 100)
            tangent_y = f_c + tangent_slope * (tangent_x - c_mvt)
            fig.add_trace(go.Scatter(
                x=tangent_x, y=tangent_y,
                mode='lines',
                name=f'Tangent at c (slope = {tangent_slope:.3f})',
                line=dict(color='green', width=2, dash='dot')
            ))
        
        fig.update_layout(
            title=f"Mean Value Theorem: {func_title}",
            xaxis_title="x",
            yaxis_title="f(x)",
            height=500,
            showlegend=True
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    # Conceptual explanation
    st.markdown("""
    <div class='concept-card'>
    <h4>🧠 Why Does This Matter?</h4>
    <p>The Mean Value Theorem guarantees that somewhere between any two points on a smooth curve, 
    the instantaneous rate of change (derivative) equals the average rate of change (slope of secant line).</p>
    
    <h5>🚗 Real-World Example:</h5>
    <p>If you drive 120 miles in 2 hours (average speed = 60 mph), then at some point during your trip, 
    your speedometer read exactly 60 mph!</p>
    
    <h5>🔍 Key Insights:</h5>
    <ul>
    <li><strong>Geometric:</strong> The tangent line at c is parallel to the secant line</li>
    <li><strong>Physical:</strong> Instantaneous velocity equals average velocity at some moment</li>
    <li><strong>Mathematical:</strong> Connects local behavior (derivative) to global behavior (average rate)</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
    
    # Real-world applications of MVT
    st.markdown("""
    <div class='interactive-section'>
    <h4>🌍 Real-World Applications of Mean Value Theorem</h4>
    </div>
    """, unsafe_allow_html=True)
    
    mvt_col1, mvt_col2 = st.columns(2)
    
    with mvt_col1:
        st.markdown("""
        <div style='background: #e3f2fd; padding: 1.5rem; border-radius: 10px; border-left: 5px solid #2196f3;'>
        <h5>🚓 Traffic Law Enforcement</h5>
        <p><strong>Speed Cameras:</strong> If cameras 10 miles apart record your car passing at specific times, police can prove you exceeded the speed limit somewhere between them using MVT!</p>
        <p><strong>Example:</strong> Pass camera A at 2:00 PM, camera B at 2:06 PM → Average speed = 100 mph → You definitely hit 100 mph at some point!</p>
        </div>
        
        <div style='background: #f3e5f5; padding: 1.5rem; border-radius: 10px; border-left: 5px solid #9c27b0; margin-top: 1rem;'>
        <h5>🏭 Manufacturing Quality Control</h5>
        <p><strong>Temperature Monitoring:</strong> If a product's temperature changes from 70°F to 150°F over 10 minutes, MVT guarantees it hit every temperature in between at some point.</p>
        <p><strong>Production Rates:</strong> Ensuring consistent manufacturing output by analyzing rate changes.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with mvt_col2:
        st.markdown("""
        <div style='background: #e8f5e8; padding: 1.5rem; border-radius: 10px; border-left: 5px solid #4caf50;'>
        <h5>🎯 Sports & Athletics</h5>
        <p><strong>Running Analysis:</strong> If a marathon runner's average pace is 7 min/mile, MVT guarantees they ran exactly that pace at some point during the race.</p>
        <p><strong>Baseball:</strong> A ball's velocity changes from 95 mph to 0 mph when caught → It had every intermediate velocity at some instant.</p>
        </div>
        
        <div style='background: #fff3e0; padding: 1.5rem; border-radius: 10px; border-left: 5px solid #ff9800; margin-top: 1rem;'>
        <h5>💊 Medical Diagnostics</h5>
        <p><strong>Blood Pressure:</strong> If systolic pressure changes from 120 to 140 mmHg during stress, it passed through every value in between.</p>
        <p><strong>Drug Metabolism:</strong> Ensuring drug concentration levels behave predictably in the bloodstream.</p>
        </div>
        """, unsafe_allow_html=True)

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
        },
        {
            "question": "According to the Mean Value Theorem, if f(x) = x² on [1,3], what is f'(c)?",
            "options": ["2", "4", "6", "8"],
            "correct": 1,
            "explanation": "Average rate = (f(3)-f(1))/(3-1) = (9-1)/2 = 4. MVT guarantees f'(c) = 4 for some c in (1,3)."
        },
        {
            "question": "For MVT to apply, a function must be:",
            "options": ["Continuous on [a,b] only", "Differentiable on (a,b) only", "Both continuous on [a,b] and differentiable on (a,b)", "Neither"],
            "correct": 2,
            "explanation": "MVT requires the function to be continuous on the closed interval [a,b] AND differentiable on the open interval (a,b)."
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
    <li><strong>Mean Value Theorem:</strong> f'(c) = [f(b) - f(a)]/(b - a) for some c in (a,b)</li>
    <li><strong>MVT Requirements:</strong> Continuous on [a,b] and differentiable on (a,b)</li>
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
    
    # Theoretical Background Section
    st.markdown("""
    <div class='concept-card'>
    <h4>📚 What are Riemann Sums?</h4>
    <p><strong>Riemann sums</strong> are a method for approximating the area under a curve by dividing it into rectangles. 
    They form the foundation of integral calculus and provide the rigorous definition of the definite integral.</p>
    
    <h5>🏗️ The Construction Process:</h5>
    <ol>
    <li><strong>Partition:</strong> Divide interval [a,b] into n subintervals of width Δx = (b-a)/n</li>
    <li><strong>Choose points:</strong> Select a point in each subinterval to determine rectangle height</li>
    <li><strong>Calculate areas:</strong> Sum up all rectangle areas: Σ f(xᵢ) · Δx</li>
    <li><strong>Take the limit:</strong> As n → ∞, the sum approaches the exact integral</li>
    </ol>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='formula-box'>
    <h4>📐 Mathematical Definition</h4>
    <p>For a function f(x) on interval [a,b], the definite integral is defined as:</p>
    <p style='text-align: center; font-size: 1.2em;'>
    <strong>∫ₐᵇ f(x) dx = lim(n→∞) Σᵢ₌₁ⁿ f(xᵢ) · Δx</strong>
    </p>
    <p>where Δx = (b-a)/n and xᵢ is a point in the i-th subinterval.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Method comparison
    col_theory1, col_theory2, col_theory3 = st.columns(3)
    
    with col_theory1:
        st.markdown("""
        <div style='background: #e3f2fd; padding: 1rem; border-radius: 8px; border-left: 4px solid #2196f3;'>
        <h5>📍 Left Riemann Sum</h5>
        <p><strong>xᵢ = a + (i-1)·Δx</strong></p>
        <p>Uses left endpoint of each subinterval</p>
        <p><em>Underestimates</em> if function is increasing</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col_theory2:
        st.markdown("""
        <div style='background: #f3e5f5; padding: 1rem; border-radius: 8px; border-left: 4px solid #9c27b0;'>
        <h5>📍 Right Riemann Sum</h5>
        <p><strong>xᵢ = a + i·Δx</strong></p>
        <p>Uses right endpoint of each subinterval</p>
        <p><em>Overestimates</em> if function is increasing</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col_theory3:
        st.markdown("""
        <div style='background: #e8f5e8; padding: 1rem; border-radius: 8px; border-left: 4px solid #4caf50;'>
        <h5>📍 Midpoint Rule</h5>
        <p><strong>xᵢ = a + (i-0.5)·Δx</strong></p>
        <p>Uses midpoint of each subinterval</p>
        <p><em>Generally more accurate</em> than left/right</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='concept-card'>
    <h4>🎯 Key Insights About Riemann Sums</h4>
    
    <h5>📈 Convergence Properties:</h5>
    <ul>
    <li><strong>More rectangles = Better approximation:</strong> As n increases, the approximation improves</li>
    <li><strong>All methods converge:</strong> Left, right, and midpoint all approach the same limit</li>
    <li><strong>Rate of convergence:</strong> Midpoint rule typically converges faster than left/right</li>
    </ul>
    
    <h5>🔍 Error Analysis:</h5>
    <ul>
    <li><strong>Error ∝ 1/n:</strong> Doubling rectangles roughly halves the error</li>
    <li><strong>Function behavior matters:</strong> Smooth functions have smaller errors</li>
    <li><strong>Interval size matters:</strong> Larger intervals generally have larger errors</li>
    </ul>
    
    <h5>🌉 Connection to FTC:</h5>
    <p>Riemann sums provide the <em>definition</em> of the definite integral, while the Fundamental Theorem 
    of Calculus gives us an <em>efficient method</em> to evaluate it using antiderivatives!</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 🎮 Interactive Exploration")
    
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
                
                # Add theoretical analysis
                st.markdown(f"""
                <div class='concept-card'>
                <h4>📊 Analysis of Current Approximation</h4>
                <p><strong>Function:</strong> f(x) = {riemann_func}</p>
                <p><strong>Interval:</strong> [{a_bound:.2f}, {b_bound:.2f}]</p>
                <p><strong>Method:</strong> {method} Riemann Sum</p>
                <p><strong>Number of rectangles:</strong> {n_rectangles}</p>
                <p><strong>Width of each rectangle (Δx):</strong> {dx:.4f}</p>
                <p><strong>Approximation:</strong> {riemann_sum:.6f}</p>
                
                <h5>🎯 Improvement Suggestions:</h5>
                <ul>
                <li>Try increasing the number of rectangles to see convergence</li>
                <li>Compare different methods (Left vs Right vs Midpoint)</li>
                <li>Notice how the approximation changes with function curvature</li>
                </ul>
                </div>
                """, unsafe_allow_html=True)
                
                # Calculate exact integral for comparison (where possible)
                try:
                    if riemann_func == "x**2":
                        exact_integral = (b_bound**3 - a_bound**3) / 3
                        error = abs(riemann_sum - exact_integral)
                        st.success(f"🎯 Exact integral: {exact_integral:.6f} | Error: {error:.6f} ({100*error/abs(exact_integral):.2f}%)")
                    elif riemann_func == "sin(x)":
                        exact_integral = -np.cos(b_bound) + np.cos(a_bound)
                        error = abs(riemann_sum - exact_integral)
                        st.success(f"🎯 Exact integral: {exact_integral:.6f} | Error: {error:.6f} ({100*error/abs(exact_integral):.2f}%)")
                except:
                    pass
                
            except Exception as e:
                st.error(f"Error creating visualization: {str(e)}")
    
    # Historical context
    st.markdown("""
    <div class='concept-card'>
    <h4>🏛️ Historical Context</h4>
    <p><strong>Bernhard Riemann (1826-1866)</strong> was a German mathematician who formalized the concept 
    of integration through his definition of Riemann sums. His work provided the rigorous foundation 
    for integral calculus that we use today.</p>
    
    <h5>📜 Before Riemann:</h5>
    <ul>
    <li>Ancient Greeks used "method of exhaustion" for areas</li>
    <li>Newton and Leibniz developed calculus but lacked rigorous definitions</li>
    <li>Cauchy began formalizing limits and continuity</li>
    </ul>
    
    <h5>🎓 Riemann's Contribution:</h5>
    <ul>
    <li>Precise definition of the definite integral</li>
    <li>Conditions for integrability (Riemann integrable functions)</li>
    <li>Foundation for modern real analysis</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
    
    # Real-world applications
    st.markdown("""
    <div class='interactive-section'>
    <h4>🌍 Real-World Applications of Riemann Sums</h4>
    </div>
    """, unsafe_allow_html=True)
    
    app_col1, app_col2 = st.columns(2)
    
    with app_col1:
        st.markdown("""
        <div style='background: #e8f5e8; padding: 1.5rem; border-radius: 10px; border-left: 5px solid #4caf50;'>
        <h5>✈️ Aerospace Engineering</h5>
        <p><strong>Wing Design:</strong> Engineers use Riemann sums to calculate the total lift generated by airplane wings by integrating pressure distributions over the wing surface.</p>
        <p><strong>Fuel Consumption:</strong> Airlines calculate total fuel usage by integrating fuel flow rate over time during flight.</p>
        </div>
        
        <div style='background: #fff3e0; padding: 1.5rem; border-radius: 10px; border-left: 5px solid #ff9800; margin-top: 1rem;'>
        <h5>🏗️ Civil Engineering</h5>
        <p><strong>Bridge Load Analysis:</strong> Calculating total stress on bridges by integrating distributed loads (traffic, wind, weight) across the span.</p>
        <p><strong>Water Flow:</strong> Determining total water volume in irregularly shaped reservoirs or river channels.</p>
        </div>
        
        <div style='background: #f3e5f5; padding: 1.5rem; border-radius: 10px; border-left: 5px solid #9c27b0; margin-top: 1rem;'>
        <h5>💊 Medical Applications</h5>
        <p><strong>Drug Dosage:</strong> Calculating total drug absorption in the body by integrating concentration over time.</p>
        <p><strong>Cardiac Output:</strong> Measuring heart function by integrating blood flow velocity over cross-sectional area.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with app_col2:
        st.markdown("""
        <div style='background: #e3f2fd; padding: 1.5rem; border-radius: 10px; border-left: 5px solid #2196f3;'>
        <h5>🚗 Automotive Industry</h5>
        <p><strong>Distance Calculation:</strong> Your car's odometer uses integration - it continuously adds up tiny distance increments (speed × time) to show total distance traveled.</p>
        <p><strong>Fuel Efficiency:</strong> EPA ratings are calculated by integrating instantaneous fuel consumption over standardized driving cycles.</p>
        </div>
        
        <div style='background: #ffebee; padding: 1.5rem; border-radius: 10px; border-left: 5px solid #f44336; margin-top: 1rem;'>
        <h5>📊 Economics & Finance</h5>
        <p><strong>Consumer Surplus:</strong> Economists integrate demand curves to calculate economic welfare and market efficiency.</p>
        <p><strong>Present Value:</strong> Financial analysts integrate cash flows over time to determine investment values.</p>
        </div>
        
        <div style='background: #e0f2f1; padding: 1.5rem; border-radius: 10px; border-left: 5px solid #009688; margin-top: 1rem;'>
        <h5>🌿 Environmental Science</h5>
        <p><strong>Pollution Levels:</strong> Calculating total emissions by integrating pollutant concentrations over time and area.</p>
        <p><strong>Population Growth:</strong> Predicting animal population changes by integrating growth rates over time.</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style='background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 1.5rem; border-radius: 10px; color: white; margin: 1rem 0;'>
    <h5>🎯 Why This Matters to Students</h5>
    <p><strong>Every time you:</strong></p>
    <ul>
    <li>🚗 Check your car's trip odometer → You're seeing Riemann sums in action!</li>
    <li>💳 Calculate compound interest → You're using continuous integration</li>
    <li>🏃‍♂️ Use a fitness tracker for calories burned → Integration of metabolic rate over time</li>
    <li>🌡️ See weather "accumulation" reports → Integration of precipitation rate</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

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
