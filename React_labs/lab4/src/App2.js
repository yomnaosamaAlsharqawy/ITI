import logo from './logo.svg';
import './App.css';
import App from './App';
import Movies from './Movies';
import React  from 'react';
import {
    BrowserRouter as Router,
    Switch,
    Route,
    Link
  } from "react-router-dom";

import Api from "./api.js"
import 'bootstrap/dist/css/bootstrap.min.css';
import {Card,Button,Alert} from 'react-bootstrap';
// import { Alert as AlertD } from 'antd';
// import TextLoop from 'react-text-loop';
// import "antd/dist/antd.css";

class App2 extends React.Component{
  

    constructor(){
      super();
    }
  
    render(){
  
      return (
          <Router>
          <div>
              <h1>Netflex</h1>
            <ul>
              <li>
                <Link to="/todolist">Todolist</Link>
              </li>
              <li>
                <Link to="/login">Login</Link>
              </li>
              <li>
                <Link to="/register">Register</Link>
              </li>
              <li>
                <Link to="/movies">Movies</Link>
              </li>
            </ul>
    
            <hr />
    
            {/*
              A <Switch> looks through all its children <Route>
              elements and renders the first one whose path
              matches the current URL. Use a <Switch> any time
              you have multiple routes, but you want only one
              of them to render at a time
            */}
            <Switch>
              <Route path="/todolist">
                <Todolists />
              </Route>
              <Route path="/login">
                <Login />
              </Route>
              <Route path="/register">
                  <Register />
              </Route>
              <Route path="/movies">
                  <Movieslist />
        </Route>
            </Switch> 
          </div>
        </Router>
      );
    }
  }
class Todolists extends React.Component{
    render(){
        return(
            <div>
                <App />
            </div>
        )
    }
}

class Login extends React.Component {
    constructor(){
        super();
        this.state = {
            email:"",
            password:"",
            error:"",
            errors:[
                
            ]
        }
    }

    login = async ()=>{
        console.log(this.state)
        let user = {
            email:this.state.email,
            password:this.state.password
        }
        let res = await Api.login(user);
        if(res.error){
            // let myarr = [...this.state.errors,res.error];
            this.setState({error:res.error});
        }
    }

    changeInput=(e)=>{
        let statepropname = e.target.name;
        this.setState({[statepropname]:e.target.value})
    }

    render(){

        
        return(
            <div>
                {this.state.error && <Alert variant="danger" onClose={(e)=>this.setState({error:""})} dismissible>
                    <Alert.Heading>Error</Alert.Heading>
                    <p>{this.state.error}</p>
                </Alert>}
                Email <input type="email" value={this.state.email} name="email" onChange={this.changeInput} /><br/>
                Password <input type="password" value={this.state.password} name="password" onChange={this.changeInput} /><br/>
                <button onClick={this.login} >Login</button>
            </div>
        );
        

    }
}




class Register extends React.Component {
    constructor(){
        super();
        this.state = {
            username:"",
            password:"",
            email:"",
            error:""
        }
    }

     register = async ()=>{
        console.log(this.state)
        let user ={
            username:this.state.username,
            password:this.state.password
        }
        let res = await Api.Register(user);
        if(res.error){
            // let myarr = [...this.state.errors,res.error];
            this.setState({error:res.error});
        }
    }

    changeInput=(e)=>{
        let statepropname = e.target.name;
        this.setState({[statepropname]:e.target.value})
    }

    render(){

        return(
            <div>
                <h1>{this.state.error}</h1>
                Username <input type="text" value={this.state.username} name="username" onChange={this.changeInput} /><br/>
                Password <input type="password" value={this.state.password} name="password" onChange={this.changeInput} /><br/>
                Email <input type="email" value={this.state.email} name="email" onChange={this.changeInput} /><br/>
                <button onClick={this.register} >Register</button>
            </div>
        );
    }
}

class Movieslist extends React.Component{
    render(){
        return(
            <div>
                <Movies />
            </div>
        )
    }
}


export default App2;