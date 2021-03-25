// import logo from './logo.svg';
import './App.css';
import React  from 'react';

import Api from "./api.js"
import 'bootstrap/dist/css/bootstrap.min.css';
import {Card,Button,Alert} from 'react-bootstrap';
// import { Alert as AlertD } from 'antd';
// import TextLoop from 'react-text-loop';
// import "antd/dist/antd.css";

class Movies extends React.Component {

    constructor(){
        super();
        this.state={
            data:[]
        }
    }
    async componentDidMount(){
        let data = await Api.getMovies();
        console.log(data);
        this.setState({data:data});
    }
    render() {
        return (
            <div>
                <h1>Movies...</h1>
                {this.state.data && this.state.data.length > 0 &&  this.state.data.map((item)=>{
                    return <Movie key={item.id} item={item} />
                })

                }
            </div>
            )
        }
    }

class Movie extends React.Component{
constructor(){
    super();

}

render(){
   return <Card style={{ width: '18rem',float:"left" }}>
   <Card.Img variant="top" src={this.props.item.avatar} />
   <Card.Body>
     <Card.Title>{this.props.item.first_name}</Card.Title>
     <Card.Text>
       Some quick example text to build on the card title and make up the bulk of
       the card's content.
     </Card.Text>
     <Button variant="primary">Go somewhere</Button>
   </Card.Body>
 </Card>
}
}

export default Movies;