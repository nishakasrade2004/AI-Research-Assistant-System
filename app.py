from flask import Flask, request, send_file
import webbrowser
import threading
import io

app = Flask(__name__)

generated_data = {}

# 🧠 CONTENT GENERATOR
def generate_content(topic):
    topic_lower = topic.lower()

    # 🔹 MACHINE LEARNING
    if "machine learning" in topic_lower:
        return {
            "main": """
Introduction:
Machine Learning is a subset of Artificial Intelligence that allows systems to learn from data and improve automatically.
Machine learning is a branch of Machine Learning in which computers learn from data and improve their performance without being explicitly programmed. Instead of following fixed rules, systems identify patterns and make predictions or decisions, which is why it is widely used in real-world applications like recommendation systems, fraud detection, and image recognition.
It is a core part of modern Artificial Intelligence and is widely used in everyday applications like recommendation systems (Netflix, Amazon), voice assistants, image recognition, and fraud detection. By using algorithms and large datasets, machine learning models can identify patterns, make predictions, and support intelligent decision-making across various industries such as healthcare, finance, and technology.

Types of Machine Learning:
- Supervised Learning
- Unsupervised Learning
- Reinforcement Learning

Working:
The working of Machine Learning in sequence form:

Data Collection - Gather relevant data from different sources.
Data Preprocessing - Clean, organize, and prepare the data for training.
Model Selection - Choose the appropriate algorithm for the task.
Training the Model - Feed data to the model so it can learn patterns.
Model Evaluation - Test the model to check accuracy and performance.
Model Tuning - Improve the model by adjusting parameters if needed.
Deployment - Use the trained model to make predictions on new data.

Advantages:
- Automation
- High accuracy
- Improves with experience

Disadvantages:
- Requires large amounts of data
- Time-consuming training process
- Lack of transparency (black box)
- Risk of biased results
- Difficult to interpret results

Limitations:
- Requires large data
- Complex models
- Overfitting and underfitting
- Data dependency
- Bias and fairness issues

Conclusion:
Machine Learning is widely used in real-world applications like prediction and automation.
""",
            "extra": {
                "Supervised Learning": """
Supervised Learning:

- Definition:
In this type, the model is trained on labeled data where both input and correct output are known.

 Types:
- Regression: Used when the output is continuous (numeric values).  
  Example: House price prediction  

- Classification: Used when the output is categorical (labels).  
  Example: Spam detection
""",
                "Unsupervised Learning": """
Unsupervised Learning:

- Definition:
This works with unlabeled data and the model tries to find hidden patterns or groupings on its own.

 Types:
- Clustering: Groups similar data points together.  
  Example: Customer segmentation  

- Association: Finds relationships between variables.  
  Example: Market basket analysis
""",
                "Reinforcement Learning": """
Reinforcement Learning:

- Definition:
In this type, the model learns by interacting with an environment and receives rewards or penalties based on its actions.

 Types:
- Model-Based: The agent uses a model of the environment (i.e., it understands how actions affect outcomes). It can plan ahead before taking actions.  
  Example: A robot simulating movements before actually performing them.

- Model-Free: The agent does not know the environment model and learns only through trial and error (experience).
  Example: Game-playing AI learning by rewards after each move.

Example: Game AI
"""
            },
            "diagram": """
Machine Learning Flow:

Data → Training → Model → Prediction
"""
        }

    # 🔹 AI
    if "ai" in topic_lower or "artificial intelligence" in topic_lower:
        return {
            "main": """
Introduction:
Artificial Intelligence enables machines to simulate human intelligence.
Artificial Intelligence is a branch of computer science that enables machines to perform tasks that normally require human intelligence, such as learning, reasoning, problem-solving, perception, and decision-making. AI systems use data, algorithms, and computing power to simulate human thinking and improve performance over time.
Today, AI is widely used in applications like virtual assistants, recommendation systems, healthcare diagnostics, self-driving cars, and automation across industries.

Working:
The working of Artificial Intelligence in a proper sequence is:

Data Collection - Gather relevant data from various sources.
Data Preprocessing - Clean and organize the data for better accuracy.
Model Selection - Choose suitable algorithms or AI models.
Training - Train the model using data to learn patterns.
Evaluation - Test the model to check performance and accuracy.
Decision Making - Use the trained model to make predictions or decisions.
Feedback & Improvement - Continuously update and improve the model based on new data.

Types of AI:
- Narrow AI
- General AI
- Super AI

Applications:
- Chatbots
- Self-driving cars
- Voice assistants

Advantages:
- Automation
- High accuracy and reduced human error
- Faster decision making
- Improved efficiency and productivity

Limitations:
- High cost
- Data dependency
- High development and maintenance cost
- Risk of biased decisions
- Limited to specific tasks (in most cases)

Disadvantages:
- Job displacement and unemployment
- Over-dependence on machines
- Privacy and security concerns
- Ethical issues and misuse
- Lack of transparency in decisions

Conclusion:
AI is shaping the future of technology. Lack of transparency in decisions
""",
            "extra": {
                "Narrow AI": """
Narrow AI:

- Designed to perform a specific task efficiently. 
  Example: Alexa, Google Assistant
""",
                "General AI": """
General AI:

- Aims to perform any intellectual task that a human can do (still theoretical).  
  Example: A human-like robot capable of reasoning, learning, and problem-solving across all domains.
""",
                "Super AI": """
Super AI:

- A future concept where AI surpasses human intelligence in all aspects.
  Example: Hypothetical systems that can outperform humans in creativity, decision-making, and emotions. 
"""
            },
            "diagram": """
AI Structure:

AI → ML → Deep Learning
"""
        }

    # 🔹 JAVA
    if "java" in topic_lower:
        return {
            "main": """
Introduction:
Java is a high-level, object-oriented programming language developed by Sun Microsystems (now owned by Oracle Corporation). It is designed to be platform-independent, meaning “Write Once, Run Anywhere” (WORA). Java is widely used for building web applications, mobile apps (Android), enterprise systems, and backend services due to its reliability, security, and scalability.

Types of Java:
Java is commonly divided into different types/platforms:

- Java SE (Standard Edition) - Core Java used for basic programming and desktop applications.
  Example: Building a calculator or simple Java application.

- Java EE (Enterprise Edition) - Used for large-scale enterprise applications with APIs like Servlets and JSP.
  Example: Banking systems, e-commerce websites.

- Java ME (Micro Edition) - Used for mobile and embedded systems with limited resources.
- Example: Applications on small devices or embedded systems.

- JavaFX - Used for building rich GUI applications.
  Example: Desktop applications with advanced UI.

Features:
- Object-Oriented
- Platform Independent
- Secure
- Simple and easy to learn
- Robust (strong memory management, exception handling)
- Multithreaded
- High performance with Just-In-Time (JIT) compiler

Applications:
- Web development
- Mobile apps
- Software development

Advantages:
- Easy to learn
- Portable
- Platform independence
- High security
- Rich APIs and libraries
- Multithreading support
- Scalability for large applications

Disadvantages:
- Slower compared to low-level languages like C/C++
- Higher memory consumption
- Verbose syntax (more code required)
- Performance overhead due to JVM

Conclusion:
Java is widely used in software industry. Java remains one of the most popular and reliable programming languages in the world. Its platform independence, strong ecosystem, and scalability make it a top choice for enterprise and application development.
""",
            "extra": {},
            "diagram": """
Java Working (How Java Works):
Java works by compiling source code into bytecode using the Java compiler. 
This bytecode is then executed by the Java Virtual Machine (JVM), 
which converts it into machine code specific to the system. Because of JVM, 
Java programs can run on any platform without modification. 
The process includes writing code → compiling → bytecode generation → execution via JVM.
Source Code → Compiler → Bytecode → JVM → Output
"""
        }

    return {
        "main": f"""
Introduction:
{topic} is an important concept.

Conclusion:
{topic} is useful in technology.
""",
        "extra": {},
        "diagram": ""
    }


# 🏠 HOME PAGE
@app.route('/')
def home():
    return '''
    <html>
    <head>
    <style>
        body {
            font-family: Arial;
            background: linear-gradient(to right, #667eea, #764ba2);
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        .box {
            background: white;
            padding: 40px;
            border-radius: 15px;
            text-align: center;
            width: 400px;
            box-shadow: 0px 0px 25px rgba(0,0,0,0.3);
        }
        input {
            padding: 12px;
            width: 90%;
            border-radius: 8px;
        }
        button {
            margin-top: 20px;
            padding: 12px 25px;
            background: #6c63ff;
            color: white;
            border: none;
            border-radius: 8px;
        }
    </style>
    </head>
    <body>
        <div class="box">
            <h2>🤖 AI Research Assistant</h2>
            <form action="/result" method="post">
                <input type="text" name="topic" placeholder="Enter topic..." required>
                <br>
                <button type="submit">Generate</button>
            </form>
        </div>
    </body>
    </html>
    '''


# 📄 RESULT PAGE
@app.route('/result', methods=['POST'])
def result():
    topic = request.form['topic']
    data = generate_content(topic)

    generated_data["topic"] = topic
    generated_data["content"] = data["main"]

    lines = data["main"].split("\n")
    formatted = ""

    for line in lines:
        line = line.strip()

        if line:
            if ":" in line:
                formatted += f'<div class="card"><b>{line}</b></div>'

            elif line.startswith("-"):
                item = line[1:].strip()
                formatted += f'<div class="card">• {item}</div>'

                if item in data["extra"]:
                    formatted += f'''
                    <button class="btn" onclick="toggle('{item}')">Read More</button>
                    <div id="{item}" style="display:none;">
                        <div class="card">{data["extra"][item]}</div>
                    </div>
                    '''

            else:
                formatted += f'<div class="card">{line}</div>'

    # Diagram add
    if data["diagram"]:
        formatted += f'<div class="card"><b>Diagram:</b><br><pre>{data["diagram"]}</pre></div>'

    return f"""
    <html>
    <head>
    <script>
    function toggle(id) {{
        var x = document.getElementById(id);
        if (x.style.display === "none") {{
            x.style.display = "block";
        }} else {{
            x.style.display = "none";
        }}
    }}
    </script>

    <style>
        body {{ font-family: Arial; background: #f4f6f9; padding: 20px; }}
        h1 {{ text-align: center; }}
        .card {{ background: white; padding: 15px; margin: 10px auto; width: 70%; border-radius: 10px; box-shadow: 0px 0px 10px rgba(0,0,0,0.1); }}
        .btn {{ padding: 10px 20px; background: #6c63ff; color: white; border-radius: 8px; border:none; margin-left:15%; }}
        .top-bar {{ display: flex; justify-content: space-between; }}
    </style>
    </head>
    <body>

    <div class="top-bar">
        <a class="btn" href="/">⬅ Back</a>
        <a class="btn" href="/download">📄 PDF</a>
    </div>

    <h1>{topic}</h1>

    {formatted}

    </body>
    </html>
    """


# 📥 PDF DOWNLOAD
@app.route('/download')
def download():
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Preformatted
    from reportlab.lib.styles import getSampleStyleSheet

    topic = generated_data.get("topic", "")
    content = generated_data.get("content", "")

    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer)
    styles = getSampleStyleSheet()

    elements = []
    elements.append(Paragraph(topic, styles['Title']))
    elements.append(Spacer(1, 20))
    elements.append(Preformatted(content, styles['Normal']))

    doc.build(elements)
    buffer.seek(0)

    return send_file(buffer, as_attachment=True, download_name="Report.pdf")


# 🌐 AUTO OPEN BROWSER
def open_browser():
    webbrowser.open("http://127.0.0.1:5000/")

if __name__ == '__main__':
    threading.Timer(1.5, open_browser).start()
    app.run(debug=True)