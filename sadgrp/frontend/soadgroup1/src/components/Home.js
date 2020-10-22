import React ,{Component}from 'react';

import axios from 'axios';
class Home extends Component{
  

   

    render(){
        if(this.props.user)
        {
            return (
            <h2>{this.props.user.email}</h2>
            )
        }
        return(
            <div>
               <h1>Hi </h1>
                </div>
        );
    }
}

export default Home;