<h1>AI Research Assistant 🧠</h1>

A RAG-Based Knowledge System for Intelligent Document Search

<h2>📌 What Is This Project?</h2>

<p>This project is an AI-powered research assistant that allows users to upload documents (PDF or text) and ask
    questions about them.</p>

<p>Instead of relying only on a language model’s memory, the system retrieves relevant information from uploaded
    documents using semantic search and then generates accurate, context-aware answers with citations.</p>

<p>It combines:</p>
<ul>
    <li>Document chunking</li>
    <li>Vector embeddings</li>
    <li>FAISS similarity search</li>
    <li>Retrieval-Augmented Generation (RAG)</li>
    <li>Context-aware LLM answering</li>
</ul>

<h2>🚀 Why This Project Matters</h2>
<p>Large Language Models alone can hallucinate.</p>

<p>This system reduces hallucination by:
<p>
<ol>
    <li>Retrieving relevant document chunks</li>
    <li>Injecting them into the LLM prompt</li>
    <li>Generating answers grounded in real data</li>
    <li>Providing source citations</li>
</ol>


<p>This architecture is widely used in modern AI products such as:</p>
<ul>
    <li>Enterprise knowledge assistants</li>
    <li>Research tools</li>
    <li>Internal company copilots</li>
    <li>AI document search engines</li>
</ul>

<h2>🧠 Key Features</h2>

<ul>
    <li>📄 Upload multiple PDF or text documents</li>
    <li>✂️ Automatic text chunking</li>
    <li>🔎 Semantic vector search with FAISS</li>
    <li>🤖 Context-aware answer generation</li>
    <li>📚 Source citation support</li>
    <li>🧠 Query history memory</li>
    <li>📝 Auto-summary mode</li>
    <li>📤 Export research report</li>
    <li>🐳 Docker-ready deployment</li>
</ul>


<h2>🏗 Technical Stack</h2>
<ul>
    <li>FastAPI (Backend API)</li>
    <li>FAISS (Vector similarity search)</li>
    <li>SentenceTransformers (Embeddings)</li>
    <li>OpenAI API (LLM)</li>
    <li>Python</li>
</ul>