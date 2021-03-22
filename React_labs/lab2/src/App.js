// import logo from './logo.svg';
import './App.css';
import React from 'react';

class App extends React.Component{
  render(){
    return(
      <div>
        <h1>ToDo List</h1>
        <Form />
      </div>
    )
  }
}

class Form extends React.Component{
  constructor(){
    super();
    this.state={
      list:[{'id':1,'name':'check your email'}],
      task:""
    }
  }

  changeInput=(e)=>{
    let statepropname = e.target.name;
    this.setState({[statepropname]:e.target.value})
  }

  addlist=()=>{
    let data = this.state.task;
    let task = {'id':this.state.list.length+1,'name':data};
    this.setState({list: [...this.state.list, task]});

  }
  deletelist=(index)=>{
    var array = [...this.state.list];
    var index1 = array.indexOf(index)
    if (index1 !== -1) {
      array.splice(index1, 1);
      console.log(array)
      this.setState({list: array});
  }
}
  render(){
    return(
      <div>
        <DisplayList data={this.state.list} action={this.deletelist}/>
        <input type='text' id='todo' value={this.state.task} name="task" onChange={this.changeInput} />
        <button onClick={this.addlist}>ADD</button>
      </div>
    )
  }
}

class DisplayList extends React.Component{
  render(){

      return (
        <div>
            {this.props.data.map((item)=>{
                return <List key={item.id} item={item} list={this.props.data} action={this.props.action}/>
            })}
        </div>
      );
    }
}

class List extends React.Component{
  constructor(props){
    super();
  }


  render(){
      return (
          <div>
            <ul>
              <li><span>{this.props.item.id}</span>
              <span>  </span>
              <span>{this.props.item.name}</span></li>
              <button onClick={()=>this.props.action(this.props.item)}>X</button>
            </ul>
          </div>
      )
  }
}

export default App;
