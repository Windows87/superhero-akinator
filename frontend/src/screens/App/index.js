import React, { Component } from 'react';

import getQuestion from '../../utils/getQuestion';

import './styles.css';

const numberOfQuestions = 12;

const SearchContainer = ({ question, answersButtons, onButtonClick }) => (
  <div className="searchContainer">
    <img src="/brain.png" alt="" />
    <h2>{ question }</h2>
    <div>
      { answersButtons.map(answer => <button key={Math.random()} onClick={() => onButtonClick(answer.value)}>{ answer.title }</button>) }
    </div>
  </div>
);

const FinishedContainer = ({ characterMatch }) => (
  <div className="finishedContainer">
    <img src={characterMatch.image} alt="" />
    <h2>{ characterMatch.name }</h2>
  </div>
);

class App extends Component {
  state = {
    alreadyFeatures: [],
    params: [],
    answers: [],
    answersButtons: [],
    question: '',
    characterMatch: null,
    loading: true,
    finished: false
  };

  componentWillMount() {
    this.setQuestion();
  }

  setQuestion = async (answer) => {
    this.setState({ loading: true });

    try {
      const { alreadyFeatures, params } = this.state;
      const { answers, characterMatch, feature, param, question } = await getQuestion(alreadyFeatures, params, [...this.state.answers, answer]);
      this.setState({ params: [...this.state.params, param], alreadyFeatures: [...this.state.alreadyFeatures, feature], answersButtons: answers, characterMatch, question, loading: false });
      if(answer) this.setState({ answers: [...this.state.answers, answer] });
    } catch(error) {
      console.log(error);
      this.setState({ loading: false });
      alert('Error on get Question');
    }
  }

  onButtonClick = async answer => {
    await this.setQuestion(answer);

    const finished = this.state.answers.length === numberOfQuestions;

    if(finished)
      this.setState({ finished: true });
  }

  render() {
    const { question, answersButtons, loading, finished, characterMatch } = this.state;

    return (
      <div className="app">
        <header>
          <h1>I WILL DISCOVER YOUR SUPERHERO!</h1>
        </header>
        <main>
          { loading && !finished ? <h2>Carregando..</h2> : null }
          { !loading && !finished ? <SearchContainer question={question} answersButtons={answersButtons} onButtonClick={this.onButtonClick} /> : null }
          { finished ? <FinishedContainer characterMatch={characterMatch} /> : null }
        </main>
      </div>
    );
  }
}

export default App;
