<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>README</title>
</head>
<body>

<h1>Blockchain Money Transfer</h1>
<p>A simple blockchain-based application for simulating money transfers between users, demonstrating the basic concepts of blockchain technology, including block creation, proof-of-work, and data immutability.</p>

<h2>Features</h2>
<ul>
    <li><strong>Blockchain Visualization:</strong> Display the entire blockchain with details of each block.</li>
    <li><strong>Transaction Form:</strong> Submit transactions to transfer money between users.</li>
    <li><strong>Proof-of-Work:</strong> Simple proof-of-work mechanism to validate new blocks.</li>
</ul>

<h2>Installation</h2>

<h3>Prerequisites</h3>
<ul>
    <li>Python 3.6 or higher</li>
    <li>Flask</li>
</ul>

<h3>Steps</h3>
<ol>
    <li><strong>Clone the repository:</strong>
        <pre><code>git clone https://github.com/your-username/blockchain-money-transfer.git
cd blockchain-money-transfer</code></pre>
    </li>
    <li><strong>Create a virtual environment and activate it:</strong>
        <pre><code>python3 -m venv venv
source venv/bin/activate  # On Windows use venv\Scripts\activate</code></pre>
    </li>
    <li><strong>Install the required packages:</strong>
        <pre><code>pip install Flask</code></pre>
    </li>
    <li><strong>Run the Flask application:</strong>
        <pre><code>python app.py</code></pre>
    </li>
    <li><strong>Open your web browser and navigate to:</strong>
        <pre><code>http://127.0.0.1:5000/</code></pre>
    </li>
</ol>

<h2>Usage</h2>
<ol>
    <li><strong>View Blockchain:</strong> The home page displays the current state of the blockchain, showing details of each block.</li>
    <li><strong>Submit Transaction:</strong> Fill out the transaction form with sender, receiver, and amount details, then submit to add a new block to the blockchain.</li>
    <li><strong>Block Validation:</strong> Each new block undergoes a simple proof-of-work validation before being added to the blockchain.</li>
</ol>

<h2>Code Overview</h2>

<h3>Frontend (HTML)</h3>
<p>The HTML file provides the structure and styling for the web interface, including the form for submitting transactions and the display of blockchain blocks.</p>

<h3>Backend (Python with Flask)</h3>
<ul>
    <li><strong>app.py:</strong> This file contains the Flask application that handles routing and blockchain logic.</li>
    <li><strong>Block</strong> and <strong>Blockchain</strong> classes: Define the structure of blocks and the blockchain, including methods for creating new blocks and calculating hashes.</li>
</ul>

<h2>Technologies Used</h2>
<ul>
    <li><strong>Frontend:</strong> HTML, CSS, JavaScript</li>
    <li><strong>Backend:</strong> Python, Flask</li>
    <li><strong>Blockchain:</strong> Custom implementation using Python classes</li>
</ul>

<h2>Contributing</h2>
<p>We welcome contributions! To contribute:</p>
<ol>
    <li><strong>Fork the repository</strong></li>
    <li><strong>Create a new branch:</strong>
        <pre><code>git checkout -b feature-branch</code></pre>
    </li>
    <li><strong>Make your changes and commit them:</strong>
        <pre><code>git commit -m 'Add new feature'</code></pre>
    </li>
    <li><strong>Push to the branch:</strong>
        <pre><code>git push origin feature-branch</code></pre>
    </li>
    <li><strong>Create a pull request</strong></li>
</ol>

</body>
</html>
