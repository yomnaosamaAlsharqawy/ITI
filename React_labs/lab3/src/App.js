// import logo from './logo.svg';
import './App.css';
import React from 'react';
import './style.css'; 

class App extends React.Component{
  render(){
    return(
      <div>
        <Calc />
      </div>
    )
  }

} 
class Calc extends React.Component{
  render(){
    return(
      <div>
        <DisplayScreen />
      </div>
      
    )
  }
}

class DisplayScreen extends React.Component{
  constructor(){
    super();
    this.state={
      result:"",
      equation:"",
      parm:['+', '-', '*', '/', '%']
    }
  }
  fordisplay=(input)=>{
    let check = this.state.parm.includes(input);
    if(check !== true && input!=="="){
      // console.log(this.state.result)
      let num = this.state.result+input;
      // console.log(num)
      this.setState({result:num});
      // console.log(this.state.result)
    }
    else if(check == true && input!="="){
      if(this.state.equation ==""){
        let eq = this.state.result + input;
        this.setState({equation:eq}); 
        console.log(this.state.equation)
      }
      else{
        let eq=this.state.equation+this.state.result+input
        this.setState({equation : eq});
        console.log(this.state.equation)
      }
      this.setState({result:""});
    }
    else if(input=="="){
      let eq = this.state.equation + this.state.result
      this.setState({equation:eq});
      let finalresult = eval(eq);
      console.log(eq)
      this.setState({result:finalresult})
      this.setState({equation:""});
    }
      
    }

    clear=()=>{
      this.setState({result:""})
      this.setState({equation:""})
    }

  
  render(){
    return(
      <div className="display">
         <span style={{color: '#136381'}}>{this.state.result}</span><br/>
         <span>{this.state.equation}</span><br/>
         <hr></hr>
         
        <Buttons action={this.fordisplay} clear={this.clear}/>
      </div>
    )
  }

}
class Buttons extends React.Component{
  render(){
    return(
      <div className="display">

        <div className="first-row">
            <button id="r1-1" style={{width: "105px"}} onClick={this.props.clear}>C</button>
            <button id="r1-3" onClick={()=>this.props.action('%')}>%</button>
            <button id="r1-4" onClick={()=>this.props.action('/')}>/</button>
         </div>
         <div className="second-row">
            <button id="r2-1" onClick={()=>this.props.action('7')}>7</button>
            <button id="r2-2" onClick={()=>this.props.action('8')}>8</button>
            <button id="r2-3" onClick={()=>this.props.action('9')}>9</button>
            <button id="r2-4"  onClick={()=>this.props.action('*')}>*</button>
         </div>
         <div className="third-row">
            <button id="r3-1" onClick={()=>this.props.action('4')}>4</button>
            <button id="r3-2" onClick={()=>this.props.action('5')}>5</button>
            <button id="r3-3" onClick={()=>this.props.action('6')} >6</button>
            <button id="r3-4" onClick={()=>this.props.action('-')}>-</button>
         </div>
         <div className="fourth-row">
            <button id="r4-1"  onClick={()=>this.props.action('1')}>1</button>
            <button id="r4-2"  onClick={()=>this.props.action('2')}>2</button>
            <button id="r4-3"  onClick={()=>this.props.action('3')}>3</button>
            <button id="r4-4"  onClick={()=>this.props.action('+')}>+</button>
         </div>
         <div className="fifth-row">
           <button id="r5-1" style={{width: "105px"}} onClick={()=>this.props.action('0')}>0</button>
           <button id="r5-2" onClick={()=>this.props.action('.')} >.</button>
           <button id="r5-3" onClick={()=>this.props.action('=')}>=</button>
         </div>
    </div>
    )
  }
}
export default App;
