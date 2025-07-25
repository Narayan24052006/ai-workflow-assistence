// frontend/src/App.js
import React, { useState } from 'react';
import axios from 'axios';
import ReactMarkdown from 'react-markdown';
import './App.css';

function App() {
  const [task, setTask] = useState('');
  const [workflowState, setWorkflowState] = useState(null);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!task) {
      setError('Please enter a task.');
      return;
    }
    setIsLoading(true);
    setError('');
    setWorkflowState(null);

    try {
      const response = await axios.post('http://localhost:5000/api/execute-workflow', { task });
      setWorkflowState(response.data);
    } catch (err) {
      setError('An error occurred. Please check the backend console and try again.');
      console.error(err);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>🤖 AI Workflow Assistant</h1>
        <p>Enter a task, and the AI will search, summarize, and draft a post for you.</p>
      </header>

      <main>
        <form onSubmit={handleSubmit}>
          <input
            type="text"
            value={task}
            onChange={(e) => setTask(e.target.value)}
            placeholder="e.g., Research laptops under ₹50,000 and write a blog post"
            disabled={isLoading}
          />
          <button type="submit" disabled={isLoading}>
            {isLoading ? 'Generating...' : 'Start Workflow'}
          </button>
        </form>

        {error && <p className="error">{error}</p>}

        {isLoading && <div className="loader"></div>}
        
        {workflowState && (
          <div className="results">
            <div className="result-step">
              <h2>Step 1: Web Search Results</h2>
              <p className="step-content">{workflowState.search_results}</p>
            </div>
            <div className="result-step">
              <h2>Step 2: Research Summary</h2>
              <div className="step-content">
                 <ReactMarkdown>{workflowState.summary}</ReactMarkdown>
              </div>
            </div>
            <div className="result-step">
              <h2>Step 3: Drafted Blog Post</h2>
              <div className="step-content blog-post">
                <ReactMarkdown>{workflowState.blog_post}</ReactMarkdown>
              </div>
            </div>
          </div>
        )}
      </main>
    </div>
  );
}

export default App;