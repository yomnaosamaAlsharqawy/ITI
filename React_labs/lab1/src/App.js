import logo from './logo.svg';
import './App.css';
import React from 'react';

class App extends React.Component{
  constructor(){
    super();
    this.state={
      title:"your score is 0",
      count:0
    }
    this.changeTitle = this.changeTitle.bind(this);
  }
  changeTitle(){
    let newcount = this.state.count+1;
    let text = "your new score is ";
    if(newcount%10==0){
      this.setState({title:text.concat(newcount)})
    }
    this.setState({count:newcount});
  }
  render(){
    return(<div>
      <h1>WELCOME TO REACT PROJECT</h1>
      <h2>{this.state.title}</h2>
      <h2>Number of clicked:<span>{this.state.count}</span></h2>
      <button onClick={this.changeTitle}>count change</button>
    </div>);
  }
} 

export default App;
